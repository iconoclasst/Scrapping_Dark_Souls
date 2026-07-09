import requests
from bs4 import BeautifulSoup

def get_bonfire_items():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'http://darksouls.wikidot.com/bonfire-items' 

    bonfire_items = {
        'name':[],
        'availability':[],
        'use':[],
        'special note':[]
    }

    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    table = dados_pagina.find('table', class_='wiki-content-table')

    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) == 0:
            continue


        bonfire_items['name'].append(tds[1].get_text(" ", strip=True))
        bonfire_items['availability'].append(tds[2].get_text(" ", strip=True))
        bonfire_items['use'].append(tds[3].get_text(" ", strip=True))
        bonfire_items['special note'].append(tds[4].get_text(" ", strip=True))
            
    return bonfire_items

print(get_bonfire_items())