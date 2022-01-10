

import requests
from flask import Flask
from models import connect_db, db, City
from secrets import WEATHER_KEY

app = Flask(__name__)
connect_db(app)


url_weather = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=4cd07ce8d2eaa374c6b57b6cdabf4c0b"

def get_weather():
    
    city='San Francisco'
    res = requests.get(url_weather.format(city)).json()
    
    print (res)
    weather_data = {
        'city':city,
        'temperature':res['main']['temp'],
        'description':res['weather'][0]['description'],
        'icon':res['weather'][0]['icon']
        
    }
    
    return weather_data


def weather_city(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={WEATHER_KEY}'
    res = requests.get(url).json()
    return res


    


