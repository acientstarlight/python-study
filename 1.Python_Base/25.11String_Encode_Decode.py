# 字符串的编码和解码
# 编码
str1="我的世界"
print(str1.encode(encoding='GBK'))    # 一个中文占两个字符
print(str1.encode(encoding='UTF-8'))    # 一个中文占三个字符

# 解码
# byte代表一个二进制的数据（字节类型的数据）
byte = str1.encode(encoding='GBK')
print(byte.decode(encoding="GBK"))

byte = str1.encode(encoding="UTF-8")
print(byte.decode(encoding="UTF-8"))

