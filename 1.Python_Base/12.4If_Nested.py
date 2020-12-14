# 分支结构if语句-嵌套
# 根据银行卡余额取不同金额，如果是客户A转账进来的则取款，否则直接退出取款操作
"""
有余额为0的银行卡，客户转账进来一笔款项，这边收到后进行取款操作
当银行卡转入大于10000时取款8000
当银行卡转入在6000-10000之间时取款6000
当银行卡转入低于6000时不取款直接结束取款
取款结束后显示输出余额
"""
moneyIn=int(input("插入银行卡，查询银行卡转入的金额："))
moneyInPerson=input("插入银行卡，查到输出转账人姓名为：")
if moneyInPerson=="A":
    print("开始取款操作")
    if moneyIn>10000:
        moneyOut=8000
        moneyLeft = moneyIn - moneyOut
        print("取款：",moneyOut,"取款后的余额为：", moneyLeft)
    elif 6000<=moneyIn<=10000:
        moneyOut=6000
        moneyLeft = moneyIn-moneyOut
        print("取款：",moneyOut,"取款后的余额为：", moneyLeft)
    else:
        print("退出取款")
        moneyLeft=moneyIn
        print("不取款，取款后的余额为：",moneyLeft)
else:
    print("不可取款，直接结束取款")
