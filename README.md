<p align="center">
  <img src="https://raw.githubusercontent.com/arshiakia/SkyWatch/main/assets/banner.png" alt="SkyWatch Banner" width="800"/>
</p>

<p align="center">
  <a href="https://github.com/arshiakia/SkyWatch/stargazers">
    <img src="https://img.shields.io/github/stars/arshiakia/SkyWatch?style=social" alt="GitHub stars"/>
  </a>
  <a href="https://github.com/arshiakia/SkyWatch/network/members">
    <img src="https://img.shields.io/github/forks/arshiakia/SkyWatch?style=social" alt="GitHub forks"/>
  </a>
  <a href="https://github.com/arshiakia/SkyWatch/issues">
    <img src="https://img.shields.io/github/issues/arshiakia/SkyWatch" alt="GitHub issues"/>
  </a>
  <a href="https://github.com/arshiakia/SkyWatch/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/arshiakia/SkyWatch" alt="License"/>
  </a>
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/python-3.7%2B-blue" alt="Python Version"/>
  </a>
</p>

---

# 🌥️ SkyWatch

> “هر روز، آسمان را نظاره کن و بدان که دنیا همیشه در حال تغییر است.”  
> یک ابزار ساده اما قدرتمند برای نمایش وضعیت آب‌وهوای هر شهر با زبان Python.

---

## 📒 فهرست مطالب

1. [📝 معرفی](#%E2%8C%90-%D9%85%D8%B9%D8%B1%D9%81%DB%8C)  
2. [✨ ویژگی‌ها](#%E2%8C%90-%D9%88%DB%8C%DA%98%DA%AF%DB%8C%E2%80%8C%D9%87%D8%A7)  
3. [📸 اسکرین‌شات‌ها](#%E2%8C%90-%D8%A7%D8%B3%DA%A9%D8%B1%DB%8C%D9%86%E2%80%8C%D8%B4%D8%A7%D8%AA%E2%80%8C%D9%87%D8%A7)  
4. [🚀 نصب و راه‌اندازی](#%E2%8C%90-%D9%86%D8%B5%D8%A8-%D9%88-%D8%B1%D8%A7%D9%87%E2%80%8C%D8%A7%D9%86%D8%AF%D8%A7%D8%B2%DB%8C)  
5. [▶️ نحوه اجرا](#%E2%8C%90-%D9%86%D8%AD%D9%88%D9%87-%D8%A7%D8%AC%D8%B1%D8%A7)  
    - [🔹 نسخه CLI](#%EF%B8%8F-نسخه-cli)  
    - [🔹 نسخه GUI](#%EF%B8%8F-نسخه-gui)  
6. [🛠️ ساختار پوشه‌ها](#%E2%8C%90-%D8%B3%D8%A7%D8%AE%D8%AA%D8%A7%D8%B1-%D9%BE%D9%88%D8%B4%D9%87%E2%80%8C%D9%87%D8%A7)  
7. [🤝 نحوه مشارکت](#%E2%8C%90-%D9%86%D8%AD%D9%88%D9%87-%D9%85%D8%B4%D8%A7%D8%B1%DA%A9%D8%AA)  
8. [📄 مجوز](#%E2%8C%90-%D9%85%D8%AC%D9%88%D8%B2)  
9. [📡 ارتباط با من](#%E2%8C%90-%D8%A7%D8%B1%D8%AA%D8%A8%D8%A7%D8%B7-%D8%A8%D8%A7-%D9%85%D9%86)

---

## 📝 معرفی

**SkyWatch** یک ابزار نوشته‌شده با پایتون است که وضعیت آب‌وهوای هر شهری را از طریق API وب‌سایت [OpenWeatherMap](https://openweathermap.org/api) می‌گیرد و با زبانی بسیار ساده و تصویری به شما نمایش می‌دهد.  
این پروژه مناسب افرادی است که دوست دارند در چند ثانیه اطلاعات کاملی مانند دما، رطوبت، فشار، سرعت باد، میزان ابری بودن، دید افقی و زمان طلوع/غروب خورشید را بدانند—هم در رابط خط فرمان و هم در یک رابط گرافیکی ساده (GUI).

🌍 **چرا SkyWatch؟**  
- **سریع و سبک**: بدون نیاز به فریم‌ورک‌های سنگین، فقط با requests و tkinter.  
- **کاربرپسند**: نمایش روان داده‌ها با ایموجی و زبان قابل فهم.  
- **چندمنظوره**: هم برای توسعه‌دهنده‌هایی که CLI را ترجیح می‌دهند و هم برای کاربرانی که عاشق پنجره‌های گرافیکی هستند.  
- **گردش واحدها**: تبدیل خودکار دما از سلسیوس به فارنهایت و سرعت باد از متر بر ثانیه به کیلومتر بر ساعت.

---

## ✨ ویژگی‌ها

- 🔍 **جست‌وجوی سریع**: کافی‌ست نام شهر را وارد کنید تا تمام اطلاعات آب‌وهوایی به نمایش دربیاید.  
- 🌡️ **دما (Temperature)**: نمایش بر حسب درجه سلسیوس و تبدیل خودکار به فارنهایت.  
- 🤒 **دما احساس‌شده (Feels Like)**: حس واقعی دمای هوا را نشان می‌دهد.  
- 💧 **رطوبت (Humidity)**: درصد رطوبت محیط.  
- 📏 **فشار هوا (Pressure)**: بر حسب هکتوپاسکال (hPa).  
- 🌤️ **وضعیت آب‌وهوا (Weather Description)**: توضیح متنی مثل “صاف”، “ابری”، “بارانی”.  
- ☁️ **ابری بودن (Cloudiness)**: درصد ابرهای موجود.  
- 💨 **سرعت باد (Wind Speed)**: نمایش بر حسب متر بر ثانیه و تبدیل خودکار به کیلومتر بر ساعت.  
- 👀 **دید افقی (Visibility)**: به متر.  
- 🌅 **طلوع خورشید (Sunrise)** و 🌇 **غروب خورشید (Sunset)**: زمان دقیق هر دو.  
- 🌧️ **بارش باران (Rain)** و ❄️ **بارش برف (Snow)**: اگر در ۱ ساعت گذشته میزان بارش وجود داشته باشد.  
- 🖥️ **دو نسخه کاربردی**:  
  - **CLI**: اجرای در ترمینال/CMD با ظاهر ساده و روان.  
  - **GUI**: یک رابط گرافیکی سبک با Tkinter برای تجربه کاربری گرافیکی.  
- 🔄 **تبدیل واحدها**: فقط کافی‌ست تأیید کنید تا واحدهای دما و باد تبدیل
