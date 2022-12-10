import requests
from bs4 import BeautifulSoup
url = "http://www.baidu.com"
r = requests.get(url, timeout=30)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text,"html.parser")
print(type(soup))
print(soup.head)
print(soup.title)
print(soup.body)