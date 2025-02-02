from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
import joblib

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.secret_key = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "churn_prediction.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)
model = joblib.load("logistic_regression_churn.pkl")

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



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_customer", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        try:
            name = request.form["name"]
            mobile = request.form["mobile"]
            email = request.form["email"]
            location = request.form["location"]

            new_customer = Customer(name=name, mobile=mobile, email=email, location=location)
            db.session.add(new_customer)
            db.session.commit()

            flash("✅ Customer added successfully!", "success")
            return redirect(url_for("index"))
        except Exception as e:
            db.session.rollback()
            flash(f"❌ Error adding customer: {e}", "danger")
            return redirect(url_for("add_customer"))

    return render_template("add_customer.html")

@app.route("/add_record", methods=["GET", "POST"])
def add_record():
    customers = Customer.query.all()

    if request.method == "POST":
        try:
            customer_id = request.form["customer_id"]
            gender = int(request.form["gender"])
            senior_citizen = int(request.form["senior_citizen"])
            partner = int(request.form["partner"])
            dependents = int(request.form["dependents"])
            tenure = int(request.form["tenure"])
            phone_service = int(request.form["phone_service"])
            multiple_lines = int(request.form["multiple_lines"])
            internet_service = request.form["internet_service"]
            online_security = int(request.form["online_security"])
            online_backup = int(request.form["online_backup"])
            device_protection = int(request.form["device_protection"])
            tech_support = int(request.form["tech_support"])
            streaming_tv = int(request.form["streaming_tv"])
            streaming_movies = int(request.form["streaming_movies"])
            contract_type = request.form["contract_type"]
            paperless_billing = int(request.form["paperless_billing"])
            payment_method = request.form["payment_method"]
            monthly_charges = float(request.form["monthly_charges"])
            total_charges = float(tenure * monthly_charges)

            contract_one, contract_two = (1, 0) if contract_type == "One Year" else (0, 1) if contract_type == "Two Year" else (0, 0)
            payment_credit = 1 if payment_method == "credit_card_automatic" else 0
            payment_echeck = 1 if payment_method == "electronic_check" else 0
            payment_mailed = 1 if payment_method == "mailed_check" else 0
            internet_fiber = 1 if internet_service == "fiber_optic" else 0
            internet_no = 1 if internet_service == "no" else 0

            new_record = Record(
                customer_id=customer_id,
                gender=gender,
                senior_citizen=senior_citizen,
                partner=partner,
                dependents=dependents,
                tenure=tenure,
                phone_service=phone_service,
                multiple_lines=multiple_lines,
                internet_service=internet_service,
                online_security=online_security,
                online_backup=online_backup,
                device_protection=device_protection,
                tech_support=tech_support,
                streaming_tv=streaming_tv,
                streaming_movies=streaming_movies,
                contract=contract_type,
                paperless_billing=paperless_billing,
                payment_method=payment_method,
                monthly_charges=monthly_charges,
                total_charges=total_charges
            )
            db.session.add(new_record)
            db.session.commit()

            flash("✅ Record added successfully!", "success")
            return redirect(url_for("index"))
        
        except Exception as e:
            db.session.rollback()
            flash(f"❌ Error adding record: {e}", "danger")
            return redirect(url_for("add_record"))

    return render_template("add_record.html", customers=customers)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    customers = Customer.query.all()
    records = None
    selected_customer_id = None
    prediction = None
    probability = None
    risk_level = None

    if request.method == "POST":
        selected_customer_id = request.form["customer_id"]
        records = Record.query.filter_by(customer_id=selected_customer_id).all()

    return render_template("predict.html", customers=customers, records=records, prediction=prediction, probability=probability, risk_level=risk_level, selected_customer_id=selected_customer_id)

@app.route("/predict_churn", methods=["POST"])
def predict_churn():
    customer_id = request.form["customer_id"]

    records = Record.query.filter_by(customer_id=customer_id).all()

    if not records:
        return redirect(url_for("predict"))

    try:
        # Prepare the DataFrame with all required fields for the model
        df = pd.DataFrame([{
            "gender": r.gender,
            "SeniorCitizen": r.senior_citizen,
            "Partner": r.partner,
            "Dependents": r.dependents,
            "tenure": r.tenure,
            "PhoneService": r.phone_service,
            "MultipleLines": r.multiple_lines,
            "OnlineSecurity": r.online_security,
            "OnlineBackup": r.online_backup,
            "DeviceProtection": r.device_protection,
            "TechSupport": r.tech_support,
            "StreamingTV": r.streaming_tv,
            "StreamingMovies": r.streaming_movies,
            "PaperlessBilling": r.paperless_billing,
            "MonthlyCharges": r.monthly_charges,
            "TotalCharges": r.total_charges,
            "Contract_One year": 1 if r.contract == "One Year" else 0,
            "Contract_Two year": 1 if r.contract == "Two Year" else 0,
            "PaymentMethod_Credit card (automatic)": 1 if r.payment_method == "Credit card (automatic)" else 0,
            "PaymentMethod_Electronic check": 1 if r.payment_method == "Electronic check" else 0,
            "PaymentMethod_Mailed check": 1 if r.payment_method == "Mailed check" else 0,
            "InternetService_Fiber optic": 1 if r.internet_service == "Fiber optic" else 0,
            "InternetService_No": 1 if r.internet_service == "No" else 0
        } for r in records], columns=[
            "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", 
            "MultipleLines", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", 
            "StreamingTV", "StreamingMovies", "PaperlessBilling", "MonthlyCharges", "TotalCharges", 
            "Contract_One year", "Contract_Two year", "PaymentMethod_Credit card (automatic)", 
            "PaymentMethod_Electronic check", "PaymentMethod_Mailed check", 
            "InternetService_Fiber optic", "InternetService_No"
        ])


        # Ensure the model is trained and aligned with the feature names
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)[:, 1]

        # Update database records with predictions and probabilities
        for i, record in enumerate(records):
            record.prediction = int(predictions[i])
            record.probability = float(probabilities[i])

        db.session.commit()
        flash("✅ Churn Prediction updated successfully!", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"❌ Error predicting churn: {e}", "danger")

    return redirect(url_for("predict"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
