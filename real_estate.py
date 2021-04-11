from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

'''
Inserting data

Whenever a house is listed then the following things need to happen:

All the relevant details of that house need to be captured, ie. 
at least: seller details, # of bedrooms, # of bathrooms, listing price, 
zip code, date of listing, the listing estate agent, 
and the appropriate office.
Whenever a house is sold then the following things need to happen:

The estate agent commission needs to be calculated. This happens on a sliding scale:
For houses sold below $100,000 the commission is 10%
For houses between $100,000 and $200,000 the commission is 7.5%
For houses between $200,000 and $500,000 the commission is 6%
For houses between $500,000 and $1,000,000 the commission is 5%
For houses above $1,000,000 the commission is 4%
A summary table containing the sum of all sale prices must be updated.
All appropriate details related to the sale must be captured, ie. at least: 
buyer details, sale price, date of sale, the selling estate agent.
The original listing must be marked as sold.
'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

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
