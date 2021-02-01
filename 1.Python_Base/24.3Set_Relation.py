# 集合之间的关系
"""判断元素是否相等"""
s1 = {1,2,3,4}
s2 = {2,3,1,4}
print(s1==s2)
"""判断一个集合是为另一个集合的子集"""
s3 = {1,2}
print(s3.issubset(s1))
"""判断一个集合是为另一个集合的父集"""
print(s2.issuperset(s3))
"""判断一个集合和另一个集合的是否没有交集"""
print(s1.isdisjoint(s3))
s4 = {5,6,7,8}
print(s1.isdisjoint(s4))
"""输出两个集合的交集"""
s5 = {1,2,3,4,5,6}
print(s1.intersection(s5))
"""原始的集合上移除不重叠的元素"""
s5.intersection_update(s1)
print(s5)
"""获取两个集合的并集"""
s6 = {1,7,8}
print(s6.union(s2))
"""输出一个集合中关于和另一个集合的差集"""
print(s2.difference(s6))
"""移除两个集合都包含的元素"""
s2.difference_update(s6)
print(s2)




