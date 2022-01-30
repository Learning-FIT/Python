import sys
import os
import datetime
from calc.order import Order
from calc.order_line import OrderLine, tax_rate
import mysql.connector

RESULT_PATH = 'result'

def main():
    tax_file = 'tax.csv'

    if len(sys.argv) == 3:
        tax_file = sys.argv[2]

    if os.path.exists(tax_file):
        try:
            with open(tax_file, mode='r') as f:
                str = f.read()
                rates = str.split(',')
                for i in range(0, len(rates)):
                    tax_rate[i] = int(rates[i])
        except ValueError as e:
            print('税率は数値で入力してください')
            exit(2)
    else:
        print('指定された税率ファイルが存在しません')
        exit(5)

    if not os.path.exists(RESULT_PATH):
        os.mkdir(RESULT_PATH)

    now = datetime.datetime.now()
    filename = '%s.txt' % now.strftime('%Y%m%d%H%M%S')
    if not os.path.exists(os.path.join(RESULT_PATH, now.strftime('%Y'))):
        os.mkdir(os.path.join(RESULT_PATH, now.strftime('%Y')))
    if not os.path.exists(os.path.join(RESULT_PATH, now.strftime('%Y'), now.strftime('%m'))):
        os.mkdir(os.path.join(RESULT_PATH, now.strftime('%Y'), now.strftime('%m')))
    with open(os.path.join(RESULT_PATH, now.strftime('%Y'), now.strftime('%m'), filename), 'w', encoding='utf-8') as f:
        order = Order()

        with mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='password',
            database='calc') as conn:

            with conn.cursor(dictionary=True) as cur:
                while True:
                    code = input('商品コードを入力してください（終了q）：')
                    if code == 'q':
                        f.writelines(order.print_lines())

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

                        # コミット
                        conn.commit()

                        break

                    cur.execute('SELECT * FROM items WHERE code=%s', (code,))
                    item = cur.fetchone()
                    if item is not None:
                        try:
                            count = int(input('個数を入力してください：'))
                        except ValueError:
                            print('個数は数値で入力してください')
                            exit(4)

                        if item['keigen']:
                            keigen = input('軽減税率を適用しますか（y/n）：')
                            if keigen != 'y' and keigen != 'n':
                                print('yかnで入力してください')
                                exit(3)
                            line = OrderLine(code, item['name'], item['price'], count, keigen == 'y')
                        else:
                            line = OrderLine(code, item['name'], item['price'], count, False)

                        f.writelines(line.print_lines())
                        f.write('\n')
                        order.add_line(line)

                    else:
                        print(f'商品コード：{code}は、存在しません')

if __name__ == '__main__':
    main()
