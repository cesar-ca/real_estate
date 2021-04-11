from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# Conditional given that __name__ is same as __main__ in this app
if __name__ == '__main__':
    app.run(debug=True)
