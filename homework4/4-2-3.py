def read_person_words(file_path):
	result = []
	my_file = open(file_path, 'r', -1, 'utf8')
	for line in my_file:
		result_item = parse(line)
		result.append(result_item)
	my_file.close()
	return result

def parse(line):
	words = line.split('\t')
	result = (words[0], words[1])
	return result

file_path = "./files/person_sayings.txt"
read_person_words(file_path)

