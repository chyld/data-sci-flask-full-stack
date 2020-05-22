from flask import Flask
from flask import render_template

app = Flask(__name__)


# 1 - basic GET
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World'

# 2 - GET with PARAMS
@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    return "Sum: {}".format(a + b)

# 3 - STATIC files

# 4 - basic templates
@app.route('/fun', methods=['GET'])
def fun():
    return render_template('fun.html')
