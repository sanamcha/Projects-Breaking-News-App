from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Optional, URL


class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class PostForm(FlaskForm):
    author = StringField('author', validators=[InputRequired()])
    title = StringField('title', validators=[InputRequired()])
    image_url = StringField("Image URL", validators=[Optional(), URL()])
    description = TextAreaField("Description", validators=[Optional()])

class CommentForm(FlaskForm):
   
    text = StringField("Comment Text", validators=[InputRequired()])
    submit = SubmitField("Post")
    posted_at = StringField("Post Date")
    


class AddNewsForm(FlaskForm):
    """News form """
    image_url = StringField("Image URL", validators=[Optional(), URL()])
    author = StringField("Author", validators=[InputRequired()])
    title = StringField("Title", validators=[InputRequired()])
    
    description = TextAreaField("Description", validators=[Optional()])




class EditNewsForm(FlaskForm):

    """Form for editing an existing news."""
    
    image_url = StringField("Image URL", validators=[Optional(), URL()])
    author = StringField("Author", validators=[Optional()])
    title = StringField("Title", validators=[Optional()])

    description = TextAreaField("Description", validators=[Optional()])


class DeleteForm(FlaskForm):
     """For delete posted news..."""

    

