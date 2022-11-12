# pip3 install jieba
import jieba
str="中华人民共和国是一个伟大的国家"
result = jieba.lcut(str)
print(type(result))
print(result)

result = jieba.lcut(str,cut_all=True)
print(result)

result = jieba.lcut_for_search(str)
print(result)