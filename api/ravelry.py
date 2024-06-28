import json
import os
import requests

endpoints = {
    'color_families': 'https://api.ravelry.com/color_families.json',
    'search_yarn': 'https://api.ravelry.com/yarns/search.json?query={query}',
    'get_yarn': 'https://api.ravelry.com/yarns/{yarn_id}.json',
    'list_stash': 'https://api.ravelry.com/people/{username}/stash/{stash_id}.json',
    'create_stash': 'https://api.ravelry.com/people/{username}/stash/create.json',
    'update_pack': 'https://api.ravelry.com/packs/{pack_id}.json'
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


def ravelry_list_stash(id: str):
    response = requests.get(endpoints['list_stash'].format(username = ravelry_user, stash_id = id), auth=auth)
    response.close()
    return response.text


def ravelry_create_stash():
    stash_params = {
        "yarn_id": 209189,
        "pack": {
            "colorway": "8080",
            "skeins": "2",
            "purchased_date": "1997-08-01",
            "total_paid": "17.38",
            "total_paid_currency": "USD"
        }
    }
    print("DEBUG: {fstash_params}".format(fstash_params=json.dumps(stash_params)))

    response = requests.post(endpoints['create_stash'].format(username = ravelry_user), auth=auth,
                             data=json.dumps(stash_params))
    response.close()
    return response.text


def ravelry_update_pack(pack_id: str):
    pack_params = {
        "colorway": "8080",
        "skeins": "2",
        "purchased_date": "1997-08-01",
        "total_paid": "17.38",
        "total_paid_currency": "USD"
    }

    response = requests.put(endpoints['update_pack'].format(pack_id = pack_id), auth=auth,
                            params=json.dumps(pack_params))
    return response.text