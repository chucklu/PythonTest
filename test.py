words = ['安安静静', '绿油油', '吃饭', 'Python', '试试看', '考察考察', '横七竖八', '波光粼粼']
dic = {1:'A',2:'B',3:'C'}
patterns = ['AABB','ABAB','ABCC','ABB','AAB']
tempDictionary = {}
for word in words:
    pattern = ''
    i = 0
    for ch in word:
        if ch not in tempDictionary:
            i = i + 1
            if(i > 3):
                continue
            tempDictionary[ch] = dic[i]
        pattern = pattern + tempDictionary[ch]    
    #print(pattern)
    if pattern in patterns:
        print(word+'为'+pattern+'型')
    else:
        print(word+'为OTHER型')