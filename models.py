from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text)
    phone_number = db.Column(db.String(20))
    orders = db.relationship('Order', backref='buyer')
    # Other profile fields


class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.Text)
    phone_number = db.Column(db.String(20))
    products = db.relationship('Product', backref='seller')
    orders = db.relationship('Order', backref='seller')
    # Other seller fields


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    category = db.Column(db.String(255))
    ideal_for = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    stock_quantity = db.Column(db.Integer)
    seller = db.relationship('Seller', backref='products')
    order_items = db.relationship('OrderItem', backref='product')


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.id'))
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(50))
    buyer = db.relationship('Buyer', backref='orders')
    seller = db.relationship('Seller', backref='orders')


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    product = db.relationship('Product', backref='order_items')

