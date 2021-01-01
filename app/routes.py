from app import app
from app.models import test, regexpy, afd, scrap

from flask import render_template,flash, url_for,Response,redirect, jsonify,request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io, requests, threading, random

#import atexit
import logging
import sys
import threading
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


logging.basicConfig(level=logging.DEBUG)


@app.route('/',methods=["POST","GET"])
@app.route('/index',methods=["POST","GET"])
def index():
    return render_template("inicio.html", value=3)

@app.route('/webscrap')
def plots():
    tabelaClass = scrap.getScrapLigaNOS()
    return render_template("webscrap.html", tabelaClass = tabelaClass)

@app.route('/regex',methods=["GET","POST"])
def regex():
    if request.method == "GET":
        return render_template("regex.html", results = None)
    else:       
        output = regexpy.checkRegex(request.form)
        return render_template("regex.html", results= output)

@app.route('/automato', methods = ["GET","POST"])
def automato():
    if request.method == "GET":
        return render_template("automato.html")
    else:
        output = afd.checkAutomato(request.form["sequencia"])
        return render_template("automato.html", result = output)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getPlot')
def plot_png():
    values = test.getRandomAxis()
    gold = scrap.obterValorOil()
    scrap.obterValorOil()
    fig = test.create_figure(gold["valores"],gold["tempos"])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/getImage')
def imageTest():
    return "<img class='flexImg'src='/getPlot' alt=''>"

if __name__ == '__main__':
    scheduler.start()
    scheduler.add_interval_ob(scrap.obterValorOil, seconds=10)
    app.run(debug = True)