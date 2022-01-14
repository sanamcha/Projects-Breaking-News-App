from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)




class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False,  unique=True)
    password = db.Column(db.String, nullable=False)
    # post = db.relationship("Post", backref="users", cascade="all,delete")



    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)

        hashed_utf8 = hashed.decode("utf8")

       
        return cls(username=username, password=hashed_utf8)

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False


DEFAULT_IMAGE = "https://ak3.picdn.net/shutterstock/videos/7816963/thumb/3.jpg"


class Post(db.Model):
    """News Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False,default = DEFAULT_IMAGE)
    author = db.Column(db.Text)
    published_at = db.Column(db.DateTime, nullable=False,default=datetime.now())
    description = db.Column(db.Text, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref="posts", cascade="all,delete")
    comments = db.relationship('Comment', backref='article', cascade='all, delete')

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.published_at.strftime("%a %b %-d  %Y, %-I:%M %p")
   
    def __repr__(self):
        return f"<Post {self.id} {self.title} {self.image_url}{self.author} {self.published_at} {self.description} {self.user_id} >"



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(100), nullable=False)

    posted_at = db.Column(db.DateTime, nullable=False,default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    user = db.relationship('User', backref="comments")
    # post = db.relationship('Post', backref="comments")
    
    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.posted_at.strftime("%a %b %-d  %Y, %-I:%M %p")


    def __repr__(self):

        return f"Comment('{self.text}','{self.posted_at}')"


# for Weather - data

class City(db.Model):

    __tablename__ = "weathers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship('User', backref="weathers")


class News(db.Model):
    """News list"""

    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, 
                    default = DEFAULT_IMAGE)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='news', cascade='all, delete')
