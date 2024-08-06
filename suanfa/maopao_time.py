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


l = random.sample(
    range(1000), 1000
)  # 生成长度为k的随机列表  k必须为小于或等于1000的值(与range的参数有关)
func(l)
