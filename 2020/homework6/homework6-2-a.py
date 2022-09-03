import re
#可能/AD 会/VV 把/BA 我们/PN 给/VV 卖了/NN
def count_gei_V(verb_dict, mat):
	if(mat==None):
		return
	print(mat)
	verb = mat.group('verb')
	if verb not in verb_dict:
		verb_dict[verb] = 0
	verb_dict[verb] += 1

def extract_gei_V(infile):
	rgx_pat = r'\s+(?P<verb>[\u4e00-\u9fa5]+[起下上住到]+/v[A-Z]*)\s+'
	rgx = re.compile(rgx_pat)
	fin =  open(infile, 'r', encoding='utf-8')
	verb_dict = {}
	for line in fin:
		for mat in rgx.finditer(line):
			count_gei_V(verb_dict, mat)
	fin.close()
	return verb_dict

infile = './files/sample_corpus_with_pos.txt'
verb_dict = extract_gei_V(infile)
outfile = './files/homework6_2_a.txt'
fout = open(outfile,'w',encoding='utf-8')
for item in verb_dict:
	fout.write(f'{verb_dict[item]}:{item}\n')
	#print(item, verb_dict[item])
fout.close()