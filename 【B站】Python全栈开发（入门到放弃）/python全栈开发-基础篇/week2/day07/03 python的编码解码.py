'''
编码 encode
解码 decode


in python2
默认 ASCII

in python3
默认 Unicode


encode在编码的同时，会把数据转在bytes类型（字节）
'''
import sys
print(sys.getdefaultencoding())	# 查看默认编码