# 字符串的替换和合并

# 字符串替换--replace
str1 = "python java"
print(str1.replace("java","C++"))
str2 = "pythonjavajavajavaJAVA"
print(str2.replace("java","C++"))
print(str2.replace("java","C++",2))    # 替换两次

# 字符串的合并--join
lst1 = ["java","python","C+="]
tup1 = ("1a","2b","3c")
print("".join(lst1),"".join(tup1),"_".join(lst1),"_".join(tup1))   # 用特定字符（包括空字符）链接不同字符

print("_".join("abcd"),"".join("efgh"))   # 对字符串序列也可以直接加入特定字符（包括空字符）进行进行合并





