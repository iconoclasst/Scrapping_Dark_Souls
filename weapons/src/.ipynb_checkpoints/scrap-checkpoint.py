import requests
from bs4 import BeautifulSoup

def get_daggers():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    url = 'http://darksouls.wikidot.com/daggers'

    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    daggers = {
        'names':[],
        'damages':[],
        'criticals':[],
        'durabilities':[],
        'weight':[],
        'stats needed/bonuses':[],
        'availability':[],
        'special notes':[]
    }

    # columns = []
    # names = []
    # damages = []
    # criticals = []
    # durabilities = []

    table = dados_pagina.find('table', class_='wiki-content-table')
    for tr in table.find_all('tr'):

        # th = tr.find_all('th')
        # for column in th:
        #     daggers['columns'].append(column.text)

        tds = tr.find_all('td')

        if len(tds) == 0:
            continue

        daggers['names'].append(tds[1].find('a').text.strip())
        daggers['damages'].append(tds[2].get_text(" ", strip=True))
        daggers['criticals'].append(tds[3].get_text(" ", strip=True))
        daggers['durabilities'].append(tds[4].get_text(" ", strip=True))
        daggers['weight'].append(tds[4].get_text(" ", strip=True))
        daggers['stats needed/bonuses'].append(tds[5].get_text(" ", strip=True))
        daggers['availability'].append(tds[6].get_text(" ", strip=True))
        daggers['special notes'].append(tds[7].get_text(" ", strip=True))
    
    return daggers