import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='password',
    database='calc')
cur = conn.cursor(dictionary=True)
cur.execute('SELECT * FROM items')
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()