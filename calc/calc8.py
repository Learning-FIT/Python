import sys
import json
import os
import datetime

RESULT_PATH = 'result'

tax_rate = [0, 0]

def main():
    global tax_rate
    if len(sys.argv) < 3:
        print('商品ファイルと税率ファイルを指定してください')
        exit(1)

    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], mode='r', encoding='UTF-8') as f:
            items = json.load(f)
    else:
        print('指定された商品ファイルが存在しません')
        exit(5)

    if os.path.exists(sys.argv[2]):
        try:
            with open(sys.argv[2], mode='r') as f:
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

    total_sum = 0
    tax_sum = 0

    if not os.path.exists(RESULT_PATH):
        os.mkdir(RESULT_PATH)

    filename = '%s.txt' % datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    with open(os.path.join(RESULT_PATH, filename), 'w', encoding='utf-8') as f:
        while True:
            code = input('商品コードを入力してください（終了q）：')
            if code == 'q':
                f.write(f'合計：{total_sum:>8,}円\n')
                f.write(f'消費税：{tax_sum:>7,}円　合計：{total_sum + tax_sum:>8,}円\n')
                break
            if code in items:
                f.write(f"商品コード：{code} 商品名：{items[code]['name']:　<10} 単価：{items[code]['price']:>5,}")
                try:
                    count = int(input('個数を入力してください：'))
                except ValueError:
                    print('個数は数値で入力してください')
                    exit(4)

                sum = items[code]['price'] * count
                total_sum += sum
                f.write(f" 個数：{count:>3,} 小計：{sum:>8,}")

                if items[code]['keigen']:
                    keigen = input('軽減税率を適用しますか（y/n）：')
                    if keigen != 'y' and keigen != 'n':
                        print('yかnで入力してください')
                        exit(3)
                    tax = calcTax(sum, keigen == 'y')
                    tax_sum += tax
                    f.write(f' 税額：{tax:>6,}')
                    f.write(' ＜軽減＞' if keigen == 'y' else '')
                else:
                    tax = calcTax(sum, keigen == 'y')
                    tax_sum += tax
                    f.write(f' 税額：{tax:>6,}')

                f.write('\n')

            else:
                print(f'商品コード：{code}は、存在しません')

def calcTax(sum, keigen):
    apply_tax_rate = tax_rate[0]
    if keigen:
        apply_tax_rate = tax_rate[1]
    return int(sum * apply_tax_rate / 100)

if __name__ == '__main__':
    main()
