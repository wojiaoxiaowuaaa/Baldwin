def set_global_var():
    global my_global_var
    my_global_var = "Hello, World!"


def use_global_var():
    return my_global_var


# 设置全局变量(必须调用 否则报错)
set_global_var()

# 使用全局变量
print(use_global_var())  # 输出 "Hello, World!"
