from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email(message="Invalid Email Address.")])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("CONTACT")