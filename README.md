Steps 

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


