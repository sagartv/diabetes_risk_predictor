from diabetes_risk_predictor.src.pipelines.predict_pipeline import PredictPipeline
import pytest
import numpy as np
from werkzeug.datastructures import ImmutableMultiDict

@pytest.fixture
def predictpipeline():
  return PredictPipeline()

@pytest.fixture
def response_form():
  form = ImmutableMultiDict([('HighBP', '1'), ('HighChol', '1'), ('BMI', '25'), ('Smoker', '1'), ('Stroke', '0'), ('HeartDiseaseorAttack', '1'), ('PhysActivity', '0'), ('HvyAlcoholConsump', '1'), ('NoDocbcCost', '1'), ('GenHlth', '5'), ('MentHlth', '10'), ('PhysHlth', '5'), ('DiffWalk', '0'), ('Age', '6'), ('Education', '4'), ('Income', '3')])
  return form

def test_classifier(predictpipeline):
  assert predictpipeline.classifier is not None
  # assert diabetes_predictor.classifier.__class__name == 'XGBClassifier'

def test_form_to_numpy(predictpipeline, response_form):
  form_numpy = predictpipeline.form_to_numpy(response_form)
  assert isinstance(form_numpy, np.ndarray)
  assert form_numpy.shape == (1,16)

def test_predict(predictpipeline, response_form):
  prediction,probability = predictpipeline.predict(response_form)
  assert isinstance(prediction, int)
  assert isinstance(probability, float)
  assert prediction >= 0 and prediction <= 1
