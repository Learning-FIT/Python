class Order:
    __lines = []
    
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

    # 課題②で追加
    def get_lines(self):
        return self.__lines