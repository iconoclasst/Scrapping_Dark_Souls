import requests
from bs4 import BeautifulSoup

def get_keys():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'http://darksouls.wikidot.com/keys' 

    keys = {
        'name':[],
        'availability':[],
        'opens':[],
        'special note':[]
    }

    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    table = dados_pagina.find('table', class_='wiki-content-table')

    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) == 0:
            continue


        keys['name'].append(tds[1].get_text(" ", strip=True))
        keys['availability'].append(tds[2].get_text(" ", strip=True))
        keys['opens'].append(tds[3].get_text(" ", strip=True))
        keys['special note'].append(tds[4].get_text(" ", strip=True))
            
    return keys