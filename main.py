from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy
from models import db, Product  # importing db models from models.py
from sqlalchemy import func

from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

from wtforms.validators import DataRequired, URL
from wtforms import StringField, SubmitField, SelectField, PasswordField
from werkzeug.security import generate_password_hash, check_password_hash

import random

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db.init_app(app)

db = SQLAlchemy()

Bootstrap(app)


# Routes
@app.route("/")
def home():
    # random_products = Product.query.order_by(func.random()).limit(3).all()  # Random products
    # categories = ["Shirts for Men", "Shirts for Women", "T-Shirts for Men", "T-Shirts for Women", ...]
    #
    # products_by_category = {}  # Dictionary to store products by category
    # for category in categories:
    #     products = Product.query.filter_by(category=category).limit(3).all()
    #     products_by_category[category] = products
    #
    # return render_template('index.html', random_products=random_products, categories=categories,
    #                        products=products_by_category)
    return render_template('index.html')


@app.route("/who", methods=['GET', 'POST'])
def who():
    return render_template("who.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    pass


if __name__ == '__main__':
    app.run(debug=True)
