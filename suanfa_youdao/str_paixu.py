# 实现一个函数让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'
def func(s):
    l = [int(i) for i in s]
    l.sort(reverse=True)
    print(l)
    for i in range(len(l)):
        if l[i] % 2 > 0:
            l.insert(0, l.pop(i))
    return ''.join(str(s) for s in l)  # join() 方法是字符串的一个常见方法，用于将序列（例如列表、元组、字符串）中的元素连接成一个新的字符串


s = '1982376455'
print(func(s))
