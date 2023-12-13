import pytest
import numpy as np
from diabetes_predictor import DiabetesPredictor
from werkzeug.datastructures import ImmutableMultiDict

@pytest.fixture
def diabetes_predictor():
  return DiabetesPredictor()

@pytest.fixture
def response_form():
  form = ImmutableMultiDict([('HighBP', '1'), ('HighChol', '1'), ('CholCheck', '1'), ('BMI', '25'), ('Smoker', '1'), ('Stroke', '0'), ('HeartDiseaseorAttack', '1'), ('PhysActivity', '0'), ('Fruits', '0'), ('Veggies', '0'), ('HvyAlcoholConsump', '1'), ('AnyHealthcare', '1'), ('NoDocbcCost', '1'), ('GenHlth', '5'), ('MentHlth', '10'), ('PhysHlth', '5'), ('DiffWalk', '0'), ('Sex', '1'), ('Age', '6'), ('Education', '4'), ('Income', '3')])
  return form

def test_diabetes_classifier(diabetes_predictor):
  assert diabetes_predictor.classifier is not None
  # assert diabetes_predictor.classifier.__class__name == 'XGBClassifier'

def test_form_to_numpy(diabetes_predictor, response_form):
  form_numpy = diabetes_predictor.form_to_numpy(response_form)
  assert isinstance(form_numpy, np.ndarray)
  assert form_numpy.shape == (1,21)

def test_predict(diabetes_predictor, response_form):
  prediction,probability = diabetes_predictor.predict(response_form)
  assert isinstance(prediction, int)
  assert isinstance(probability, float)
  assert prediction >= 0 and prediction <= 1
