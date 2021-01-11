# 字典的创建
# 创建空字典
dict1 = {}
# 直接赋值创建
dict2= {"小王":28,"小刘":20,"小张":25}
print(dict1,dict2)
# 通过关键字dict和key/value创建
dict3 = dict(a=1,b=2,c=3)
print(dict3)
# 通过二元组创建
list1 = [("小王",29),("夏丽丽",21)]
dict4 = dict(list1)
print(dict4)
# 与zip结合创建
dict5 = dict(zip("abcd",(1,3,2,4)))
print(dict5)
# 通过字典推导式创建
dict6 = {i*2:i*3 for i in range(1,20,2)}
print(dict6)
# 通过dict.fromkeys()创建,通常用来初始化字典, 设置value的默认值
dict7 = dict.fromkeys(range(1,10,3),"python")
print(dict7)
