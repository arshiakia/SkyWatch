import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        sys = data["sys"]
        clouds = data["clouds"]["all"]
        visibility = data.get("visibility", "N/A")
        temperature = main["temp"]
        temp_min = main["temp_min"]
        temp_max = main["temp_max"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        weather_description = weather["description"]
        wind_speed = wind["speed"]
        sunrise = datetime.fromtimestamp(sys["sunrise"]).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(sys["sunset"]).strftime('%H:%M:%S')
        rain = data.get("rain", {}).get("1h", 0)  # میزان بارش در ۱ ساعت گذشته (میلیمتر)
        snow = data.get("snow", {}).get("1h", 0)  # میزان بارش برف در ۱ ساعت گذشته (میلیمتر)

        temp_f = (temperature * 9 / 5) + 32
        wind_speed_kph = wind_speed * 3.6

        print(f"\n🌍 City: {city_name}")
        print(f"🌡️ Temperature: {temperature}°C (Min: {temp_min}°C, Max: {temp_max}°C) / {temp_f}°F")
        print(f"🤒 Feels like: {feels_like}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"📏 Pressure: {pressure} hPa")
        print(f"🌤️ Weather: {weather_description}")
        print(f"☁️ Cloudiness: {clouds}%")
        print(f"💨 Wind Speed: {wind_speed} m/s / {wind_speed_kph} km/h")
        print(f"👀 Visibility: {visibility} meters")
        print(f"🌅 Sunrise: {sunrise}")
        print(f"🌇 Sunset: {sunset}")

        if rain > 0:
            print(f"🌧️ Rain: {rain} mm in last hour")
        if snow > 0:
            print(f"❄️ Snow: {snow} mm in last hour")
    else:
        print("❌ City not found!")

if __name__ == "__main__":
    while True:
        city_name = input("\n🔎 Please enter your city name: ").strip()
        get_weather(city_name, api_key)

        search_again = input("\n🔄 Do you want to search for another city? (yes/no): ").strip().lower()
        if search_again != "yes":
            print("👋 Exiting the program. Have a great day!")
            break
