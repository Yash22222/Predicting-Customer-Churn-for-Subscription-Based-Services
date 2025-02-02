from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "churn_prediction.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = "customer"
    
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(50))

    records = db.relationship("Record", backref="customer", cascade="all, delete-orphan")

class Record(db.Model):
    __tablename__ = "records"

    record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.customer_id"), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    senior_citizen = db.Column(db.Integer, nullable=False)
    partner = db.Column(db.Integer, nullable=False)
    dependents = db.Column(db.Integer, nullable=False)
    tenure = db.Column(db.Integer, nullable=False)
    phone_service = db.Column(db.Integer, nullable=False)
    multiple_lines = db.Column(db.Integer, nullable=False)
    internet_service = db.Column(db.String(50), nullable=False)
    online_security = db.Column(db.Integer, nullable=False)
    online_backup = db.Column(db.Integer, nullable=False)
    device_protection = db.Column(db.Integer, nullable=False)
    tech_support = db.Column(db.Integer, nullable=False)
    streaming_tv = db.Column(db.Integer, nullable=False)
    streaming_movies = db.Column(db.Integer, nullable=False)
    contract = db.Column(db.String(20), nullable=False)
    paperless_billing = db.Column(db.Integer, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    monthly_charges = db.Column(db.Float, nullable=False)
    total_charges = db.Column(db.Float, nullable=False)
    prediction = db.Column(db.Integer, nullable=True)
    probability = db.Column(db.Float, nullable=True)

# Initialize Database
with app.app_context():
    db.create_all()
    print("✅ Database initialized successfully.")
