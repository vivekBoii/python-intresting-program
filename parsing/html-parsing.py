import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/Blog"

r=requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

for link in soup.find_all("p"):
    print(link.text)