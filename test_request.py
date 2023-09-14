import requests
import json

# get items for game=appid as json
url = "https://steamcommunity.com/market/search/render/"
payload = {
    "search_description": "0",
    "appid": "730",
    "sort_column": "default",
    "sort_dir": "desc",
    "norender": "1",
    "count": "100",
}


data = requests.get(url, params=payload)
data_json = data.json()

with open("api/data.json", "w") as f:
    f.write(json.dumps(data_json, indent=4))
