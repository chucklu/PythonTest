def split_cn_sents(txt):
    puncts = set('；。！…？')
    sents = []
    # Add your code below
    count = len(txt)
    temp = ""
    encounter_punct = False
    for i in range(0,count,1):
    	ch = txt[i]
    	temp = f"{temp}{ch}"
    	if(ch in puncts):
    		sents.append(temp)
    		temp = ""
    return sents

def test():
    txt = '治国凭圭臬，安邦靠准绳。厉行法治，重在法之必行！！'
    sents = split_cn_sents(txt)
    print(sents)
    #sents = ['治国凭圭臬，安邦靠准绳。', '厉行法治，重在法之必行。']

test()
