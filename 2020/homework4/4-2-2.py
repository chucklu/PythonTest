
def stat_grades(grades):
    dicCount = {'Excellent': 0, 'Good': 0,'Pass':0,'Fail':0}
    dicStandard = {'Excellent': 8.5, 'Good': 7.0,'Pass':6.0, 'Fail':0}
    for grade in grades:
    	for standardName in dicStandard:
    		if(grade >= dicStandard[standardName]):
    			dicCount[standardName] = dicCount[standardName] + 1
    			break   
    return dicCount

grades = [9.5, 8.8, 7.9, 9.0, 6.0, 6.5, 8.0, 8.1, 5.4, 7.8]
results = stat_grades(grades)
for result in results:
    print(f"{result}:{results[result]}")