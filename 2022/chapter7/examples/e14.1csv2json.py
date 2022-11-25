import json
fr = open("price2016.csv", "r", encoding='UTF-8')
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
fr.close()
fw = open("price2016.json", "w", encoding='UTF-8')
for i in range(1, len(ls)):
    temp = zip(ls[0], ls[i])
    # print(type(temp)) #<class 'zip'>
    ls[i] = dict(temp)
# print(ls)
print("ls length is {}".format(len(ls)))
toPrint = ls[1:len(ls)]  # ls[1:]
json.dump(toPrint, fw, sort_keys=True, indent=4, ensure_ascii=False)
fw.close()
