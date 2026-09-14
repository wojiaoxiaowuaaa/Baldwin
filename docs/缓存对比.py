from cachetools import cached
from functools import lru_cache, cache
import time


@cached(cache={})
def func(n):
    print("fun is running")
    if n <= 1:
        return 1
    return n * func(n - 1)


# 第一次调用,它会执行实际的逻辑并缓存结果
res = func(5)
print(res)

# 第二次调用,它会直接从缓存中拿结果(未打印print语句)
res = func(5)
print(res, "___")


"""

from functools import lru_cache
import cProfile


# 当fibonacci函数被调用时,@lru_cache会缓存其参数和返回值.如果之后再次以相同的参数调用fibonacci函数,@lru_cache会直接从缓存中返回结果,而不是重新计算.
# 缓存的数据存储在进程的内存中.这意味着缓存只在当前进程的生命周期内有效,进程结束后,缓存中的数据也会随之丢失.
# 加了缓存装饰器后如果函数执行过 统计到的执行耗时是0(不加缓存会耗时几十秒)
@lru_cache(maxsize=100)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


cProfile.run('fib(40)')
print('-'*100)
cProfile.run('fib(40)')

"""
