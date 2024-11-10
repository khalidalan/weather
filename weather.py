import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "ad91326942c517882655cf821c98c25f"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        weather_data = response.json()

        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            rain_chance = weather_data['clouds']['all']
            pressure = weather_data['main']['pressure']

            temp_label.config(text=f"Temperature: {temperature}°C")
            humidity_label.config(text=f"Humidity: {humidity}%")
            wind_label.config(text=f"Wind Speed: {wind_speed} km/h")
            pressure_label.config(text=f"Pressure: {pressure} hPa")
            rain_label.config(text=f"Precipitation: {rain_chance}%")
            result_label.config(text="")

            check_another_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
        
        else:
            result_label.config(text="City not found. Please try again.")
            check_another_button.grid_forget()  
            
    except Exception as e:
        result_label.config(text="Error fetching weather data.")
        check_another_button.grid_forget()  

def check_another_location():

    city_entry.delete(0, tk.END)  
    temp_label.config(text="Temperature: --")
    humidity_label.config(text="Humidity: --")
    wind_label.config(text="Wind Speed: --")
    pressure_label.config(text="Pressure: --")
    rain_label.config(text="Precipitation: --")
    result_label.config(text="")
    check_another_button.grid_forget()  

root = tk.Tk()
root.title("Weather Forecast")
root.geometry("400x300")

location_label = tk.Label(root, text="Location:", font=("Helvetica", 12))
location_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(root, width=20)
city_entry.grid(row=0, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Search", command=get_weather)
search_button.grid(row=0, column=2, padx=10, pady=10)

temp_label = tk.Label(root, text="Temperature: --", font=("Helvetica", 12))
temp_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

humidity_label = tk.Label(root, text="Humidity: --", font=("Helvetica", 12))
humidity_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

wind_label = tk.Label(root, text="Wind Speed: --", font=("Helvetica", 12))
wind_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

pressure_label = tk.Label(root, text="Pressure: --", font=("Helvetica", 12))
pressure_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

rain_label = tk.Label(root, text="Precipitation: --", font=("Helvetica", 12))
rain_label.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)


check_another_button = tk.Button(root, text="Check another location", command=check_another_location)
check_another_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
check_another_button.grid_forget()  

root.mainloop()
