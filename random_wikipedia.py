from bs4 import BeautifulSoup
import requests

# Open random wikipedia URL
wiki_url = 'https://en.wikipedia.org/wiki/Special:Random'
r = requests.get(wiki_url)

# Parse the HTML
soup = BeautifulSoup(r.text, 'html.parser')

# Find the title and the paragraphs of the page
title = soup.find('h1').text
paragraphs = soup.select('p')

# Print title and first 3 paragraphs
print(title, '\n')
for p in paragraphs[:3]:
    print(p.getText())