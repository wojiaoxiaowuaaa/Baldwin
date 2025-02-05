def count_characters(file_path):
    """统计文本中字符的出现次数 排序后展示最高频的前十个. 初始化一个空字典hashmap来存储字符及其出现次数"""
    hashmap = {}
    try:
        with open(file_path, "r") as f:
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


def count_file(pwd):
    """统计文件中小写字母的数量"""
    count = 0

    with open(pwd, "r") as f:
        data = f.read()
        for _ in data:
            if _.islower():  # 统计大写用 isupper
                count += 1
    return count

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
input_string = "统计字符示例字符串,aabbcc 111"


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


# print(reverse_integer(1234))
# print(reverse_int(1234))


def filter_numbers(l):
    """处理输入的列表  要求返回的新列表中的每个元素都是偶数&&该元素在原list中的下标也是偶数"""
    # return [number for index, number in enumerate(l) if index % 2 == 0 and number % 2 ==0]
    return [i for i in l if i % 2 == 0 and l.index(i) % 2 == 0]


# print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def is_prime(n):
    """判断素数的函数"""
    if n > 1:
        from math import sqrt
        for factor in range(2, int(sqrt(n)) + 1):
            if n % factor == 0:
                return False
        return True if n != 1 else False
    return False


def file_write():
    """
    1. if 语句:用于判断一个条件是否为真.如果条件为真,则执行 if 代码块中的语句.
    2. elif 语句:是"else if"的缩写,用于在前面的 if 或 elif 条件不满足时,检查另一个条件.如果 elif 条件为真,则执行 elif 代码块中的语句.
    3. else 语句:用于在所有前面的 if 和 elif 条件都不满足时执行代码块"""
    filenames = (
        "../config/log/aaa.txt",
        "../config/log/aaab.txt",
        "../config/log/aaac.txt",
    )
    l = []
    try:
        for file in filenames:
            l.append(open(file, "w"))
        for num in range(1, 200):
            if is_prime(num):
                if num <= 10:
                    l[0].write(str(num) + "\n")
                elif num <= 100:
                    l[1].write(str(num) + "\n")
                else:
                    l[2].write(str(num) + "\n")
    except IOError as e:
        print(e)
    finally:
        for f in l:
            f.close()


def is_valid(s: str) -> bool:
    """检查字符串是否表示一个有效的括号序列.有效括号序列是指由左括号("(", "{", "[")和相应的右括号(")", "}", "]")组成,且左括号和右括号成对出现,没有多余的括号"""

    stack = []  # 1. 初始化一个空栈`stack`,用于存储遇到的左括号.

    mapping = {")": "(",  "}": "{", "]": "["}  # 2. (字典的key均为右括号)创建一个映射字典,它将每个右括号映射到其对应的左括号.

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


# print(is_hui(12321))
# print(count_characters(__file__))
# print(is_valid("()[]{}"))


# from log_util import logger
# dict_set = set(logger.__dict__.keys())
# dir_set = set(dir(logger))

# # 计算交集
# # intersection = dict_set.intersection(dir_set)
# intersection = dict_set & dir_set


# # 计算并集
# union = dict_set.union(dir_set)

# # 打印结果
# logger.critical("交集:")
# for item in sorted(intersection): logger.critical(item)

# logger.critical("并集:")
# for item in sorted(union): logger.critical(item)

# # 额外信息:只在 dir() 中出现的项
# only_in_dir = dir_set - dict_set
# logger.critical("\n只在 dir() 中出现的项:")
# for item in sorted(only_in_dir): logger.critical(item)

# # 额外信息:只在 __dict__ 中出现的项
# only_in_dict = dict_set - dir_set
# logger.critical("\n只在 __dict__ 中出现的项:")
# for item in sorted(only_in_dict): logger.critical(item)