# beautiful soup

import requests
from bs4 import BeautifulSoup

reponse = requests.get('https://g1.globo.com/')
content = reponse.content

site = BeautifulSoup(content, 'html.parser')

# html
# site.find('div', class_ = 'feed-post')
noticia = site.find('div', attrs={'class': 'feed-post'})

# title
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

# local
local = noticia.find('span', attrs={'class': 'feed-post-metadata-section'})

print('titulo: ', titulo.text)
print('Local: ', local.text)
