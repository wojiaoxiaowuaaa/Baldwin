# import random
# from log_util import logger

def func(ll, tar):
    """给定一个整数数组和一个目标值,找出数组中和为目标值的两个数并返回下标"""
    hashmap = {}
    # enumerate() 是 Python 内置函数之一,它用于将一个可迭代对象(如列表、元组、字符串等)组合为一个枚举对象,可以同时获取索引和对应的元素值.
    for index, value in enumerate(ll):
        hashmap[value] = index
    for k, v in enumerate(ll):
        # 对于列表中的每个元素 v,查找是否存在另一个数 tar - v
        j = hashmap.get(tar - v)
        # 在字典 hashmap 中.如果存在&&下标不与当前元素的下标相同,说明找到了符合条件的两个数,即它们的和等于目标值 target.
        if j is not None and j != k:
            return k, j


# ll = [1, 3, 7, 11, 12]
# target = 12
# print(func(ll, target))


def two_sum(l: list, tar: int) -> list:
    #  这个函数的时间复杂度是O(n),因为它只遍历一次列表.空间复杂度也是O(n),因为在最坏的情况下,字典需要存储列表中的所有元素.
    hashmap = {}
    result = []  # 用于存储所有满足条件的索引对
    for i, num in enumerate(l):
        hashmap[num] = i
        # 计算目标值与当前元素的差值var
        var = tar - num
        # 检查var是否已经在字典hashmap中.如果在,说明我们已经找到了一个数与当前数相加等于目标值的组合,将这两个数的索引`hashmap[var][和](file://abc_test.py#6#85)i`加入结果列表
        if var in hashmap:
            result.append((hashmap[var], i))
        #  如果var不在字典中,将当前元素的值和它的索引存入字典,以便后续查找.
        # hashmap[num] = i
    # 遍历结束后,返回所有满足条件的数对
    return result


res = two_sum([2, 7, 10, 15, 5, 12], 17)
print(res)


def find_all_indices(lst, element):
    """找列表中指定元素的下标.遍历列表中的每个元素,检查它是否等于我们要查找的元素,如果是,则将该元素的下标添加到列表中"""
    res = [index for index, value in enumerate(lst) if value == element]
    return res if res else "Not found"


def find_index(lst, element):
    """可以使用 list.index() 方法来查找列表中指定元素的下标.如果元素不在列表中,它会引发 ValueError 异常."""
    try:
        return lst.index(element)
    except ValueError:
        return "Not found"


# print(find_all_indices([1, 2, 3, 4, 5], 1111))


def fib(n):
    # 生成器生成斐波那契数列
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


# for i in fib(10): print(i, end=" ")

def func_di(numbs):
    """
    递归三原则
    (1)递归算法必须有基本情况;(算法停止递归的条件)
    (2)递归算法必须改变其状态并向基本情况靠近;
    (3)递归算法必须递归地调用自己.
    """
    if len(numbs) == 1:
        return numbs[0]
    return numbs[0] + func_di(numbs[1:])


# print(func_di([1, 2, 3, 4]))

def func_sum(x):
    """递归的特性:
    1.必须有一个明确的结束条件;
    2.每次进入更深一层递归时,问题规模相比上次递归都应有所减少
    3.相邻两次重复之间有紧密的联系,前一次要为后一次做准备(通常前一次的输出就作为后一次的输入).
    4.递归效率不高,递归层次过多会导致栈溢出(在计算机中,函数调用是通过栈(stack)这种数据结构实现的,每当进入一个函数调用,栈就会加一层栈帧,每当函数返回,栈就会减一层栈帧.由于栈的大小不是无限的,所以,递归调用的次数过多,会导致栈溢出)
    5.递归的终止条件一般定义在递归函数内部, 在递归调用前要做一个条件判断, 根据判断的结果选择是继续调用自身, 还是return, 返回终止递归;"""
    if x > 0:
        return x + func_di(x - 1)
    else:
        return 0


# print(func_sum(100))

# def recursive_function():
# return recursive_function()  # 无限递归
# try:
#     recursive_function()
# except RecursionError as e:
#     print("RecursionError:", e)  # RecursionError: maximum recursion depth exceeded


# def quick_sort(arr):  # 快速排序
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
# arr = [3, 6, 8, 10, 1, 2, 1]
# print(quick_sort(arr))

def quick_sort(arr):
    # 增加异常处理以确保传入的是列表并且列表中至少有一个元素
    # if not isinstance(arr, list) or len(arr) == 0:
    #     return []
    # 递归基:数组长度小于等于1时,直接返回
    if len(arr) <= 1:
        return arr
    # 选择基准元素:这里使用数组中间位置的元素
    pivot = arr[len(arr) // 2]
    # 三向切分:通过一次遍历,将数组分成小于、等于和大于基准元素的三个部分(不断地缩小问题规模)
    less, equal, greater = [], [], []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    # 递归地对小于和大于基准的部分进行排序,然后连接三个部分
    return quick_sort(less) + equal + quick_sort(greater)

# arr = [3, 6, 8, 10, 1, 2, 1, 11, 5, 7, 7, 9, 0, 4, 4, 4, 4]
# print(quick_sort(arr))

# def mao(l):
#     for i in range(len(l)):
#         for j in range(len(l) - 1 - i):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     return l

# 生成长度为k的随机列表(从指定序列中随机抽取k个不重复的元素并以列表形式返回这些元素)
# l = random.sample(range(10), 10)
# print(mao(l))
