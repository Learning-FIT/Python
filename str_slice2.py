text = input('文字列を入力してください：')
start = int(input('開始位置を入力してください：'))

if len(text) < start+1:
    print('開始位置が文字列長を超えています。')
    exit()

length = int(input('文字数を入力してください：'))

if len(text) < start+length:
    print('開始位置＋文字数が文字列長を超えています。')
    exit()

print(text[start:start+length])