def read_person_words(file_path):
	result = []
	my_file = open(file_path, 'r', -1, 'utf8')
	for line in my_file:
		result_item = parse(line)
		result.append(result_item)
	my_file.close()
	return result

def parse(line):
	line = line.strip()
	words = line.split('\t')
	result = (words[0], words[1])
	return result

def print_quotes(name, word):
    print(f"{name} said, \"{word}\"")

file_path = "./files/person_sayings.txt"
results = read_person_words(file_path)
for result in results:
	print_quotes(result[0],result[1])

