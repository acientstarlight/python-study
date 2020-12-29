# else语句
"""else语句-while循环
银行卡取款输入密码，输入正确密码即可取款
如果密码输入错误，提示密码错误
至多可输入密码三次，三次输错，提示退出
"""
a = 3
while a>0:
    password = int(input("请输入取款密码："))
    if password == 888888:
        print("密码正确")
        break
    else:
        print("密码输入不正确")
    a -= 1
else:
    print("密码错误三次，退出取款")
