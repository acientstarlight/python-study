# 分支结构if语句-单分支
# ATM输入不同的取款金额执行取款金额，并显示取款结束提示和余额信息
money=1000
s=int(input("输入取款金额："))
if money>=s:
    money=money-s
    print("取款后的金额为：",money)  # 如果if的条件不成立，则缩进的部分不执行，跳出执行后面程序
print("取款结束")
print("当前的余额为：",money)

