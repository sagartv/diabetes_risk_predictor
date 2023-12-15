from flask import Flask, render_template, request
from src.pipelines.predict_pipeline import PredictPipeline


app = Flask(__name__)


#route to this function when nothing succeeds the "/" in the url
@app.route('/')
def render_home():

  #Render the home.html page
  return render_template('home.html')


#Use POST method to get form data from the questionnaire
@app.route('/predict', methods= ['post'])
def process_submission():
  data = request.form
  prediction, probability = PredictPipeline().predict(data)

  if prediction == 0:
    return render_template('result_negative.html', data = probability)
  elif prediction == 1:
    return render_template('result_positive.html', data = probability)
    


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000, debug = False)