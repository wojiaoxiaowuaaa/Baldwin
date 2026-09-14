text = "  , !Hello & , ) World! _ + = 1  , "
# 去除开头和结尾的空格. strip()方法移除字符串开头和结尾的指定字符（默认是空白字符、空格、换行符、制表符等).
text = text.strip()
# 处理掉所有的特殊字符
tar = "".join(char for char in text if char.isalpha() or char.isspace())
# 去除所有的空格
str = text.replace(" ", "")
# 去除开头和结尾的逗号
# str = text.strip(",")