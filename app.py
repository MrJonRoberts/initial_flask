<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    title = "Home Page"
    pageHeader = "This is the home page"
    return render_template("home.html", title=title, pageHeader=pageHeader)


if __name__ == '__main__':
    app.run()
=======
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    title = "Home Page"
    pageHeader = "This is the home page"
    return render_template("home.html", title=title, pageHeader=pageHeader)


if __name__ == '__main__':
    app.run()
>>>>>>> 0e50d8fc17dfe4592d59d27939703059391608a1
