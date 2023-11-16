import requests
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar

def get_weather(api_key, location):
    # API endpoint for current weather data
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    
    # API parameters
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    try:
        # Make the API request
        response = requests.get(endpoint, params=params)
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']

        # Display weather information in GUI
        result_text.set(f"Weather in {location}:\n"
                        f"Temperature: {temperature}°C\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind Speed: {wind_speed} m/s\n"
                        f"Description: {description}")

    except requests.exceptions.RequestException as e:
        result_text.set(f"Error fetching data: {e}")

# Function to handle "Search" button click
def on_search_click():
    location = location_entry.get()
    get_weather(api_key, location)

# Function to handle "Reset" button click
def on_reset_click():
    result_text.set("")
    location_entry.delete(0, 'end')

# Function to handle "Exit" button click
def on_exit_click():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Weather Forecast App")

# Create and pack widgets
location_label = Label(root, text="Enter the name of a city or a zip code:")
location_label.pack(pady=10)

location_entry = Entry(root, width=30)
location_entry.pack(pady=10)

result_text = StringVar()
result_label = Label(root, textvariable=result_text)
result_label.pack(pady=10)

# Frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

search_button = Button(button_frame, text="Search", command=on_search_click, bg='blue', fg='white')
search_button.grid(row=0, column=0, padx=5)

reset_button = Button(button_frame, text="Reset", command=on_reset_click, bg='blue', fg='white')
reset_button.grid(row=0, column=1, padx=5)

exit_button = Button(button_frame, text="Exit", command=on_exit_click, bg='red', fg='white')
exit_button.grid(row=0, column=2, padx=5)

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'c07aa467d127aa3e28e6f8bb0606eee0'

# Start the GUI main loop
root.mainloop()
