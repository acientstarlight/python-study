# 转义和原始字符

# 1.换行符
print("good\njob")
# 2.退格
print("good\bjod")
# 3.覆盖(后面的字符串覆盖前面的字符串)
print("good\rjob")
# 4.制表符(4位一数,补齐一个4位)
print("today\trainy")
# 5.转义字符对反斜杠/、单引号''和双引号""的处理（打印http:\\www.baidu.com）
print("http:\\\\www.baidu.com")
print("他说：\'明天来\'")
print('她说：\"好的\"')
# 6.原字符（使得字符串中包含了转义字符格式的字符不起作用）r或者R
print(r"good\njob")
# 但是如果字符串最尾部的字符为\则不能直接加r或者R来防止转义，如防转义good\njob\,需要将最后一个\转义
# print(R"good\njod\\"),因为最后的反斜杠转义了后面跟着的引号,要对转义进行反转义，然后删除最后一个反义字符
print(R"good\njod\\"[:-1])









