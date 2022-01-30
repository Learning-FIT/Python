items = {
    'A01': {'price': 100},
    'A02': {'price': 200},
    'B01': {'price': 1000}
}

def main():
    sum = 0
    while True:
        code = input('商品コードを入力してください（終了q）：')
        if code == 'q':
            print(f'合計：{sum}円')
            tax = calcTax(sum)
            print(f'消費税：{tax}円　合計：{sum + tax}円')
            break
        if code in items:
            print(f"商品コード：{code} 単価：{items[code]['price']}")
            count = int(input('個数を入力してください：'))
            sum += items[code]['price'] * count
        else:
            print(f'商品コード：{code}は、存在しません')

def calcTax(sum):
    return int(sum * 0.1)

if __name__ == '__main__':
    main()
