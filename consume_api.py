import requests
import json

uri = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
response = requests.get(uri)

for data in response.json()['items']:
    print(data['title'])