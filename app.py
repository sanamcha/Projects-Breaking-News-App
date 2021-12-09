from flask import Flask, render_template, redirect, session, flash, jsonify, request, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Comment, Post, datetime, City
from forms import UserForm , PostForm, AddNewsForm, EditNewsForm, DeleteForm, CommentForm
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import Unauthorized
import json
import requests
from secrets import API_SECRET_KEY

from weathers import get_weather, url_weather, weather_city
from news import  get_general_news, get_technology_news, get_health_news, get_business_news, get_entertainment_news, get_sports_news, get_science_news

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///breaking_news"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '12345secretkey67890'

app.config['DEBUG'] = True


toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()



@app.errorhandler(404)
def page_not_found(e):
    """Show 404 NOT FOUND page."""

    return render_template('404.html'), 404

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

# ########  username ############
@app.route("/users/<user_id>")
def user_show(user_id):

    if "user_id" not in session or user_id != session['user_id']:
        raise Unauthorized()
    weather= get_weather()
    user = User.query.get(user_id)
   
    form = PostForm()

    return render_template("post/post-news.html", user=user, form=form, weather=weather )



# ######## user_id delete ########
@app.route("/users/<user_id>/delete", methods=["POST"])
def user_remove(user_id):

    if "user_id" not in session or user_id != session['user_id']:
        raise Unauthorized()

    user = User.query.get(user_id)
    db.session.delete(user)

    db.session.commit()
    session.pop("user_id")

    return redirect("/login")




# ############### Post News ############

@app.route('/post-news')
def post_news():
    """posting news"""
    weather=get_weather()
    posts = Post.query.all()

    if "user_id" not in session:
        
        flash("Please login first!", "danger")
        return redirect('/')
    
    return render_template('post/post-news.html', posts=posts, weather=weather)



@app.route('/post-news/add', methods=["GET", "POST"])
def add_news():
    """adding news"""

    weather=get_weather()
    form = AddNewsForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        
        posts_news = Post(image_url = form.image_url.data, 
                    author = form.author.data, 
                    title = form.title.data, 
                    description = form.description.data,
                    )

        db.session.add(posts_news)
        db.session.commit()

        flash(f"{posts_news.title} added.")
        return redirect("/post-news")
        # return redirect(f"/users/{posts.user_id}")

    else:
        return render_template("post/add-news.html", form=form, weather=weather)


@app.route("/post-news/<int:post_id>/update", methods=["GET", "POST"])
def edit_news(post_id):
    """Edit pet."""

    weather=get_weather()
    post = Post.query.get_or_404(post_id)

    form = EditNewsForm(obj=post)

    if form.validate_on_submit():
        post.image_url = form.image_url.data
        post.author = form.author.data
        post.title = form.title.data
        post.description = form.description.data
        
       
        db.session.commit()

        flash(f"{post.title} updated.")
        return redirect("/post-news")
       

    else:
        return render_template("post/edit-news.html", form=form, post=post, weather=weather)



@app.route("/post-news/<int:post_id>/delete", methods=["POST"])
def delete_news(post_id):
    """To Delete news post..."""

    post = Post.query.get_or_404(post_id)
   
    db.session.delete(post)
    db.session.commit()

    flash(f"Post {post.title} deleted.")

    return redirect("/post-news")
 
# ######## add comment #######



@app.route("/post-news/<int:post_id>/comment", methods=["GET", "POST"])

def comment_post(post_id):

    weather=get_weather()
    post = Post.query.get_or_404(post_id)
    comment = Comment.query.filter_by(post_id=post.id).all()
    

    form = CommentForm()
    if request.method == 'POST':

        if form.validate_on_submit():
            comment = Comment(text=form.text.data, post_id=post.id)
            db.session.add(comment)
            db.session.commit()
            flash("Your comment has been added to the post", "success")
            return redirect(url_for("show_post_comment", post_id=post.id))

    return render_template("post/comment-post.html", form=form, post_id=post_id, comment=comment, weather=weather, post=post)


@app.route("/post-news/<int:post_id>", methods=["GET", "POST"])
def show_post_comment(post_id):

    weather=get_weather()
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post.id).all()

    return render_template("post/show-comment-post.html", post_id=post_id, comments=comments, weather=weather, post=post)

@app.route("/post-news/<int:comment_id>/delete", methods=["POST"])
def delete_comment(comment_id):
    """To Delete feedback."""

    comment = Comment.query.get(comment_id)
  
   
    db.session.delete(comment)
    db.session.commit()

    return redirect("/post-news")



# ####### weather ############


@app.route('/weathers')
def list_weather():
    """Weather page"""

    cities =City.query.all()
    weather= get_weather

    weathers = []

    for city in cities:
        res =weather_city(city.name)
        print(res)
        # import pdb
        # pdb.set_trace()

        weather = {
            'city':city.name,
            'temperature':res['main']['temp'],
            'description':res['weather'][0]['description'],
            'icon':res['weather'][0]['icon']
        }

        weathers.append(weather)


    return render_template("weather.html", weathers=weathers, weather=weather)

@app.route('/weathers', methods=['POST'])
def post_weather():
    """Weather page"""

    err_msg = ''
    add_city = request.form.get('city')
        
    if add_city:
        existing_city = City.query.filter_by(name=add_city).first()

        if not existing_city:
            
            new_city_data =weather_city(add_city)

            if new_city_data['cod'] == 200:
                new_city_obj = City(name=add_city)

                db.session.add(new_city_obj)
                db.session.commit()
            else:
                err_msg = 'City does not exist in the world!'
        else:
            err_msg = 'City already exists in the database!'

    if err_msg:
        flash(err_msg, 'error')
    else:
        flash('City added succesfully!')

    return redirect(url_for('list_weather'))

@app.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    db.session.delete(city)
    db.session.commit()

    flash(f'Successfully deleted { city.name }', 'success')
    return redirect(url_for('list_weather'))



