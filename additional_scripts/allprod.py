import requests
import json


def all_prod():
    url = 'https://api.squarespace.com/1.0/commerce/products'
    headers = {'Authorization': 'Bearer b7d97a8e-a112-4893-bd98-2b3fe5a9e1e5', 'user-agent': 'GPT_Test'}
    r = requests.get(url, headers=headers)
    return r.text
