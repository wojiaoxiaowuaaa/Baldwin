# 实现一个函数让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，如字符串'1982376455',变成'1355798642'
# def func(s):
#     l = [int(i) for i in s]
#     l.sort(reverse=True)
#     # print(l)
#     for i in range(len(l)):
#         if l[i] % 2 > 0:
#             l.insert(0, l.pop(i))
#     return ''.join(str(s) for s in l)  # join()是字符串的一个常见方法,用于将序列(例如列表/元组/字符串)中的元素连接成一个新的字符串
#
#
# s = '1982376455'
# print(func(s))


def sort_str(s):
    # 将字符串转换为列表  map函数将可迭代对象s中的每个元素依次作用在int函数上并返回一个可迭代对象
    l = list(map(int, s))
    # 对奇偶数进行分类
    two = [j for j in l if j % 2 == 0]
    one = [k for k in l if k % 2 != 0]
    # 排序
    one.sort()
    two.sort(reverse=True)
    # 合并后返回
    return "".join(map(str, one + two))


s = '1982376455'
print(sort_str(s))
