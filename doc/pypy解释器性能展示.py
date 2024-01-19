import time

t = time.time()

for i in range(10 ** 9):
    continue

print(time.time() - t)  # 38.539549112319946/1.7057199478149414  cpython解释器与pypy解释器的性能差异


