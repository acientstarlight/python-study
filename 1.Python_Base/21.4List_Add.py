# list元素的增加
lst1 = [1,2,3,4]
lst2 =[6,7,8]
lst1.append(5)  # 列表末尾添加一个值
print(lst1)
lst1.extend(lst2)  # 列表末尾添加一个列表里的所有元素（多个值）
print(lst1)
lst1.append(lst2)
print(lst1)
lst2.insert(2,"python")  # 在列表的特定位置（从0开始）添加一个值，添加后该添加的元素的索引为2
print(lst2)
lst4 = [10,20]
lst5 = ["hello","python"]
lst4[-1:] = lst5  # 切片操作，start倒数第一个起（保留倒数第一个），往后添加lst5中的元素（不会产生新的lst4列表对象）,lst5 = lst4[-1:]产生了一盒新的列表对象
print(lst4)
lst4[:-1] = lst5  # 切片操作，stop倒数第一个起（保留倒数第一个），往后添加lst5中的元素直至开头
print(lst4)

