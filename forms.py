from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL


class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class PostForm(FlaskForm):
    post = StringField('posts', validators=[InputRequired()])
    title = StringField('title', validators=[InputRequired()])

class CommentForm(FlaskForm):
    comment = StringField('posts', validators=[InputRequired()])

    # text = StringField("Comment Text", validators=[InputRequired()])
    # posted_at = StringField("Post Date", validators=[InputRequired()])
    


class AddNewsForm(FlaskForm):
    """News form """
    image_url = StringField("Image URL", validators=[Optional(), URL()])
    author = StringField("Author", validators=[InputRequired()])
    title = StringField("Title", validators=[InputRequired()])
    
    
    description = TextAreaField("Description", validators=[Optional()])




class EditNewsForm(FlaskForm):

    """Form for editing an existing news."""
    
    image_url = StringField("Image URL", validators=[Optional(), URL()])

    description = TextAreaField("Description", validators=[Optional()])

    

