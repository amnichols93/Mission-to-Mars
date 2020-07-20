from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrapingChallenge

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app_challenge"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("indexChallenge.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrapingChallenge.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return render_template("scrape.html", mars=mars)

@app.route("/hem1")
def hem1():
    mars = mongo.db.mars.find_one()
    return render_template("Hem1.html", mars=mars)

@app.route("/hem2")
def hem2():
    mars = mongo.db.mars.find_one()
    return render_template("Hem2.html", mars=mars)

@app.route("/hem3")
def hem3():
    mars = mongo.db.mars.find_one()
    return render_template("Hem3.html", mars=mars)

@app.route("/hem4")
def hem4():
    mars = mongo.db.mars.find_one()
    return render_template("Hem4.html", mars=mars)

if __name__ == "__main__":
    app.run()

