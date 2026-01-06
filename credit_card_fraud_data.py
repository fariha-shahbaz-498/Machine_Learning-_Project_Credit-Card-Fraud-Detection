import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score , classification_report
df=pd.read_csv("credit_card_fraud_data.csv")
print(df.head())
X=df[['transaction_amount','is_unusual_location','time_since_last_txn_mins']]
Y=df['is_fraudulent']
X_train,X_test , Y_train , Y_test=train_test_split(X,Y, test_size=0.2, random_state=42)
model=LogisticRegression()
model.fit(X_train,Y_train)
Y_train_pred=model.predict(X_train)
Y_test_pred=model.predict(X_test)
train_accuracy=accuracy_score(Y_train , Y_train_pred)
test_accuracy=accuracy_score(Y_test , Y_test_pred)
print("training accuracy:" ,train_accuracy)
print("training testing :" ,test_accuracy)
new_creditcard = pd.DataFrame([[1734,0,445]],columns=['transaction_amount','is_unusual_location','time_since_last_txn_mins'])
prediction=model.predict(new_creditcard)
print("1-fraudulent , 0-not fraudulent:", prediction[0])