import random
import time


# 冒泡排序 统计耗时
def calculate_execution_time(func):
    def wrapper_er(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 的执行时间为: {execution_time} 秒")
        return result

    return wrapper_er


@calculate_execution_time
def func(l):
    for i in range(len(l)):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


# 生成长度为k的随机列表(从指定序列中随机抽取k个不重复的元素并以列表形式返回这些元素)
l = random.sample(range(10), 10)
print(func(l))
