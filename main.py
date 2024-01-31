import requests
import webbrowser


def buy(token, debug=False):
    '''Функция для открытия сайта покупки\n\ntoken - Ваш токен на товар\ndebug - Для отлади'''
    webbrowser.open(
        'https://donate.rkprojects.ru/buy.php?token=' + token, new=2)

    if debug == True:
        print('You open page donate, this token = "' + token + '"')


def check_payment(token, debug=False):
    '''Функция для проверки оплаты товара\n\ntoken - Ваш токен на товар\ndebug - Для отлади'''

    res = requests.get(
        'https://donate.rkprojects.ru/checkbuy.php?token=' + token)

    if debug == True:
        print('request status: ' + str(res.status_code))

    if res.status_code == 200:

        if res.text == 'no':
            if debug == True:
                print('User don`t buy : ' + str(token))

            return False
        elif res.text == 'yes':
            if debug == True:
                print('User buyed: ' + token)

            return True
        else:
            return res.text
