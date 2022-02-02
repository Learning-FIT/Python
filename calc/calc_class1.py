import sys
import json
import os
import datetime

RESULT_PATH = 'result'

tax_rate = [0, 0]

class Order:
    def __init__(self):
        self.__lines = []

    def add_line(self, line):
        # OrderLinesオブジェクトを追加します
        self.__lines.append(line)

    def calc_total_sum(self):
        # 合計金額（税抜）を計算します
        total_sum = 0
        for line in self.__lines:
            total_sum += line.calc_sum()
        return total_sum

    def calc_tax_sum(self):
        # 税額の合計を計算します
        total_tax = 0
        for line in self.__lines:
            total_tax += line.calc_tax()
        return total_tax

    def print_lines(self):
        # 最後に出力する文字列を生成します
        print_lines = []
        print_lines.append(f'合計：{self.calc_total_sum():>8,}円\n')
        print_lines.append(f'消費税：{self.calc_tax_sum():>7,}円　合計：{self.calc_total_sum() + self.calc_tax_sum():>8,}円\n')
        return print_lines

class OrderLine:
    def __init__(self, code, name, price, count, keigen):
        self.code = code
        self.name = name
        self.price = price
        self.count = count
        self.keigen = keigen

    def calc_sum(self):
        # 明細行ごとの合計金額（税抜）を計算します
        return self.price * self.count

    def calc_tax(self):
        # 明細行ごとの税額を計算します
        apply_tax_rate = tax_rate[0]
        if self.keigen:
            apply_tax_rate = tax_rate[1]
        return int(self.calc_sum() * apply_tax_rate / 100)

    def print_lines(self):
        # 明細行ごとに出力する文字列を生成します
        print_lines = []
        print_lines.append(f"商品コード：{self.code} 商品名：{self.name:　<10} 単価：{self.price:>5,}")
        print_lines.append(f" 個数：{self.count:>3,} 小計：{self.calc_sum():>8,}")
        if self.keigen:
            print_lines.append(f' 税額：{self.calc_tax():>6,} ＜軽減＞')
        else:
            print_lines.append(f' 税額：{self.calc_tax():>6,}')
        return print_lines

def main():
    global tax_rate

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
