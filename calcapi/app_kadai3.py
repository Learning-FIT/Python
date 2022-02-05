from flask import Flask, request, Response
import json
import mysql.connector
import os

app = Flask(__name__)

# 課題：Flask（3）
@app.route('/item', methods=['POST'])
def item():
    payload = request.json
    code = payload['code']

    with mysql.connector.connect(
            host=os.environ['MYSQL_HOST'], port=os.environ['MYSQL_PORT'], user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASS'], database=os.environ['MYSQL_DATABASE']) as conn:
        with conn.cursor(dictionary=True) as cur:
            cur.execute('SELECT * FROM items WHERE code=%s', (code,))
            row = cur.fetchone()

    return Response(json.dumps(row, ensure_ascii=False), content_type='application/json')
