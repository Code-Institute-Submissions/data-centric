import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_properties")
def get_properties():
    properties = list(mongo.db.Properties.find())
    return render_template("properties.html", properties=properties)


@app.route("/add_property", methods=["GET", "POST"])
def add_property():
    if request.method == "POST":
        Viewing_Available = "yes" if request.form.get("Viewing_Available") else "no"
        Properties = {
            "PropertyType_Name": request.form.get("PropertyType_Name"),
            "Properties_Name": request.form.get("Properties_Name"),
            "Properties_Description": request.form.get("Properties_Description"),
            "Viewing_Available": Viewing_Available,
            "Auction_Date": request.form.get("Auction_Date"),
            "Img_URL": request.form.get("Img_URL")
        }
        mongo.db.Properties.insert_one(Properties)
        flash("Property added successfully")
        return redirect(url_for("get_properties"))
        
    propertytypes = mongo.db.PropertyType.find().sort("PropertyType_Name", 1)
    return render_template("add_property.html", propertytypes=propertytypes)


@app.route("/edit_property/<property_id>", methods=["GET", "POST"])
def edit_property(property_id):

    if request.method == "POST":
        Viewing_Available = "yes" if request.form.get("Viewing_Available") else "no"
        enter = {
            "PropertyType_Name": request.form.get("PropertyType_Name"),
            "Properties_Name": request.form.get("Properties_Name"),
            "Properties_Description": request.form.get("Properties_Description"),
            "Viewing_Available": Viewing_Available,
            "Auction_Date": request.form.get("Auction_Date"),
            "Img_URL": request.form.get("Img_URL")
        }
        mongo.db.Properties.update({"_id": ObjectId(property_id)}, enter)
        flash("Property updated successfully")

    property = mongo.db.Properties.find_one({"_id": ObjectId(property_id)})
    propertytypes = mongo.db.PropertyType.find().sort("PropertyType_Name", 1)
    return render_template("edit_property.html", property=property, propertytypes=propertytypes)


@app.route("/delete_property/<property_id>")
def delete_property(property_id):
    mongo.db.Properties.remove({"_id": ObjectId(property_id)})
    flash("Task deleted successfully")
    return redirect(url_for("get_properties"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
