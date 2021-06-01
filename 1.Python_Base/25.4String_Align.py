#  字符串对齐
#  字符串居中
str1 = "python"
print(str1.center(30))    # 如果设置的宽度大于字符串自身宽度就在左右两侧补齐宽度至设置值,第二个参数不设置默认为空格
print(str1.center(30,"爱"))
print(str1.center(6))     # 如果设置的宽度小于等于字符串自身宽度，则返回本身
#  字符串左对齐
print(str1.ljust(30))     # 如果设置的宽度大于字符串自身宽度就在右侧补齐宽度至设置值,第二个参数不设置默认为空格
print(str1.ljust(30,"爱"))
print(str1.ljust(6))      # 如果设置的宽度小于等于字符串自身宽度，则返回本身
#  字符串右对齐
print(str1.rjust(30))     # 如果设置的宽度大于字符串自身宽度就在左右两侧补齐宽度至设置值,第二个参数不设置默认为空格
print(str1.rjust(30,"爱"))
print(str1.rjust(6))      # 如果设置的宽度小于等于字符串自身宽度，则返回本身
#  字符串右对齐,左边用0填充
print(str1.zfill(20))     # 如果设置的宽度大于字符串自身宽度,就左侧用0补齐至宽度
print(str1.zfill(6))      # 如果设置的宽度小于等于字符串自身宽度，则返回本身
str2 = "-100"
str3 = "-100-100"
print(str2.zfill(6))      # 如果字符串“-”开头，则在开头那个“-”后补齐0至宽度
print(str3.zfill(20))



