# diabetes_risk_predictor

## Diabetes Risk Prediction using XGBoost

A FLASK-based web application that predicts the likelihood of the user having diabetes or prediabetes based on the user's responses to a questionnaire. The app currently uses an XGBoost (Extreme Gradient Boosting) model trained on a Kaggle Dataset (https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset?select=diabetes_binary_health_indicators_BRFSS2015.csv) of 253,680 survey responses to the Center for Disease Control's(CDC)  Behavioral Risk Factor Surveillance System (BRFSS2015) in 2015.

The Dataset was balanced using SMOTEENN and then trained using XGBoost Classifier.

## Docker Image on Hub
Docker Image Pushed to Hub: https://hub.docker.com/repository/docker/sagartv/diabetes_risk_predictor/

To get this latest image use: docker pull sagartv/diabetes_risk_predictor:0.0.4.RELEASE

To run, expand optional settings and provide a Port Number for your system, this will map to the image's port 3000.


## TODO:
Add Tests *
Build CI/CD Pipelines
Deploy on Cloud




