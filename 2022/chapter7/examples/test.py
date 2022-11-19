import locale
import sys
encoding = locale.getpreferredencoding() 
print(encoding)#cp936

print( sys.getfilesystemencoding())#utf-8
print(locale.getpreferredencoding(False))#cp936
print(locale.getpreferredencoding(True))#cp936