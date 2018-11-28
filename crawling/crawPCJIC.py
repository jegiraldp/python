import requests
from bs4 import BeautifulSoup

def analizarTest(palabra):
    url="http://200.38.75.90:8986/F/6SVFV496824RAD8DL42HCV19699NE1HND9323D566BD3KMBPVH-08490"
    retorno="-"

    #parametros
    par = {'func': 'find-b', 'request': palabra, 'find_code': 'WRD','adjacent': 'N','x':'44','y':'6'
        ,'filter_code_1':'WLN','filter_request_1': '',  'filter_code_2' : 'WYR','filter_request_2':''
        , 'filter_code_3': 'WYR', 'filter_request_3': '', 'filter_code_4': 'WFM', 'filter_request_4': ''
        , 'filter_code_5': 'WYR', 'filter_request_5': ''}

    retorno = "-"
    code = requests.get(url, params=par)
    #print(code.url)
    soup = BeautifulSoup(code.text, "html.parser")
    retorno += (soup.title.string)
    tituloRta=str(soup.findAll("div", {'class': 'text3'})[0].string)
    titleRta=tituloRta[:tituloRta.find(";")]
    retorno += titleRta+"\n*************************************\n"

    for tr in soup.findAll("tr", {'valign': 'baseline'}):
        losTd = tr.find_all("td")
        retorno+="Estudiante: "+losTd[2].text+"\n"
        for scr in tr.find_all("script"):
            titulo = scr.string
            retorno+="Título: "+titulo[titulo.find("'") + 1:titulo.find(";") - 1]+"\n"
            retorno+="----------------------------------\n"
    return retorno