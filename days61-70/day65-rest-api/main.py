from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy, session
import json
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(
        { "cafe":
            { "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
            }
        }
    )

@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    cafe_dict = {}
    for i in range(len(cafes)):
        cafe_dict[i + 1] = cafes[i].name
    return cafe_dict

@app.route("/search")
def search():
    location = request.args.get('location')
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        if cafe.location == location: # This needs to be redone. Maybe create a new list of cafes that have a location that matches and return JSON with data for all of them.
            cafe_list.append(
                { "cafe":
                    { "name": cafe.name,
                    "map_url": cafe.map_url,
                    "img_url": cafe.img_url,
                    "location": cafe.location,
                    "seats": cafe.seats,
                    "has_toilet": cafe.has_toilet,
                    "has_wifi": cafe.has_wifi,
                    "has_sockets": cafe.has_sockets,
                    "can_take_calls": cafe.can_take_calls,
                    "coffee_price": cafe.coffee_price,
                    }
                }
            )
    if cafe_list != []:
        return cafe_list
    else:
        return jsonify (
            { "error": 
                { "Not Found": "Sorry, no cafes exist at that location"}
            }
        )

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form.get("cafe_name")
        map_url = request.form.get("map_url")
        img_url = request.form.get("img_url")
        location = request.form.get("location")
        seats = request.form.get("seats")
        has_toilets = bool(request.form.get("has_toilets"))
        has_wifi = bool(request.form.get("has_wifi"))
        has_sockets = bool(request.form.get("has_sockets"))
        can_take_calls = bool(request.form.get("can_take_calls"))
        coffee_price = request.form.get("coffee_price")
        new_cafe = Cafe(name=name, map_url=map_url, img_url=img_url, location=location, seats=seats, has_toilet=has_toilets, has_wifi=has_wifi, has_sockets=has_sockets,
        can_take_calls=can_take_calls, coffee_price=coffee_price)
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    return render_template("add.html")

@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new-price")
    cafe_to_update = db.session.query.filter_by(id=id).first()
    if cafe_to_update != None:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": {"Cafe price successfully updated!"}}), 200
    else:
        return jsonify(response={"error": {"Not Found: A cafe with that ID was not found in the database."}}), 404

@app.route("delete-cafe/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    api_key = "apikey"
    user_key = request.args.get("user-key")
    if api_key == user_key:
        cafe_to_delete = db.session.query.filter_by(id=id).first()
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": {"Cafe removed from the database. Thanks for the update!"}}), 200
        else:
            return jsonify(response={"error": {"Not Found: A cafe with that ID was not found in the database."}}), 404
    else:
        return jsonify(response={"error": {"Sorry, you must use the correct API Key!"}})



if __name__ == '__main__':
    app.run(debug=True)
