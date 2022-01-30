i = 0
while True:
    i += 1
    gengo = input(f'元号を選択してください（{i}回目）[M/T/S/H/R/q]：')
    if gengo == 'q':
        break
    wareki = int(input('和暦を入力してください：'))
    supported = True
    if gengo == 'R':
        year = wareki + 2018
    elif gengo == 'H':
        year = wareki + 1988
    elif gengo == 'S':
        year = wareki + 1925
    elif gengo == 'T':
        year = wareki + 1911
    elif gengo == 'M':
        year = wareki + 1867
    else:
        supported = False
    if supported:
        print(f'{gengo}{wareki}年は西暦{year}年です。')
    else:
        print(f'入力された元号は対応していません。')