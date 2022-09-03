
import jieba
import jieba.posseg as pos_tagger

def split_cn_sents(txt):
    puncts = set('；。！…？?!;')
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

def segment_file_cn(infile, outfile, infile_encoding='utf-8', outfile_encoding='utf-8'):
    # Read in the text
    fin = open(infile, 'r', encoding = infile_encoding)
    txt = fin.read()
    fin.close()

    # Get rid of all empty chars other than white space
    txt = txt.replace('\t', ' ').replace('\r', '').replace('\n', '')

    # split the text into sentences
    sents = split_cn_sents(txt)

    postagged_sents = []
    for sent in sents:
        word_pos_list = pos_tagger.cut(sent)
        temp = []
        for word, flag in word_pos_list:
            temp.append(f"{word}/{flag}  ")
        postagged_sents.append(temp)

    fout = open(outfile, 'w', encoding = outfile_encoding)
    for item1 in postagged_sents:
        for item2 in item1:
            fout.write(item2)
        fout.write('\n')
    fout.close()

def test_seg():
    sent = '河北石家庄，铁路运输法院法官赵毅正通过网络开展诉前调解。'
    seg_list = jieba.cut(sent)
    print('  '.join(seg_list))

def test_postag():
    txt = '河北石家庄，铁路运输法院法官赵毅正通过网络开展诉前调解。“为当事人提供一站式多元解纷和诉讼服务，化解矛盾，是我们法官的职责所在。”赵毅说。'
    sents = split_cn_sents(txt)
    for sent in sents:
        # word_pos_list = jieba.posseg.cut(sent_2)
        word_pos_list = pos_tagger.cut(sent)
        print('  '.join([f'{word}/{flag}' for word, flag in word_pos_list]))

def test():
    # You can change your code below
    infile = r'./files/corpus_cn_1_gbk.txt'
    outfile = r'./files/corpus_cn_1_postagged.txt'
    segment_file_cn(infile, outfile, 'gbk', 'utf-8')

#test_seg()
#test_postag()
test()
