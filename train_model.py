# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import json
import os

print("🔄 Starting model training and file preparation...")

# --- Load dataset ---
if not os.path.exists("salary_prediction_data.csv"):
    print("❌ ERROR: 'salary_prediction_data.csv' not found in directory!")
    exit()

df = pd.read_csv("salary_prediction_data.csv")
print("✅ Dataset loaded.")

# --- Categorize salary ---
df['Salary_Category'] = pd.qcut(df['Salary'], q=[0, 0.33, 0.66, 1.0], labels=['Low', 'Medium', 'High'])
print("✅ Salary categories created.")

# --- Define features and target ---
X = df[['Education', 'Experience', 'Job_Title', 'Age', 'Gender']]
y = df['Salary_Category']

# --- Encode categorical features ---
categorical_columns = ['Education', 'Gender', 'Job_Title']
encoders = {}

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Update X with encoded values
X = df[['Education', 'Experience', 'Job_Title', 'Age', 'Gender']]

# --- Train-Test Split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train Random Forest ---
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("✅ Model trained.")

# --- Save Model and Encoders ---
joblib.dump({"model": model, "label_encoders": encoders}, "salary_predictor.pkl")
with open("model_columns.json", "w") as f:
    json.dump(X.columns.tolist(), f)

print("✅ Model and metadata saved (salary_predictor.pkl & model_columns.json).")
