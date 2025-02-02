# 📊 Predicting Customer Churn for Subscription-Based Services 

## 🚀 Project Overview  
This project aims to **predict customer churn** based on various features like customer tenure, monthly charges, payment methods, and contract types. The system not only predicts churn but also **automates customer retention strategies** by sending promotional SMS and emails to at-risk customers.  

### 🔥 **Why This Project?**
- **Business Impact:** Helps businesses **reduce churn** by taking proactive retention actions.  
- **Automation:** Auto-generates **personalized retention offers** for high-risk customers.  
- **Data-Driven:** Uses machine learning models to predict churn probabilities.  

---

## 🛠️ **Tech Stack**
- **Backend:** Flask, SQLAlchemy (Database ORM)  
- **Frontend:** HTML, CSS, JavaScript  
- **Machine Learning:** Scikit-learn, XGBoost  
- **Database:** SQLite (Can be extended to PostgreSQL, MySQL)  
- **Third-Party APIs:** Twilio (for SMS notifications), Google Generative AI (for personalized retention messages)  

---

## 📌 **Features**
### ✅ Customer Management  
- Add new customers with **name, mobile, email, location**.  
- Store customer **subscription & service details** in a structured database.  

### 🔮 **Churn Prediction & Retention Strategy**
- Uses **Logistic Regression, Random Forest, and XGBoost** to predict churn.  
- Identifies **high-risk customers** based on churn probability.  
- Generates **personalized retention offers** using **Generative AI**.  
- **Automated SMS & Email notifications** for retention campaigns.  

### 📡 **Model Training & Evaluation**
- Trains machine learning models on the **Telco Customer Churn dataset**.  
- Performs **feature engineering, encoding, and scaling** for better performance.  
- Evaluates models using **AUC-ROC, precision-recall, and confusion matrices**.  

---

## 🏗️ **Project Structure**
```
📂 customer-churn-prediction
│-- 📁 static/              # CSS & JS files for frontend
│-- 📁 templates/           # HTML templates for frontend
│-- 📁 models/              # Machine learning models
│-- 📁 database/            # SQLite database files
│-- app.py                  # Main Flask application
│-- db_setup.py             # Database schema & table creation
│-- requirements.txt        # Required Python packages
│-- README.md               # Project documentation
```

---

## 🛠️ **Setup & Installation**
### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Set up the database**
```bash
python db_setup.py
```

### 4️⃣ **Run the Flask application**
```bash
python app.py
```
Open in browser: **http://127.0.0.1:5000/**  

---

## 📊 **Churn Prediction Workflow**
1️⃣ **User selects a customer** from the database.  
2️⃣ **System fetches their service history** and applies the trained model.  
3️⃣ **Churn probability is calculated**, and risk level (High, Medium, Low) is assigned.  
4️⃣ **Retention strategy is suggested** using AI-generated offers.  
5️⃣ If churn probability is **above 70%**, an **automated SMS & email** is sent to the customer.  

---

## 📡 **Deployment**
Can be deployed on:
- **Heroku** (`heroku create && git push heroku main`)
- **AWS (EC2, Lambda)**
- **Render.com**
- **Google Cloud (App Engine, Cloud Run)**

---

## 📧 **Notifications & Retention Strategy**
| Risk Level  | Churn Probability | Suggested Action | Automated Response |
|-------------|------------------|------------------|--------------------|
| 🚨 **High** | > 70% | Special discount offers | **SMS & Email notification** |
| 🤔 **Medium** | 50-70% | Targeted engagement | **Email notification only** |
| ✅ **Low** | < 50% | Retain customer normally | **No action needed** |

---

## 🏆 **Key Achievements**
✅ Successfully trained **3 ML models** for churn prediction.  
✅ **Automated retention strategy** based on prediction results.  
✅ Integrated **Twilio for SMS** and **Google AI for personalized offers**.  
✅ **Web-based UI** to manage customers, records, and predictions.  

---

## 💡 **Future Enhancements**
🔹 **Advanced NLP Sentiment Analysis** (Analyze customer feedback for better predictions).  
🔹 **Dynamic Learning** (Update model based on new data).  
🔹 **Hybrid AI Models** (Combine rule-based and deep learning approaches).  

---

## 🤝 **Contributors**
👨‍💻 **Your Name** - Data Science & ML Engineer  
👩‍💻 **Team Member 2** - Web Developer  
👨‍💻 **Team Member 3** - Database & API Specialist  

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## ⭐ **Support & Feedback**
Found this project useful? **Give it a star ⭐ on GitHub!**  
For feedback & issues, open a **GitHub Issue**.  

---
