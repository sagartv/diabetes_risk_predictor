import pickle
import numpy as np
import pandas as pd
import xgboost


#Loads the XGBoost Model
def load_diabetes_model():
  model = None
  with open('./models/diabetes_model_v2.pk', 'rb') as f_in:
    model = pickle.load(f_in)
    f_in.close()
  return model

#Takes the form data and turns it into numpy
def preprocess_input(instance):
  df = pd.DataFrame(instance.to_dict(flat = True), index = [0])
  instance = df.to_numpy()
  return instance

#Returns model's predicted class, as well as probability of class predicted using predict_proba

def predict_diabetes(instance,model):
  instance = preprocess_input(instance)
  prediction = model.predict(instance)
  probability = model.predict_proba(instance)[0][1] * 100.0
  return prediction, probability
  
    