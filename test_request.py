import requests

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


f = requests.get(url, params=payload)
print(f.json())