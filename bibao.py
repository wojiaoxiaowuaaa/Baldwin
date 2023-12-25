count = 0
print('开始执行前的全局count:', count)


def func(count):
    def inner(x):
        nonlocal count
        count += x
        print('闭包内的count ---', count)
        # return count

    return inner


res = func(count)
res(3)
res(3)
res(3)
print('执行结束后的全局count', count)
