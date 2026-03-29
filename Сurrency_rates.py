import requests
from datetime import datetime

def get_currency_rates():
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'

    target_currencies = ['USD', 'EUR', 'CNY', 'GBP'] # Список валют

    response = requests.get(url, timeout=10) #отправка
    response.raise_for_status() #получение
    from xml.etree import ElementTree as ET
    root = ET.fromstring(response.content)
    rates = {}


    currency_names = {
        'USD': 'Доллар США',
        'EUR': 'Евро',
        'CNY': 'Китайский юань',
        'GBP': 'Фунт стерлингов'
    }


    for valute in root.findall('Valute'):
        char_code = valute.find('CharCode').text

        if char_code in target_currencies:
            name = valute.find('Name').text
            value = float(valute.find('Value').text.replace(',', '.'))
            nominal = int(valute.find('Nominal').text)
            rate = value / nominal

            rates[char_code] = {
                'name': currency_names[char_code],
                'rate': round(rate, 4),
                'original_value': value,
                'nominal': nominal
            }

    date_str = root.attrib['Date']
    return rates, date_str




def user_rubles():
    try:
        rubles = float(input('Введите сумму в рублях: '))
        if rubles < 0:
            print('Пожалуйста, введите положительное число.')
        else:
            return rubles
    except ValueError:
        print('Ошибка! Пожалуйста, введите корректное число.')





def convert(rubles, rates):
    print(f'\nКонвертация {rubles} руб.:')
    order = ['USD', 'EUR', 'CNY', 'GBP']
    for currency_code in order:
        if currency_code in rates:
            rate = rates[currency_code]['rate']
            if currency_code == 'CNY':
                converted = (rubles / rate) / 10
                print(f'{rubles:,} руб. = {converted:,.2f} {rates[currency_code]["name"]} ({currency_code})')
            else:
                converted = rubles / rate
                print(f'{rubles:,} руб. = {converted:,.2f} {rates[currency_code]["name"]} ({currency_code})')




def display(rates, date):
    print(f'Курсы валют на {date}: ')
    order = ['USD', 'EUR', 'CNY', 'GBP']
    for currency_code in order:
        if currency_code in rates:
            data = rates[currency_code]
            print(f'{data["name"]} ({currency_code}): {data["rate"]} руб.')



def main_main():
    if __name__ == '__main__':
        rates, date = get_currency_rates()
        if rates:
            display(rates, date)
            rubles = user_rubles()
            convert(rubles, rates)
        else:
            print('Не удалось получить курсы валют.')