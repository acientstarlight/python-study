# 字符串的分割
# split()--从左往右分割
str1 = "hello-world-ni-hao"
str2 = '111111-2'
print(str2.split('-',1)[0])
print(str1.split())     # 默认的从左往右根据空格“ ”分割，返回字符串数组
print(str1.split(sep="o"))    # 默认的从左往右根据特定字符“o”分割，返回字符串数组,"o"去除，如果"0为最末尾字符，最后一个分割出一个空字符串''
print(str1.split(sep="o",))    # 默认的从左往右根据特定字符“o”分割,最大的分割次数为两次

# rsplit()--从右向左分割
print(str1.rsplit())
print(str1.rsplit(sep="h"))
print(str1.rsplit(sep="h",maxsplit=2))
