# 字典元素的获取
dict1 = {"zhang":20,"li":29,"fei":30}
print(dict1["li"])
print(dict1.get("zhang"))
# 根据key获取value,不存在则返回None
print(dict1.get("2"))
# 根据key获取value,不存在则为990
print(dict1.get("2",990))
