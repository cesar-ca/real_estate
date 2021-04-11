from datetime import datetime
from real_estate import db

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    listings = db.relationship('Listing', backref='agent', lazy=True)

    def __repr__(self):
        return f"Agent('{self.name}')"

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