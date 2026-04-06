from datetime import datetime, date
import requests
from xml.etree import ElementTree as ET

def get_currency_rates():
    url = 'https://cbr.ru/scripts/XML_daily.asp'
    target_currencies = ['USD', 'EUR', 'CNY', 'GBP']
    rates = {}

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)

        date_str = root.attrib.get('Date', '')
        if date_str:
            try:
                xml_date = datetime.strptime(date_str, '%d.%m.%Y').date()
                today = date.today()
                if xml_date < today:
                    print(f"⚠️ Внимание: используются курсы от {date_str} (не сегодняшний день)\n")
            except ValueError:
                print("⚠️ Ошибка: не удалось распознать дату в ответе ЦБ, используется текущая дата\n")
                date_str = today.strftime('%d.%m.%Y')
        else:
            print("⚠️ Предупреждение: дата не найдена в ответе ЦБ\n")
            date_str = date.today().strftime('%d.%m.%Y')

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
    except requests.RequestException as e:
        print(f"Ошибка при получении данных от ЦБ: {e}\n")
        return {}, date.today().strftime('%d.%m.%Y')
    except ET.ParseError as e:
        print(f"Ошибка парсинга XML: {e}\n")
        return {}, date.today().strftime('%d.%m.%Y')

    return rates, date_str

def user_rubles():
    while True:
        try:
            rubles = float(input('Введите сумму в рублях: '))
            if rubles < 0:
                print('Пожалуйста, введите положительное число.')
            else:
                return rubles
        except ValueError:
            print('Ошибка! Пожалуйста, введите корректное число.')

def convert(rubles, rates):
    print(f'Конвертация {rubles} руб.:')
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

def display(rates, date_str):
    xml_date = datetime.strptime(date_str, '%d.%m.%Y')
    month_names = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ]
    day = xml_date.day
    month = month_names[xml_date.month - 1]
    year = xml_date.year
    formatted_date = f'{day} {month} {year} года'
    print(f'Курсы валют на {formatted_date}:')
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

if __name__ == '__main__':
    main_main()
