from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import Agent, Listing



listings = [
    {
        'seller': 'Emanuel Castro',
        'bedrooms': 'Two',
        'bathrooms': 'Two',
        'price': '10000',
        'zipcode': '94102',
        'date': 'May 14, 2017',
        'agent': 'Bucky Barnes',
        'office': 'Tenderloin'
    },
    {
        'seller': 'Norma Varela',
        'bedrooms': 'Three',
        'bathrooms': 'Four',
        'price': '100500',
        'zipcode': '94108',
        'date': 'November 30, 2019',
        'agent': 'Sam Wilson',
        'office': 'Chinatown'
    },
    
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', listings=listings)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Conditional given that __name__ is same as __main__ in this app
if __name__ == '__main__':
    app.run(debug=True)
