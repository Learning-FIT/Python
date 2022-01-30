import mysql.connector

with mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='password',
    database='calc') as conn:

    with conn.cursor(dictionary=True) as cur:
        cur.execute('INSERT INTO items VALUES (NULL, %s, %s, %s, %s)', (
            'A04',
            'ブロッコリー',
            200,
            1,
        ))

        print('追加したID:', cur.lastrowid)

        conn.commit()
