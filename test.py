words = ['安安静静', '绿油油', '吃饭', 'Python', '试试看', '考察考察', '横七竖八', '波光粼粼']
dic = {1:'A',2:'B',3:'C'}
templates = ['AABB','ABAB','ABCC','ABB','AAB','OTHER']
tempDictionary = {}
for word in words:
    template = ''
    i = 0
    for ch in word:
        if ch not in tempDictionary:
            i = i + 1
            if(i > 3):
                template = 'OTHER'
                continue
            tempDictionary[ch] = dic[i]
        template = template + tempDictionary[ch]    
    if template in templates:
        print(word+'为'+template+'型')
    else:
        print(word+'为OTHER型')