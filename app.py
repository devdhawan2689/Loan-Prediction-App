from flask import Flask, render_template, request
from sklearn.tree import DecisionTreeClassifier
import pickle
import joblib

app = Flask(__name__)

model = joblib.load("final_model.joblib")

with open('feature_importance.pkl', 'rb') as f:
            important_features = pickle.load(f)

import sklearn; print(sklearn.__version__)

@app.route('/')
def index():
    return render_template('index.html')
    # return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    no_of_dependents = int(request.form['no_of_dependents'])
    education = request.form['education']
    self_employed = request.form['self_employed']
    income_annum = int(request.form['income_annum'])
    loan_amount = int(request.form['loan_amount'])
    loan_term = int(request.form['loan_term'])
    cibil_score = int(request.form['cibil_score'])
    residential_assets_value = int(request.form['residential_assets_value'])
    commercial_assets_value = int(request.form['commercial_assets_value'])
    luxury_assets_value = int(request.form['luxury_assets_value'])
    bank_assets_value = int(request.form['bank_assets_value'])

    if education == "Graduate":
        education = 1
    else:
        education = 0
    
    if self_employed == "Yes":
        self_employed = 1
    else:
        self_employed = 0

    print([[no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_assets_value]])

    data = [[no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_assets_value]]

    prediction = model.predict(data)

    print(predict)

    if prediction[0] == 0:
        return render_template("loan_rejection.html",rejection_factors=important_features[:5])
    else:
        return render_template("loan_approval.html")
    # return render_template('login_page.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000) 