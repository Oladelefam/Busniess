from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# My app

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy()

@app.route("/")

def index():
    return render_template("Main.html")

    

if __name__ == "__main__":
    app.run(debug=True)