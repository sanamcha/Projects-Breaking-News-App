import requests
from secrets import API_SECRET_KEY


url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_SECRET_KEY}'

url_general= f'https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={API_SECRET_KEY}'

url_sports= f'https://newsapi.org/v2/top-headlines?country=us&category=sport&apiKey={API_SECRET_KEY}'

url_entertainment= f'https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey={API_SECRET_KEY}'

url_business= f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_SECRET_KEY}'

url_health= f'https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey={API_SECRET_KEY}'

url_technology= f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_SECRET_KEY}'

url_science= f'https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={API_SECRET_KEY}'

url_bitcoin = f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_SECRET_KEY}'

url_jobs = f'https://newsapi.org/v2/everything?q=jobs&apiKey={API_SECRET_KEY}'

url_travel =f'https://newsapi.org/v2/everything?q=travels&apiKey={API_SECRET_KEY}'

url_stocks =f'https://newsapi.org/v2/everything?q=stocks&apiKey={API_SECRET_KEY}'

url_fitness =f'https://newsapi.org/v2/everything?q=fitness&apiKey={API_SECRET_KEY}'

url_pets =f'https://newsapi.org/v2/everything?q=pets&apiKey={API_SECRET_KEY}'

url_military =f'https://newsapi.org/v2/everything?q=military&apiKey={API_SECRET_KEY}'

url_tech =f'https://newsapi.org/v2/everything?q=tech&apiKey={API_SECRET_KEY}'

url_animals =f'https://newsapi.org/v2/everything?q=animals&apiKey={API_SECRET_KEY}'

url_relationships =f'https://newsapi.org/v2/everything?q=relationships&apiKey={API_SECRET_KEY}'

url_beauty =f'https://newsapi.org/v2/everything?q=beauty&apiKey={API_SECRET_KEY}'

url_weather =f'https://newsapi.org/v2/everything?q=weathers&apiKey={API_SECRET_KEY}'





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

def get_bitcoin_news():
    bitcoin_data = requests.get(url_bitcoin).json()
    return bitcoin_data['articles']

def get_jobs_news():
    jobs_data = requests.get(url_jobs).json()
    return jobs_data['articles']

def get_travel_news():
    travel_data = requests.get(url_travel).json()
    return travel_data['articles']

def get_stocks_news():
    stocks_data = requests.get(url_stocks).json()
    return stocks_data['articles']

def get_fitness_news():
    fitness_data = requests.get(url_fitness).json()
    return fitness_data['articles']

def get_pets_news():
    pets_data = requests.get(url_pets).json()
    return pets_data['articles']

def get_military_news():
    military_data = requests.get(url_military).json()
    return military_data['articles']

def get_tech_news():
    tech_data = requests.get(url_tech).json()
    return tech_data['articles']

def get_animals_news():
    animals_data = requests.get(url_animals).json()
    return animals_data['articles']

def get_relationships_news():
    relationships_data = requests.get(url_relationships).json()
    return relationships_data['articles']

def get_beauty_news():
    beauty_data = requests.get(url_beauty).json()
    return beauty_data['articles']

def get_weather_news():
    weather_data = requests.get(url_weather).json()
    return weather_data['articles']