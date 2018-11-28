import requests
from bs4 import BeautifulSoup

def analizarImg(url):
    code = requests.get(url)
    texto= code.text
    soup = BeautifulSoup(texto, "html.parser")
    retorno=""
    cont=len(soup.findAll('img'))
    for link in soup.findAll('img'):
        retorno += str(link.get('src')) + "\n"
    return "total de <img>: "+str(cont)+"\n"+retorno

def analizarHiper(url):
    code = requests.get(url)
    texto= code.text
    soup = BeautifulSoup(texto, "html.parser")
    retorno=""
    cont=len(soup.findAll('a'))
    for link in soup.findAll('a'):
        retorno += str(link.get('href')) + "\n"
    return "total de <a>: "+str(cont)+"\n"+retorno