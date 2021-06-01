# 字符串的判断操作
# 判断字符串是否是合法的标识符（字母数字和下划线组成）
print("1","hello,world".isidentifier(),"张三abc123_".isidentifier())
# 判断字符串是否全部由空白字符组成（回车键、换行，水平制表符,换页符等转义字符）
print("2",'\t'.isspace(),"\r".isspace(),"\n".isspace(),"\f".isspace(),"\b".isspace(),"\\".isspace(),"a".isspace())
# 判断字符串是否全部由字母组成
print("3","张三".isalpha(),"张三123".isalpha(),"!张三".isalpha())
# 判断字符串是否全部由十进制数字组成
print("4","123".isdecimal(),"Ⅱ".isdecimal(),"123四".isdecimal())
# 判断字符串是否全部由数字组成
print("5","123".isnumeric(),"123四".isnumeric(),"Ⅱ".isnumeric(),"张".isnumeric(),"i_".isnumeric())
# 判断字符串是否全部由子母和数字组成
print("6","is123".isalnum(),"张123".isalnum(),"123abc!".isalnum())
