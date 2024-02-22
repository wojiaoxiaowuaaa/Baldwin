import os


# 遍历文件夹查找指定格式的文件
def func(file, pwd):
    kings = []
    # os.walk：Python 的标准库函数，用于以递归的方式遍历目录树。
    # 它返回一个生成器，每次迭代都会返回一个包含三个元素的元组：当前目 st录的路径，当前目录下的子目录列表，以及当前目录下的文件列表。
    for root, dirs, files in os.walk(pwd):
        for f in files:
            name, postfix = os.path.splitext(f)
            if postfix == file:
                kings.append(f)
    return len(kings), kings


landing = func('.py', '/Users/wl/Desktop')
print(landing)