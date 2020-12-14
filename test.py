import re
import requests

def get_webpage(url):
    #print('satrt get_webpage')
    x = requests.get(url, verify=False)
    # Show the status code: 200 means "OK". 404 means "page not found."
    print(url)
    print('Response:', x.status_code)
    return x.text

def extract_post_source(content):
    print('start extract_post_source')
    source = '' 
    rgx_pat = r'.*(?P<source><div.*>.*<div>).*'
    regex = re.compile(rgx_pat,flags = re.MULTILINE|re.DOTALL)
    mat = regex.search(content)
    source = mat.group('source')
    print(source)
    print('end extract_post_source')
    return source

def export(url, outfile):
    #print(f'start export {url}, {outfile}')
    content = get_webpage(url)
   
    source = extract_post_source(content)
  
    fout = open(outfile,'w',encoding='utf-8')
  
    fout.write(f'{source}\n')

    fout.close()
    #print('end export')

def test():
    url = 'https://news.163.com/20/1116/09/FRHVKCJH000189FH.html?clickfrom=w_yw'
    outfile = f'./files/export_web_3.txt'
    export(url, outfile)
test()