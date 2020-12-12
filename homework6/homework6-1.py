#sample_corpus_with_pos
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

def test():
    # You can change your code below
    infile = r'./files/sample_corpus.txt'
    outfile = r'./files/sample_corpus_with_pos.txt'
    segment_file_cn(infile, outfile, 'utf-8', 'utf-8')

#test_seg()
#test_postag()
test()