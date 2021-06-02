# 字符串的比较操作
str1="Apple"
str2="AppleID"
str3="apple"
print(str2>str1)    # 比较的是字符串的原始值
print(str3==str1,str2==str1,str2<=str1,str3>=str1,str3!=str1)
print(ord('a'),ord('c'))    # ord() 函数是 chr() 函数,它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
print('a'>'c')
print(ord('杨'))
print(chr(26472))
"""is和==的区别，is比较的是是否相等，==比较的是value是否相等
"""
a=b="java"
c="java"
print(a==c)
print(a is c)
print(id(a),id(b),id(c))

