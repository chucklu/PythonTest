def stat_grades(grades):
    dicCount = {'Excellent': 0, 'Good': 0,'Pass':0,'Fail':0}
    dicStandard = {'Excellent': 8.5, 'Good': 7.0,'Pass':6.0, 'Fail':0}
    for grade in grades:
    	for standardName in dicStandard:
    		if(grade >= dicStandard[standardName]):
    			dicCount[standardName] = dicCount[standardName] + 1
    			break   
    return dicCount

def read_scores(file_path):
	result = []
	my_file = open(file_path, 'r', -1, 'utf8')
	for line in my_file:
		result_item = parse(line)
		result.append(result_item)
	my_file.close()
	return result

def parse(line):
	line = line.strip()
	words = line.split(',')
	result = (words[0],float(words[1]))
	return result

file_path = "./files/student_scores.txt"
results = read_scores(file_path)
scores = []
for result in results:
	scores.append(result[1])
statistics = stat_grades(scores)
for item in statistics:
	print(f"{item}:{statistics[item]}")
