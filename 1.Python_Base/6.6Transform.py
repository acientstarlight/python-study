# 数据类型转换
#  其他类型转换成字符串类型
a=12  # str()
b=12.1
c=True
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
# int() 其他类型转成int类型
d=1.1
e="12"
f=False
print(int(d),int(e),int(f),type(int(d)),type(int(e)),type(int(f)))
# 其他类型转成float
g=10
h="12"
i="12.1"
j=True
print(float(g),float(h),float(i),float(j),type(float(g)),type(float(i)),type(float(j)))
# list转成str类型
list1=['1','2','我的','True']
print(''.join(list1),type(''.join(list1)))
list2=[1,2,12.1]
print(''.join([str(i) for i in list2]),type(''.join([str(i) for i in list2])))
# str类型转成list类型
string='我的123True'
print(list(string),type(list(string)))

