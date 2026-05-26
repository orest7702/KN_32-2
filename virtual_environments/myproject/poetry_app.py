import requests


def get_current_weather():
    # Координати Львова (Широта та Довгота)
    # ВИПРАВЛЕНО: Прибрано зайву розмітку []() з URL
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Оновлені параметри згідно з поточною документацією Open-Meteo
    params = {
        "latitude": 49.8397, 
        "longitude": 24.0297, 
        "current": "temperature_2m,wind_speed_10m,wind_direction_10m"
    }

    try:
        # Відправка HTTP-запиту через бібліотеку, встановлену через Poetry
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Зчитуємо дані з нового блоку "current"
        current = data["current"]

        print("==============================================")
        print("🌤️  ПОТОЧНА ПОГОДА У ЛЬВОВІ (ОТРИМАНО ЧЕРЕЗ POETRY)")
        print("==============================================")
        print(f"🌡️  Температура: {current['temperature_2m']}°C")
        print(f"💨  Швидкість вітру: {current['wind_speed_10m']} км/год")
        print(f"🧭  Напрямок вітру: {current['wind_direction_10m']}°")
        print("==============================================")

    except requests.exceptions.RequestException as e:
        print(f"❌ Помилка при відправці запиту: {e}")


if __name__ == "__main__":
    get_current_weather()
