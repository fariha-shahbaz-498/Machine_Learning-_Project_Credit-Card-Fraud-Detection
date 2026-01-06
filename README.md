# Machine_Learning-_Project_Credit-Card-Fraud-Detection
credit Card Fraud Detection model using Python &amp; Logistic Regression
# Credit Card Fraud Detection using Machine Learning

## 📌 Project Overview

This project demonstrates a **Credit Card Fraud Detection system** built using **Python** and **Machine Learning**. The goal is to classify transactions as **fraudulent** or **non-fraudulent** based on transaction-related features.

The project uses **Logistic Regression**, a widely used classification algorithm, and focuses on understanding the end-to-end ML workflow.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* VS Code

---

## 📂 Dataset

The dataset (`credit_card_fraud_data.csv`) contains the following features:

| Column Name              | Description                                |
| ------------------------ | ------------------------------------------ |
| transaction_amount       | Amount of the transaction                  |
| is_unusual_location      | 1 if location is unusual, else 0           |
| time_since_last_txn_mins | Minutes since last transaction             |
| is_fraudulent            | Target variable (1 = Fraud, 0 = Not Fraud) |

---

## ⚙️ Workflow

1. Load dataset using Pandas
2. Explore and inspect data
3. Select relevant features
4. Split data into training and testing sets
5. Train Logistic Regression model
6. Evaluate model using accuracy score
7. Predict fraud on new transaction data

---

## 🧠 Model Used

**Logistic Regression**

* Simple and effective for binary classification
* Easy to interpret
* Performs well on structured datasets

---

## 📊 Results

* **Training Accuracy:** 92.5%
* **Testing Accuracy:** 100% (on sample dataset)

> Note: High accuracy on small datasets may indicate overfitting. Future improvements are planned.

---

## ▶️ How to Run the Project

1. Clone the repository or download the files
2. Install dependencies:

   ```bash
   pip install pandas scikit-learn
   ```
3. Run the Python script:

   ```bash
   python credit_card_fraud_data.py
   ```

---

## 🔮 Future Improvements

* Feature scaling using StandardScaler
* Handle class imbalance
* Use advanced models (Random Forest, XGBoost)
* Add confusion matrix & ROC curve
* Use larger real-world datasets

---

## 📌 Conclusion

This project provides hands-on experience with machine learning classification and fraud detection concepts. It serves as a strong foundation for building more advanced financial security systems.

---

## 📬 Contact

If you have suggestions or feedback, feel free to connect!

Happy Learning 🚀
