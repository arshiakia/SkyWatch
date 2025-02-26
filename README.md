# SkyWatch

# EasyCalc
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

همچنین میتوانید با نصب برنامه گیت پروژه را در کامپیوتر خود کلون کنید.

ا1_بتدا مطمعن شوید برنامه git روی لپتاپ شما نصب است. ( [وبسایت رسمی](https://git-scm.com/downloads)  )
2_ سپس محیط cmd کامپیوتر را باز کنید و دستورات زیر را بنویسید.
```
git clone https://github.com/arshiakia/SkyWatch.git
```
سپس وارد فولدر skywatch می شویم.
```
cd skywatch
```
نصب کتابخانه های مورد نیاز پروژه
```
pip install -r requirements.txt
```

برای تست نصب صحیح کتابخانه ها
```
python test_install_libery.py
```
استارت برنامه
```
python SkyWatch.main.py
```

توضیح ماشین حساب ( EasyCalc )
 
این ماشین حساب ساده با استفاده از زبان برنامه‌نویسی پایتون طراحی شده است تا کاربران بتوانند به راحتی محاسبات ریاضی خود را انجام دهند. این برنامه به‌طور ویژه برای کاربرانی که به دنبال ابزاری سریع و کارآمد برای انجام عملیات پایه‌ای ریاضی هستند، مناسب است. 

ویژگی‌های کلیدی ماشین حساب:

1. عملیات پایه: ماشین حساب قابلیت انجام چهار عمل اصلی ریاضی: جمع، تفریق، ضرب و تقسیم را دارد. کاربران می‌توانند با وارد کردن دو عدد و انتخاب نوع عمل، نتیجه را به سرعت دریافت کنند.

2. راحتی در استفاده: این برنامه به گونه‌ای طراحی شده است که کاربر به سادگی می‌تواند گزینه مورد نظر خود را انتخاب کند و وارد کردن اعداد نیز به سادگی انجام می‌شود. 

3. مدیریت خطا: یکی از ویژگی‌های مهم این ماشین حساب، مدیریت خطاهاست. به‌عنوان مثال، در صورت تلاش برای تقسیم بر صفر، برنامه پیام مناسب را به کاربر نمایش می‌دهد.

4. قابلیت خروج: برنامه به کاربران این امکان را می‌دهد که با وارد کردن کلمه «exit» از برنامه خارج شوند. این ویژگی تجربه کاربری را بهبود می‌بخشد و از گیج شدن کاربر جلوگیری می‌کند.





Calculator Description

This simple calculator has been designed using the Python programming language to allow users to easily perform their mathematical calculations. This program is particularly suitable for users seeking a quick and efficient tool for basic arithmetic operations.

Key Features of the Calculator:

1. Basic Operations: The calculator is capable of performing four main arithmetic operations: addition, subtraction, multiplication, and division. Users can quickly obtain results by entering two numbers and selecting the desired operation.

2. Ease of Use: The program is designed in such a way that users can easily select their desired option and input numbers without complications.

3. Error Handling: One of the important features of this calculator is its error management. For example, if a user attempts to divide by zero, the program displays an appropriate message to the user.

4. Exit Capability: The program allows users to exit by entering the command "exit." This feature enhances the user experience and prevents confusion.


