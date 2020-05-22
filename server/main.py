from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("../models/model.p", "rb"))

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

# 5 - send list of numbers
@app.route('/product', methods=['GET'])
def product_get():
    return render_template('product.html')

# 6 - get product of list numbers
@app.route('/product', methods=['POST'])
def product_post():
    nums = [int(s) for s in request.form['nums'].split(',')]
    nums = np.array(nums)
    prod = nums.prod()
    return render_template('product.html', prod=prod)

# 7 - master with links
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# 8 - model diagnostics
@app.route('/diagnostics', methods=['GET'])
def diagnostics():
    return render_template('diagnostics.html', model=model)
