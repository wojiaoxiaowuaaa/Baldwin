def func(ll, tar):
    """给定一个整数数组和一个目标值，找出数组中和为目标值的两个数并返回下标"""
    hashmap = {}

    # enumerate() 是 Python 内置函数之一，它用于将一个可迭代对象（如列表、元组、字符串等）组合为一个枚举对象，可以同时获取索引和对应的元素值。
    for index, value in enumerate(ll):
        hashmap[value] = index

    for k, v in enumerate(ll):
        # 对于列表中的每个元素 v，查找是否存在另一个数 tar - v
        j = hashmap.get(tar - v)

        # 在字典 hashmap 中。如果存在&&下标不与当前元素的下标相同，说明找到了符合条件的两个数，即它们的和等于目标值 target。
        if j is not None and j != k:
            return k, j


ll = [1, 3, 7, 11, 12]
target = 12


# print(func(l, target))


def two_sum(l: list, tar: int) -> list:
    #  这个函数的时间复杂度是O(n)，因为它只遍历一次列表。空间复杂度也是O(n)，因为在最坏的情况下，字典需要存储列表中的所有元素。
    hashmap = {}

    for i, num in enumerate(l):
        # 计算目标值与当前元素的差值var
        var = tar - num
        # 检查var是否已经在字典hashmap中。如果在，说明我们已经找到了一个数与当前数相加等于目标值的组合，返回这两个数的索引`hashmap[var]`和`i`
        if var in hashmap:
            return [hashmap[var], i]
        #  如果var不在字典中，将当前元素的值和它的索引存入字典，以便后续查找。遍历结束后，如果没有找到满足条件的数对，则返回空列表。
        hashmap[num] = i

    return []


# print(two_sum(l, target))


# 找列表中指定元素的下标
def find_all_indices(lst, element):
    """如果你希望查找所有出现的下标，可以使用列表推导式.整个列表推导式的作用是：遍历列表中的每个元素，检查它是否等于我们要查找的元素，如果是，则将该元素的下标添加到新列表中。"""
    res = [index for index, value in enumerate(lst) if value == element]
    return res if res else "Not found"


def find_index(lst, element):
    """可以使用 list.index() 方法来查找列表中指定元素的下标。如果元素不在列表中，它会引发 ValueError 异常。"""
    try:
        return lst.index(element)
    except ValueError:
        return "Not found"


# my_list = [10, 20, 30, 40, 30, 50]
# element_to_find = 30

# print(find_all_indices(my_list, element_to_find))
# print(find_index(my_list, element_to_find))


def fib(n):
    # 生成器生成斐波那契数列
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


for i in fib(10):
    print(i, end=" ")
