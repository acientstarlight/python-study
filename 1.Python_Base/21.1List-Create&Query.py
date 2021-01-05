# 列表的创建和获取里面元素
lst = [901,"我的",12.1]
print(type(lst))
print(id(lst))
print(lst)
print(lst[2])
# 获取列表元素的索引（存在相同value的元素，则返回第一个的索引
lst2 = ["我","我",1,{1,2}]
print(lst2.index("我"),lst2.index({1,2}))
# 在指定位置区域寻找指定的元素
print(lst2.index({1,2},2,4))
print(lst[-1])
print(lst2[-4])
