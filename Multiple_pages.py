import requests
from bs4 import BeautifulSoup
base_url = "https://quotes.toscrape.com/page/{}/"

for page in range(1,4):
    url = base_url.format(page)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    qoutes = soup.find_all("span", class_="text")
    print(f"\n---page {page}---")
    for qoute in qoutes:
        print(qoute.text)