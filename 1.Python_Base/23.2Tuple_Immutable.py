# 元组的不可变序列
tup = (1,2,[3,4,5],6)
print(tup[1],id(tup[1]))
print(tup[2],id(tup[2]))
print(tup[2][2],id(tup[2][2]))
# 修改其中可变的元素（列表）中的元素
tup[2][2] = 50
print(tup,id(tup))
print(tup[1],id(tup[1]))
print(tup[2],id(tup[2]))
print(tup[2][2],id(tup[2][2]))
# 在其中可变元素（列表）增加元素
tup[2].append(6)
print(tup[2],id(tup[2]))
tup[2].insert(0,0)
print(tup[2],id(tup[2]))



