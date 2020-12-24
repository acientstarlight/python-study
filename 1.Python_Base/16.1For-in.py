# for-in循环
"""依次输出abc中的字母"""
for i in "abc":
    print(i)
"""依次输出0-3整数"""
for j in range(4):
    print(j)
"""打印3次nice to ,meet you"""
for _ in range(3):
    print("nice to ,meet you")
"""计算1-1000之间的偶数"""
sum=0
for k in range(1,1001):
    if k%2==0:
        sum+=k
print(sum)
