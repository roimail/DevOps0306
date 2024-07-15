from flask import Flask, request

# app = Flask("moshe")
app = Flask(__name__)

# the def function after @app.route is related to it, in the format written
@app.route('/')
def hello():
    return "Hello there"

@app.route('/cars', methods=['GET', 'POST'])
def cars():
    if request.method == 'GET':
        return "mazda, chevrolet, citroen, hyundai"
    if request.method == 'POST':
        return "creating a new car", 201

@app.route('/motors')
def motors():
    return "honda, yamaha"

app.run(debug=True)