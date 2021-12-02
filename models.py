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
    username = db.Column(db.Text, nullable=False,  unique=True)
    password = db.Column(db.Text, nullable=False)

    def posts(self):
        return Post.query.order_by(Post.timestamp.desc())

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
    image_url = db.Column(db.Text, nullable=False, 
                    default = DEFAULT_IMAGE)
    author = db.Column(db.Text)
    published_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow())
    description = db.Column(db.Text, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref="posts")
    # comments =db.relationship('Comments', backref="posts")
   
    def __repr__(self):
        return f"<Post {self.id} {self.title} {self.image_url}{self.author} {self.published_at} {self.description} {self.user_id} >"

  


    def serialize(self):
        """To serialize news"""

        return {
            "id": self.id,
            "title": self.title,
            "image": self.image,
            "author": self.author,
            "published_at":self.published_at,
            "description": self.description,
            
        }


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(100), nullable=False)

    timestamp = db.Column(db.DateTime, nullable=False,default=datetime.utcnow())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    users = db.relationship('User', backref="comments")
    

    def __repr__(self):
        return f"<Comment {self.id} {self.text} {self.timestamp} {self.user_id} {self.post_id} >"

# for Weather - data

class City(db.Model):

    __tablename__ = "weathers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('weathers.id'))
    # user = db.relationship('User', backref="weathers")