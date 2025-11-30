🕵️‍♂️ Phishing Website Detection using Machine Learning

This project focuses on detecting phishing websites using machine learning techniques based on URL-based and webpage-based feature analysis. The aim is to build a classification model that helps identify malicious websites and enhance cybersecurity awareness.

# Project Overview

Phishing attacks are one of the most common cybercrimes where attackers trick users into revealing sensitive information.
This project uses a dataset of website characteristics to classify websites into:

1 → Legitimate
0 → Suspicious
-1 → Phishing

The model analyzes 30+ features extracted from website URLs and HTML content to detect phishing patterns.

 # Dataset Features
Some key features used in this project:
having_IP_Address
URL_Length
Shortining_Service
SSLfinal_State
Domain_registeration_length
Request_URL
Iframe
web_traffic
Page_Rank
Google_Index
Result (Target Column)
Most features are numeric and represent website behavior patterns.

# Technologies Used
Python
Pandas
NumPy
Matplotlib / Seaborn
Scikit-learn

Machine Learning Models:
Random Forest
XGBoost

Jupyter Notebook

Streamlit (for deployment)

# Model Building Steps

Data loading and preprocessing
Exploratory Data Analysis (EDA)
Feature engineering and encoding (if required)
Splitting dataset into Train/Test
Training multiple ML models
Evaluating accuracy, confusion matrix, and classification report
Selecting the best-performing model
Deploying using Streamlit

# Model Deployment (Streamlit)

The project includes a Streamlit web app where users can manually enter website parameters or connect it with feature extraction logic.

To run the app:
streamlit run app.py

# Results
The model performs well on the dataset and accurately classifies phishing vs. legitimate websites.
Metrics evaluated:

Accuracy
Precision
Recall
F1-score
Confusion Matrix

# How to Run the Project

Clone the repository:
git clone <repo-link>

Install dependencies:
pip install -r requirements.txt

Run Jupyter Notebook to train the model:
jupyter notebook

Run Streamlit app:
streamlit run app.py

🤝 Contribution
Feel free to fork this repository, create issues, or submit pull requests to enhance the project.
