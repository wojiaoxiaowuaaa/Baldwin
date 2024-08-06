set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 交集
intersection = set1 & set2
print("交集:", intersection)  # {4, 5}

# 并集
union = set1 | set2
print("并集:", union)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 差集（set1 相对于 set2 的差集）
difference1 = set1 - set2
print("差集 set1 - set2:", difference1)  # {1, 2, 3}

# 差集（set2 相对于 set1 的差集）
difference2 = set2 - set1
print("差集 set2 - set1:", difference2)  # {6, 7, 8}

# 对称差集（亦或集）
symmetric_difference = set1 ^ set2
print("对称差集:", symmetric_difference)  # {1, 2, 3, 6, 7, 8}
