# Author David kimemia Thuku


# Flask Code Challenge - Pizza Restaurants
This is a Flask API code challenge that involves working with a Pizza Restaurant domain. my  
task is to build a Flask API with the specified functionality. Below, you'll find details about the models, validations, routes, and how to test the endpoints.

# Models
You need to create the following relationships in your database:

A Restaurant has many Pizzas through RestaurantPizza.
A Pizza has many Restaurants through RestaurantPizza.
A RestaurantPizza belongs to a Restaurant and belongs to a Pizza.
Start by creating the models and migrations for the database tables as depicted in the provided domain diagram.

# Validations
RestaurantPizza Model Validations:

Each RestaurantPizza must have a price between 1 and 30.
Restaurant Model Validations:

Each Restaurant must have a name less than 50 characters in length.
Each Restaurant must have a unique name.
Routes
# Set up the following routes in your Flask API. Make sure to return JSON data in the specified format along with the appropriate HTTP verb.

# GET /restaurants
Returns JSON data in the following format:
json

[
{"id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue"},
{
  "id": 2,
  "name": "Pizza Hut",
"address": "Westgate Mall, Mwanzi Road, Nrb 100"}
]

# GET /restaurants/:id
If the Restaurant exists, return JSON data in the following format:
json

{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

# If the Restaurant does not exist, return the following JSON data along with the appropriate HTTP status code:
json

{
  "error": "Restaurant not found"
}


# DELETE /restaurants/:id
If the Restaurant exists, it should be removed from the database, along with any RestaurantPizzas that are associated with it. After deleting the Restaurant, return an empty response body along with the appropriate HTTP status code.

If the Restaurant does not exist, return the following JSON data along with the appropriate HTTP status code:

json

{
  "error": "Restaurant not found"
}

# GET /pizzas
Returns JSON data in the following format:
json


[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]


# POST /restaurant_pizzas
This route should create a new RestaurantPizza that is associated with an existing Pizza and Restaurant. It should accept an object with the following properties in the body of the request:
json


{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}


# If the RestaurantPizza is created successfully, send back a response with the data related to the Pizza in the following format:
json


{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}

If the RestaurantPizza is not created successfully (e.g., due to validation errors), return the following JSON data along with the appropriate HTTP status code:
json

{
  "errors": ["validation errors"]
}

#Testing
To test your endpoints, you can follow these steps:

Run the Flask server.
Use a tool like Postman to make requests to the defined endpoints.
# MIT License

# Copyright (c) [2023] [David Kimemia Thuku]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

