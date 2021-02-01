# 集合的创建
s1 = {1,1,1,1,1,2,3,4,5,6,}      # 直接使用{}来创建
s2 = {1,2,3,4,5,6}               # 集合中的元素是不能重复的，此为规范写法
print(s1,type(s1))
print(s2,type(s2))
str1 = "python"
s3 = set(str1)                   # 将字符串类型切分成集合类型
print(s3,type(s3))
s4 = set(range(6))               # 使用内置函数range(),生成集合
print(s4)
dict1 = {1: 2, 21: 21, "王": 24}
print(set(dict1))                # 将dict转换成set，只转换key
tup1 = (1,2,3,4,5,6)
print(set(tup1),type(tup1))      # 将元组转换集合
lst1 = [1,2,3,4,5,6]
print(set(lst1),type(lst1))      # 将列表转成集合
s5 = set()
print(s5,type(s5))




