from flask import Flask, render_template, request, jsonify, Response
import json
import mysql.connector
import os
import datetime
from calc.order import Order
from calc.order_line import OrderLine

app = Flask(__name__)

# 最小のアプリケーション
@app.route('/')
def index():
    return '<p>Hello, World!</p>'

# Jinjaテンプレートの活用
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

# フォームの使用
@app.route('/hello2', methods=['GET', 'POST'])
def hello2():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('hello2.html', name=name)
    else:
        return render_template('hello2.html')

# Web APIの作成
@app.route('/hello/<name>.json')
def hello_json(name):
    result = {
        'message': f'Hello, {name}!'
    }
    return jsonify(result)
    #return Response(json.dumps(result), content_type='application/json')

# JSONパラメータの取得
@app.route('/hello3', methods=['POST'])
def hello3():
    payload = request.json
    name = payload['name']
    result = {
        'message': f'Hello, {name}!'
    }
    return jsonify(result)
