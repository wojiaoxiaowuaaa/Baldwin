from sortedcontainers import SortedDict, SortedList, SortedSet


def func():
    """高性能的排序用三方库"""
    arr = [3, 6, 8, 10, 1, 2, 1, 11, 5, 7, 7, 9, 0, 4, 4, 4, 4]
    arr = list(SortedList(arr))
    print(arr)
    
    dic = {'c': -3, 'a': 1, 'b': 2}
    dic = SortedDict(dic)
    print(dict(dic))


# func()
