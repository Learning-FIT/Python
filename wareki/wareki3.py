year = int(input('西暦を入力してください：'))
if year > 2018:
    gengo = '令和'
    wareki = year - 2018
elif year > 1988:
    gengo = '平成'
    wareki = year - 1988
print(f'{year}年は{gengo}{wareki}年です。')
