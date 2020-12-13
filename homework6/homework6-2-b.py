import re
#别管/c 了/ul ，/x 戴夫/nr ，/x 把/p 东西/ns 带/v 好/a 咱们/r 快/a 闪/v ！/x
def count_gei_V(verb_dict, mat):
	if(mat==None):
		return
	print(mat)
	verb = mat.group(0)
	if verb not in verb_dict:
		verb_dict[verb] = 0
	verb_dict[verb] += 1

def extract_gei_V(infile):
	rgx_pat = r'\s+把/[a-z]+\s+(?P<noun>[\u4e00-\u9fa5]/n[a-z]*)\s+(?P<verb>[\u4e00-\u9fa5]+/v[a-z]*)\s+'
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
outfile = './files/homework6_2_b.txt'
fout = open(outfile,'w',encoding='utf-8')
for item in verb_dict:
	fout.write(f'{verb_dict[item]}:{item}\n')
	#print(item, verb_dict[item])
fout.close()