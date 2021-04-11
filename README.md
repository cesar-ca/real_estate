Steps to Run CS162 - DB Application - INITIAL SETUP

Go to the github repo, you will find it here: github.com/cesar-ca/real_estate

Open the command line (terminal)


1. Make sure you have git installed on your device, run the following command on the terminal:

```
git --version
```

2. Clone the repo to a "local" directory (on your computer),

```
git clone https://github.com/cesar-ca/real_estate
```

then change into the directory

```
cd real_estate
```

3. To make sure everything is up to date on your end, run

```
git pull
```

## Run Virtual Environment

Virtual environment is a key component in ensuring that the application is configured in the right environment

To make sure you have the most basic requirements, run
```
python3 --version
```
and 
```
pip3 --version
```
* You should be able to see your version pop up


##### Installation
To install virtualenv via pip run:
```
$ pip3 install virtualenv
```

On Windows:

```
python -m pip install virtualenv
```

##### Usage
Creation of virtualenv:
```
virtualenv -p python3 venv
```

If the above code does not work, you could also do
```
python3 -m venv venv
```

To activate the virtualenv:
```
source venv/bin/activate
```

Install dependencies in virtual environment:

```
pip3 install -r requirements.txt
```

Then, run the application 

```
python3 run.py
```

YOU SHOULD BE ABLE TO HAVE EVERYTHING REQUIRED NOW

You can take a look at the Real Estate Head Office in your localhost

This is a database system for a large franchised real estate company. The company has many offices located all over the country (and the world). Each office is responsible for selling houses in a particular area. However an estate agent can be associated with one or more offices. (An agent is associated only with 1 id).

### Insertion of data

You can use the UI to insert data, for example you can list a house for sale (provided you are an agent with an ID)

When you list a house for sale (navigate to the top right corner where it says "Create Listing") the following happens:

All the relevant details of that house is captured
seller details
\# of bedrooms 
\# of bathrooms
listing price 
zip code
date of listing
the listing estate agent
the office

Once all of that is captured, you are redirected to the home page where you can see the stream of house listings

A listing agent can also be the selling agent, but it is not required. An sale agent can "Check out the listing" and "Mark as sold"

Whene a house is sold (by a sale agent) the following happens:

A summary table "Summary of all sale prices" is updated.

All details related to the sale are captured
buyer details
sale price
date of sale
the selling estate agent

The original listing is marked as sold

Testing:

To test my UI, I created fictitious data (that can be accessed once you get your copy of this repo) to ensure that the DB application runs correctly.

Submission:

For this assignment I used SQLAlchemy and wrote python code. 

My primary submission is this README.md file followed by the rest of my code. 
Secondary submission is a zip file containing all the code. (this repo)

I believe I have exceeded the requirements of this assignment by creating a rough UI where it is not necessary to write SQL queries, but rather just use the interface for the needed features (listing, selling, etc.)

However, if desired you can also use a python3 repl to run the code and print the results of SQL queries. 

Execution (Python):

In this README.md file I have included a series of commands to execute all the relevant parts of my code
