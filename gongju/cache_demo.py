from cachetools import cached


@cached(cache={})
def fibonacci(n):
    if n < 2:
        return n
    print('执行了低递归算法')
    return fibonacci(n - 1) + fibonacci(n - 2)


# 第一次调用fibonacci(5)，它会执行实际的逻辑并缓存结果
result = fibonacci(5)
print(result)

# 第二次调用 fibonacci(5)，它会直接从缓存中拿结果(未打印执行了低递归算法相关的print语句)
result = fibonacci(5)
print(result)
