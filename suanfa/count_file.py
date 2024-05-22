import os


def func(pwd):
    """统计文件中小写字母的数量"""
    count = 0

    with open(pwd, 'r') as f:
        data = f.read()
        for _ in data:
            if _.islower():  # 统计大写用 isupper
                count += 1
    return count


print(func(os.path.abspath(__file__)))  # os.path.dirname(__file__)返回的是当前文件所在的目路径

