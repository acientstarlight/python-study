# 字典元素的遍历
dict1 = {"李":21,"王":23,"张":26}
for key in dict1.keys():
    for i in range(1,len(dict1)+1):
        # 遍历字典的key
        print("第",i,"次遍历的键：",key)
for value in dict1.values():
    for i in range(1,len(dict1)+1):
        # 遍历字典的value
        print("第",i,"次遍历的值：",value)
for items in dict1.items():
    for i in range(1,len(dict1)+1):
        # 遍历字典的元素（键值对）
        print("第",i,"次遍历的键值对：",items)
for i in dict1:
    for j in range(1,len(dict1)+1):
        # 遍历字典的键
        print("第",j,"次遍历的字典的键为：",i)
        # 遍历字典的值
        print("第",j,"次遍历的字典的值为：",dict1[i])
        # 遍历字典的键值对
        print("第",j,"次遍历的字典的键值对为：",i,dict1[i])
        # 遍历字典元素的value
        print("第",j,"次遍历的字典的值为：",dict1.get(i))

