def split_cn_sents(txt):
    puncts = set('；。！…？')
    sents = []
    end_index_list = []
    ch_count = len(txt)
    for i in range(0,ch_count,1):
        ch = txt[i]
        if(ch in puncts):
            end_index_list.append(i)
            #print(i)
    #print(end_index_list)
    real_end_index_list = remove_duplicate_end_index(end_index_list)
    #print(real_end_index_list)
    end_index_count = len(real_end_index_list)

    start_index = 0
    for i in range(0,end_index_count):
        end_index = real_end_index_list[i]
        sent = txt[start_index:end_index+1]
        start_index = end_index+1
        #print(sent)
        sents.append(sent)
    return sents

def remove_duplicate_end_index(end_index_list):
    count =  len(end_index_list)
    has_popped = False
    #print(f"count={count}")
    for i in range(0,count-1,1):
        #print(f"i={i}")
        if(end_index_list[i]+1==end_index_list[i+1]):
            end_index_list.pop(i)
            has_popped = True
            break
    if(has_popped==True):
        return remove_duplicate_end_index(end_index_list)
    else:
        #print(end_index_list)
        return end_index_list


def test():
    txt = '治国凭圭臬，安邦靠准绳。厉行法治，重在法之必行！！'
    sents = split_cn_sents(txt)
    print(sents)
    #sents = ['治国凭圭臬，安邦靠准绳。', '厉行法治，重在法之必行！！']

test()
