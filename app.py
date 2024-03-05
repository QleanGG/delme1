from flask import Flask
import json
app = Flask(__name__)

data = [1,2,3,45]

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_data')
def get_data():
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)