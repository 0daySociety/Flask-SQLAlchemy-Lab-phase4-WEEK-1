from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })

db = SQLAlchemy()

class Pizzas(db.Model,SerializerMixin):
    __tablename__="pizzas"

    serialize_rules=('-restaurant_pizzas.pizza',)


  
    
    id =db.Column(db.Integer,primary_key =True)
    name =db.Column(db.String)
    ingredients =db.Column(db.String)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at =db.Column(db.DateTime,server_default =db.func.now())


    restaurant_pizzas=db.relationship("Restaurant_Pizzas",backref="pizza")

    def __repr__(self):
        return f"name is {self.name} , ingredients is {self.ingredients} "
    
class Restaurant_Pizzas(db.Model,SerializerMixin):
    __tablename__="restaurant_pizzas"

    serialize_rules=('-pizza.restaurant_pizzas','-restaurant.restaurant_pizzas')
   
    id =db.Column(db.Integer,primary_key=True)
    pizza_id =db.Column(db.Integer,  db.ForeignKey("pizzas.id"))
    restaurant_id=db.Column(db.Integer,db.ForeignKey("restaurants.id"))

    price=db.Column(db.Integer())
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,server_default=db.func.now())

    def __repr__(self):
        return f"prize is {self.price}"
    
class Restaurants(db.Model,SerializerMixin):

    __tablename__="restaurants"

    serialize_rules=('-restaurant_pizzas.restaurant',)

  
    id =db.Column(db.Integer,primary_key =True,nullable=False)
    name =db.Column(db.String())
    address=db.Column(db.String())    
    restaurant_pizzas=db.relationship('Restaurant_Pizzas',backref="restaurant")

def __repr__(self):
        return f"name is {self.name} , address is {self.address}"