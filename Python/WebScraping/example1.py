from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup.find('div', class_ = 'small-widget')

soup.find('div', attrs = {'class': 'small-widget'})

n = soup.find('div', class_ = 'small-widget').h2.next_element

print(n)
