# 分支结构if语句-条件表达式
# 根据银行卡余额转帐给不同的人，如果金额大于100000，转账给A,否则转账给B
moneyIn=int(input("查询银行卡余额："))
print("转账给A" if moneyIn>100000 else "转账给B")
