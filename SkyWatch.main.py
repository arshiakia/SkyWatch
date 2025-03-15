import requests
from datetime import datetime

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
        temperature = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        weather_description = weather["description"]
        wind_speed = wind["speed"]
        sunrise = datetime.fromtimestamp(sys["sunrise"]).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(sys["sunset"]).strftime('%H:%M:%S')

        print(f"\nCity: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather: {weather_description}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")

        convert_units(temperature, wind_speed)
    else:
        print("City not found!")


def convert_units(temp_c, wind_speed_mps):
    choice = input("\nDo you want to convert units? (yes/no): ").strip().lower()

    if choice == "yes":
        temp_f = (temp_c * 9 / 5) + 32
        print(f"\nTemperature in Fahrenheit: {temp_f}°F")

        wind_speed_kph = wind_speed_mps * 3.6
        print(f"Wind Speed in km/h: {wind_speed_kph} km/h")
    else:
        print("No unit conversion requested.")


if __name__ == "__main__":
    api_key = "461fc1ff3a0923d864d6a3305f0b78f4"
    city_name = input("Please enter your city name: ")
    get_weather(city_name, api_key)



    #arshia_kiakazemi
