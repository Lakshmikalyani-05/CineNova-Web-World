from flask import Flask, jsonify, send_from_directory
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/movies")
def get_movies():
    with open(os.path.join(BASE_DIR, "backend", "movies.json"), "r", encoding="utf-8") as file:
        movies = json.load(file)
    return jsonify(movies)

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)