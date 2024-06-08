import telebot  # импортируем библиотеку telebot
from telebot import types  # импортируем модуль types из библиотеки telebot
import requests  # импортируем библиотеку requests
from weather import WeatherAPI  # импортируем класс WeatherAPI из модуля weather


API_KEY = 'b7a21354ab464ff233aeb13939fb9582'  # задаем API ключ для использования


bot = telebot.TeleBot("7205887797:AAFmTbG_Lryr8Nh3BE5DI9ARujI-Dvc7UzY")  # создаем экземпляр бота


user_data = {}  # создаем словарь для хранения данных пользователя

# создаем обработчик сообщений для команд '/start' и '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == "/start":  # если команда '/start'
        bot.send_message(message.chat.id, 
                         "Hello, I am a weather bot. I can provide weather conditions all over the world. "
                         "You can ask me about:\n"
                         "- Weather in a specific city\n"
                         "Examples:\n"
                         "weather: Moscow, Russia\n"
                         "I will be happy to help you :)")  # отправляем приветственное сообщение
    elif message.text == "/help":  # если команда '/help'
        bot.send_message(message.chat.id, "You can type /start to begin or /help to see this message again.")  # отправляем сообщение с подсказкой



# создаем обработчик для всех других сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text.lower()  # приводим текст сообщения к нижнему регистру
    if text.startswith('weather:'):  # если сообщение начинается с 'weather:'
        city_country = text[len('weather:'):].strip()  # извлекаем название города и страны
        handle_weather_request(message, city_country)  # вызываем функцию для обработки запроса погоды
    else:
        bot.send_message(message.chat.id, "Sorry, I didn't understand that. Please use 'weather:' followed by the city and country.")  # отправляем сообщение об ошибке


# функция для обработки запроса погоды
def handle_weather_request(message, city_country):
    place = city_country.split(",")  # разделяем строку на город и страну
    if len(place) == 2:  # если удалось разделить на две части
        city = place[0].strip()  # получаем название города
        country = place[1].strip()  # получаем название страны
        try:
            weather = WeatherAPI(city=city, country=country)  # создаем экземпляр класса WeatherAPI
            weather_info = weather.get_weather_info()  # получаем информацию о погоде
            
            bot.send_message(message.chat.id, f"Weather in {city}, {country}:\n{weather_info}")  # отправляем сообщение с информацией о погоде

            # сохраняем экземпляр weather в данных пользователя
            user_data[message.chat.id] = weather

            keyboard = types.InlineKeyboardMarkup()  # создаем клавиатуру с кнопками
            key_temp = types.InlineKeyboardButton(text='temperature', callback_data=f'temperature_{message.chat.id}')  # кнопка для температуры
            keyboard.add(key_temp)
            key_humidity = types.InlineKeyboardButton(text='humidity', callback_data=f'humidity_{message.chat.id}')  # кнопка для влажности
            keyboard.add(key_humidity)
            key_preasure = types.InlineKeyboardButton(text="pressure", callback_data= f'pressure_{message.chat.id}')  # кнопка для давления
            keyboard.add(key_preasure)
            key_no_need = types.InlineKeyboardButton(text="thanks", callback_data="thanks")  # кнопка для благодарности
            keyboard.add(key_no_need)
            
            question = f'what additional weather conditions do you want to know about {city}, {country}?'  # формируем вопрос
            bot.send_message(message.chat.id, text=question, reply_markup=keyboard)  # отправляем сообщение с кнопками
        
        except Exception as e:  # обработка исключений
            bot.send_message(message.chat.id, f"An error occurred: {str(e)}")  # отправляем сообщение об ошибке
    else:
        bot.send_message(message.chat.id, "Please provide the location in 'city, country' format.")  # отправляем сообщение с просьбой корректного ввода



# обработчик для кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:  # если сообщение существует
            chat_id = call.message.chat.id
            if call.data.startswith('temperature'):  # если нажата кнопка температуры
                if chat_id in user_data:
                    weather = user_data[chat_id]  # получаем данные пользователя
                    detailed_info = weather.get_weather_temp()  # получаем подробную информацию о температуре
                    
                    bot.send_message(call.message.chat.id, f"Here is more detailed information about the weather:\n{detailed_info}")  # отправляем сообщение с подробной информацией
                else:
                    bot.send_message(call.message.chat.id, "No weather information found. Please start again by typing /start.")  # отправляем сообщение об ошибке

            elif call.data.startswith('pressure'):  # если нажата кнопка давления
                if chat_id in user_data:
                    weather = user_data[chat_id]  # получаем данные пользователя
                    detailed_info = weather.get_weather_pressure()  # получаем подробную информацию о давлении
                    
                    bot.send_message(call.message.chat.id, f"Here is more detailed information about the weather:\n{detailed_info}")  # отправляем сообщение с подробной информацией
                else:
                    bot.send_message(call.message.chat.id, "No weather information found. Please start again by typing /start.")  # отправляем сообщение об ошибке

            elif call.data.startswith('humidity'):  # если нажата кнопка влажности
                if chat_id in user_data:
                    weather = user_data[chat_id]  # получаем данные пользователя
                    detailed_info = weather.get_humidity()  # получаем информацию о влажности
                    
                    bot.send_message(call.message.chat.id, f"Here is the humidity information:\n{detailed_info}")  # отправляем сообщение с информацией о влажности
                else:
                    bot.send_message(call.message.chat.id, "No weather information found. Please start again by typing /start.")  # отправляем сообщение об ошибке
            elif call.data == 'thanks':  # если нажата кнопка благодарности
                bot.send_message(call.message.chat.id, "You're welcome! If you need more information, just ask.")  # отправляем сообщение с благодарностью
    except Exception as e:  # обработка исключений
        bot.send_message(call.message.chat.id, f"An error occurred: {str(e)}")  # отправляем сообщение об ошибке

# запускаем polling
bot.polling(none_stop=True)  # бот будет работать непрерывно

