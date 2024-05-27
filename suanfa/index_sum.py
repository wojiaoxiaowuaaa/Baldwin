

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


l = [1, 3, 7, 11, 12]
target = 12
print(func(l, target))


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


print(two_sum(l, target))
