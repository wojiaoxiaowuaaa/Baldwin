# 使用 iter() 函数创建迭代器，使用 lambda 函数作为可调用对象

# iter() 函数接受两个参数，分别是可调用对象和哨兵值。它会不断调用可调用对象，直到返回哨兵值为止。
# 哨兵值（sentinel value）是一个特殊的值，用于表示迭代的终止条件。当迭代器产生哨兵值时，for 循环会认为迭代结束，从而退出循环。
my_iterator = iter(lambda: input("Enter a number or 'stop' to end: "), 'stop')

# 使用 for 循环遍历迭代器
for i in my_iterator:
    print(i)
