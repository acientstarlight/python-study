# Continue流程控制语句
"""for-in-continue,输出1-2000（包含2000）之间的5的倍数之和"""
sum=0
for i in range(1,2001):
    if i%5!=0:
        continue
    else:
        sum+=i
print(sum)

sum2=0
a=2001
while a>1:
    a = a - 1
    if a%5!=0:
        continue
    sum2 += a
print(sum2)
