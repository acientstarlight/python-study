# 字典生成式
name = ["张","王","李"]
age = [22,23,24,25,26]
info = {name:age for name,age in zip(name,age)}
print(info)
