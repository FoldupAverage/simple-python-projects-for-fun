import requests
from bs4 import BeautifulSoup

url = input('URL to extract links from: ')

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

links = []
for link in soup.find_all('a'):
    href = link.get('href')
    links.append(href)

print(f'First 10 links on : {url}')
for link in links[:10]:
    print(link)