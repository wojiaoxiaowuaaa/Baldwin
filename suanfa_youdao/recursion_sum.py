def func(numbs):
    """
    递归三原则
    (1)递归算法必须有基本情况；(算法停止递归的条件)
    (2)递归算法必须改变其状态并向基本情况靠近；
    (3)递归算法必须递归地调用自己。
    """
    if len(numbs) == 1:
        return numbs[0]
    return numbs[0] + func(numbs[1:])


func([1, 2, 3, 4])
