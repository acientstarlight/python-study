# 比较运算符
a,b,c,d,e=1,12,16,12.0,True
print(a<b)
print(b>c)
print(a<=e)
print(e>=c)
print(b==d)  # ==比较的对象的值，比较对象标识（id)用is
g=12
h=12
print(id(g),id(h))
print(g==h)
print(g is h)
i=[1,2,3]
j=[1,2,3]
print(id(i),id(j))
print(i==j,i is j,i is not j)







