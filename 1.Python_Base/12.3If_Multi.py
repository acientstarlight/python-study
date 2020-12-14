# 分支结构if语句-多分支
# 根据银行卡余额取不同金额
"""
有余额为0的银行卡，客户转账进来一笔款项，这边收到后进行取款操作
当银行卡转入大于10000时取款8000
当银行卡转入在6000-10000之间时取款6000
当银行卡转入在2000-5999之间时取款1500
当银行卡转入在1000-1999之间时取款800
当银行卡转入低于1000时不取款直接结束取款
取款结束后显示输出余额
"""
moneyIn = int(input("插入银行卡，查询银行卡转入的金额："))
if moneyIn>10000:
    moneyOut = 8000
    moneyLeft = moneyIn-moneyOut
    print("取款后银行卡余额为",moneyLeft)
elif 6000<=moneyIn<=10000:
    moneyOut = 6000
    moneyLeft = moneyIn-moneyOut
    print("取款后银行卡余额为", moneyLeft)
elif 2000<=moneyIn<6000:
    moneyOut = 1500
    moneyLeft = moneyIn-moneyOut
    print("取款后银行卡余额为", moneyLeft)
elif 1000<=moneyIn<2000:
    moneyOut = 800
    moneyLeft = moneyIn - moneyOut
    print("取款后银行卡余额为", moneyLeft)
else:
    print("直接退出取款")
    moneyLeft = moneyIn
    print("取款后银行卡余额为", moneyLeft)
print("结束取款")
