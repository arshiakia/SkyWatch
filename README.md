# SkyWatch

# Program Description

این برنامه یک ابزار پایتون برای دریافت اطلاعات آب و هوایی از یک شهر است که با استفاده از وب‌سایت OpenWeatherMap کار می‌کند.

این برنامه به کاربر اجازه می‌دهد تا با وارد کردن نام یک شهر، اطلاعات مربوط به وضعیت آب و هوای آن را دریافت کند.
داده‌های آب و هوایی از API OpenWeatherMap دریافت می‌شوند که شامل اطلاعاتی مانند**دما ، رطوبت ، فشار ، سرعت باد ، و زمان طلوع و غروب خورشید** است.

# اطلاعات ارائه شده :

   - دما (درجه سانتی‌گراد)
   - دمای احساس شده (درجه سانتی‌گراد)
   - رطوبت (%)
   - فشار (هکتوپاسکال)
   - توضیحات وضعیت آب و هوا (مثلاً آفتابی، بارانی و غیره)
   - سرعت باد (متر بر ثانیه)
   - زمان طلوع و غروب خورشید (به فرمت ساعت)

تبدیل واحدها :
برنامه به کاربر این امکان را می‌دهد که در صورت تمایل ، **دما را به فارنهایت** و **سرعت باد را به کیلومتر بر ساعت** تبدیل کند.

---


This program is a Python tool for obtaining weather information from a city using the OpenWeatherMap website.

This program allows the user to enter the name of a city and receive information about the current weather conditions there. Weather data is retrieved from the OpenWeatherMap API and includes information such as **temperature, humidity, pressure, wind speed, and sunrise and sunset times**.

# Provided Information:

- Temperature (in degrees Celsius)
- Feels like temperature (in degrees Celsius)
- Humidity (%)
- Pressure (hPa)
- Weather condition description (e.g., sunny, rainy, etc.)
- Wind speed (meters per second)
- Sunrise and sunset times (in hour format)

Unit Conversion:
The program gives the user the option to convert **temperature to Fahrenheit** and **wind speed to kilometers per hour** if desired.

# python code
```
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
    api_key = "9223600940f768c665c5a16a81bb6d56"
    city_name = input("Please enter your city name: ")
    get_weather(city_name, api_key)
```
# کلون کردن پروژه skywatch 

همچنین میتوانید با نصب برنامه گیت  پروژه را در کامپیوتر خود کلون کنید.

1_ ابتدا پایتون را سیستم خود نصب کنید. ( [وبسایت رسمی](https://www.python.org/downloads/)  )
و برای اینکه بدانیم سیستم پایتون را شناخته است یا خیر دستور زیر را در cmd اجرا کنید.
```
python --version
```
2_مطمعن شوید برنامه git روی لپتاپ شما نصب است. ( [وبسایت رسمی](https://git-scm.com/downloads)  )


3_ سپس محیط cmd کامپیوتر را باز کنید و دستورات زیر را بنویسید تا پروژه کلون شود.
```
git clone https://github.com/arshiakia/SkyWatch.git
```
4_ سپس وارد فولدر skywatch می شویم.
```
cd skywatch
```
5_ نصب کتابخانه های مورد نیاز پروژه
```
pip install -r requirements.txt
```

6_ برای تست نصب صحیح کتابخانه ها
```
python test_install_libery.py
```
7_ استارت برنامه
```
python SkyWatch.main.py
```

