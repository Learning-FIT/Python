import mysql.connector

with mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='password',
    database='calc') as conn:

    with conn.cursor(dictionary=True) as cur:
        cur.execute('UPDATE items SET price=%s WHERE code=%s', (
            250,
            'A04',
        ))

        conn.commit()
