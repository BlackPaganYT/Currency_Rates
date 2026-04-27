# Конвентатор валют
Простой конвертер валют на [Python](https://www.python.org), который получает актуальные курсы от [Центрального банка РФ](https://www.cbr.ru) и позволяет конвертировать рубли в основные мировые валюты.


## Функциональность
Программа позволяет:
* получать актуальные курсы валют от ЦБ РФ (USD, EUR, CNY, GBP);
* видеть дату обновления курсов;
* вводить сумму в рублях для конвертации;
* конвертировать рубли во все поддерживаемые валюты;
* отображать курсы в удобном читаемом формате.


## Поддерживаемые валюты
* **USD** — Доллар США;
* **EUR** — Евро;
* **CNY** — Китайский юань (курс за 10 единиц);
* **GBP** — Фунт стерлингов.

  
## Пояснения к проэкту
В этом проекте используется библиотеки Python [**requests**](https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests) и [**datetime**](https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python).


## Установка
Установка проекта: Зелёная кнопка Code, Download ZIP, открываем папку, запускаем Main.py и пользуемся


## Пример работы:
[![Пример работы](https://img.youtube.com/vi/BGKLTqbtqdE/0.jpg)](https://www.youtube.com/watch?v=BGKLTqbtqdE)


## Технические детали
- Источник данных: официальный [API Центрального банка РФ](https://www.cbr.ru/scripts/XML_daily.asp).
- Формат данных: XML.
- Библиотеки: [requests](https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests) (HTTP‑запросы), стандартная библиотека Python ([xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html), [datetime](https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python)).
- Обработка ошибок: проверка статуса HTTP‑ответа, обработка исключений при парсинге и вводе данных.

## Требования
- Python 3.6 или выше;
- доступ в интернет для получения данных от [ЦБ РФ](https://www.cbr.ru);
- библиотека [requests](https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests)

## Контакты
- Автор: **Black Pagan (BP)**
- GitHub: https://github.com/BlackPaganYT
- Автор на YouTube: https://www.youtube.com/@Black_Pagan_YT
- Автор на Rutude: https://www.rutube.ru/channel/69025093
- Автор на Twitch: https://www.twitch.tv/blackc_dw

