from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from real_estate.models import Agent, Listing


class ListingForm(FlaskForm):
    seller = StringField('Name of Seller', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    bedrooms = StringField('Number of Bedrooms (in written form)', validators=[DataRequired()])
    bathrooms = StringField('Number of Bathrooms (in written form)', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    office = StringField('Office', validators=[DataRequired()])
    #sold = StringField('Sold', validators=[DataRequired()])
    agent_id = StringField('Agent ID', validators=[DataRequired()])
    submit = SubmitField('Create New Listing')

class SoldForm(FlaskForm):
    sold = StringField('Sold', validators=[DataRequired()])
    buyer = StringField('Buyers name', validators=[DataRequired()])
    saleprice = StringField('Price at sale', validators=[DataRequired()])
    #saledate = StringField('Date of Sale', validators=[DataRequired()])
    saleoffice = StringField('Office', validators=[DataRequired()])
    agent_id = StringField('Agent ID', validators=[DataRequired()])
    #saleagent_id = StringField('Agent ID', validators=[DataRequired()])
    #price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Mark as Sold')


class AgentForm(FlaskForm):
    name = StringField('Write your name below', validators=[DataRequired()])
    submit = SubmitField('Register as a Listing Agent')

'''
class SaleAgentForm(FlaskForm):
    name = StringField('Write your name below', validators=[DataRequired()])
    submit = SubmitField('Register as a Selling Agent')
'''