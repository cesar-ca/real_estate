from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from real_estate.models import Agent


class ListingForm(FlaskForm):
    seller = StringField('Name of Seller', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    bedrooms = StringField('Number of Bedrooms (in written form)', validators=[DataRequired()])
    bathrooms = StringField('Number of Bathrooms (in written form)', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    office = StringField('Office', validators=[DataRequired()])
    agent_id = StringField('Agent ID', validators=[DataRequired()])
    submit = SubmitField('Create New Listing')

class AgentForm(FlaskForm):
    name = StringField('Write your name below', validators=[DataRequired()])
    submit = SubmitField('Register as Agent')