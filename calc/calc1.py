sum = 0
while True:
    text = input('単価を入力してください（終了q）：')
    if text == 'q':
        print(f'合計：{sum}円')
        break
    price = int(text)
    count = int(input('個数を入力してください：'))
    sum += price * count
