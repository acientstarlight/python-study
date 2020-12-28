# break流程控制语句
"""for in循环
银行卡取款输入密码，输入正确密码即可取款
如果密码输入错误，提示密码错误
至多可输入密码三次，三次输错，直接退出
"""
for i in range(3):
    password=int(input("1-输入取款密码:"))
    if password==888888:
        print("密码正确")
        break
    else:
        print("密码错误")

a=0
while a<3:
    pwd=int(input("2-输入取款密码:"))
    if pwd == 888888:
        print("密码正确")
        break
    else:
        print("密码错误")
    a+=1
