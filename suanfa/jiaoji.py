"""求a, b两个列表的交集"""

a = [1, 2, 3, 4, 5, 7]
b = [3, 4, 5, 6, 7, 0]

# 使用集合求交集.在 Python 中，& 运算符用于对集合（set）进行交集操作。交集操作会返回两个集合中都包含的元素。
# 集合（set）是一种无序且不重复的元素集合。集合支持多种数学集合操作，比如并集、交集、差集等。print(list(set(a) - set(b))) 求差集. print(list(set(a) | set(b))) 求并集.
intersection = list(set(a) & set(b))
print(intersection)

# 使用列表推导式
tar = [i for i in a if i in b]
print(tar)

# 使用内置函数
res = list(filter(lambda x: x in b, a))
print(res)
