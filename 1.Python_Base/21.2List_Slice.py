# 列表的切片操作
lst1 = [1,2,3,4,5,6,7,8,9,10,11,12]
lst2 = lst1[2:6]  # lst2 = lst1[2:6:] / lst2 = lst1[2:6:1]
# [start；stop:step] step为整数
print(lst2)
lst3 = lst1[0:5:2]
print(lst3)
# stop为8 start默认为从0开始，步长为2
lst4 = lst1[:8:2]
print(lst4)
# start为2，步长为3，stop默认为列表的长度（末尾）
lst5 = lst1[2::3]
print(lst5)
# 列表步长为负数
lst6 = lst1[::-1]  # lst6 = lst1[11::-1]
print(lst6)
# start为10，stop为1，step为2
lst7 = lst1[10:1:-2]
print(lst7)
# start为2，stop为0，step为1
lst8 = lst1[2::-1]
print(lst8)
# 复制列表
lst9 = lst1[:]
print(lst9)
# start为列表-2(倒数第二个元素)开始，stop为-4（倒数第4个元素）
lst10 = lst1[-2:-5:-1]
print(lst10)
# start为倒数第二个元素，stop为一直到末尾
lst11 = lst1[-2:]
print(lst11)
# start为从开头开始,stop为列表倒数第三个数（不包含倒数第三个数）
lst12 = lst1[:-3]
print(lst12)

