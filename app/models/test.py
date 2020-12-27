from bs4 import BeautifulSoup
import requests
import re
import numpy as np 
from matplotlib.figure import Figure
import threading
import random


def getRandom():
    x = random.randint(0,9)
    return x

def create_figure():
    resultst0, resultst1, resultst2 = [], [], []
    mediat0, mediat1,mediat2 = 0,0,0

    NPagest0 = 1 #13
    NPagest1 = 1 #82
    NPagest2 = 1 #120

    #T0
    
    for page in range(1,NPagest0+1):
        source = requests.get(f"https://www.imovirtual.com/arrendar/apartamento/?search%5Bfilter_enum_rooms_num%5D%5B0%5D=zero&search%5Bregion_id%5D=11&page={page}").text
        soup = BeautifulSoup(source, 'lxml')
        resultst0 += [soup.find_all('li', class_=('offer-item-price'))]
    string = ""
    for result in resultst0:
        for n in result:
            string += str(n)
    pricet0 = re.findall(r'(?=\S)[\d\s]*(?= \S )', string)
    Pricest0 = []
    for prices in pricet0:
        if n is not None:
            Pricest0 += [int(prices.replace(" ",""))]

    for p in Pricest0:
        mediat0 += p
    #T1
    for page in range(1,NPagest1+1):
        source = requests.get(f"https://www.imovirtual.com/arrendar/apartamento/lisboa/?search%5Bfilter_enum_rooms_num%5D%5B0%5D=1&search%5Bregion_id%5D=11&page={page}").text
        soup = BeautifulSoup(source, 'lxml')
        resultst1 += [soup.find_all('li', class_=('offer-item-price'))]
    string = ""
    for result in resultst1:
        for n in result:
            string += str(n)
    pricet1 = re.findall(r'(?=\S)[\d\s]*(?= \S )', string)
    Pricest1 = []
    for prices in pricet1:
        if n is not None:
            Pricest1 += [int(prices.replace(" ",""))]
    for p in Pricest1:
        mediat1 += p
    #T2

    for page in range(1,NPagest2+1):
        source = requests.get(f"https://www.imovirtual.com/arrendar/apartamento/?search%5Bfilter_enum_rooms_num%5D%5B0%5D=2&search%5Bregion_id%5D=11&page={page}").text
        soup = BeautifulSoup(source, 'lxml')
        resultst2 += [soup.find_all('li', class_=('offer-item-price'))]
    string = ""
    for result in resultst2:
        for n in result:
            string += str(n)
    pricet2 = re.findall(r'(?=\S)[\d\s]*(?= \S )', string)
    Pricest2 = []
    for prices in pricet2:
        if n is not None:
            Pricest2 += [int(prices.replace(" ",""))]
    for p in Pricest2:
        mediat2 += p

    
    timer = threading.Timer(10,logVeado)
    fig = Figure()
    x = [Pricest0,Pricest1,Pricest2] # ZUKINHA
    ax = fig.add_subplot()
    ax.set_title('Diferença entre T0, T1, T2')
    ax.boxplot(x)
    return fig


   
