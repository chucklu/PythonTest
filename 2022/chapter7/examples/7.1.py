
import os
# os.chdir('absolute-path-to-workingDir')
path = os.path.abspath(os.getcwd())
print("path is "+path)

fileName = "7.1-2.txt"

textFile = open(fileName, "rt")  # chcp in cmd, Active code page: 936
#textFile = open("7.1.txt", "rt", encoding='UTF-8')
print(textFile.readline())
textFile.close()

binFile = open(fileName, "rb")
print(binFile.readline())
binFile.close()
