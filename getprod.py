import requests
import json

all_url = 'https://api.squarespace.com/1.0/commerce/products'
headers = {'Authorization': 'Bearer b7d97a8e-a112-4893-bd98-2b3fe5a9e1e5', 'user-agent': 'GPT_Test'}

choice = int(input('Fetch all products? \n'
                   'Enter 1 for Yes or 2 for No: '))


def pid(x):
    url = 'https://api.squarespace.com/1.0/commerce/products/'
    updated_url = url + x
    return updated_url


while choice == 1:
    all_prod = requests.get(all_url, headers=headers)
    print(all_prod.text)
    break
else:
    single_url = pid(input('Enter product ID: '))
    r = requests.get(single_url, headers=headers)
    print(json.dumps(r.text))
