This repository contains a web application that predicts whether a person will be granted a loan or not, based on their provided information. The application utilizes a Decision Tree model for prediction.

## Overview

This project aims to provide a simple and accessible tool for loan prediction. It takes into account various factors such as income, credit history, and loan amount to determine the likelihood of loan approval.

## Features

* **User-friendly interface:** Easy-to-use web interface for inputting loan application details.
* **Decision Tree model:** Utilizes a trained Decision Tree model for accurate predictions.
* **Clear prediction results:** Provides a straightforward "Loan Approved" or "Loan Rejected" output.
* **Input Validation:** Validates user inputs to ensure data integrity.

## Technologies Used

* **Python:** Programming language for backend logic and model training.
* **Scikit-learn:** Machine learning library for building and training the Decision Tree model.
* **Flask:** Web framework for creating the application's backend.
* **HTML/CSS/JavaScript:** For the frontend web interface.
* **Pandas:** For data manipulation and analysis.
* **Pickle:** For serializing and deserializing the trained model.

## Getting Started

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/loan-prediction-app.git](https://www.google.com/search?q=https://github.com/your-username/loan-prediction-app.git)
    cd loan-prediction-app
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

    * On Windows:

        ```bash
        venv\Scripts\activate
        ```

    * On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    python app.py
    ```

5.  **Open your browser and navigate to `http://127.0.0.1:5000/`**


## About the Dataset
**Fields in the Dataset**

```bash
**`loan_id`	`no_of_dependents`	`education`	`self_employed`	`income_annum`	`loan_amount`	`loan_term`	`cibil_score`	`residential_assets_value`	`commercial_assets_value`	`luxury_assets_value`	`bank_asset_value`	`loan_status`**
 ```

Then Predicts wheter the person should be given a loan or not. 

Here is a Sample Demo of the User Form:
![Home Page](https://github.com/user-attachments/assets/8d4a7028-12b1-4163-8d3e-fc6a36f7fe11)

Approval/ Rejection Message:
![Approved and Rejected Screen](https://github.com/user-attachments/assets/c16fdf10-04b4-46d7-b90d-3a295761bd90)
