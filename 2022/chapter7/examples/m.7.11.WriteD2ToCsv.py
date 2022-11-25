fr = open("price2016.csv", "r", encoding='UTF-8')
fw = open("price2016out.csv", "w", encoding='UTF-8')
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
for i in range(len(ls)):
    for j in range(len(ls[i])):
        temp = ls[i][j].replace(".", "")
        print("temp{}{} = {}".format(i,j,temp))
        if (temp.isnumeric()):
            print("{} is numeric".format(temp))
            percentage = float(ls[i][j]/100)
            ls[i][j] = "{:.2f}%".format(percentage)
for row in ls:
    print(row)
    fw.write(",".join(row)+"\n")
print(ls)
fr.close()
fw.close()
