# criando arquivo csv

import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

reponse = requests.get('https://g1.globo.com/')
content = reponse.content

site = BeautifulSoup(content, 'html.parser')

# html
noticias = site.findAll('div', attrs={'class': 'feed-post'})

for noticia in noticias:

    # title
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    # print('titulo: ', titulo.text)
    # print('link: ', titulo['href'])

    lista_noticias.append([titulo.text, titulo['href']])

    print()

news = pd.DataFrame(lista_noticias, columns=['title', 'link'])
news.to_excel('news.xlsx', index=False) #index são os numeros das linhas.

print(news)
