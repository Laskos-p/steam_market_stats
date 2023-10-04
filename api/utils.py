import json

import requests

url = "https://steamcommunity.com/market/search/render/"


# get items for game=appid as json
async def get_data_json(
    appid,
    search_description=0,
    sort_column="default",
    sort_dir="desc",
    norender=1,
    count=100,
):
    payload = {
        "search_description": search_description,
        "appid": appid,
        "sort_column": sort_column,
        "sort_dir": sort_dir,
        "norender": norender,
        "count": count,
    }
    f = requests.get(url, params=payload)
    return f.json()


# from collections import deque
# import json
#
#
# with open("data.json", "r") as f:
#     data = json.load(f)


async def filter_data(data: dict, filter_keys: list):
    """
    Filter data from json
    :param data: Data from json
    :param filter_keys: List of keys to filter from data
    :return: Dict containing keys from filter_keys and their values
    """
    filtered_data = []
    item_keys = []
    item_description_keys = []
    for key in filter_keys:
        if key in data["results"][0].keys():
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

        filtered_data.append(
            await split_name(result["name"])
            | {key: result[key] for key in item_keys}
            | {key: result["asset_description"][key] for key in item_description_keys}
        )
        # print(filtered_data)

    return filtered_data


async def split_name(full_name: str):
    """
    Split name into name, weapon, StatTrak, quality
    :param full_name: Full name of item
    :return: {name: name, weapon: weapon, stattrak: stattrak, quality: quality}
    """
    if "|" not in full_name:
        return {
            "name": full_name,
            "weapon": "Invalid",
            "stattrak": False,
            "quality": "Invalid",
        }
    weapon, name = full_name.strip().split(" | ")
    stattrak = False
    if "StatTrak" in weapon:
        weapon = weapon[10:]
        stattrak = True
    name, quality = name.split(" (")
    quality = quality[:-1]
    return {"name": name, "weapon": weapon, "stattrak": stattrak, "quality": quality}


# db_columns = ["name", "sell_listings", "sell_price", "icon_url", "appid"]
# print(filter_data(data, db_columns)[0])
