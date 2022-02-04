import requests
import json
from tkinter import *
from PIL import ImageTk, Image
import datetime as dt
from datetime import timezone, timedelta

api_key = ''

api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?id=' + str(6077243) + '&appid=' + api_key + '&units=metric')
response = api_request.text
json_data = json.loads(response)

dict_tz = {-43200: -12, -39600: -11, -36000: -10, -34200: -9.5, -32400: -9, -28800: -8, -25200: -7, -21600: -6, -18000: -5, -16200: -4.5, -14400: -4,
-12600: -3.5, -10800: -3, -7200: -2, -3600: -1, 0: 0, 3600: 1, 7200: 2, 10800: 3, 12600: 3.5, 14400: 4, 16200: 4.5, 18000: 5, 19800: 5.5, 20700: 5.75, 21600: 6,
23400: 6.5, 25200: 7, 28800: 8, 32400: 9, 34200: 9.5, 36000: 10, 37800: 10.5, 39600: 11, 41400: 11.5, 43200: 12, 45900: 12.75, 46800: 13, 50400: 14}

weather_main = json_data['weather'][0]['main']
weather_description = json_data['weather'][0]['description']
weather_icon = json_data['weather'][0]['icon'] + '@2x.png'
temperature = str(json_data['main']['temp'])
feels_like = str(json_data['main']['feels_like'])
country = json_data['sys']['country']
city = json_data['name']
time = json_data['dt']
timezone_ = json_data['timezone']
tz = timezone(timedelta(hours=dict_tz[timezone_]))

root = Tk()
root.title('Weather App')

city_label = Label(root, text=city + ', ' + country, font=('Georgia', 40))
city_label.grid(row=0, column=0, columnspan=2)

date = dt.datetime.fromtimestamp(time, tz).strftime("%Y/%m/%d %H:%M")
date_label = Label(root, text=date, font=('Georgia', 30))
date_label.grid(row=1, column=0, columnspan=2)

temp_label = Label(root, text='Temperature : ' + temperature + '°C', font=('Georgia', 40))
temp_label.grid(row=2, column=0, columnspan=2)

feels_label = Label(root, text='Feels like : ' + feels_like + '°C', font=('Georgia', 30))
feels_label.grid(row=3, column=0, columnspan=2)

main_label = Label(root, text=weather_main + ' : ' + weather_description, font=('Georgia', 40))
main_label.grid(row=4, column=0, columnspan=2)

icon = ImageTk.PhotoImage(Image.open('./images/' + weather_icon))
icon_label = Label(root, image=icon)
icon_label.grid(row=5, column=0, columnspan=2)

entry = Entry(root, width=25, bd=3)
entry.grid(row=6, column=0, padx=(50,0))

def enter():
    global ico
    city = entry.get()
    entry.delete(0, END)
    api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key + '&units=metric')
    response = api_request.text
    json_data = json.loads(response)
    weather_main = json_data['weather'][0]['main']
    weather_description = json_data['weather'][0]['description']
    weather_icon = json_data['weather'][0]['icon'] + '@2x.png'
    temperature = str(json_data['main']['temp'])
    feels_like = str(json_data['main']['feels_like'])
    country = json_data['sys']['country']
    city = json_data['name']
    time = json_data['dt']
    city_label['text'] = city + ', ' + country
    temp_label['text'] = 'Temperature : ' + temperature + '°C'
    feels_label['text'] = 'Feels like : ' + feels_like + '°C'
    main_label['text'] = weather_main + ' : ' + weather_description
    ico = ImageTk.PhotoImage(Image.open('./images/' + weather_icon))
    icon_label['image'] = ico
    icon_label.grid(row=5, column=0, columnspan=2)
    time = json_data['dt']
    timezone_ = json_data['timezone']
    tz = timezone(timedelta(hours=dict_tz[timezone_]))
    date = dt.datetime.fromtimestamp(time, tz).strftime("%Y/%m/%d %H:%M")
    date_label['text'] = date

button = Button(root, text='Enter', padx=20, pady=20, command=enter)
button.grid(row=6, column=1, pady=(0,15), padx=(0, 120))

root.mainloop()