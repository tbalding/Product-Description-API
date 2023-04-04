# Welcome to the Product Description Generator

The Product Description Generator utilizes Squarespace’s Products API and OpenAI’s API to automatically generate and publish product descriptions. The more details added to the product, such as title, images, and dimensions, the more accurate the description output.

## Setup

To begin using, generate authorization tokens through the Developer API Keys panel of the designated Squarespace site, ensuring that product permissions are set to read and write:

https://support.squarespace.com/hc/en-us/articles/236297987-Squarespace-API-keys#toc-api-key-security

As well as through your OpenAI account:

https://platform.openai.com/account/api-keys

These tokens will then be added to your directory’s .env file as  `OPEN_AI_KEY`  and  `SQSP_KEY`.

The app.py file can then be launched from a code editor, such as  [Pycharm](https://www.jetbrains.com/pycharm/download/#section=mac). To interact with the API, I recommend using the  [Postman Desktop Agent](https://learning.postman.com/docs/getting-started/installation-and-updates/#installing-the-postman-desktop-agent).

## Using the API

Replace  `product_id`  with the desired Product ID.

**Retrieve info for all products:**

	GET http://localhost:5002/all

**Retrieve info for a single product:**

	GET http://localhost:5002/single/product_id

**Generate a description without updating the product:**

	POST http://localhost:5002/describe/product_id

**Generate a description and update the product:**

	PUT http://localhost:5002/update/product_id

**Delete the product description:**

	DELETE http://localhost:5002/delete/product_id
