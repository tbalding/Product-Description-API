import requests
import json


headers = {'Authorization': 'Bearer b7d97a8e-a112-4893-bd98-2b3fe5a9e1e5', 'user-agent': 'GPT_Test'}


def pid(x):
    url = 'https://api.squarespace.com/1.0/commerce/products/'
    updated_url = url + x
    r = requests.get(updated_url, headers=headers)
    # return json.dumps(r.text)
    return r.text