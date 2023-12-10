from flask import Flask, render_template, jsonify, request
import sklearn
import pandas as pd
import numpy as np
import pickle
import xgboost


app = Flask(__name__)




#route to this function when nothing succeeds the "/" in the url
@app.route('/')
def render_home():

  #Render the home.html page
  return render_template('home.html')


#Use POST method to get form data 
@app.route('/submission', methods= ['post'])
def process_submission():
  data = request.form
  df = pd.DataFrame(data.to_dict(flat = True), index = [0])
  instance = np.array(df)
  print(df.shape)
  print(instance.shape)
  
  pipeline = None
  with open('./models/diabetes_model_v1.pk', 'rb') as f_in:
    pipeline = pickle.load(f_in)
    f_in.close()
  # if type(data) == dict:
  #   df = pd.DataFrame(data)
  # else:
  #   df = config
  y_pred = pipeline.predict(instance)
  print(y_pred)
  # return y_pred

  return render_template('submission.html', data = data)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81, debug = True)