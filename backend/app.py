from flask import Flask
import json

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/")
def home():
    return "CineNova Backend is Working!"

@app.route("/movies")
def get_movies():
    with open("backend/movies.json", "r", encoding="utf-8") as file:
        movies = json.load(file)
    return movies

if __name__ == "__main__":
    app.run(debug=True)