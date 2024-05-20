import os
import requests

endpoints = {
    'yarn_search': 'https://api.ravelry.com/color_families.json'
}

ravelry_username = os.getenv('RAVELRY_USERNAME')
ravelry_password = os.getenv('RAVELRY_PASSWORD')

def get_yarn():
    auth = (ravelry_username, ravelry_password)
    response = requests.get(endpoints['yarn_search'], auth=auth)
    response.close()
    return response.text

