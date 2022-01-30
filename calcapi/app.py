from flask import Flask, render_template, request, jsonify, Response
import json
import mysql.connector
import os
import datetime
from calc.order import Order
from calc.order_line import OrderLine

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Hello, World!</p>'

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/hello2', methods=['GET', 'POST'])
def hello2():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('hello2.html', name=name)
    else:
        return render_template('hello2.html')

@app.route('/wareki', methods=['GET', 'POST'])
def wareki():
    if request.method == 'POST':
        year = int(request.form.get('seireki'))
        if year > 2018:
            if year == 2019:
                wareki = '令和1（平成31）'
            else:
                wareki = f'令和{year - 2018}'
        elif year > 1988:
            if year == 1989:
                wareki = '平成1（昭和64）'
            else:
                wareki = f'平成{year - 1988}'
        elif year > 1925:
            if year == 1926:
                wareki = '昭和1（大正15）'
            else:
                wareki = f'昭和{year - 1925}'
        elif year > 1911:
            if year == 1912:
                wareki = '大正1（明治45）'
            else:
                wareki = f'大正{year - 1911}'
        elif year > 1867:
            wareki = f'明治{year - 1867}'
        return render_template('wareki.html', seireki=year, wareki=wareki)
    else:
        return render_template('wareki.html')

@app.route('/hello/<name>.json')
def hello_json(name):
    result = {
        'message': f'Hello, {name}!'
    }
    return jsonify(result)
    #return Response(json.dumps(result), content_type='application/json')

@app.route('/hello3', methods=['POST'])
def hello3():
    payload = request.json
    name = payload['name']
    result = {
        'message': f'Hello, {name}!'
    }
    return jsonify(result)

@app.route('/wareki2', methods=['POST'])
def wareki2():
    payload = request.json
    year = payload['seireki']
    if year > 2018:
        if year == 2019:
            wareki = '令和1（平成31）'
        else:
            wareki = f'令和{year - 2018}'
    elif year > 1988:
        if year == 1989:
            wareki = '平成1（昭和64）'
        else:
            wareki = f'平成{year - 1988}'
    elif year > 1925:
        if year == 1926:
            wareki = '昭和1（大正15）'
        else:
            wareki = f'昭和{year - 1925}'
    elif year > 1911:
        if year == 1912:
            wareki = '大正1（明治45）'
        else:
            wareki = f'大正{year - 1911}'
    elif year > 1867:
        wareki = f'明治{year - 1867}'
    result = {
        'wareki': wareki
    }
    return Response(json.dumps(result, ensure_ascii=False), content_type='application/json')

@app.route('/item', methods=['POST'])
def item():
    payload = request.json
    code = payload['code']

    with mysql.connector.connect(
            host=os.environ['MYSQL_HOST'], user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASS'], database=os.environ['MYSQL_DATABASE']) as conn:
        with conn.cursor(dictionary=True) as cur:
            cur.execute('SELECT * FROM items WHERE code=%s', (code,))
            row = cur.fetchone()

    return Response(json.dumps(row, ensure_ascii=False), content_type='application/json')

@app.route('/save_order', methods=['POST'])
def save_order():
    payload = request.json
    print(payload)

    now = datetime.datetime.now()

    # OrderオブジェクトとOrderLineオブジェクトを組み立てる
    order = Order()
    for line in payload['order_lines']:
        order_line = OrderLine(line['code'], line['name'], line['price'], line['count'], line['keigen'])
        order.add_line(order_line)

    # MySQLに接続して保存する
    with mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='password',
        database='calc') as conn:

        with conn.cursor(dictionary=True) as cur:
            # Orderインスタンスの内容をordersテーブルへの書き込み
            cur.execute('INSERT INTO orders VALUES (NULL, %s)', (now,))

            # ordersテーブルに追加した行のIDの取得
            order_id = cur.lastrowid

            # Orderインスタンスが保持するOrderLineインスタンスを順に取得
            for line in order.get_lines():
                # OrderLineインスタンスの内容をorder_linesテーブルへ書き込み
                cur.execute('INSERT INTO order_lines VALUES (NULL, %s, %s, %s, %s, %s, %s)', (
                    order_id,
                    line.code,
                    line.name,
                    line.price,
                    line.count,
                    1 if line.keigen else 0
                ))

            conn.commit()

    return jsonify({
        'order_print_lines': order.print_lines()
    })
