from flask import Flask
from flask import render_template
from datetime import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API")
app = Flask(__name__)


def guess_age(name):
    age_url = f"https://api.agify.io/?name={name}"
    response = requests.get(url=age_url).json()
    # response = {"count":341,"name":"sharma","age":65}
    age = response["age"]
    return age


def guess_gender(name):
    gender_url = f"https://api.genderize.io?name={name}"
    response = requests.get(gender_url).json()
    gender = response["gender"]
    return gender


@app.route("/")
def server_main():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)


@app.route("/guess/<name>")
def guess(name):
    age = guess_age(name)
    gender = guess_gender(name)
    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
