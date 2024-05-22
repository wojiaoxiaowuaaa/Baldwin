# 反转一个int类型 方法一&方法二:

def reverse_int(x):
    s = [i for i in str(x)][::-1]  # 列表反向切片
    return ''.join(s)


def reverse_integer(number):
    l = list(str(number))  # 将str转换为list(注:int类型不可以直接转为list会报错TypeError: 'int' object is not iterable)
    # l.reverse()
    # return ''.join(l)
    result = ""
    while len(l) > 0:
        result += l.pop()  # 出栈
    return int(result)


# print(reverse_integer(1234))
print(reverse_int(1234))
