from flask import render_template, url_for, flash, redirect, request, abort
from real_estate import app, db
from real_estate.forms import ListingForm
from real_estate.models import Agent, Listing


@app.route("/")
@app.route("/home")
def home():
    listings = Listing.query.all()
    return render_template('home.html', listings=listings)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/new_listing", methods=['GET', 'POST'])
def new_listing():
    form = ListingForm()
    if form.validate_on_submit():
        #listing = Listing(seller=form.seller.data, bedrooms=form.bedrooms.data, bathrooms=form.bathrooms.data, zipcode=form.zipcode.data, office=form.office.data, agent_id=form.agent_id.data)
        listing = Listing(seller=form.seller.data, price=form.price.data, bedrooms=form.bedrooms.data, bathrooms=form.bathrooms.data, zipcode=form.zipcode.data, office=form.office.data, agent_id=form.agent_id.data)
        db.session.add(listing)
        db.session.commit()
        flash('The listing has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_listing.html', title='New Listing', form=form)
 