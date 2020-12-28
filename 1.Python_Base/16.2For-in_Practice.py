# 输出100-999之间的水仙花数之和
sum=0
for i in range(100,1000):
    bai=i//100
    shi=i//10%10
    ge=i%10
    if bai**3+shi**3+ge**3==i:
        print(i)
        sum+=i
print("输出100-999之间的水仙花数之和为：",sum)
