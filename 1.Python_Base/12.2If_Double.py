# 分支结构if语句-双分支
# ATM输入取款金额执行取款数，如果超出余额(1000)直接退出，如果小于等于余额，则执行取款，并显示取款结束提示和余额信息
money=1000
s=int(input("输入取款金额："))
if s<=money:
    money=money-s
    print("取款成功，取款后余额为：",money)
else:
    print("余额不足，退出，当前余额为：",money)
print("结束取款，回家")

