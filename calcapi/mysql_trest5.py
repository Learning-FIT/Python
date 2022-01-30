import mysql.connector

with mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='password',
    database='calc') as conn:

    with conn.cursor(dictionary=True) as cur:
        cur.execute('DELETE FROM items WHERE code=%s', (
            'A04',
        ))

        conn.commit()
