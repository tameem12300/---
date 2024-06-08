# Проект Бот погоды в Телеграме
Этот проект представляет собой помощника, который показывает нам информацию о погоде в каком - то городе в мире в то время, который нам нравится. Он включает в себя телеграм - бот и данные про погоду во всех городах с помощью API
# Основа проекта
## Работа с информацией погоды
* Используем сервис **OpenWeatherMap**, реализуем программу, которая показывает погоду, влажность и давление в указанном городе "city_name" и в указанной стране "country_name".
* Мы используем токен **API_KEY** и выполняем запрос `requests.get("website")` чтобы получить доступ к сервису. Базовый URL для API OpenWeatherMap http://api.openweathermap.org
* Типы данных погоды мы создаём в форме класса WeatherAPI и сохраниили в отделном файле weather.py
* после того как получить доступ к сервису и отправить запрос к сервису, мы преобразуем ответ в **JSON-формат** через команду `response.json()`
## Телеграм - бот
* В файле telebot.py мы пишем программу, которая запускает бота работать.
* Во время исползования бота, должно запускать программу одновременно.
* Мы используем декоратор чтобы выполнять сообщение между пользователью и ботом
* пример:
<pre><code>@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
...</code></pre>
Это функция, которая определить команды для бота
* Мы используем функцию `InlineKeyboardMarkup` и `InlineKeyboardButton` чтобы создать клавиатуру с кнопками для выбора информации
## Команды для бота
1. отправить команду `/start` для начала сообщения.
2. отправить боту команду `/help` для получения помощи про сообщение.
3. отправить боту команду `weather: город, страна` чтобы получить общую оценку про погоду в том городе
## Библиотеки, которые нужные для проекта
1. `telebot` - помогает создать бота
2. `requests` - помогает отправить запрос к сервису `OpenWeatherMap`
3. модуль `types` библиотеки `telebot` - помогает создать клавиатуру с кнопками


