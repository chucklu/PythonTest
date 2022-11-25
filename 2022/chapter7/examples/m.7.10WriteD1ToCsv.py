fo = open("price2016bj.csv", "w", encoding='UTF-8')
ls = ['北京', '101.5', '120.7', '121.4']
text = ",".join(ls)
fo.write(text+"\n")
fo.close()
