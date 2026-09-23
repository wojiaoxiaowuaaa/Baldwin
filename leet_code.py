from typing import Optional, Tuple

def two_sum(arr: list[int], target: int) -> Optional[Tuple[int, int]]:
    """两数之和"""
    hashmap = {}
    for index, value in enumerate(arr):
        if target - value in hashmap:
            return hashmap[target - value], index
        hashmap[value] = index
    return None

def quick_sort(arr):
    """快排"""
    if len(arr) <= 1: return arr
    p = arr[len(arr) // 2]
    left = [i for i in arr if i < p]
    middle = [i for i in arr if i == p]
    right = [i for i in arr if i > p]
    return quick_sort(left) + middle + quick_sort(right)

def max_number_substring(s: str) -> str:  # 寻找字符串中的最大连续数字子串
    max_str = ""
    cur = ""
    for ch in s + "\0":          # 末尾加一个非数字哨兵
        if ch.isdigit():
            cur += ch
        elif cur:                # 只有一段真正结束时才结算
            if not max_str or int(cur) > int(max_str):
                max_str = cur
            cur = ""
    return max_str

def removeDuplicates(nums):
    """一个非严格递增排列的数组 nums 请你原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。元素的相对顺序保持一致。示例：nums = [1, 1, 2, 2, 3, 5]
    去重后唯一元素：[1,2,3,5]返回 k=4"""
    if not nums: return 0
    k = 1  # 下一个不重复元素要存放的位置下标，同时也代表目前已经找到的不重复元素总个数
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k
    
def func_max_diff(arr: list[int]) -> int:
    """查找数组中后一个数减前一个数的最大差值。股票买卖问题"""
    if not arr: return 0
    min_num = arr[0]
    max_diff = 0
    for num in arr[1:]:
        min_num = min(min_num, num)
        max_diff = max(max_diff, num - min_num)
    return max_diff

def move_zero(arr):
    """给定一个数组 nums,编写一个函数将所有 0 移动到数组的末尾,同时保持非零元素的相对顺序"""
    arr[:] = [i for i in arr if i] + [0] * arr.count(0)

def find_all_indices(lst, element):
    """找列表中指定元素的下标"""
    res = [index for index, value in enumerate(lst) if value == element]
    return res if res else "Not found"
    # 👉这这种写法只会返回目标元素第一次出现时的下标,有多个符合条件的元素时不适用 return lst.index(element) if element in lst else "Not Found"

def fib(n):
    # 生成器生成斐波那契数列  for i in fib(10): print(i, end=" ")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def count_characters(file_path):
    """统计文本中字符的出现次数 排序后展示最高频的前十个. 初始化一个空字典hashmap来存储字符及其出现次数"""
    hashmap = {}
    try:
        with open(file_path) as f:
            for char in f.read():
                if char.isspace():  # 跳过空格和换行符
                    continue
                if char in hashmap:
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到")
        return
    except PermissionError:
        print(f"没有权限读取文件 {file_path}.")
        return
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return

    hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    res = hashmap[:10]
    return dict(res)

def reverse_int(x):
    """反转一个int类型 方法一&方法二"""
    return int("".join([i for i in str(x)][::-1]))


# def reverse_integer(number):
#     arr = list(str(number))  # 将str转换为list(注:int类型不可以直接转为list会报错TypeError: 'int' object is not iterable)
#     # l.reverse()
#     # return ''.join(l)
#     result = ""
#     while len(arr) > 0:
#         result += arr.pop()  # 出栈
#     return int(result)


# def filter_numbers(l):  # noqa: E741
#     """处理输入的列表  要求返回的新列表中的每个元素都是偶数&&该元素在原list中的下标也是偶数"""
#     return [number for index, number in enumerate(l) if index % 2 == 0 and number % 2 == 0]
#     # return [i for i in l if i % 2 == 0 and l.index(i) % 2 == 0]


# def is_hui(num):
#     """判断一个整数是否是回文数 转换成str后使用反向切片判断"""
#     return str(num) == str(num)[::-1]

# def quick_sort(arr):
#     # 增加异常处理以确保传入的是列表并且列表中至少有一个元素
#     # if not isinstance(arr, list) or len(arr) == 0:
#     #     return []
#     # 递归基:数组长度小于等于1时,直接返回
#     if len(arr) <= 1:
#         return arr
#     # 选择基准元素:这里使用数组中间位置的元素
#     pivot = arr[len(arr) // 2]
#     # 三向切分:通过一次遍历,将数组分成小于、等于和大于基准元素的三个部分(不断地缩小问题规模)
#     less, equal, greater = [], [], []
#     for x in arr:
#         if x < pivot:
#             less.append(x)
#         elif x == pivot:
#             equal.append(x)
#         else:
#             greater.append(x)
#     # 递归地对小于和大于基准的部分进行排序,然后连接三个部分
#     return quick_sort(less) + equal + quick_sort(greater)


# def func_di(numbs):
#     """
#     递归三原则
#     (1)递归算法必须有基本情况;(算法停止递归的条件)
#     (2)递归算法必须改变其状态并向基本情况靠近;
#     (3)递归算法必须递归地调用自己.
#     """
#     if len(numbs) == 1:
#         return numbs[0]
#     return numbs[0] + func_di(numbs[1:])

# def mao(l):
#     for i in range(len(l)):
#         for j in range(len(l) - 1 - i):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     return l

