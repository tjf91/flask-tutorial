from flask import Flask,render_template, jsonify
from flask_pymongo import PyMongo

app =  Flask(__name__)
app.config.from_object('config.Config')

@app.route("/")
def home():
    print(app.config)
    return render_template('index.html', name= 'James')

@app.route('/api/hello')
def hello():
    return jsonify({"response":"hello"})



@app.route('/api/<id>')
def employee_details(id):
    return render_template('index.html', id=id)

app.run()