from flask import Flask
from models import db,Restaurant_Pizzas,Restaurants,Pizzas
from flask_restful import Api
from flask_migrate import Migrate

app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///hotel.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

migrate =Migrate(app,db)
db.init_app(app)


