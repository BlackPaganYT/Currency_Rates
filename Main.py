import Currency_rates

def main():
    while True:
        try:
            operation = int(input("Введите, что вы хотите сделать (1 — Узнать курс на сегодня; 2 — Конвертер валют в рубли): "))
            print('-' * 100)
            if operation == 1:
                rates, date = Currency_rates.get_currency_rates()
                if rates:
                    Currency_rates.display(rates, date)
                    print('-' * 100)
                else:
                    print("Не удалось получить курсы валют.")
            elif operation == 2:
                rates, _ = Currency_rates.get_currency_rates()
                if rates:
                    rubles = Currency_rates.user_rubles()
                    print('-' * 100)
                    if rubles is not None:
                        Currency_rates.convert(rubles, rates)
                        print('-' * 100)
                else:
                    print("Не удалось получить курсы валют.")
            else:
                print("Вы ввели некорректное значение!")
        except ValueError:
            print("Вы ввели некорректное значение!")

def start():
    print("!!Добро пожаловать!!")
    print("!!Это конвертер валют!!")
    print("!!Он получает курсы валют из Центрального банка РФ!!")
    print("!!Он может вывести курсы и также перевести рубли в поддерживаемые валюты!!")
    print('-' * 100)

if __name__ == '__main__':
    start()
    main()
