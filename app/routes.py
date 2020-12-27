from app import app
from flask import render_template, url_for,Response
from app.models import test
import io 
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import requests
import threading

@app.route('/')
@app.route('/index')
def index():
    x = 0
    def getX():
        x = test.getRandom()
        timer = threading.Timer(10,index)
        timer.start()
    return render_template("inicio.html", value=getX())
    
@app.route('/veadoPaulo')
def plot_png():
    fig = test.create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run()