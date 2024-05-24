from cachetools import cached
import time


def fib(n):
    # 计算斐波那契数列的第N个数
    return n if n < 2 else fib(n - 1) + fib(n - 2)


s = time.time()
fib(36)
print("Time Taken:", time.time() - s)

# Now using cached
s = time.time()


# Use this decorator to enable caching
@cached(cache={})
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


fib(36)
print("with cached Time Taken: ", time.time() - s)

"""
from cachetools import cached


@cached(cache={})
def func(n):
    print('fun is running')
    if n <= 1:
        return 1
    return n * func(n - 1)


# 第一次调用，它会执行实际的逻辑并缓存结果
res = func(5)
print(res)

# 第二次调用，它会直接从缓存中拿结果(未打印执行了低递归算法相关的print语句)
res = func(5)
print(res)

"""