import requests
from bs4 import BeautifulSoup
import section

def get_weapons():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    urls = section.get_links()

    weapons = {
        'name':[],
        'damage':[],
        'critical':[],
        'durability':[],
        'weight':[],
        'stats needed/bonuses':[],
        'availability':[],
        'special notes':[]
    }

    for u in urls:
        url = 'http://darksouls.wikidot.com' + u
        pagina = requests.get(url, headers=headers)

        dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

        table = dados_pagina.find('table', class_='wiki-content-table')
        for tr in table.find_all('tr'):

            tds = tr.find_all('td')

            if len(tds) == 0:
                continue

            if len(tds) == 9:
                weapons['name'].append(tds[1].get_text(" ", strip=True))
                weapons['damage'].append(tds[2].get_text(" ", strip=True))
                weapons['critical'].append(tds[3].get_text(" ", strip=True))
                weapons['durability'].append(tds[4].get_text(" ", strip=True))
                weapons['weight'].append(tds[5].get_text(" ", strip=True))
                weapons['stats needed/bonuses'].append(tds[6].get_text(" ", strip=True))
                weapons['availability'].append(tds[7].get_text(" ", strip=True))
                weapons['special notes'].append(tds[8].get_text(" ", strip=True))

            elif len(tds) == 8:
                weapons['name'].append(tds[1].get_text(" ", strip=True))
                weapons['damage'].append(tds[2].get_text(" ", strip=True))
                weapons['critical'].append(None)
                weapons['durability'].append(tds[3].get_text(" ", strip=True))
                weapons['weight'].append(tds[4].get_text(" ", strip=True))
                weapons['stats needed/bonuses'].append(tds[5].get_text(" ", strip=True))
                weapons['availability'].append(tds[6].get_text(" ", strip=True))
                weapons['special notes'].append(tds[7].get_text(" ", strip=True))
    
    return weapons