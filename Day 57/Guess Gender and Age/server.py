import requests
from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def home():
#     year = datetime.date.today()
#     copyright_year = year.year
#     random_number = random.randint(1, 10)
#     return render_template("index.html", num=random_number, year=copyright_year)

@app.route("/guess/<name>")
def guess_gender_age(name):
    age = requests.get(url=f'https://api.agify.io?name={name}').json()
    gender = requests.get(url=f'https://api.genderize.io?name={name}').json()
    data = {
        "age": age['age'],
        "gender": gender['gender'],
        "name": name.title()
    }
    return render_template("guess.html", data=data)




if __name__ == "__main__":
    app.run(debug=True)
