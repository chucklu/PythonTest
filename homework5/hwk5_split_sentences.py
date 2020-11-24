def split_cn_sents(txt):
    puncts = set('；。！…？')
    sents = []
    ch_count = len(txt)
    temp = ""
    for i in range(0,ch_count,1):
    	ch = txt[i]
    	if(ch in puncts and temp==""):
    		sents_count = len(sents)
    		index = sents_count-1
    		sents[index] =  f"{sents[index]}{ch}"
    	else:
    		temp = f"{temp}{ch}"
    		if(ch in puncts):
    			sents.append(temp)
    			temp = ""
    return sents

def test():
    txt = '治国凭圭臬，安邦靠准绳。厉行法治，重在法之必行！！'
    sents = split_cn_sents(txt)
    print(sents)
    #sents = ['治国凭圭臬，安邦靠准绳。', '厉行法治，重在法之必行！！']

test()
