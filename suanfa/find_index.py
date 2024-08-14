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


my_list = [10, 20, 30, 40, 30, 50]
element_to_find = 30

# print(find_all_indices(my_list, element_to_find))
# print(find_index(my_list, element_to_find))

def fib(n):
    # 生成器生成斐波那契数列
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


for i in fib(10):
    print(i, end=" ")
