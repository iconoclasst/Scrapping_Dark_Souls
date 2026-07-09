import requests
from bs4 import BeautifulSoup

def get_consumables():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'http://darksouls.wikidot.com/consumables' 

    consumables = {
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

            
            consumables['name'].append(tds[1].get_text(" ", strip=True))
            consumables['use'].append(tds[2].get_text(" ", strip=True))
            consumables['availability'].append(tds[3].get_text(" ", strip=True))
            
    return consumables

# print(get_consumables())