# 基本数据类型
import time,datetime;
print(1,12.1,True,"从左到右依次是整数、浮点、布尔、字符串、列表、元组",[1,"wode",23.11,True],(1,"12",1.12,True))
set1 = {1,2,"123"}
set2 = {}
set3 = set('hello')
set4 = set([12345654321])
# set4 = set("hello","python",1)  # 会报错“set expected at most 1 argument, got 2”!原因：set()函数可以创建一个无序不重复的元素集，这个函数至多可以传一个参数；
print(set1)
print(set2)
print(set3)
print(set4)
print("set2的数据类型是：",type(set2))
dict1 = {"name":"123",121:1}
print(dict1)
local_time = time.strftime('%Y-%m-%d %H:%M:%S')  # 获取当前的时间（返回的是字符串类型）
local_time2 = datetime.datetime.strptime(local_time,"%Y-%m-%d %H:%M:%S")  # 将字符串类型日期转成日期格式
print(type(local_time),type(local_time2))
print(local_time,local_time2)



