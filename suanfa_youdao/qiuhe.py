# 递归求和
def func(l, target):
    hashmap = {}

    for index, value in enumerate(l):
        hashmap[value] = index

    for i, v in enumerate(l):
        lord = hashmap.get(target - v)

        if lord is not None and lord != i:
            return i, lord


l = [1, 3, 7, 11]
target = 12
print(func(l, target))
