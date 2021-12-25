from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data":data,
        "message":"Star found",
    }),200

@app.route("/Star")

def Star():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["Star_name"] == name)
    return jsonify({
        "star_data":planet_data,
        "message":"data shown"
    }),200

if __name__ == "__main__":
    app.run()

