import requests
from bs4 import BeautifulSoup

def get_daggers():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    url = 'http://darksouls.wikidot.com/daggers'

    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    daggers = []
    columns = []
    names = []
    damages = []
    criticals = []
    durabilities = []

    table = dados_pagina.find('table', class_='wiki-content-table')
    for tr in table.find_all('tr'):

        th = tr.find_all('th')
        for column in th:
            columns.append(column.text)

        tds = tr.find_all('td')

        if len(tds) == 0:
            continue

        names.append(tds[1].find('a').text.strip())
        damages.append(tds[2].get_text(" ", strip=True))
        criticals.append(tds[3].get_text(" ", strip=True))
        durabilities.append(tds[4].get_text(" ", strip=True))

    daggers.append(columns)
    daggers.append(names)
    daggers.append(damages)
    daggers.append(criticals)
    daggers.append(durabilities)
    
    return daggers