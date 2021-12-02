import requests
from secrets import API_SECRET_KEY


url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_SECRET_KEY}'

url_general= f'https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={API_SECRET_KEY}'

url_sports= f'https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={API_SECRET_KEY}'

url_entertainment= f'https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={API_SECRET_KEY}'

url_business= f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_SECRET_KEY}'

url_health= f'https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={API_SECRET_KEY}'

url_technology= f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_SECRET_KEY}'

url_science= f'https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={API_SECRET_KEY}'


def get_latest_news():
    news_data = requests.get(url).json()
    return news_data['articles']

def get_general_news():
    general_data = requests.get(url_general).json()        
    return general_data['articles']

def get_sports_news():
    sports_data = requests.get(url_sports).json()
    return sports_data['articles']

def get_entertainment_news():
    entertainment_data = requests.get(url_entertainment).json()
    return entertainment_data['articles']

def get_business_news():
    business_data = requests.get(url_business).json()
    return business_data['articles']

def get_health_news():
    health_data = requests.get(url_health).json()
    return health_data['articles']


def get_technology_news():
    technology_data = requests.get(url_technology).json()
    return technology_data['articles']

def get_science_news():
    science_data = requests.get(url_science).json()
    return science_data['articles']





