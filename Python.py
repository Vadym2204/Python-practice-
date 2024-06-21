import requests
from datetime import datetime

def get_weather(city, date):
    # API ключ з OpenWeatherMap
    api_key = "41351127e52089017a6b30522320eed2"
    
    # Форматуємо дату у відповідний формат
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    date_str = date_obj.strftime("%Y-%m-%d")
    
    # Формуємо URL запиту
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&dt={date_str}&appid={api_key}&units=metric"
    
    # Надсилаємо запит та отримуємо відповідь
    response = requests.get(url)
    data = response.json()
    
    # Перевіряємо чи запит був успішним
    if response.status_code == 200:
        # Виводимо погодні дані
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"Погода в місті {city} на {date}: {weather}, температура {temp}°C")
    else:
        print("Виникла помилка при отриманні погодних даних.")

# Приклад використання
get_weather("Kyiv", "2024-06-11")