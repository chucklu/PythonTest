def split_cn_sents(txt):
    puncts = set('；。！…？')
    sents = []
    ch_count = len(txt)
    start_index = 0
    end_index = 0
    for i in range(0,ch_count,1):
    	ch = txt[i]
    	if(ch in puncts and i==start_index):
    		sents_count = len(sents)
    		index = sents_count-1
    		sents[index] =  f"{sents[index]}{ch}"
    		start_index += 1
    	else:
    		if(ch in puncts):
    			#print(f"i = {i}, start_index = {start_index}")
    			end_index = i+1
    			sent = txt[start_index:end_index]
    			sents.append(sent)
    			start_index = i+1
    return sents

def test():
    txt = '治国凭圭臬，安邦靠准绳。厉行法治，重在法之必行！！'
    sents = split_cn_sents(txt)
    print(sents)
    #sents = ['治国凭圭臬，安邦靠准绳。', '厉行法治，重在法之必行！！']

test()
