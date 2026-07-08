import requests
from bs4 import BeautifulSoup

def get_links():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = 'http://darksouls.wikidot.com/items'
    pagina = requests.get(url, headers=headers)

    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    links = []

    div = dados_pagina.find('div', id='page-content')

    for h3 in div.find_all('h3'):
        a = h3.find('a')
        if a.get('href') == '/head':
            break

        links.append(a.get('href'))
    
    return links
