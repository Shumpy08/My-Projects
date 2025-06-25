import random
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.date.today()
    copyright_year = year.year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=copyright_year)


if __name__ == "__main__":
    app.run(debug=True)
