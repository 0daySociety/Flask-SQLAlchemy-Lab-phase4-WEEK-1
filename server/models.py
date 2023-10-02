from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })
# creating an object instance  in sqlalchemy to be able to access the methods in the class
db = SQLAlchemy()

class Pizzas(db.Model,SerializerMixin):
    __tablename__="pizzas"
# adding serlization rule 
    serialize_rules=('-restaurant_pizzas.pizza',)


#   adding columns ass attributes in the table
    
    id =db.Column(db.Integer,primary_key =True)
    name =db.Column(db.String)
    ingredients =db.Column(db.String)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at =db.Column(db.DateTime,server_default =db.func.now())

#one to many relationships
    restaurant_pizzas=db.relationship("Restaurant_Pizzas",backref="pizza")

    def __repr__(self):
        return f"name is {self.name} , ingredients is {self.ingredients} "
    
class Restaurant_Pizzas(db.Model,SerializerMixin):
    __tablename__="restaurant_pizzas"

    serialize_rules=('-pizza.restaurant_pizzas','-restaurant.restaurant_pizzas')
#    attributes as table columns
    id =db.Column(db.Integer,primary_key=True)
    pizza_id =db.Column(db.Integer,  db.ForeignKey("pizzas.id"))
    restaurant_id=db.Column(db.Integer,db.ForeignKey("restaurants.id"))

    price=db.Column(db.Integer())
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,server_default=db.func.now())
# adding validator to the price attribute in the table 
    @validates('price')
    def validate_price(self,key,price):
         if price not in range(1,31):
            #   raising error message if the condition is not met 
              raise ValueError("price must be in the range of 1 and 30")
         else:
              return price

    def __repr__(self):
        return f"prize is {self.price}"
    
class Restaurants(db.Model,SerializerMixin):

    __tablename__="restaurants"

    serialize_rules=('-restaurant_pizzas.restaurant',)

  
    id =db.Column(db.Integer,primary_key =True,nullable=False)
    name =db.Column(db.String() ,unique=True)
    address=db.Column(db.String())    
    #one to many relationships
    restaurant_pizzas=db.relationship('Restaurant_Pizzas',backref="restaurant")
# validator for the name attribute 
    @validates('name')
    def validates_name(self,key,name):
         if len(name) >50:
              raise ValueError("Restaurant name must be less that 50 characters")
         else :
              return name

   
         

def __repr__(self):
        return f"name is {self.name} , address is {self.address}"