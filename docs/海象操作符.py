# 海象操作符的主要目的是允许在表达式中直接进行变量赋值，这样可以简化代码并提高可读性。
# 通常情况下，赋值操作和条件判断会分开，而海象操作符允许将它们结合在一起。
if (n := len([1, 2, 3])) > 2:
    print(f"List is too long ({n} elements, expected <= 2)")

# 使用海象操作符在列表推导式中进行赋值
squares = [square := x**2 for x in range(10)]
print(square)
print(squares)

# 使用海象操作符在循环中同时进行赋值和比较
# while (line := input('--->')) != "stop":
#     print("Input:", line)

# readline 读取一行文件
with open("../requirements.txt", "r") as f:
    while (data := f.readline()) != "":
        print(data)
