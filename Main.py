import Сurrency_rates

def main():
    while True:
        try:
            operation = int(input("Введите, что вы хотите сделать (1 — Узнать курс на сегодня; 2 — Конвертер валют в рубли): "))
            print('-' * 100)
            if operation == 1:
                rates, date = Сurrency_rates.get_currency_rates()
                if rates:
                    Сurrency_rates.display(rates, date)
                    print('-' * 100)
                else:
                    print("Не удалось получить курсы валют.")
            elif operation == 2:
                rates, _ = Сurrency_rates.get_currency_rates()
                if rates:
                    rubles = Сurrency_rates.user_rubles()
                    print('-' * 100)
                    if rubles is not None:
                        Сurrency_rates.convert(rubles, rates)
                        print('-' * 100)
                else:
                    print("Не удалось получить курсы валют.")
            else:
                print("Вы ввели некорректное значение!")
        except ValueError:
            print("Вы ввели некорректное значение!")

if __name__ == '__main__':
    main()
