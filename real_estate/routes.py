from flask import render_template, url_for, flash, redirect, request, abort
from real_estate import app, db
from real_estate.forms import ListingForm, AgentForm
from real_estate.models import Agent, Listing


@app.route("/")
@app.route("/home")
def home():
    listings = Listing.query.all()
    return render_template('home.html', listings=listings)

@app.route("/registered_agents")
def registered_agents():
    agents = Agent.query.all()
    return render_template('registered_agents.html', title='Registered Agents', agents=agents)

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
 
@app.route("/agent_register", methods=['GET', 'POST'])
def agent_register():
    form = AgentForm()
    if form.validate_on_submit():
        #listing = Listing(seller=form.seller.data, bedrooms=form.bedrooms.data, bathrooms=form.bathrooms.data, zipcode=form.zipcode.data, office=form.office.data, agent_id=form.agent_id.data)
        agent = Agent(name=form.name.data)
        db.session.add(agent)
        db.session.commit()
        flash('You are registered as an agent!', 'success')
        return redirect(url_for('registered_agents'))
    return render_template('agent_register.html', title='Agent Registration', form=form)