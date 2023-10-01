from models import db,Restaurant_Pizzas,Restaurants,Pizzas
from random import randint, choice as rc

from faker import Faker

from app import app



pizzas =[
      "Margherita",
    "Pepperoni Passion",
    "Hawaiian Delight",
    "Veggie Supreme",
    "BBQ Chicken",
    "Meat Lovers",
    "Buffalo Ranch",
    "Mediterranean Magic",
    "Pesto Perfection",
    "Four Cheese",
    "Spinach and Feta",
    "Taco Fiesta",
    "Mushroom Madness",
    "White Garlic",
    "Sausage Sensation",
    "Garden Fresh",
    "Bacon Bliss",
    "Supreme Sizzler",
    "Caprese Classic",
    "The Works"

]


restaurants = [
    "Tony's Pizzeria",
    "Mama Mia Trattoria",
    "The Cheesecake Factory",
    "Ristorante Italiano",
    "Sushi Samba",
    "Cafe Parisienne",
    "The Burger Joint",
    "Taco Fiesta",
    "La Taqueria",
    "Szechuan Palace",
    "Thai Orchid",
    "Casa de Tapas",
    "The Steakhouse Grill",
    "Vegetarian Delight",
    "Seafood Shack",
    "Mediterranean Breeze",
    "Pasta Paradise",
    "Samosa Street",
    "BBQ King",
    "The Veggie Patch"
]


pizza_ingredients = [
    "Dough",
    "Tomato Sauce",
    "Mozzarella Cheese",
    "Pepperoni",
    "Mushrooms",
    "Green Bell Peppers",
    "Onions",
    "Black Olives",
    "Sausage",
    "Bacon",
    "Ham",
    "Pineapple",
    "Jalapenos",
    "Anchovies",
    "Garlic",
    "Oregano",
    "Basil",
    "Red Pepper Flakes",
    "Parmesan Cheese",
    "Olive Oil",
]

list_address=[
     "P.O. Box 1234",
    "P.O. Box 5678",
    "P.O. Box 7890",
    "P.O. Box 2468",
    "P.O. Box 1357",
    "P.O. Box 8642",
    "P.O. Box 9876",
    "P.O. Box 5432",
    "P.O. Box 1010",
    "P.O. Box 2222",

]


fake =Faker()
with app.app_context():
    Pizzas.query.delete()
    Restaurant_Pizzas.query.delete()
    Restaurants.query.delete()


    my_pizzas =[]
    for i in range(50):
        p =Pizzas(name=rc(pizzas),ingredients=rc(pizza_ingredients))
        my_pizzas.append(p)
    db.session.add_all(my_pizzas)    


    my_restaurants=[]
    for i in range(50):
        r =Restaurants(
            name =rc(restaurants),
            address=rc(list_address)
        )
        my_restaurants.append(r)
    db.session.add_all(my_restaurants)

    my_restaurants_pizzas=[]
    for u in my_pizzas:
        for i in range(randint(1,10)):
            x=Restaurant_Pizzas(
               
                 price =randint(1,1000),
                 restaurant=rc(my_restaurants),
                 pizza =u)
            my_restaurants_pizzas.append(x)

    db.session.add_all(my_restaurants_pizzas)
    db.session.commit()
        
