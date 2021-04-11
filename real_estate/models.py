from datetime import datetime
from real_estate import db

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    listings = db.relationship('Listing', backref='agent', lazy=True)

    def __repr__(self):
        return f"Agent('{self.name}')"

'''
class SaleAgent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    listings = db.relationship('Listing', backref='saleagent', lazy=True)

    def __repr__(self):
        return f"SaleAgent('{self.name}')"
'''

# The Listing class holds the real estate listings
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seller = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    bedrooms = db.Column(db.String(100), nullable=False)
    bathrooms = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(100), nullable=False)
    sold = db.Column(db.String(100), nullable=False, default="No")
    office = db.Column(db.String(100), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
    buyer = db.Column(db.String(100), nullable=False, default="")
    saleprice = db.Column(db.String(100), nullable=False, default="")
    saledate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    saleoffice = db.Column(db.String(100), nullable=False, default="")
    #saleagent_id = db.Column(db.Integer, db.ForeignKey('saleagent.id'), nullable=True)

    def __repr__(self):
        return f"{self.saleprice}"