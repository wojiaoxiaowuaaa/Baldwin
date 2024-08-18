import random
import time

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
#
# arr = [3, 6, 8, 10, 1, 2, 1]
# print(quick_sort(arr))


def quick_sort(arr):
    # 增加异常处理以确保传入的是列表并且列表中至少有一个元素
    # if not isinstance(arr, list) or len(arr) == 0:
    #     return []
    # 递归基：数组长度小于等于1时，直接返回
    if len(arr) <= 1:
        return arr

    # 选择基准元素：这里使用数组中间位置的元素
    pivot = arr[len(arr) // 2]

    # 三向切分：通过一次遍历，将数组分成小于、等于和大于基准元素的三个部分(不断地缩小问题规模)
    less, equal, greater = [], [], []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    # 递归地对小于和大于基准的部分进行排序，然后连接三个部分
    return quick_sort(less) + equal + quick_sort(greater)


arr = [3, 6, 8, 10, 1, 2, 1, 11, 5, 7, 7, 9, 0, 4, 4, 4, 4]
# print(quick_sort(arr))


# 冒泡排序 统计耗时
# def calculate_execution_time(func):
#     def wrapper_er(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         execution_time = end_time - start_time
#         print(f"函数 {func.__name__} 的执行时间为: {execution_time} 秒")
#         return result

#     return wrapper_er


# @calculate_execution_time
def func(l):
    for i in range(len(l)):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


# 生成长度为k的随机列表(从指定序列中随机抽取k个不重复的元素并以列表形式返回这些元素)
l = random.sample(range(10), 10)
# print(func(l))

