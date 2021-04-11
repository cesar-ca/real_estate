from flask import render_template, url_for, flash, redirect, request, abort
from real_estate import app, db
from real_estate.forms import ListingForm, AgentForm, SoldForm
from real_estate.models import Agent, Listing


@app.route("/")
@app.route("/home")
def home():
    listings = Listing.query.all()
    return render_template('home.html', listings=listings)

@app.route("/summary")
def summary():
    listings = Listing.query.all()
    return render_template('summary.html', listings=listings)

@app.route("/registered_agents")
def registered_agents():
    agents = Agent.query.all()
    return render_template('registered_agents.html', title='Registered Agents', agents=agents)

'''
@app.route("/registered_sale_agents")
def registered_sale_agents():
    agents = SaleAgent.query.all()
    return render_template('registered_sale_agents.html', title='Registered Sale Agents', agents=agents)
'''

@app.route("/listing/new", methods=['GET', 'POST'])
def new_listing():
    form = ListingForm()
    if form.validate_on_submit():
        #listing = Listing(seller=form.seller.data, bedrooms=form.bedrooms.data, bathrooms=form.bathrooms.data, zipcode=form.zipcode.data, office=form.office.data, agent_id=form.agent_id.data)

        #Legacy 
        #listing = Listing(seller=form.seller.data, price=form.price.data, bedrooms=form.bedrooms.data, bathrooms=form.bathrooms.data, zipcode=form.zipcode.data, office=form.office.data, agent_id=form.agent_id.data)
        listing = Listing(seller=form.seller.data, price=form.price.data, bedrooms=form.bedrooms.data, bathrooms=form.bathrooms.data, zipcode=form.zipcode.data, office=form.office.data, agent_id=form.agent_id.data)
        db.session.add(listing)
        db.session.commit()
        flash('The listing has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_listing.html', title='New Listing', 
                            form=form, legend='New Listing')

@app.route("/listing/<int:listing_id>")
def listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    return render_template('listing.html', title=listing.seller, listing=listing)
 
@app.route("/listing/<int:listing_id>/mark_as_sold", methods=['GET', 'POST'])
def sold_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    form = SoldForm()
    if form.validate_on_submit():
        listing.sold = form.sold.data
        listing.buyer = form.buyer.data
        listing.saleprice = form.saleprice.data
        #listing.saledate = form.saledate.data
        listing.saleoffice = form.saleoffice.data
        listing.agent_id = form.agent_id.data
        #listing.price = form.price.data
        #listing.bathrooms = form.bathrooms.data
        #listing.bedrooms = form.bedrooms.data
        #listing.zipcode = form.zipcode.data
        #listing.agent = form.agent.data
        #listing.office = form.office.data
        db.session.commit()
        flash('The listing has been marked as sold!', 'success')
        return redirect(url_for('listing', listing_id=listing.id))
    #elif request.method == 'GET':
        #listing.seller.data = listing.seller
        #listing.bathrooms.data = listing.bathrooms
        #listing.bedrooms.data = listing.bedrooms
        #listing.price.data = listing.price
        #listing.zipcode.data = listing.zipcode
        #listing.office.data = listing.office
        #listing.agent.data = listing.agent
    return render_template('mark_as_sold.html', title='Mark Listing as Sold', 
                            form=form, legend='Mark Listing as Sold')


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