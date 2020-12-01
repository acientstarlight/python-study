# 浮点型
from decimal import *
a = 12.1
b = 12.2
print(a+b)
print(Decimal(a)+Decimal(b))
print(Decimal('12.1')+Decimal('12.2'))
print(Decimal(5.55))
print(Decimal('5.55'))
print(Decimal.from_float(12.33))   # 将浮点型转成Decimal类型
print(Decimal('5.55165').quantize(Decimal('0.000')))   # 四舍五入，保留三位小数
print(str(Decimal(5.556).quantize(Decimal("0.00"))))   # 将5.552转成字符串并四舍五入保留两位小数

