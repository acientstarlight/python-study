# 集合相关操作
"""判断元素在集合中是否存在"""
s1 = {1,2,3,4,5,6,7}
print(8 in s1,8 not in s1)
'''在集合中添加元素'''
s1.add(8)
print(s1)
s1.update([9,10])
s1.update({11,12})
print(s1)
"""集合元素的删除操作"""
s1.remove(12)
print(s1)
s1.discard(13)
s1.discard(11)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)

