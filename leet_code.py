# import random
# from log_util import logger

def move_zero(arr):
    """双指针.给定一个数组 nums,编写一个函数将所有 0 移动到数组的末尾,同时保持非零元素的相对顺序."""
    if not arr: return 0  # noqa: E701

    j = 0  # 第一次遍历的时候,j指针记录非0的个数,只要是非0的统统都赋给nums[j]

    for i in range(len(arr)):
        if arr[i]:
            arr[j] = arr[i]
            j += 1

    for z in range(j, len(arr)):  # 非0元素统计完了,剩下的都是0了所以第二次遍历把末尾的元素都赋为0即可
        arr[z] = 0

    return arr


def max_len(arr):
    """找到一个整数数组中最长连续递增序列的长度"""
    if not arr:
        return 0  # 空数组返回0

    arr.sort()

    res_len = 1  # 用于记录最长连续序列的长度,初始值为1因为至少有一个元素时序列长度为1
    cur_len = 1  # 用于记录当前连续序列的长度
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            cur_len += 1
            res_len = max(res_len, cur_len)
        elif arr[i] == arr[i - 1]:
            pass
        else:
            cur_len = 1  # 序列中断 重置当前连续序列的长度为1
    return res_len


def find_max(s):
    """找出字符串中的最大数字子串"""
    current = 0
    max_num = 0

    for char in s:
        if char.isdigit():  # 判断字符是否为数字
            current = current * 10 + int(char)
            if current > max_num:
                max_num = current
        else:
            current = 0

    return max_num


def func_index(arr, target):
    """两数之和对应下标"""
    hashmap = {}

    for index, value in enumerate(arr):
        hashmap[value] = index

        if target - value in hashmap:
            j = hashmap.get(target - value)

            if j != index and j is not None:
                return j, index


# def func(ll, tar):
#     """给定一个整数数组和一个目标值,找出数组中和为目标值的两个数并返回下标"""
#     hashmap = {}
#     # enumerate() 是 Python 内置函数之一,它用于将一个可迭代对象(如列表、元组、字符串等)组合为一个枚举对象,可以同时获取索引和对应的元素值.
#     for index, value in enumerate(ll):
#         hashmap[value] = index
#     for k, v in enumerate(ll):
#         # 对于列表中的每个元素 v,查找是否存在另一个数 tar - v
#         j = hashmap.get(tar - v)
#         # 在字典 hashmap 中.如果存在&&下标不与当前元素的下标相同,说明找到了符合条件的两个数,即它们的和等于目标值 target.
#         if j is not None and j != k:
#             return k, j

# def func(arr, target):
#     """求两数之和的下标"""
#     for i in arr:
#         for j in arr:
#             if i + j == target:
#                 return arr.index(i), arr.index(j)


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
