import pickle
import numpy as np
import pandas as pd
import xgboost



#Diabetes Prediction Class
class DiabetesPredictor:
  def __init__(self):
    self.classifier_path = './classifiers/diabetes_model_v2.pk'
    self.classifier = self.load_classifier(self.classifier_path)

  def return_classifier_path(self):
    return self.classifier_path

  def return_classifier(self):
    return self.classifier
    
  #Loads the XGBoost Model
  def load_classifier(self, filename):
    classifier = None
    with open(filename, 'rb') as f_in:
      classifier = pickle.load(f_in)
      f_in.close()
    return classifier

  #Takes the form data returns a dict
  def form_to_dict(self,form):
    return form.to_dict(flat = True)

  #Takes form data and returns a pandas dataframe
  def form_to_df(self,form):
    form_df = pd.DataFrame(form.to_dict(flat = True), index = [0])
    return form_df

  #Takes form data and returns a numpy ndarray
  def form_to_numpy(self,form):
    form_df = pd.DataFrame(form.to_dict(flat = True), index = [0])
    return form_df.to_numpy()
    
  #makes prediction 
  def predict(self,form):
    data = self.form_to_numpy(form)
    classifier = self.classifier
    prediction = classifier.predict(data)
    probability = classifier.predict_proba(data)[0][1] * 100.0
    probability = round(probability,1)
    return prediction, probability

    