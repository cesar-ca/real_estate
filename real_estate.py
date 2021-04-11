from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    listings = db.relationship('Listing', backref='agent', lazy=True)

# The Listing class holds the real estate listings
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seller = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    bedrooms = db.Column(db.String(100), nullable=False)
    bathrooms = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(100), nullable=False)
    office = db.Column(db.String(100), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)

    def __repr__(self):
        return f"Listing('{self.seller}', '{self.date}')"


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
