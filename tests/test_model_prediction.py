import pytest
import model_prediction


def test_load_diabetes_model():
  assert model_prediction.load_diabetes_model() is not None

