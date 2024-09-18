from memory_profiler import profile, memory_usage
import psutil
import os

print(psutil.Process(os.getpid()).memory_info().rss/1024**2)

print(memory_usage()[0])

@profile
def my_func():
    a = 1
    b = 2
    return a + b

if __name__ == "__main__":
    my_func()



