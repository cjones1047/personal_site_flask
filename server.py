from flask import Flask
from flask import render_template

app = Flask(__name__)


# print(__name__)


@app.route('/')
def home():
    return render_template("casey.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
