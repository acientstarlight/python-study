# 算术运算符
a=11
b=3
c=12.3
d=True
e=-4
f=-11
print(a+b)
print(b-c)
print(a*d)
print(a/d)    # 除法，返回浮点型
print(a//b)   # 表示整除
print(b**5)   # 表示b的5次方
print(a//e)   # 11除以-4为-2余-3，一正一负向下取整为-3(同为负则按两个整数看待)
print(f//3)   # -11除以3为-3余-2，一正一负向下取整为-4
print(a%e)    # 一正一副取余，遵循公式：余数=被除数-除数*商 11%-4  余数=11-（-4）*（-3）=-1(同为负则按两个整数看待)
print(f%b)    # -11%3  余数=-11-3*（-4)=1


