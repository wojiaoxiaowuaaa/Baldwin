from cachetools import cached
import time


def fib(n):
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
