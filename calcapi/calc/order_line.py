import os

# tax_rate = [0, 0]

# .envを使う
tax_rate = [int(os.environ['TAX_RATE']), int(os.environ['TAX_RATE_KEIGEN'])]

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