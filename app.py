import os
from dotenv import load_dotenv
from flask import Flask, render_template
import requests
import openai


app = Flask(__name__, template_folder='template_files', static_folder='static_files')

# save keys to .env file
load_dotenv()
openai.api_key = os.getenv("OPEN_AI_KEY")
SQSP_key = os.getenv("SQSP_KEY")
headers = {'Authorization': SQSP_key, 'User-Agent': 'Product_Description_Generator', 'Content-Type': 'application/json'}


def pid(x):
    url = 'https://api.squarespace.com/1.0/commerce/products/'
    updated_url = url + x
    r = requests.get(updated_url, headers=headers)
    return r.text


def all_prod():
    url = 'https://api.squarespace.com/1.0/commerce/products/'
    r = requests.get(url, headers=headers)
    return r.text


def generate_product_description(obj):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # The content prompt can be adjusted to alter the description output
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


# retrieve all product info
@app.route('/all', methods=['GET'])
def allprod():
    result = all_prod()
    return result


# retrieve info for a single product based off ID
@app.route('/single/<string:id>', methods=['GET'])
def singleprod(id: str):
    result = pid(id)
    return result


# generate a product description without updating the product
@app.route('/describe/<string:product_id>', methods=['POST'])
def describe(product_id: str):
    obj = pid(product_id)
    product_description = generate_product_description(obj)
    return product_description


# generate and update product description
@app.route('/update/<string:product_id>', methods=['PUT'])
def update(product_id: str):
    obj = pid(product_id)
    product_description = generate_product_description(obj)
    data = {"description": product_description}
    url = 'https://api.squarespace.com/1.0/commerce/products/' + product_id
    r = requests.post(url, headers=headers, json=data)
    return r.text


# delete existing product description
@app.route('/delete/<string:product_id>', methods=['DELETE'])
def delete(product_id: str):
    data = {"description": ""}
    url = 'https://api.squarespace.com/1.0/commerce/products/' + product_id
    r = requests.post(url, headers=headers, json=data)
    return r.text


@app.route('/')
def welcome():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5002, debug=True)
