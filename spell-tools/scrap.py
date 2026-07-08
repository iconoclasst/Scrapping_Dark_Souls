import requests
from bs4 import BeautifulSoup
import section

def get_spell_tools():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    urls = section.get_links()

    spell_tools = {
        'name':[],
        'magic adjustment':[],
        'damage':[],
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

            spell_tools['name'].append(tds[1].get_text(" ", strip=True))
            spell_tools['magic adjustment'].append(tds[2].get_text(" ", strip=True))
            spell_tools['damage'].append(tds[3].get_text(" ", strip=True))
            spell_tools['durability'].append(tds[4].get_text(" ", strip=True))
            spell_tools['weight'].append(tds[5].get_text(" ", strip=True))
            spell_tools['stats needed/bonuses'].append(tds[6].get_text(" ", strip=True))
            spell_tools['availability'].append(tds[7].get_text(" ", strip=True))
            spell_tools['special notes'].append(tds[8].get_text(" ", strip=True))

    return spell_tools