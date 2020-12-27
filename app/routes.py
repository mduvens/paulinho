from app import app
from flask import render_template, url_for
from app.models import test

@app.route('/')
@app.route('/index')
def index():
    x = test.multiply()
    return render_template("inicio.html", value=x)

@app.route('/about')
def about():
    return render_template("pauloveado.html")

@app.route('/appA')
def appA():
    return render_template("appA.html")

if __name__ == '__main__':
    app.run()