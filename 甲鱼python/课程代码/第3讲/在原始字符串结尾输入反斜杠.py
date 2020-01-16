'''
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str = r'c:\a\b'
>>> print(str)
c:\a\b
>>> str = r'c:\a\b\\'
>>> print(str)
c:\a\b\\
>>> str = r'c:\a\b\'
SyntaxError: EOL while scanning string literal
>>> str = r'c:\a\b"\"'
>>> print(str)
c:\a\b"\"
>>> str = r'c:\a\b''\'
SyntaxError: EOL while scanning string literal
>>> str = r'c:\a\b"\'
SyntaxError: EOL while scanning string literal
>>> str = r'C:\Program Files\FishC\Good''\\'
>>> print(str)
C:\Program Files\FishC\Good\
>>> str = r'c:\a\b\c\d''\\'
>>> pirnt(str)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    pirnt(str)
NameError: name 'pirnt' is not defined
>>> print(str)
c:\a\b\c\d\
>>> str = r'C:\Program Files\FishC\Good''\\'   #这里的Good''\\'的 '' 是两个单引号
'''