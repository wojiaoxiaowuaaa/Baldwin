# 判断一个整数是否是回文数
# 转换成str后使用反向切片判断
def is_hui(num):
    return str(num) == str(num)[::-1]


print(is_hui(12321))
