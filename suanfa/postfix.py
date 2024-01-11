import os


# 遍历文件夹查找指定格式的文件
def func(file, pwd):
    kings = []
    for root, dirs, files in os.walk(pwd):
        for f in files:
            name, postfix = os.path.splitext(f)
            if postfix == file:
                kings.append(f)
    return len(kings), kings


landing = func('.py', '/Users/wl/')
