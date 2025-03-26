def move_zero(arr):
    """给定一个数组 nums,编写一个函数将所有 0 移动到数组的末尾,同时保持非零元素的相对顺序.推导式"""
    # return [i for i in arr if i] + [0]*arr.count(0)
    arr[:] = [i for i in arr if i] + [0] * arr.count(0)


# def move_zero01(arr):
#     """给定一个数组 nums,编写一个函数将所有 0 移动到数组的末尾,同时保持非零元素的相对顺序.双指针."""
#     if not arr: return arr  # noqa: E701
#
#     j = 0  # 第一次遍历的时候,j指针记录非0的个数,只要是非0的统统都赋给nums[j]
#
#     for i in range(len(arr)):
#         if arr[i]:
#             arr[j] = arr[i]
#             j += 1
#
#     for z in range(j, len(arr)):  # 非0元素统计完了,剩下的都是0了所以第二次遍历把末尾的元素都赋为0即可
#         arr[z] = 0
#
#     return arr


# def move_zero02(arr):
#     if not arr: return arr  # noqa: E701
#
#     j = 0  # 指向下一个非0元素应该放置的位置
#
#     for i in range(len(arr)):  # [1, 3, 0, 8, 0, 1]
#         if arr[i]:
#             # print(i)  0 1 3 5
#             # print(j)  0 1 2 3
#             arr[j], arr[i] = arr[i], arr[j]
#             j += 1
#
#     return arr  # [1, 3, 8, 1, 0, 0]


def max_len(arr):
    """找到一个整数数组中最长连续递增序列的长度"""
    if not arr: return 0  # 空数组返回0  # noqa: E701

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


def find_max(s: str):
    """找出字符串中的最大数字子串"""
    cur_num = 0  # 存储当前正在处理的数字
    max_num = 0  # 存储最大的数字

    for char in s:
        if char.isdigit():
            cur_num = cur_num * 10 + int(char)
            max_num = max(cur_num, max_num)
        else:
            cur_num = 0

    return max_num


def two_sum(arr, target):
    """两数只和下标"""
    hashmap = {}

    for index, value in enumerate(arr):
        if target - value in hashmap:
            return hashmap[target - value], index  # 可以在找到结果时立即返回 不需要继续循环
        hashmap[value] = index
    return None


# def func_index(arr, target):
#     hashmap = {}
#
#     for index, value in enumerate(arr):
#         hashmap[value] = index
#
#         if target - value in hashmap:
#             j = hashmap.get(target - value)
#
#             if j != index:
#                 return j, index


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
    return dict(hashmap)


# def count_file(pwd):
#     """统计文件中小写字母的数量"""
#     count = 0
#
#     with open(pwd) as f:
#         data = f.read()
#         for _ in data:
#             if _.islower():  # 统计大写用 isupper
#                 count += 1
#     return count


def count_letters(s):
    """统计字符串中字母出现的次数"""
    letter_dict = {}
    for char in s:
        if char.isalpha():  # 判断字符是否为字母(中文+英文)
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    return letter_dict


# 示例字符串
# input_string = "统计字符示例字符串,aabbcc 111"


# 调用函数
# result = count_letters(input_string)
# 输出结果
# for letter, count in result.items():
#     print(f"'{letter}': {count}")
# print(result)


def reverse_int(x):
    """反转一个int类型 方法一&方法二"""
    s = [i for i in str(x)][::-1]  # 列表反向切片
    return int("".join(s))


def reverse_integer(number):
    arr = list(str(number))  # 将str转换为list(注:int类型不可以直接转为list会报错TypeError: 'int' object is not iterable)
    # l.reverse()
    # return ''.join(l)
    result = ""
    while len(arr) > 0:
        result += arr.pop()  # 出栈
    return int(result)


def filter_numbers(l):
    """处理输入的列表  要求返回的新列表中的每个元素都是偶数&&该元素在原list中的下标也是偶数"""
    # return [number for index, number in enumerate(l) if index % 2 == 0 and number % 2 ==0]
    return [i for i in l if i % 2 == 0 and l.index(i) % 2 == 0]


# print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# def is_prime(n):
#     """判断素数的函数"""
#     if n > 1:
#         from math import sqrt
#         for factor in range(2, int(sqrt(n)) + 1):
#             if n % factor == 0:
#                 return False
#         return True if n != 1 else False
#     return False


# def file_write():
#     """
#     1. if 语句:用于判断一个条件是否为真.如果条件为真,则执行 if 代码块中的语句.
#     2. elif 语句:是"else if"的缩写,用于在前面的 if 或 elif 条件不满足时,检查另一个条件.如果 elif 条件为真,则执行 elif 代码块中的语句.
#     3. else 语句:用于在所有前面的 if 和 elif 条件都不满足时执行代码块"""
#     filenames = (
#         "../config/log/aaa.txt",
#         "../config/log/aaab.txt",
#         "../config/log/aaac.txt",
#     )
#     l = []
#     try:
#         for file in filenames:
#             l.append(open(file, "w"))
#         for num in range(1, 200):
#             if is_prime(num):
#                 if num <= 10:
#                     l[0].write(str(num) + "\n")
#                 elif num <= 100:
#                     l[1].write(str(num) + "\n")
#                 else:
#                     l[2].write(str(num) + "\n")
#     except IOError as e:
#         print(e)
#     finally:
#         for f in l:
#             f.close()


def is_valid(s: str) -> bool:
    """检查字符串是否表示一个有效的括号序列.有效括号序列是指由左括号("(", "{", "[")和相应的右括号(")", "}", "]")组成,且左括号和右括号成对出现,没有多余的括号"""

    stack = []  # 1. 初始化一个空栈`stack`,用于存储遇到的左括号.

    mapping = {")": "(", "}": "{", "]": "["}  # 2. (字典的key均为右括号)创建一个映射字典,它将每个右括号映射到其对应的左括号.

    for char in s:  # 3. 遍历输入字符串`s`中的每个字符`char`:如果`char`是一个右括号(即在`mapping`字典的键中),检查栈顶元素(如果栈不为空则弹出,否则假设为'-') 如果栈顶元素不是与当前右括号匹配的左括号,返回`False`,因为这意味着括号不匹配.否则,`char`是一个左括号,将其压入栈中.
        if char in mapping:
            top_element = stack.pop() if stack else "-"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack  # 遍历结束后,如果栈为空,说明所有左括号都有对应的右括号,返回`True`;否则返回`False`,因为存在未闭合的左括号.


def is_hui(num):
    """判断一个整数是否是回文数 转换成str后使用反向切片判断"""
    return str(num) == str(num)[::-1]
