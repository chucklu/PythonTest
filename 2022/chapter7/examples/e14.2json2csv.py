import json
fr = open("price2016.json", "r", encoding='UTF-8')
ls = json.load(fr)
# print(ls)
# print(type(ls))
data = [list(ls[0].keys())]
print(data)
for item in ls:
    print(type(item))
    # print(item.values())
    data.append(list(item.values()))
fr.close()
print(data)

fw = open("price2016_from_json.csv", "w", encoding='UTF-8')
for item in data:
    fw.write(",".join(item) + "\n")
fw.close()
