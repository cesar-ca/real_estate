Steps to Run CS162 - DB Application

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


```
python3 --version
```



##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

On Windows:

```
python -m pip install virtualenv
```



On your terminal

1. Navigate to the directory where you have your copy of this project.

2. Before you run the application, set up an environment variable to the file that you want to be the Flask application.

For example, (Mac/Linux)

```
$ export FLASK_APP=real_estate.py
```

(Windows)

```
$ set FLASK_APP=real_estate.py
```

3. With the environment variable set, run the application with the following

```
$ flask run
```

4. You should be able to see the application by going to your localhost

These will allow you to see the app as much as required if you do not wish to contribute.

### If you wish to contribute and wish to see the server show changes without the need to restart the application, you can run the application in DEBUG MODE.

After step 2 above, do the following 

2.a. On your terminal

(Mac/Linux)

```
$ export FLASK_DEBUG=1
```

(Windows)

```
$ set FLASK_DEBUG=1
```

Then you can continue to step 3


### If you do not wish to set up envrironment variables 

You can run the module directly (Disclaimer, the Flask documentation uses the flask run command, so it would be recommended to follow it)

```
$ python3 real_estate.py
```


*** Instead of relying on dummy data, we will create a database for the real estate listings. We will work with SQLAlchemy (very popular Object Relational Mapper)


### The Models 

The models contained here represent the structure of the database

To create the database:

- Open the command line (terminal) and run

```
$ python3
```

Within the python repl run

```
>>> from real_estate import db
```

then create the database with

```
>>> db.create_all()
```
