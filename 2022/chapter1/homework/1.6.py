#健康食谱输出 两两组合
#C52  
diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
totalCount = 0
for i in range(0,5):
    for j in range(0,5):
        if(j<i):
            totalCount=totalCount+1
            print("{},{}".format(diet[j],diet[i]))
print("一共有{}组合".format(totalCount))