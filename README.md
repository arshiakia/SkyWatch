# SkyWatch

# Program Description

این برنامه یک ابزار پایتون برای دریافت اطلاعات آب و هوایی از یک شهر است که با استفاده از وب‌سایت OpenWeatherMap کار می‌کند.

این برنامه به کاربر اجازه می‌دهد تا با وارد کردن نام یک شهر، اطلاعات مربوط به وضعیت آب و هوای آن را دریافت کند.
داده‌های آب و هوایی از API OpenWeatherMap دریافت می‌شوند که شامل اطلاعاتی مانند**دما ، رطوبت ، فشار ، سرعت باد ، و زمان طلوع و غروب خورشید** است.

# اطلاعات ارائه شده :

نام شهر

دما

دمای احساس شده

رطوبت

فشار هوا

توضیحات وضعیت آب و هوا

میزان ابری بودن

سرعت باد

دید افقی

زمان طلوع خورشید

زمان غروب خورشید

بارش

برف

تبدیل واحدها :
برنامه به کاربر این امکان را می‌دهد که در صورت تمایل ، **دما را به فارنهایت** و **سرعت باد را به کیلومتر بر ساعت** تبدیل کند.

---


This program is a Python tool for obtaining weather information from a city using the OpenWeatherMap website.

This program allows the user to enter the name of a city and receive information about the current weather conditions there. Weather data is retrieved from the OpenWeatherMap API and includes information such as **temperature, humidity, pressure, wind speed, and sunrise and sunset times**.

# Provided Information:

1_City Name

2_Temperature

3_Feels Like

4_Humidity

5_Pressure

6_Weather Description

7_Cloudiness

8_Wind Speed

9_Visibility

10_Sunrise

11_Sunset

12_Rain 

13_Snow

Unit Conversion:
The program gives the user the option to convert **temperature to Fahrenheit** and **wind speed to kilometers per hour** if desired.

# python code
```
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
8_ استارت برنامه با محیط گرافیکی (GUI)
```
python skywatch.main.GUI.py
```

![Code frequency](https://github.com/user-attachments/assets/92b1eea8-04ea-4e3e-8bfc-f97996f938f8)

# Contributors
![Contributors](https://github.com/user-attachments/assets/e45e22ae-3ccf-4f0e-a3f3-9ee94fde193c)



