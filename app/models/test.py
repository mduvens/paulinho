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
    # ax = fig.add_subplot(2,2,1)
    # ax.set(xlabel='time (s)', ylabel='value ($)', title='Gold Price')
    # ax.grid()
    # ax.grid(False)
    # ax.plot(x,y)
    ax2 = fig.add_subplot(1,1,1)
    ax2.set(xlabel='time (s)', ylabel='value ($)', title='Gold Price')
    ax2.grid()
    ax2.grid(False)
    x2 = [getRandom() for i in range(5)]
    y2= [getRandom() for i in range(5)]
    ax2.plot(x2,y2)
    return fig


   
