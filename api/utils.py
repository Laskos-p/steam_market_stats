import requests

url = "https://steamcommunity.com/market/search/render/"


# get items for game=appid as json
def get_data_json(
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
# with open("api/data.json", "r") as f:
#     data = json.load(f)

# print(data)


def filter_data(data: dict, filter_keys: list):
    filtered_data = []
    item_keys = []
    item_description_keys = []
    for key in filter_keys:
        if key in data["results"][0].keys():
            item_keys.append(key)
        else:
            item_description_keys.append(key)

    # print(item_keys, item_description_keys)

    for result in data["results"]:
        # desc_dict = {}
        # for key in item_description_keys:
        #     desc_dict[key] = result["asset_description"][key]

        filtered_data.append(
            {key: result[key] for key in item_keys}
            | {key: result["asset_description"][key] for key in item_description_keys}
        )
        # print(desc_dict)

    return filtered_data


# db_columns = ["name", "sell_listings", "sell_price", "icon_url", "appid"]
# print(filter_data(data, db_columns)[0])
