import requests

def get_webpage(url):
    x = requests.get(url)
    # Show the status code: 200 means "OK". 404 means "page not found."
    print(url)
    print('Response:', x.status_code)
    return x.text

def save_news_titles(titles, outfile, encoding='utf-8'):
    # Add your code below
    pass

def extract_title(content):
    title = ''
    # Add your code below

    return title

# def extract_article(content):
#     article = ''
#     return article

def test_webpage_request():
    url = 'https://www.reuters.com/article/us-health-coronavirus-usa-records/u-s-covid-19-cases-cross-11-million-as-pandemic-intensifies-idUSKBN27V0RX'
    content = get_webpage(url)
    print(content)

def test():
    urls = ['https://news.163.com/20/1116/09/FRHVKCJH000189FH.html?clickfrom=w_yw',
            'https://dy.163.com/article/FRLH5NV30532B1TX.html']
    titles = [extract_title(get_webpage(url)) for url in urls]
    outfile = './files/webpage_titles.txt'
    save_news_titles(titles, outfile)

# test_webpage_request()
test()
