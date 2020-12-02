# 赋值运算符（执行顺序从左向右）
a=b=c=10  # 链式赋值
print(a,b,c,id(a),id(b),id(c))  # 三个变量的引用指向了同一个内存地址
d=3
e=8
d+=6      # 参数赋值
print(d,type(d))
e-=1
print(e,type(e))
d*=2
print(d,type(d))
e/=3
print(e,type(e))
d//=7
print(d,type(d))
e//=2
print(e,type(e))
a%=4
print(a,type(a))
a0,b0,c0=1,1,1  # 系列解包赋值
print(a0,b0,c0,id(a0),id(b0),id(c0))
a0,b0,c0=11,12,13  # 系列解包赋值
print(a0,b0,c0,id(a0),id(b0),id(c0))
a1,b1=10,20      # 交换两个变量的值
print("交换前:  ","a1:",a1,"b1:",b1)
a1,b1=b1,a1
print("交换后:  ","a1:",a1,"b1:",b1)
a2,b2,c2=7,8,9
print("交换前:  ","a2:",a2,"b2:",b2,"c2:",c2)
a2,b2,c2=c2,a2,b2
print("交换后:  ","a2:",a2,"b2:",b2,"c2:",c2)



