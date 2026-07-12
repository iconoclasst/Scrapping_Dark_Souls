import requests
from bs4 import BeautifulSoup

def get_multiplayer_items():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'http://darksouls.wikidot.com/multiplayer-items' 

    multiplayer_items = {
        'name':[],
        'use':[],
        'availability':[],
    }

    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    tables = dados_pagina.find_all('table', class_='wiki-content-table')

    for table in tables:
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) == 0:
                continue

            
            multiplayer_items['name'].append(tds[1].get_text(" ", strip=True))
            multiplayer_items['use'].append(tds[2].get_text(" ", strip=True))
            multiplayer_items['availability'].append(tds[3].get_text(" ", strip=True))
            
    return multiplayer_items

# print(get_multiplayer_items())