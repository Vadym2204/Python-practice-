import requests
from datetime import datetime, timedelta


def get_weather(city, date):
    api_key = "41351127e52089017a6b30522320eed2"

    date_obj = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.now().date()

    if date_obj.date() < current_date:
        print("Неможливо отримати історичні дані.")
        return
    elif (date_obj.date() - current_date).days > 5:
        print("Прогноз доступний лише на 5 днів вперед.")
        return

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        for forecast in data['list']:
            forecast_date = datetime.fromtimestamp(forecast['dt'])
            if forecast_date.date() == date_obj.date():
                weather = forecast['weather'][0]['description']
                temp = forecast['main']['temp']
                print(f"Прогноз погоди в місті {city} на {date}: {weather}, температура {temp}°C")
                return
        print(f"Не знайдено прогнозу на {date}")
    else:
        print("Виникла помилка при отриманні погодних даних.")


# Приклад використання
get_weather("Ivano-Frankivsk", "2024-06-25")