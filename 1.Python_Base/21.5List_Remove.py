# list元素的删除
lst1 = [10,20,30,40,50,40,30,20,10]
# 根据元素的值删除元素，如果有重复值的元素则删除第一个
lst1.remove(10)
print(lst1)
# 根据索引删除元素，如果不填写索引，则默认删除最后一个元素
lst1.pop(3)
print(lst1)
lst1.pop()
print(lst1)
# 删除多个对象,删除第二、第三个元素
lst1[1:3] = []
print(lst1)
# 删除lst1除第二、第三个元素的其他元素,会产生一个新的list对象lst2
lst2 = lst1[1:3]
print(lst2)
lst1.clear()
print(lst1)
del lst1
