from flask import Flask, render_template, redirect, session, flash, jsonify, request, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Comment, Post, datetime, City
from forms import UserForm
from sqlalchemy.exc import IntegrityError
import json
import requests
from secrets import API_SECRET_KEY

from weathers import get_weather
from news import  get_general_news, get_technology_news, get_health_news, get_business_news, get_entertainment_news, get_sports_news, get_science_news

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///news-app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = 'abcdefghijkl123456789'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)

toolbar = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """The home page"""
    url =f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_SECRET_KEY}'
    
    response = requests.get(url).json()
    article = {
        'articles' : response["articles"]
    }
    weather=get_weather()

    return render_template('home-page.html', article=article, weather=weather)



@app.route('/general')
def general_news():
    general_articles = get_general_news()
    weather=get_weather()
    return render_template("news.html", articles=general_articles, weather=weather)

@app.route('/sports')
def sports_news():
    sports_articles = get_sports_news()
    weather=get_weather()
    return render_template("news.html", articles=sports_articles, weather=weather)

@app.route('/technology')
def technology_news():
    technology_articles = get_technology_news()
    weather=get_weather()
    return render_template("news.html", articles=technology_articles, weather=weather)

@app.route('/science')
def science_news():
    science_articles = get_science_news()
    weather=get_weather()
    return render_template("news.html", articles=science_articles, weather=weather)

@app.route('/entertainment')
def entertainment_news():
    entertainment_articles = get_entertainment_news()
    weather=get_weather()
    return render_template("news.html", articles=entertainment_articles, weather=weather)

@app.route('/health')
def health_news():
    health_articles = get_health_news()
    weather=get_weather()
    return render_template("news.html", articles=health_articles, weather=weather)

@app.route('/business')
def business_news():
    business_articles = get_business_news()
    weather=get_weather()
    return render_template("news.html", articles=business_articles, weather=weather)



@app.route('/search', methods=['POST', 'GET'])
def search():
    weather=get_weather()
    if request.method =='POST':
        search = request.form['search']
  
        url =(f'https://newsapi.org/v2/everything?q={search}&apiKey={API_SECRET_KEY}')

        response = requests.get(url)
        data = response.json()
        articles = data['articles']
        
        return render_template('search.html', articles=articles, search=search, weather=weather)




@app.route('/news')
def login_news_page():
    """The home page"""
    weather=get_weather()
    url = f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey={API_SECRET_KEY}" 
   
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    return render_template('news.html', articles=articles, weather=weather)

@app.route("/covid")
def covid_news():
    weather=get_weather()
    url=f"https://newsapi.org/v2/top-headlines?q=covid&apiKey={API_SECRET_KEY}"
    

    response = requests.get(url).json()

    article = {
        'articles' : response["articles"]
    }
    return render_template ("/covid-news.html", article=article, weather=weather)


#   ###############  for user register  ###############

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    weather=get_weather()
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)

        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append('Username taken.  Please pick another')
            return render_template('register.html', form=form)
        session['user_id'] = new_user.id
        flash('Welcome! Successfully Created Your Account!', "success")
        return redirect('/news')

    return render_template('register.html', form=form, weather=weather)


################ for user login###############

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    weather=get_weather()
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!", "primary")
            session['user_id'] = user.id
            return redirect('/news')
        else:
            form.username.errors = ['Invalid username/password.']

    return render_template('login.html', form=form, weather=weather)


######## for logout ###############
@app.route('/logout')
def logout_user():
    session.pop('user_id')
    flash("Goodbye!", "info")
    return redirect('/')
















