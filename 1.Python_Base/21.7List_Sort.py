# 列表元素的排序
# sort方法不会产生新的对象
lst1 = [21,32,1,38,99,88]
lst1.sort()  # 默认为升序
# lst1.sort(reverse=False)  # 等同于lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)

# 调用list的内置函数sorted(),会产生一个新的list对象
lst2 = [12,32.26,423,21]
lst3 = sorted(lst2)  # 默认为升序
# lst3 = sorted(lst3,reverse=False)  # 等同于lst3 = sorted(lst2)
print(lst3)
lst4 = sorted(lst2,reverse=True)
print(lst4)


