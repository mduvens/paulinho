from app import app
from app.models import test, regexpy, automatopy

from flask import render_template,flash, url_for,Response,redirect, jsonify,request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io, requests, threading, random



@app.route('/',methods=["POST","GET"])
@app.route('/index',methods=["POST","GET"])
def index():
    return render_template("inicio.html", value=3)

@app.route('/webscrap')
def plots():
    return render_template("webscrap.html")

@app.route('/regex',methods=["GET","POST"])
def regex():
    if request.method == "GET":
        return render_template("regex.html", results = None)
    else:       
        output = regexpy.checkRegex(request.form)
        return render_template("regex.html", results= output)
# @app.route('/processInputs',methods=['POST'])
# def processInputs():
#         name = request.form["name"]
#         number = regexpy.checkNumber(request.form["number"])
#         email = regexpy.checkEmail(request.form["email"])
#         postalCode = regexpy.checkPostal(request.form["postalCode"])
#         if name and number and email and postalCode:
#             return jsonify({"name":name,"number":number,"email":email,"postalCode":postalCode})
#         else:
#             return jsonify({"error": 'Missing data'})
@app.route('/automato', methods = ["GET","POST"])
def automato():
    if request.method == "GET":
        return render_template("automato.html")
    else:
        output = automatopy.checkAutomato(request.form["sequencia"])
        return render_template("automato.html", result = output)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getPlot')
def plot_png():
    values = test.getRandomAxis()
    fig = test.create_figure(values[0],values[1])
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/getImage')
def imageTest():
    return "<img class='flexImg'src='/getPlot' alt=''>"

if __name__ == '__main__':
    app.run(debug = True)