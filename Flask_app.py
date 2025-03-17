import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from flask import Flask, render_template, request
import numpy as np

# Load dataset
df = pd.read_excel(r"C:\Users\ARYAN\Downloads\loan_approval_dataset.xlsx")
df = df.drop(columns=["loan_id"])

# Encode categorical variables
df["education"] = df["education"].map({"Graduate": 1, "Not Graduate": 0})
df["self_employed"] = df["self_employed"].map({"Yes": 1, "No": 0})
df["loan_status"] = df["loan_status"].map({"Approved": 1, "Rejected": 0})

# Define features and target
y = df["loan_status"]
X = df.drop("loan_status", axis=1)

# Train Decision Tree model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
feature_importances_dict=dict(zip(list(df.columns),list(model.feature_importances_)))
sorted_feature_importances=dict(sorted(feature_importances_dict.items(), key=lambda item: item[1], reverse=True))
print(list(sorted_feature_importances.keys()))

correlation=df.corr()


correlation=correlation.drop("loan_status",axis=0)
correlation=correlation["loan_status"]
correlation = correlation.abs().sort_values(ascending=False)

print(list(correlation.index))

# print(model.feature_importances_)
# print(f"Accuracy: {accuracy:.4f}")
# print("Classification Report:\n", report)

# Flask application setup
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check_loan", methods=["POST"])
def check_loan():
    input_data = {
        "education": int(request.form.get("education", 0)),
        "no_of_dependents":int(request.form.get("no_of_dependents", 0)),
        "self_employed": int(request.form.get("self_employed", 0)),
        "income_annum": float(request.form.get("income_annum", 0)),
        "loan_amount": float(request.form.get("loan_amount", 0)),
        "loan_term": float(request.form.get("loan_term", 0)),
        "cibil_score": float(request.form.get("cibil_score", 0)),
        "residential_assets_value": float(request.form.get("residential_assets_value", 0)),
        "commercial_assets_value": float(request.form.get("commercial_assets_value", 0)),
        "luxury_assets_value": float(request.form.get("luxury_assets_value", 0)),
        "bank_asset_value": float(request.form.get("bank_asset_value", 0))
    }
    arr=list(input_data.values())
    arr=np.array(arr)
    arr=arr.reshape(1, -1)
        # Convert input data to DataFrame
    # print(input_data)
    # input_df = pd.DataFrame([input_data])
    # print(input_df)
    prediction = model.predict(arr)
    print(prediction)
    # print(prediction)
    
    if prediction == 1:
        return render_template("loan_approved.html")
    else:
        feature_importances_dict=dict(zip(list(df.columns),list(model.feature_importances_)))
        sorted_feature_importances=dict(sorted(feature_importances_dict.items(), key=lambda item: item[1], reverse=True))
        sorted_feature_importances=list(sorted_feature_importances.keys())[:10]
        # print(sorted_feature_importances)

        correlation=df.corr()


        correlation=correlation.drop("loan_status",axis=0)
        correlation=correlation["loan_status"]
        correlation = correlation.abs().sort_values(ascending=False)
        correlation=list(correlation[:10])

        ''' or put correlation instead of sorted_feature_importances'''
        return render_template("loan_rejection.html",rejection_factors=sorted_feature_importances)
   

if __name__ == "__main__":
    app.run(debug=True)