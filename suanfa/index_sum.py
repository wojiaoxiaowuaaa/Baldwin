"""根据两数之和 找出两数的下标"""


def func(ll, tar):
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


l = [1, 3, 7, 11]
target = 12
print(func(l, target))
