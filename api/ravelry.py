import os
import requests

endpoints = {
    'color_families': 'https://api.ravelry.com/color_families.json',
    'search_yarn': 'https://api.ravelry.com/yarns/search.json?query={query}',
    'get_yarn': 'https://api.ravelry.com/yarns/{yarn_id}.json',
    'list_stash': 'https://api.ravelry.com/people/{username}/stash/list.json'
}

ravelry_username = os.getenv('RAVELRY_USERNAME')
ravelry_password = os.getenv('RAVELRY_PASSWORD')
auth = (ravelry_username, ravelry_password)

ravelry_user = os.getenv('RAVELRY_USER')


def ravelry_get_color_families():
    response = requests.get(endpoints['color_families'], auth=auth)
    response.close()
    return response.text


def ravelry_search_yarn(query: str):
    response = requests.get(endpoints['search_yarn'].format(query = query), auth=auth)
    response.close()
    return response.text


def ravelry_get_yarn(id: int):
    response = requests.get(endpoints['get_yarn'].format(yarn_id = id), auth=auth)
    response.close()
    return response.text


def ravelry_list_stash():
    response = requests.get(endpoints['list_stash'].format(username = ravelry_user), auth=auth)
    response.close()
    return response.text
