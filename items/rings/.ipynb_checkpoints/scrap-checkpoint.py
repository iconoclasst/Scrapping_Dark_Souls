import requests
from bs4 import BeautifulSoup

def get_rings():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'http://darksouls.wikidot.com/rings' 

    rings = {
        'name':[],
        'use':[],
        'availability':[]
    }

    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    table = dados_pagina.find('table', class_='wiki-content-table')

    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) == 0:
            continue


        rings['name'].append(tds[1].get_text(" ", strip=True))
        rings['use'].append(tds[2].get_text(" ", strip=True))
        rings['availability'].append(tds[3].get_text(" ", strip=True))
            
    return rings