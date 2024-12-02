import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
BASE_URL = os.getenv('BASE_URL')

if not API_TOKEN or not BASE_URL:
    print(API_TOKEN, BASE_URL)

headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'accept': 'application/json'
}

def get_data(endpoint):
    url = f'{BASE_URL}/{endpoint}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def get_all_data(endpoint):
    url = f'{BASE_URL}/{endpoint}'
    final_data = []

    init_response = requests.get(url, headers=headers)
    data = init_response['data']
    final_data.extend(data)

    while data:
        cursor = response['version']['max']
        response = requests.get(url + f'?after={cursor}', headers=headers)

        if response['data']:
            data = response['data']
            final_data.append(data)
        else:
            data = None
            break
    
    return final_data
