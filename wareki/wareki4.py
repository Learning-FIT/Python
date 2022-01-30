year = int(input('西暦を入力してください：'))
supported = True
if year > 2018:
    gengo = '令和'
    wareki = year - 2018
elif year > 1988:
    gengo = '平成'
    wareki = year - 1988
else:
    supported = False
if supported:
    print(f'{year}年は{gengo}{wareki}年です。')
else:
    print(f'{year}年は対応していません。')
