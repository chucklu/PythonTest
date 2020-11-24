
def split_cn_sents(txt):
    puncts = set('；。！…？')
    sents = []
    # Add your code below

    return sents

def test():
    txt = '治国凭圭臬，安邦靠准绳。厉行法治，重在法之必行！！'
    sents = split_cn_sents(txt)
    print(sents)
    #sents = ['治国凭圭臬，安邦靠准绳。', '厉行法治，重在法之必行。']

test()
