from flask import Flask, render_template, request

app = Flask(__name__)

# 課題：Flask（1）
@app.route('/wareki', methods=['GET', 'POST'])
def wareki():
    if request.method == 'POST':
        year = int(request.form.get('seireki'))
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
        elif year > 1925:
            if year == 1926:
                wareki = '昭和1（大正15）'
            else:
                wareki = f'昭和{year - 1925}'
        elif year > 1911:
            if year == 1912:
                wareki = '大正1（明治45）'
            else:
                wareki = f'大正{year - 1911}'
        elif year > 1867:
            wareki = f'明治{year - 1867}'
        return render_template('wareki.html', seireki=year, wareki=wareki)
    else:
        return render_template('wareki.html')
