from app import app
from flask import render_template,flash, url_for,Response,redirect
from app.models import test
import io 
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import requests
import threading


@app.route('/')
@app.route('/index')
def index():
    return render_template("inicio.html", value=3)

@app.route('/plotTest')
def plotTest():
    return render_template("plotTest.html")

@app.route('/getImage')
def plot_png():
    values = test.getRandomAxis()
    n = 5
    fig = test.create_figure(values[0],values[1])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run()