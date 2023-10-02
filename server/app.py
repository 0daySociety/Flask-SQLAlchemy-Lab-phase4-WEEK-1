from flask import Flask,make_response,request,jsonify
from models import db,Restaurant_Pizzas,Restaurants,Pizzas
from flask_restful import Api,Resource
from flask_migrate import Migrate


app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///hotel.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.json.compact=False
api =Api(app)


migrate =Migrate(app,db)
# connecting the database with the app instance 
db.init_app(app)

# creating views for the enpoints to return json data  
class restaurants_resource(Resource):
    def get(self):
        # normal quering 
        restaurants = Restaurants.query.all()
        serialized_restaurants = [restaurant.to_dict() for restaurant in restaurants]
        response =make_response(serialized_restaurants,200)
        return response
    def post(self):
        post_restaurant =Restaurants(
            name=request.form.get("name"),
            address=request.form.get("address")
        )
        db.session.add(post_restaurant)
        db.session.commit()
        response =make_response(post_restaurant.to_dict(),201)
        return response 
    
# using the add_resource method that we inherited from the resource class  to add the route 
# to display data from the database to the frontend
api.add_resource(restaurants_resource, "/restaurant")

# endpoints for restaurant using ids 
class restaurant_id(Resource):
    # this view is for accessing the restaurant endpoint using the id 
    def get(self,id):
        restaurant =Restaurants.query.get(id).to_dict()
        response=make_response(restaurant,200)
        return response
    
    def delete(self,id):
        restaurant_delete=Pizzas.query.get(id)
        db.session.delete(restaurant_delete)
        db.session.commit()
        message ={"Status":"Deleted Successfully"}
        response =make_response(jsonify(message),200)
        return response
    
    def patch(self,id):
        restaurant_patch=Pizzas.query.get(id)
        for atr in request.form:
            setattr(restaurant_patch,atr,request.form[atr])
        db.session.add(restaurant_patch)
        db.session.commit()
        response=make_response(restaurant_patch.to_dict(),200)     
        return response
api.add_resource(restaurant_id,"/restaurant/<int:id>")


class pizza_resource(Resource):
    # using the restful method to access the endpoints
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
        db.session.commit()
        response =make_response(post_pizza.to_dict(),201)

        return response    
api.add_resource(pizza_resource, "/pizza")    

# endpoints using ids 
class pizza_id(Resource):
    # adding the valid head's to access perform different data and also to modify it 
    def get(self,id):
        pizza =Pizzas.query.get(id).to_dict()
        response=make_response(pizza,200)
        return response
    
    def delete(self,id):
        pizza_delete=Pizzas.query.get(id)
        db.session.delete(pizza_delete)
        db.session.commit()
        message ={"Status":"Deleted Successfully"}
        response =make_response(jsonify(message),200)
        return response
    
    def patch(self,id):
        pizza_patch=Pizzas.query.get(id)
        for atr in request.form:
            setattr(pizza_patch,atr,request.form[atr])
        db.session.add(pizza_patch)
        db.session.commit()
        response=make_response(pizza_patch.to_dict(),200)     
        return response

api.add_resource(pizza_id,"/pizza/<int:id>")


        
      

         
    


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
        db.session.commit()
        response =make_response(r_pizza.to_dict(),201)
        return response
    

api.add_resource(rp_resource,"/restaurant_pizza")

# endpoints using ids 
class rp_id(Resource):
    def get(self,id):
        rp =Restaurant_Pizzas.query.get(id).to_dict()
        response=make_response(rp,200)
        return response
    
    def delete(self,id):
        rp_delete=Restaurant_Pizzas.query.get(id)
        db.session.delete(rp_delete)
        db.session.commit()
        message ={"Status":"Deleted Successfully"}
        response =make_response(jsonify(message),200)
        return response
    
    def patch(self,id):
        rp_patch=Restaurant_Pizzas.query.get(id)
        for atr in request.form:
            setattr(rp_patch,atr,request.form[atr])
        db.session.add(rp_patch)
        db.session.commit()
        response=make_response(rp_patch.to_dict(),200)     
        return response

api.add_resource(rp_id,"/restaurant_pizza/<int:id>")


if __name__=="__main__":
    app.run(port=5555,debug=True)



