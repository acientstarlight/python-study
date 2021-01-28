# 元组的创建
tup1 = ("liming",23,"广州")          # 使用(),包含多个元素
print(tup1)
tup2 = tuple(("liming",[20,21],{1,2,3},12.3,(2.1,3),"广州"))     # 使用tuple(),包含多个元素
print(tup2)
tup3 = "zhangqian",25,"xi‘an"       # 省略小括号()
print(tup3)
t1 = "fu"
tup4 = tuple(t1)                    # 将字符串字母分割
print(tup4)
tup5 = ("wang",)                    # 只有一个元素，用小括号()和逗号，
print(tup5)
tup6 = ()                           # 空元组
print(tup6)
tup7 = tuple()                      # 空元组
print(tup7)

