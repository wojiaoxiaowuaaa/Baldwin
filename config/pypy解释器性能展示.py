import time

"""使用pypy版的Python解释器,下面的命令是该解释器的绝对路径:
/Users/wl/Documents/pypy3.10-v7.3.15-macos_x86_64/bin/pypy    /Users/wl/Desktop/Baldwin/config/pypy解释器性能展示.py

lrwxrwxrwx 1 wl staff 8   Jan 14 22:52  /Users/wl/Documents/pypy3.10-v7.3.15-macos_x86_64/bin/pypy -> pypy3.10
-rwxrwxrwx 1 wl staff 33K Jan 14 22:52  pypy3.10
"""
t = time.time()

for i in range(10**9):
    continue

print(
    time.time() - t
)  # 32.539549112319946/1.2057199478149414  cpython解释器与pypy解释器的性能差异
