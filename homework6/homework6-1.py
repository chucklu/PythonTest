#sample_corpus_with_pos
import jieba
import jieba.posseg as pos_tagger

def remove_spaces(infile, outfile, infile_encoding='utf-8', outfile_encoding='utf-8'):
    fin = open(infile, 'r', encoding = infile_encoding)
    txt = fin.read()
    fin.close()

    txt = txt.replace(" ","");
    fout = open(outfile, 'w', encoding = outfile_encoding)
    fout.write(txt)
    fout.close()

def segment_file_cn(infile, outfile, infile_encoding='utf-8', outfile_encoding='utf-8'):
    # Read in the text
    fin = open(infile, 'r', encoding = infile_encoding)
    lines = fin.readlines()
    fin.close()

    postagged_sents = []
    for line in lines:
        word_pos_list = pos_tagger.cut(line)
        temp = []
        for word, flag in word_pos_list:
            if(word!='\n'):
            	#jieba will recognize \n with \x
                temp.append(f"{word}/{flag}")
        sent = ' '.join(temp)
        postagged_sents.append(sent)

    fout = open(outfile, 'w', encoding = outfile_encoding)
    for sent in postagged_sents:
    	fout.write(f'{sent}\n')
    fout.close()

def test():
    # You can change your code below
    infile = r'./files/sample_corpus.txt'
    outfile_without_space = r'./files/sample_corpus_without_spaces.txt'
    outfile = r'./files/sample_corpus_with_pos.txt'
    remove_spaces(infile, outfile_without_space)
    segment_file_cn(outfile_without_space, outfile, 'utf-8', 'utf-8')

#test_seg()
#test_postag()
test()