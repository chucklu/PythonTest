import requests
import re

def get_webpage(url):
    #print('satrt get_webpage')
    x = requests.get(url, verify=False)
    # Show the status code: 200 means "OK". 404 means "page not found."
    print(url)
    print('Response:', x.status_code)
    return x.text

def extract_title(content):
    #print(content)
    title = ''
    rgx_pat = r'.*<title>(?P<title>.*)</title>.*'
    regex = re.compile(rgx_pat,flags = re.MULTILINE|re.DOTALL)
    mat = regex.match(content)
    title = mat.group('title')
    return title

def extract_post_time(content):
    time = ''
    return time

def extract_post_source(content):
    source = ''
    return source

def extract_text(content):
    text = ''
    return text

def export(url, outfile):
    #print(f'start export {url}, {outfile}')
    content = get_webpage(url)
    title = extract_title(content)
    time = extract_post_time(content)
    source = extract_post_source(content)
    text = extract_text(content)
    fout = open(outfile,'w',encoding='utf-8')
    fout.write(title)
    fout.write(time)
    fout.write(source)
    fout.write(text)
    fout.close()
    #print('end export')


def test():
    urls = ['https://news.163.com/20/1116/09/FRHVKCJH000189FH.html?clickfrom=w_yw',
            'https://dy.163.com/article/FRLH5NV30532B1TX.html']
    i = 0
    for url in urls:
        i += 1
        outfile = f'./files/export_web_{i}.txt'
        export(url, outfile)
    titles = [extract_title(get_webpage(url)) for url in urls]

test()
