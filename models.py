from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text, nullable=False)

    posted_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

    user = db.relationship('User', backref="comments")
    


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.Text, nullable=False,  unique=True)

    password = db.Column(db.Text, nullable=False)

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

    __tablename__ = "post_news"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.Text, nullable=False, 
                    default = DEFAULT_IMAGE)
    author = db.Column(db.Text)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    published_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref="post_news")

   
    
    
    def serialize(self):
        """To serialize news"""

        return {
            "id": self.id,
            "image": self.image,
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "published_at":self.published_at
        }


# for Weather - data

class City(db.Model):

    __tablename__ = "weathers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = True)
