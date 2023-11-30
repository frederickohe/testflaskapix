from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! This is a simple Flask API.'

@app.route('/api')
def get_data():
    data = {'message': 'This is data from the API', 'status': 'success'}
    return jsonify(data)

