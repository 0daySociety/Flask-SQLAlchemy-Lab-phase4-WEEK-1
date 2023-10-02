from models import db,Restaurant_Pizzas,Restaurants,Pizzas
from random import randint, choice as rc

from faker import Faker

from app import app


with app.app_context():
    
    Restaurant_Pizzas.query.delete()
    Pizzas.query.delete()
    Restaurants.query.delete()


    pizza_uno =Pizzas(
        name="Dimino's",
        ingredients="wheat,cheese,onions")
    db.session.add(pizza_uno)

    pizza_dos=Pizzas(
        name ="Pepperoni Passion",
        ingredients="Dough,Tomato Sauce,Mozzarella Cheese,Pepperoni")
    db.session.add(pizza_dos)

    pizza_tres=Pizzas(
        name="Veggie Supreme",
        ingredients="Green Bell Peppers,Onions,Black Olives,Sausage"
    )
    db.session.add(pizza_tres)

    restaurant_uno=Restaurants(
        name="Tony's Pizzeria",
        address="P.O. Box 1234",

    )
    db.session.add(restaurant_uno)
    restaurant_dos=Restaurants(
        name="Ristorante Italiano",
        address= "P.O. Box 5678",

    )
    db.session.add(restaurant_dos)

    restaurant_tres=Restaurants(
        name="Taco Fiesta",
        address ="P.O. Box 2222"

    )

    db.session.add(restaurant_tres)

    Rp_uno=Restaurant_Pizzas(
        price=1000,
        pizza=pizza_uno,
        restaurant=restaurant_uno

    )
    db.session.add(Rp_uno)

    RP_dos=Restaurant_Pizzas(
        price=670,
        pizza=pizza_dos,
        restaurant=restaurant_dos
    )
    db.session.add(RP_dos)

    RP_tres=Restaurant_Pizzas(
        price=780,
        pizza=pizza_tres,
        restaurant=restaurant_tres
    )

    db.session.add(RP_tres)
    db.session.commit()








   
        
