import mysql.connector

with mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='password',
    database='calc') as conn:

    with conn.cursor(dictionary=True) as cur:
        cur.execute('SELECT * FROM items WHERE code=%s', (
            'A01',
        ))
        row = cur.fetchone()
        if row is not None:
            print(f"コード:{row['code']} 品名:{row['name']} 単価:{row['price']:,} 軽減:{'対象' if row['keigen'] else '対象外'}")
        else:
            print('マッチする商品は存在しません。')
