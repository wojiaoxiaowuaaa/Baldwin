def filter_numbers(l):
    """处理输入的列表  要求返回的新列表中的每个元素都是偶数&&该元素在原list中的下标也是偶数"""
    # return [number for index, number in enumerate(l) if index % 2 == 0 and number % 2 ==0]
    return [i for i in l if i % 2 == 0 and l.index(i) % 2 == 0]


print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
