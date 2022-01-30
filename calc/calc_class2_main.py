import sys
import json
import os
import datetime
from calc_class2_mod import Order, OrderLine, tax_rate

RESULT_PATH = 'result'

def main():
    item_file = 'items2.json'
    tax_file = 'tax.csv'

    if len(sys.argv) == 3:
        item_file = sys.argv[1]
        tax_file = sys.argv[2]

    if os.path.exists(item_file):
        with open(item_file, mode='r', encoding='UTF-8') as f:
            items = json.load(f)
    else:
        print('指定された商品ファイルが存在しません')
        exit(5)

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
        while True:
            code = input('商品コードを入力してください（終了q）：')
            if code == 'q':
                f.writelines(order.print_lines())
                break
            if code in items:
                try:
                    count = int(input('個数を入力してください：'))
                except ValueError:
                    print('個数は数値で入力してください')
                    exit(4)

                if items[code]['keigen']:
                    keigen = input('軽減税率を適用しますか（y/n）：')
                    if keigen != 'y' and keigen != 'n':
                        print('yかnで入力してください')
                        exit(3)
                    line = OrderLine(code, items[code]['name'], items[code]['price'], count, keigen == 'y')
                else:
                    line = OrderLine(code, items[code]['name'], items[code]['price'], count, False)

                f.writelines(line.print_lines())
                f.write('\n')
                order.add_line(line)

            else:
                print(f'商品コード：{code}は、存在しません')

if __name__ == '__main__':
    main()
