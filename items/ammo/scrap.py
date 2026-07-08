import requests
from bs4 import BeautifulSoup
import section

def get_ammo():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'http://darksouls.wikidot.com/ammo' 

    ammo = {
        'name':[],
        'damage':[],
        'bow dist rate bonus':[],
        'auxiliary effects':[],
        'availability':[],
        'souls':[],
        'special note':[]
    }

    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    tables = dados_pagina.find_all('table', class_='wiki-content-table')

    for table in tables:
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) == 0:
                continue

            
            ammo['name'].append(tds[1].get_text(" ", strip=True))
            ammo['damage'].append(tds[2].get_text(" ", strip=True))
            ammo['bow dist rate bonus'].append(tds[3].get_text(" ", strip=True))
            ammo['auxiliary effects'].append(tds[4].get_text(" ", strip=True))
            ammo['availability'].append(tds[5].get_text(" ", strip=True))
            ammo['souls'].append(tds[6].get_text(" ", strip=True))
            if len(tds) == 8:
                ammo['special note'].append(tds[7].get_text(" ", strip=True))
            else:
                ammo['special note'].append(None)
            
    return ammo

# print(get_ammo())