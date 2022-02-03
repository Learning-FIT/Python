from flask import Flask, request, jsonify
import mysql.connector
import datetime
from calc.order import Order
from calc.order_line import OrderLine
import os

app = Flask(__name__)

# 課題：Flask（4）
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
            host=os.environ['MYSQL_HOST'], port=os.environ['MYSQL_PORT'], user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASS'], database=os.environ['MYSQL_DATABASE']) as conn:

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
