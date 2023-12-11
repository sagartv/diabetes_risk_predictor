# diabetes_risk_predictor

## Diabetes Risk Prediction using XGBoost

A FLASK-based web application that predicts the likelihood of the user having diabetes or prediabetes based on the answers to a questionnaire. The app currently uses an XGBoost (Extreme Gradient Boosted Model) model trained on a Kaggle Dataset (https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_health_indicators_BRFSS2015.csv) of 253,680 survey responses to the Center for Disease Control's(CDC)  Behavioral Risk Factor Surveillance System (BRFSS2015) in 2015.

The Dataset was balanced using SMOTEENN and then trained using XGBoost Classifier.


TODO:
Add Tests
Build CI/CD Pipelines
Dockerize
Deploy on Cloud




