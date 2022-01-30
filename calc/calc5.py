import sys

items = {
    'A01': {'price': 100},
    'A02': {'price': 200},
    'B01': {'price': 1000}
}

tax_rate = [0, 0]

def main():
    global tax_rate
    if len(sys.argv) < 3:
        print('通常税率と軽減税率を指定してください')
        exit(1)
    try:
        tax_rate[0] = int(sys.argv[1])
        tax_rate[1] = int(sys.argv[2])
    except ValueError as e:
        print('税率は数値で入力してください')
        exit(2)

    sum = 0

    keigen = input('軽減税率を適用しますか（y/n）：')
    if keigen != 'y' and keigen != 'n':
        print('yかnで入力してください')
        exit(3)

    while True:
        code = input('商品コードを入力してください（終了q）：')
        if code == 'q':
            print(f'合計：{sum}円')
            tax = calcTax(sum, keigen == 'y')
            print(f'消費税：{tax}円　合計：{sum + tax}円')
            break
        if code in items:
            print(f"商品コード：{code} 単価：{items[code]['price']}")
            try:
                count = int(input('個数を入力してください：'))
            except ValueError:
                print('個数は数値で入力してください')
                exit(4)
            sum += items[code]['price'] * count
        else:
            print(f'商品コード：{code}は、存在しません')

def calcTax(sum, keigen):
    apply_tax_rate = tax_rate[0]
    if keigen:
        apply_tax_rate = tax_rate[1]
    return int(sum * apply_tax_rate / 100)

if __name__ == '__main__':
    main()
