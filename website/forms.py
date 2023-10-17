from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, IntegerField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed 

# Define a set of allowed image file extensions
ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

# Form for creating an event
class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[InputRequired()])
    description = TextAreaField('Event Description', validators=[InputRequired()])
    venue = TextAreaField('Event Venue', validators=[InputRequired()])
    date = TextAreaField('Event Date', validators=[InputRequired()])
    image = FileField('Event Image', validators=[FileRequired(message='Image cannot be empty'), FileAllowed(ALLOWED_FILE, message='File is not supported')])
    submit = SubmitField("Create")

# Form for user login
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

# Form for user registration
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    password = PasswordField("Password", validators=[InputRequired(), EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")

# Form for adding comments
class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')
