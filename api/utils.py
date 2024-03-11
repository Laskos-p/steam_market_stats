from datetime import datetime

import aiohttp

url = "https://steamcommunity.com/market/search/render/"


async def get_data_json(
    appid,
    search_description=0,
    sort_column="default",
    sort_dir="desc",
    norender=1,
    start=0,
    count=100,
):
    payload = {
        "search_description": search_description,
        "appid": appid,
        "sort_column": sort_column,
        "sort_dir": sort_dir,
        "norender": norender,
        "start": start,
        "count": count,
    }

    async with aiohttp.ClientSession() as client:
        try:
            response = await client.get(url, params=payload)

        except Exception as e:
            print("Error fetching data:", e)
            return None

        if response.status != 200:
            print("To many requests")
            print(response.status)
            response.raise_for_status()
            return None

        return await response.json()


async def filter_data(data: dict, filter_keys: list):
    """
    Filter data from json
    :param data: Data from json
    :param filter_keys: List of keys to filter from data
    :return: Dict containing keys from filter_keys and their values
    """
    filtered_data = []
    name_keys = []
    item_keys = []
    item_description_keys = []
    for key in filter_keys:
        if key == "full_name" or key == "type":
            name_keys.append(key)
        elif key in data["results"][0].keys():
            if key == "name":
                continue
            item_keys.append(key)
        else:
            item_description_keys.append(key)

    # print(item_keys)
    for result in data["results"]:
        # desc_dict = {}
        # for key in item_description_keys:
        #     desc_dict[key] = result["asset_description"][key]
        # desc = await split_name(result["name"])
        # for s in desc:
        #     print(s)
        # for key, something in (await split_name(result["name"])).items():
        #     print(something)
        #     print(type(something))

        filtered_data.append(
            # await split_name(result["name"])
            # {"full_name": result["name"]}
            {key: something for key, something in (await split_name(result["name"])).items() if key in name_keys}
            | {key: result[key] for key in item_keys}
            | {key: result["asset_description"][key] for key in item_description_keys}
            | {"updated_at": datetime.now()}
        )
        # print(filtered_data)

    return filtered_data


async def split_name(full_name: str):
    """
    Split name into full_name, name, weapon, StatTrak, quality
    :param full_name: Full name of item
    :return: {full_name: full_name, name: name, weapon: weapon, stattrak: stattrak, quality: quality}
    """
    item_type = "other"
    # match case for stickers, capsules, graffiti, patches
    match = [
        "Sticker",
        "Graffiti",
        "Capsule",
        "Music",
        "Agent",
        "Case",
        "Key",
    ]
    for m in match:
        if m in full_name:
            item_type = m.lower()
            return {
                "full_name": full_name,
                "name": "",
                "weapon": "",
                "stattrak": False,
                "quality": "",
                "type": item_type,
            }

    if "|" not in full_name:
        return {
            "full_name": full_name,
            "name": "",
            "weapon": "",
            "stattrak": False,
            "quality": "",
            "type": item_type,
        }
    # if (
    #     "Sticker" in full_name
    #     or "Graffiti" in full_name
    #     or "Capsule" in full_name
    #     or "Patch" in full_name
    # ):
    #     return {
    #         "full_name": full_name,
    #         "name": "",
    #         "weapon": "",
    #         "stattrak": False,
    #         "quality": "",
    #         "type": item_type,
    #     }
    try:
        weapon, name = full_name.strip().split(" | ")
        stattrak = False
        if "StatTrak" in weapon:
            weapon = weapon.replace("StatTrak™ ", "")
            stattrak = True

        if "(" in name:
            split = name.split(" (")
            if len(split) == 3:
                split = name.split(" (")
                name = split[0] + " " + split[1]
                quality = split[2][:-1]
            else:
                name = split[0]
                quality = split[1][:-1]
        else:
            quality = ""

    except Exception as e:
        print(e)
        print(full_name.encode("utf-8"))
        name = "ERROR"
        quality = "ERROR"
        weapon = "ERROR"
        stattrak = False

    return {
        "full_name": full_name,
        "name": name,
        "weapon": weapon,
        "stattrak": stattrak,
        "quality": quality,
        "type": "weapon",
    }


# print(split_name("StatTrak™ M4A4 | 龍王 (Dragon King) (Field-Tested)"))
# db_columns = ["name", "sell_listings", "sell_price", "icon_url", "appid"]
# print(filter_data(data, db_columns)[0])
