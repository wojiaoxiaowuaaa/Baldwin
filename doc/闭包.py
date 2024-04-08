from loguru import logger

count = 0
logger.info(f'开始执行前的全局count:{count}')


def func(count):
    def inner(x):
        """声明一个变量是非局部(non-local)的,使得在函数内部能够访问并修改上一层（但不是全局层）的变量。
        nonlocal 是一个关键字，在嵌套函数中标识一个变量，告诉解释器这个变量不是局部变量，也不是全局变量，而是外部（封闭）函数中的变量。
        nonlocal 关键字的使用场景通常是在闭包中，即在一个函数内部定义了另一个函数。
        使用 nonlocal 关键字有助于在闭包中正确引用外部函数的变量，而不会创建新的局部变量。
        """
        nonlocal count
        count += x
        logger.info(f'闭包内的count --- {count}')

    return inner


res = func(count)
res(3)
res(6)
logger.info(f'执行结束后的全局count: {count}')
