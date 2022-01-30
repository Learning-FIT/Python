i = 0
while True:
    i += 1
    year = int(input(f'西暦を入力してください（{i}回目）：'))
    supported = True
    if year > 2018:
        if year == 2019:
            wareki = '令和1（平成31）'
        else:
            wareki = f'令和{year - 2018}'
    elif year > 1988:
        if year == 1989:
            wareki = '平成1（昭和64）'
        else:
            wareki = f'平成{year - 1988}'
    else:
        supported = False
    if supported:
        print(f'{year}年は{wareki}年です。')
    else:
        print(f'{year}年は対応していません。')