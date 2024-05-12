import requests
import pprint

params = {
    'q': 'html'
}

response = requests.get('https://api.github.com/search/repositories', params=params)

response_json = response.json()
pprint.pprint(response_json)
print(f'количество репозиториев с использованием html: {response_json["total_count"]}')