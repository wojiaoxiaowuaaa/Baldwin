def jihe():
    """求a, b两个列表的交集"""
    a = [1, 2, 3, 4, 5, 7]
    b = [3, 4, 5, 6, 7, 0]
    # 使用集合求交集.在 Python 中 & 运算符用于对集合(set)进行交集操作.交集操作会返回两个集合中都包含的元素.
    # 集合(set)是一种无序且不重复的元素集合.集合支持多种数学集合操作,比如并集、交集、差集等.
    # print(list(set(a) - set(b))) 求差集.
    # print(list(set(a) | set(b))) 求并集.
    intersection = list(set(a) & set(b))  # 求交集
    print(intersection)

    # 使用列表推导式
    tar = [i for i in a if i in b]
    print(tar)

    # 使用内置函数
    res = list(filter(lambda x: x in b, a))
    print(res)


def func(pwd):
    """生成器读取文件"""
    block_size = 1024

    with open(pwd, "r") as f:
        while True:
            data = f.read(block_size)
            if data:
                yield data

            # 使用return的效果:
            # 1. 立即终止函数: 当 return 被执行时,函数 func 会立即终止,并且不会再继续执行循环或任何其他代码. 2.停止迭代: 由于 return 会立即退出函数,yield 的生成器也会终止.
            # 使用break的效果:
            # 1. 退出当前循环: 当 break 被执行时,它只会退出当前的 while 循环,而不是整个函数. 2. 继续执行后续代码: 在 break 之后,函数中的其他代码(如果有)仍然会继续执行. 3.完整读取文件: 由于 break 只退出循环,生成器会继续读取文件的所有数据块,直到文件结束
            return


# for i in func('jiaoji.py'): print(i)
