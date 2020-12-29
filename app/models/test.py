from bs4 import BeautifulSoup
import requests
import re
import numpy as np 
from matplotlib.figure import Figure
import threading
import random
import time



def getRandom():
    x = random.randint(0,9)
    return x

def getRandomAxis():
    x = [getRandom() for i in range(5)]
    y = [getRandom() for i in range(5)]
    return [x,y]

def create_figure(x,y):
    fig = Figure()
    ax = fig.add_subplot(1,1,1)
    ax.set(xlabel='time (s)', ylabel='value ($)', title='Gold Price')
    ax.grid()
    ax.grid(False)
    ax.plot(x,y)
    return fig


   
