#1. 设计一个编码转换的函数，功能为将一个具有某个编码（如GBK编码）的文件读入，并用另外一种指定编码（如UTF-8）保存为另外一个文件。
def transfer_encoding(infile, infile_encoding, outfile, outfile_encoding):
	input_file = open(infile,'r',-1,infile_encoding)
	content = input_file.read()
	input_file.close()
	output_file = open(outfile,'w',encoding=outfile_encoding)
	output_file.write(content)
	output_file.close()

infile = "./files/01_infile.txt"
outfile = "./files/01_outfie.txt"
infile_encoding = "gbk"
outfile_encoding = "utf-8"
transfer_encoding(infile,infile_encoding,outfile,outfile_encoding)