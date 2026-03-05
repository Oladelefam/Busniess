from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime

app = Flask(__name__)

#Data base
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

# Finance Database
class MyFinance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Expense: {self.expense}"


# Home Page
@app.route("/", methods=["GET", "POST"])


def index():

    
    # Add Data
    expenses = MyFinance.query.order_by(MyFinance.date.desc()).all()
    
    # Total expense 
    total = db.session.query(func.sum(MyFinance.cost))\
        .filter(MyFinance.category != "Income")\
        .scalar() or 0

    # Total income
    income = db.session.query(func.sum(MyFinance.cost))\
        .filter(MyFinance.category == "Income")\
        .scalar() or 0
          
    return render_template("Home.html", expenses=expenses, total=total, income=income)
       
@app.route("/Add", methods=["GET", "POST"])

def Add():
    if request.method == "POST":
        expense = request.form["expense"]
        cost = request.form["cost"]

        new_expense = MyFinance(
            expense=expense,
            cost=float(cost),
            category="General",
            description="None"
        )

        db.session.add(new_expense)
        db.session.commit()
        return redirect("/Add")

    expenses = MyFinance.query.order_by(MyFinance.date).all()
    return render_template("Add.html", expenses=expenses)






if __name__ == "__main__":
    app.run(debug=True)