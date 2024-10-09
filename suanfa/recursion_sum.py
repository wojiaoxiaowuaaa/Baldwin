import random
import time


def func(numbs):
    """
    递归三原则
    (1)递归算法必须有基本情况；(算法停止递归的条件)
    (2)递归算法必须改变其状态并向基本情况靠近；
    (3)递归算法必须递归地调用自己。
    """
    if len(numbs) == 1:
        return numbs[0]
    return numbs[0] + func(numbs[1:])


# print(func([1, 2, 3, 4]))


def func_sum(x):
    """递归的特性:
    1.必须有一个明确的结束条件；
    2.每次进入更深一层递归时，问题规模相比上次递归都应有所减少
    3.相邻两次重复之间有紧密的联系，前一次要为后一次做准备（通常前一次的输出就作为后一次的输入）。
    4.递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）
    5.递归的终止条件一般定义在递归函数内部, 在递归调用前要做一个条件判断, 根据判断的结果选择是继续调用自身, 还是return, 返回终止递归;"""
    if x > 0:
        return x + func(x - 1)
    else:
        return 0


# print(func_sum(100))



def recursive_function():
    return recursive_function()  # 无限递归

try:
    recursive_function()
except RecursionError as e:
    print("RecursionError:", e)  # RecursionError: maximum recursion depth exceeded


# def quick_sort(arr):  # 快速排序
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


# arr = [3, 6, 8, 10, 1, 2, 1, 11, 5, 7, 7, 9, 0, 4, 4, 4, 4]
# print(quick_sort(arr))

def func(l):
    for i in range(len(l)):
        for j in range(len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


# 生成长度为k的随机列表(从指定序列中随机抽取k个不重复的元素并以列表形式返回这些元素)
# l = random.sample(range(10), 10)
# print(func(l))

