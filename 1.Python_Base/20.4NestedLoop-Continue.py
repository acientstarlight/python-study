# 嵌套循环中continue语句
"""
1-5分别和100-199相乘，输出每次乘积中的所有水仙花数及其乘数
当乘积不是水仙花数时跳过，继续执行内循环
"""
for i in range(1,6):
    for j in range(100,200):
        if (i*j//100)**3+(i*j//10%10)**3+(i*j%10)**3!=i*j:
            continue
        print("执行到第",i,"次外循环""找到了水仙花数，内循环执行到了第", j-99, "次","乘积水仙花数为：",i*j,"构成第一个水仙花数乘积的两个数为",i," ",j)
    print("外循环执行完了第",i,"次")
