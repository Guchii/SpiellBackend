from flask import Flask, jsonify
from recommendation import recommend

app = Flask(__name__)


@app.route("/")
def home():
    return "Spiel: Movie Recommendation System"


@app.route("/recommend/<name>", methods=["GET"])
def recommendd(name):
    return jsonify(recommend(name))


app.run(debug=True)
