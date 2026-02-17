from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("Home.html")


#Data base
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class MyFinance(db.Model):
    Expense = db.Column(db.String(100), nullable=False)
    Cost = db.Column(db.Float, primary_key=True)
    Date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(100), nullable=False)
    Describition = db.Column(db.String(100), nullable=False)

 




if __name__ == "__main__":
    app.run(debug=True)