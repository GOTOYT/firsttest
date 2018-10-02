import requests
from bs4 import BeautifulSoup

sach={'q':'Python', 'users':'1000'}
url = 'http://b.hatena.ne.jp/search/text'
req = requests.get(url, params = sach, timeout = 15)
print(req)

soup = BeautifulSoup(req.text, 'html.parser')

bookmarks = []

for b in soup.findAll('h3', {'class':''}):
    title = b.find('a').get('title')
    url = b.find('a').get('href')
    bookmarks.append([title, url])

print(bookmarks)
