# Конвентатор волют
Простой конвертер валют на Python, который получает актуальные курсы от Центрального банка РФ и позволяет конвертировать рубли в основные мировые валюты.


## Разработчик
Привет! Это конвентатор волют. Его сделал я, **Black Pagan (BP)**. Я есть на [YouTube](https://www.youtube.com/@Black_Pagan_YT), на [Rutube](rutube.ru/channel/69025093), и на [Twich](https://www.twitch.tv/blackc_dw).


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
1. Клонируйте репозиторий:
   ```
   git clone https://github.com/your-username/currency-converter.git
   ```
2. Перейдите в папку проекта:
   ```
   cd currency-converter
   ```
3. Установите зависимости:

   ```
   pip install requests
   ```

## Пример работы:
[![Пример работы](https://img.youtube.com/vi/BGKLTqbtqdE/0.jpg)](https://www.youtube.com/watch?v=BGKLTqbtqdE)


## Технические детали
- Источник данных: официальный API Центрального банка РФ (https://www.cbr.ru/scripts/XML_daily.asp).
- Формат данных: XML.
- Библиотеки: requests (HTTP‑запросы), стандартная библиотека Python (xml.etree.ElementTree, datetime).
- Обработка ошибок: проверка статуса HTTP‑ответа, обработка исключений при парсинге и вводе данных.





