import requests

url = "https://store.steampowered.com/api/appdetails"


def get_game_json(appid: int):
    payload = {"appids": appid}
    f = requests.get(url, params=payload)
    return f.json()


def filter_data(data: dict, filter_keys: list):
    filtered_data = []

    for key in filter_keys:
        filtered_data.append(data[str(list(data.keys())[0])]["data"][key])

    return filtered_data
