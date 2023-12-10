from flask import Flask, render_template, jsonify, request
app = Flask(__name__)




#route to this function when nothing succeeds the "/" in the url
@app.route('/')
def render_home():

  #Render the home.html page
  return render_template('home.html')