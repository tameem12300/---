import requests  # Импорт библиотеки requests для выполнения HTTP-запросов

API_KEY = 'b7a21354ab464ff233aeb13939fb9582'  # Ключ API для доступа к OpenWeatherMap

class WeatherAPI:  # Определение класса WeatherAPI
    base_url = 'http://api.openweathermap.org'  # Базовый URL для API OpenWeatherMap
    url_coord = '/geo/1.0/direct'  # URL для получения координат
    url_weather = '/data/2.5/weather'  # URL для получения данных о погоде
    
    def __init__(self, city='Saint-Petersburg', country='Russia', lg='ru'):  # Конструктор класса
        self.city = city  # Инициализация города
        self.country = country  # Инициализация страны
        self.lg = lg  # Инициализация языка
        self.lat = 0  # Инициализация широты
        self.lon = 0  # Инициализация долготы

    def retrieve_coord(self):  # Метод для получения координат
        params = {'q': f'{self.city},{self.country}', 'limit': 1, 'appid': API_KEY}  # Параметры запроса
        url = f'{self.base_url}{self.url_coord}'  # Формирование полного URL
        response = requests.get(url, params=params)  # Выполнение GET-запроса
        data = response.json()  # Преобразование ответа в JSON-формат
        if response.status_code == 200 and data:  # Проверка успешности запроса
            self.lat = data[0]['lat']  # Извлечение широты из ответа
            self.lon = data[0]['lon']  # Извлечение долготы из ответа
        else:
            raise Exception(f"Error retrieving coordinates for {self.city}, {self.country}")  # Генерация исключения в случае ошибки

    def get_weather_info(self):  # Метод для получения информации о погоде
        if self.lat == 0 and self.lon == 0:  # Проверка, получены ли координаты
            self.retrieve_coord()  # Получение координат
        
        params = {'lat': self.lat, 'lon': self.lon, 'units': 'metric', 'lang': self.lg, 'appid': API_KEY}  # Параметры запроса
        url = f'{self.base_url}{self.url_weather}'  # Формирование полного URL
        response = requests.get(url, params=params)  # Выполнение GET-запроса
        data = response.json()  # Преобразование ответа в JSON-формат
        
        if response.status_code == 200:  # Проверка успешности запроса
            description = data['weather'][0]['main']  # Извлечение описания погоды
            weather_info = (f"City: {self.city}\n"  # Формирование строки с информацией о погоде
                            f"Weather: {description.capitalize()}")
            return weather_info  # Возврат информации о погоде
        else:
            raise Exception(f"Error retrieving weather for {self.city}, {self.country}")  # Генерация исключения в случае ошибки
        
    def get_weather_temp(self):  # Метод для получения температуры
        if self.lat == 0 and self.lon == 0:  # Проверка, получены ли координаты
            self.retrieve_coord()  # Получение координат
        
        params = {'lat': self.lat, 'lon': self.lon, 'units': 'metric', 'lang': self.lg, 'appid': API_KEY}  # Параметры запроса
        url = f'{self.base_url}{self.url_weather}'  # Формирование полного URL
        response = requests.get(url, params=params)  # Выполнение GET-запроса
        data = response.json()  # Преобразование ответа в JSON-формат

        if response.status_code == 200:  # Проверка успешности запроса
            temp = data['main']['temp']  # Извлечение температуры из ответа
            temp_info = (f"City: {self.city}\n"  # Формирование строки с информацией о температуре
                         f"Temperature: {temp}°C\n")
            return temp_info  # Возврат информации о температуре
        else:
            raise Exception(f"Error retrieving weather for {self.city}, {self.country}")  # Генерация исключения в случае ошибки
        
    def get_humidity(self):  # Метод для получения влажности
        if self.lat == 0 and self.lon == 0:  # Проверка, получены ли координаты
            self.retrieve_coord()  # Получение координат
        
        params = {'lat': self.lat, 'lon': self.lon, 'units': 'metric', 'lang': self.lg, 'appid': API_KEY}  # Параметры запроса
        url = f'{self.base_url}{self.url_weather}'  # Формирование полного URL
        response = requests.get(url, params=params)  # Выполнение GET-запроса
        data = response.json()  # Преобразование ответа в JSON-формат

        if response.status_code == 200:  # Проверка успешности запроса
            humidity = data['main']['humidity']  # Извлечение влажности из ответа
            humidity_info = (f"City: {self.city}\n"  # Формирование строки с информацией о влажности
                             f"Humidity: {humidity}%\n")
            return humidity_info  # Возврат информации о влажности
        else:
            raise Exception(f"Error retrieving weather for {self.city}, {self.country}")  # Генерация исключения в случае ошибки
        
    def get_weather_pressure(self):  # Метод для получения давления
        if self.lat == 0 and self.lon == 0:  # Проверка, получены ли координаты
            self.retrieve_coord()  # Получение координат
        
        params = {'lat': self.lat, 'lon': self.lon, 'units': 'metric', 'lang': self.lg, 'appid': API_KEY}  # Параметры запроса
        url = f'{self.base_url}{self.url_weather}'  # Формирование полного URL
        response = requests.get(url, params=params)  # Выполнение GET-запроса
        data = response.json()  # Преобразование ответа в JSON-формат

        if response.status_code == 200:  # Проверка успешности запроса
            pressure = data['main']['pressure']  # Извлечение давления из ответа
            pressure_info = (f"City: {self.city}\n"  # Формирование строки с информацией о давлении
                         f"pressure: {pressure} Pa\n")
            return pressure_info  # Возврат информации о давлении
        else:
            raise Exception(f"Error retrieving weather for {self.city}, {self.country}")  # Генерация исключения в случае ошибки

