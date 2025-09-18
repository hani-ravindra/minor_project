# script to train ML model on phishing dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

#load dataset
df = pd.read_csv('phishing.csv')

#feature (all except Index and class)
X = df.drop(['Index', 'class'], axis=1)
y = df['class']

#split into train and test 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#predictions
y_pred = model.predict(X_test)

#evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n",classification_report(y_test, y_pred))

#save model
joblib.dump(model, 'phishing_model.pkl')
print("Model saved as phishing_model.pkl")