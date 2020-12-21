# range函数
"""创建range函数，一个参数"""
r=range(20)  # 不包含20，0-19，步长默认为1
print(list(r))
"""创建range函数，两个参数"""
r2=range(2,20)  # 从2开始，不包含20，2-19，步长默认为1
print(list(r2))
"""创建range函数，三个参数"""
r3=range(2,20,3)  # 从2开始，不包含20，步长为3
print(list(r3))
print(20 not in r3)
print(20 in r3)
print(5 in r3)

