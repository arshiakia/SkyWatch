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

---

# Contributors
![Contributors](https://github.com/user-attachments/assets/e45e22ae-3ccf-4f0e-a3f3-9ee94fde193c)

# Code frequency over the history of arshiakia/SkyWatch
![Code frequency](https://github.com/user-attachments/assets/09e3c421-ee5d-40b9-9fa4-0862b6e26318)


