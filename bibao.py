count = 0
print('开始执行前的全局count:', count)


def func(count):
    def inner(x):
        nonlocal count  # 声明一个变量是非局部(non-local)的,使得在函数内部能够访问并修改上一层（但不是全局层）的变量。
        count += x
        print('闭包内的count ---', count)

    return inner


res = func(count)
res(3)
res(3)
res(3)
print('执行结束后的全局count', count)
