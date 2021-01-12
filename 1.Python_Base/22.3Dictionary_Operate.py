# 字典的增删改操作
age = {"王":12,"李":21,"陈":26}
print(age)
# 新增元素
age["张"] = 30
print(age)
# 删除元素
del age["张"]
print(age)
# 修改元素的值
age["陈"] = 36
print(age)
# 清空字典里的元素
age.clear()
print(age)
age3 = {"人员":20}
age2 = {"王2":18,"李2":31,"陈2":29}
# 将age2的元素（键值对）添加复制到age3后
age3.update(age2)
print(age3)
# pop方法用来获得对应于给定键的值，然后将这个键-值对从字典中移除
print(age2.pop("王2"))
print(age2)
# popitem() 方法返回并删除字典中的最后一对键和值。
print(age2.popitem())
print(age2)
# 删除字典
del age




