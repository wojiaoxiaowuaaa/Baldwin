# 生成器生成斐波那契数列
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


for i in fib(10):
    print(i, end=" ")
