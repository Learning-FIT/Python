items = {
    'A01': {'price': 100},
    'A02': {'price': 200},
    'B01': {'price': 1000}
}

code = input('商品コードを入力してください：')
if code in items:
    print(f"商品コード：{code} 単価：{items[code]['price']}")
else:
    print(f'商品コード：{code}は、存在しません')