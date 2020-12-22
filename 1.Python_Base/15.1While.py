# while循环
"""
银行卡取款，查询显示当前余额,当银行卡余额超过20万时取款
因ATM每次取款限额1万，每次取1万
计算取款的总数，当取款达到6万时停止取款,输出取款结束时的余额和总取款数
"""
moneyLeft=int(input("查询到余额为："))
moneyOutTotal=0
while moneyLeft>200000 and moneyOutTotal<=50000:
    moneyOut=10000
    moneyOutTotal=moneyOutTotal+moneyOut
    moneyLeft=moneyLeft-moneyOut
    print("当前的余额为：",moneyLeft,"\n当前的取款总数为：",moneyOutTotal)
else:
    print("结束取款")
