# 嵌套循环
"""打印5×6的实心矩阵"""
for i in range(1,6):
    for j in range(1,7):
        print("*",end='')
    print()
a = 1
while a<6:
    b = 1
    while b<7:
        print("*", end='')
        b += 1
    a += 1
    print()
for k in range(1,6):
    c = 1
    while c<7:
        print("*",end='')
        c += 1
    print()
e = 1
while e<6:
    for m in range(1,7):
        print("*",end="")
    e += 1
    print()









