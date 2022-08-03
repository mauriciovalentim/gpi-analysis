import requests
from helpers import *
from bs4 import BeautifulSoup

def getDataGPI2022():
    req = requests.get("https://en.wikipedia.org/wiki/Global_Peace_Index")
    dadosGPI = dict()
    contador = 1
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, "html.parser")
        peaceIndexTable = soup.find("table", class_ = "wikitable sortable")
        for info in peaceIndexTable.find_all("tbody"):
            info = info.find_all("td")
            for dados in info:
                if contador==1:
                    pais = dados.text.strip()
                    contador += 1
                elif contador == 2:
                    contador += 1
                    continue
                elif contador == 3:
                    dadosGPI[pais] = dados.text.strip()
                    contador = 1
        return dadosGPI

def getDataGPIPast():
    url = 'https://en.wikipedia.org/wiki/Global_Peace_Index#Global_Peace_Index_rankings_(2008%E2%80%932019'
    req = requests.get(url)
    dadosGPI = dict()
    paises = dict()
    score = dict()
    contador = 0
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, "html.parser")
        peaceIndexTable = soup.find_all("table", class_ = "wikitable sortable")[1]
        peaceIndexTable = peaceIndexTable.find("tbody")
        for info_country in peaceIndexTable.find_all("tr")[1:]:
            info_country = info_country.find_all("td")
            info_country = info_country[0::2]
            for data in info_country:
                palavra = data.text.strip() + " "
                if contador == 0:
                    pais = data.text.strip()
                    contador+=1
                elif contador <= 11:
                    if palavra == " ":
                        score[definirAno(contador)] = 0
                    else:
                        score[definirAno(contador)] = float(data.text.strip())
                    contador+=1
                elif contador == 12:
                    if palavra == " ":
                        score[definirAno(contador)] = 0
                    else:
                        score[definirAno(contador)] = float(data.text.strip())
                    dadosGPI[pais] = score.copy()
                    score.clear()
                    contador=0
    return dadosGPI

