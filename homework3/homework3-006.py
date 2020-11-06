dict_id_021 = {'id':'021', 'name':'John', 'health_code': 'green'}
dict_id_022 = {'id':'022', 'name':'Mary', 'health_code': 'red'}
dict_id_023 = {'id':'023', 'name':'Ann', 'health_code':'green'}
dict_all = {'021' : dict_id_021 , '022' : dict_id_022 , '023' : dict_id_023}

inputList = ['022','023','024']
for id in inputList:
	if id in dict_all:
	    tempDictionary = dict_all[id]
	    healthCode = tempDictionary["health_code"]
	    name = tempDictionary["name"]
	    if(healthCode == "green"):
	        print("允许%s进入" %name)
	    else:
	    	print("不允许%s进入" %name)
	else:
		print("user with id %s not exist" %id)