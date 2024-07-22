# %%

import requests
from bs4 import BeautifulSoup

def get_content(url):

    headers = {
        'authority': 'www.residentevildatabase.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'pt-BR,pt;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    resp = requests.get(url, headers=headers)
    return resp

def get_basic_infos(soup):
    div_page = soup.find('div', class_='td-page-content')
    paragrafo = div_page.find_all('p')[1]
    ems = paragrafo.find_all('em')
    data = {}
    for i in ems:
        chave, valor = i.text.split(":")
        chave = chave.strip(' ')
        data[chave] = valor.strip(' ')
        
    return data

# %%

url = 'https://www.residentevildatabase.com/personagens/alex-wesker/'
resp = get_content(url)

if resp.status_code != 200:
    print(f'Não foi possível obter os dados.\ncódigo:{resp.status_code}')
else:
    print(f'OK.\ncódigo:{resp.status_code}')
    soup = BeautifulSoup(resp.text)
    get_basic_infos(soup)

# %%

soup.find('div', class_='td-page-content').find('h4').find_next()