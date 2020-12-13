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

# <div class="post_time_source">
#                 2020-11-16 09:38:24 来源: <a id="ne_article_source" href="http://www.xinhuanet.com/politics/2020-11/15/c_1126743154.htm" target="_blank">新华网</a>
                
#                 <a href="http://jubao.aq.163.com/" target="_blank" class="post_jubao" title="举报本文">举报</a>
#             </div>
def extract_post_time(content):
    time = ''
    rgx_pat = r'.*(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+)来源.*<'
    regex = re.compile(rgx_pat,flags = re.MULTILINE|re.DOTALL)
    mat = regex.match(content)
    time = mat.group('time')
    return time

def extract_post_source(content):
    #print('start extract_post_source')
    source = '' 
    # rgx_pat = r'.*(?P<source>来源.*\s+.*)post_jubao.*>举报</a>.*'
    # regex = re.compile(rgx_pat,flags = re.MULTILINE|re.DOTALL)
    # mat = regex.match(content)
    # source = mat.group('source')
    #print(source)
    #print('end extract_post_source')
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
    fout.write(f'{title}\n')
    fout.write(f'{time}\n')
    fout.write(f'{source}\n')
    fout.write(f'{text}\n')
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

test()
