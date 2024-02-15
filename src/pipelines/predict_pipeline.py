import os
import pickle
import numpy as np
import pandas as pd
import xgboost



#Prediction Pipeline Class
class PredictPipeline:
  def __init__(self):
    '''
    Initialize PredictPipeline class by loading classifier from pathname

    '''
    self.classifier_path = os.path.join("classifiers","diabetes_model_v3.pk")
    self.classifier = self.load_classifier(self.classifier_path)

  def return_classifier_path(self):
    '''
    Returns:
      classifier_path (str): Path to the classifier file
    '''
    return self.classifier_path

  def return_classifier(self):
    '''
    Returns:
      classifier (xgboost.XGBClassifier): Classifier object
    '''
    return self.classifier
    
  #Loads the XGBoost Model
  def load_classifier(self, filename):
    '''
    Args:
      filename (str): Path to the classifier file

    Returns:
      classifier (xgboost.XGBClassifier): Classifier object
    
    '''
    classifier = None
    with open(filename, 'rb') as f_in:
      classifier = pickle.load(f_in)
      f_in.close()
    return classifier

  #Takes the form data returns a dict
  def form_to_dict(self,form):
    '''
    Args:
      form (Flask Form): Form object

    Returns:
      form_dict (dict): Dictionary of form data
    '''
    return form.to_dict(flat = True)

  #Takes form data and returns a pandas dataframe
  def form_to_df(self,form):
    '''
    Args:
      form (Flask Form): Form object

    Returns:
      form_df (pd.DataFrame): DataFrame of form data
    '''
    form_df = pd.DataFrame(form.to_dict(flat = True), index = [0])
    return form_df

  #Takes form data and returns a numpy ndarray
  def form_to_numpy(self,form):
    '''
    Args:
      form (Flask Form): Form object

    Returns:
      form_df.to_numpy() (np.ndarray): Numpy array of form data
    
    '''
    form_df = pd.DataFrame(form.to_dict(flat = True), index = [0])

    return form_df.to_numpy()
    
  #makes prediction with classifier
  def predict(self,form):
    '''
    Args:
      form (Flask Form): Form Object

    Returns: 
      prediction (float): Prediction of diabetes status
      probability (float64): Probability of diabetes status
    '''
    #convert Flask form to numpy ndarray
    data = self.form_to_numpy(form)
    print(data.shape)
    print(data)
    classifier = self.classifier
    #make prediction
    prediction = int(classifier.predict(data)[0])
    #extract probability: note predict_proba is not reliable
    probability = classifier.predict_proba(data)[0][1] * 100.0
    probability = round(probability,1)
    return prediction, probability

    