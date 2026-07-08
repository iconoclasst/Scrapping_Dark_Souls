import requests
from bs4 import BeautifulSoup

def get_links():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'http://darksouls.wikidot.com/spell-tools'
    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    links = []

    table = dados_pagina.find('td')

    for h3 in table.find_all('h3'):
        a = h3.find('a')
        links.append(a.get('href'))
    
    return links