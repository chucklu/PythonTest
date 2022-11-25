fo = open("price2016.csv", "r", encoding='UTF-8')
ls = []
for line in fo:
    line = line.replace("\n", "")
    list = line.split(',')
    text = '\t'.join(list)
    print(text)
fo.close()
