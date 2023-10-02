from flask import Flask,make_response,request
from models import db,Restaurant_Pizzas,Restaurants,Pizzas
from flask_restful import Api,Resource
from flask_migrate import Migrate

app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///hotel.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.json.compact=False
api =Api(app)


migrate =Migrate(app,db)

db.init_app(app)

class restaurants_resource(Resource):
    def get(self):
        restaurants = Restaurants.query.all()
        serialized_restaurants = [restaurant.to_dict() for restaurant in restaurants]
        response =make_response(serialized_restaurants,200)
        return response
    

api.add_resource(restaurants_resource, "/restaurant")

class pizza_resource(Resource):
    def get(self):
        pizza = Pizzas.query.all()
        serialized_pizza = [pizza.to_dict() for pizza in pizza]
        response =make_response(serialized_pizza,200)
        return response
    def post(self):
        post_pizza =Pizzas(
            name=request.form.get("name"),
            ingredients=request.form.get("ingredients")
        )
        db.session.add(post_pizza)
        response =make_response(post_pizza.to_dict(),201)
        return response
        
      

         
    

api.add_resource(pizza_resource, "/pizza")


class rp_resource(Resource):
    def get(self):
        rp = Restaurant_Pizzas.query.all()
        serialized_rp = [rp.to_dict() for rp in rp]
        response =make_response(serialized_rp,200)
        return response
    def post(self):
        r_pizza =Restaurant_Pizzas(
            price=request.form.get("price"),
            restaurant_id=request.form.get("restaurant_id"),
            pizza_id=request.form.get("pizza_id"))
        
        db.session.add(r_pizza)
        response =make_response(r_pizza.to_dict(),201)
        return response
    

api.add_resource(rp_resource,"/restaurant_pizza")


class pizza_id(Resource):
    def get(self,id):
        pizza =Pizzas.query.get(id).to_dict()
        response=make_response(pizza,200)
        return  response
    
    


    
api.add_resource(pizza_id,"/pizza/<int:id>")



if __name__=="__main__":
    app.run(port=5555,debug=True)



