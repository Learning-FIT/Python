import json
import requests

def main():
    # APIの呼び出し側ではOrderクラスやOrderLineクラスは使用しない
    order_lines = []
    
    while True:
        code = input('商品コードを入力してください（終了q）：')
        if code == 'q':
            # save_order APIを呼び出す
            response = None

            # save_order APIの戻り値を用いて出力する
            # for print_line in response.json()['order_print_lines']:
            #     print(print_line)

            break

        # item APIを使って商品を検索する
        response = None

        item = response.json()
        print(f"商品コード：{code} 品名：{item['name']} 単価：{item['price']}")

        if item is not None:
            try:
                count = int(input('個数を入力してください：'))
            except ValueError:
                print('個数は数値で入力してください')
                exit(4)

            if item['keigen']:
                keigen = input('軽減税率を適用しますか（y/n）：')
                if keigen != 'y' and keigen != 'n':
                    print('yかnで入力してください')
                    exit(3)
                order_lines.append({
                    'code': code,
                    'name': item['name'],
                    'price': item['price'],
                    'count': count,
                    'keigen': keigen == 'y'
                })
            else:
                order_lines.append({
                    'code': code,
                    'name': item['name'],
                    'price': item['price'],
                    'count': count,
                    'keigen': False
                })

        else:
            print(f'商品コード：{code}は、存在しません')


if __name__ == '__main__':
    main()
