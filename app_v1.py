from flask import Flask
# from singleprod import pid
# from allprod import all_prod
import requests
import openai


app = Flask(__name__)

openai.api_key = "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"


headers = {'Authorization': 'Bearer b7d97a8e-a112-4893-bd98-2b3fe5a9e1e5', 'user-agent': 'GPT_Test', 'Content-Type': 'application/json'}


def pid(x):
    url = 'https://api.squarespace.com/1.0/commerce/products/'
    updated_url = url + x
    r = requests.get(updated_url, headers=headers)
    return r.text


def all_prod():
    url = 'https://api.squarespace.com/1.0/commerce/products'
    r = requests.get(url, headers=headers)
    return r.text


def generate_product_description(obj):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "This JSON object represents a product on my website. Can you write me a short product description that suggests ways the product can be used? "},
            {"role": "user", "content": obj}
                  ],
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.7,
    )
    description = response['choices'][0]['message']['content']
    return description


@app.route('/all')
def allprod():
    result = all_prod()
    return result


@app.route('/single/<string:id>')
def single_param(id: str):
    result = pid(id)
    return result


@app.route('/describe/<string:product_id>')
def describe(product_id: str):
    obj = pid(product_id)
    product_description = generate_product_description(obj)
    return product_description


@app.route('/update/<string:product_id>', methods=['POST'])
def update(product_id: str):
    obj = pid(product_id)
    product_description = generate_product_description(obj)
    data = {"description": product_description}
    url = 'https://api.squarespace.com/1.0/commerce/products/' + product_id
    r = requests.post(url, headers=headers, json=data)
    return r.text


if __name__ == '__main__':
    app.run(port=5002)
