import os
import requests
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

# Function to fetch and display weather details
def get_weather():
    city_name = city_entry.get().strip()
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
        rain = data.get("rain", {}).get("1h", 0)
        snow = data.get("snow", {}).get("1h", 0)

        # Unit conversion
        temp_f = (temperature * 9 / 5) + 32
        wind_speed_kph = wind_speed * 3.6

        # Display the weather info in the label
        result_text.set(f"\n🌍 City: {city_name}\n"
                        f"🌡️ Temperature: {temperature}°C (Min: {temp_min}°C, Max: {temp_max}°C) / {temp_f}°F\n"
                        f"🤒 Feels like: {feels_like}°C\n"
                        f"💧 Humidity: {humidity}%\n"
                        f"📏 Pressure: {pressure} hPa\n"
                        f"🌤️ Weather: {weather_description}\n"
                        f"☁️ Cloudiness: {clouds}%\n"
                        f"💨 Wind Speed: {wind_speed} m/s / {wind_speed_kph} km/h\n"
                        f"👀 Visibility: {visibility} meters\n"
                        f"🌅 Sunrise: {sunrise}\n"
                        f"🌇 Sunset: {sunset}\n")

        if rain > 0:
            result_text.set(result_text.get() + f"🌧️ Rain: {rain} mm in last hour\n")
        if snow > 0:
            result_text.set(result_text.get() + f"❄️ Snow: {snow} mm in last hour\n")
    else:
        messagebox.showerror("Error", "City not found!")

# Creating the GUI
root = Tk()
root.title("Weather App")
root.geometry("600x600")
root.config(bg="#1e2a47")

# City name input label
city_label = Label(root, text="Enter City Name:", font=("Arial", 16, "bold"), fg="white", bg="#1e2a47")
city_label.pack(pady=20)

# City name input entry
city_entry = Entry(root, font=("Arial", 14), width=25, bd=2, relief="solid", justify="center")
city_entry.pack(pady=10)

# Search button
search_button = Button(root, text="Get Weather", font=("Arial", 14), bg="#4CAF50", fg="white", command=get_weather)
search_button.pack(pady=20)

# Result label
result_text = StringVar()
result_label = Label(root, textvariable=result_text, font=("Arial", 12), fg="white", bg="#1e2a47", justify=LEFT)
result_label.pack(pady=10, padx=20)

# Styling the window background color
root.config(bg="#1e2a47")

# Run the GUI
root.mainloop()
