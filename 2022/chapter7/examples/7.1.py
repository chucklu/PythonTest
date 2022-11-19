
import os
#os.chdir('absolute-path-to-workingDir')
path = os.path.abspath(os.getcwd())
print("path is "+path)

#textFile = open("7.1.txt", "r")
textFile = open("7.1.txt", "r", encoding='UTF-8')
print(textFile.readline())
textFile.close()
