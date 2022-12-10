import requests
from bs4 import BeautifulSoup

# Set the User-Agent header to the value of a Chrome browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

url = "http://www.baidu.com"
url = "https://www.usnews.com/best-colleges/rankings/national-universities"
r = requests.get(url, timeout=30, headers=headers)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, "html.parser")
print(type(soup))
print(soup.head)
print(soup.title)
print(soup.body)
