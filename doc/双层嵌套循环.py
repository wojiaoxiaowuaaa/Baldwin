# 双层循环拆分嵌套列表 组合数据
# 双层循环可以被理解为“循环中的循环”。外层循环每执行一次，内层循环就会完整地执行一遍。
names = ["name", "dob", "gender"]

values = [
    ["jason", "2000-01-01", "male"],
    ["mike", "1999-01-01", "male"],
    ["nancy", "2001-02-01", "female"],
]

results = []

for value in values:
    hashmap = {}
    for index, name in enumerate(names):
        hashmap[name] = value[index]
    print(hashmap)
    results.append(hashmap)

print(results)

# 使用字典+列表推导式
# zip() 函数是处理多个可迭代对象的强大工具，特别是当你需要将它们的元素配对或者按位置组合时。它的主要限制是，当输入的可迭代对象长度不一致时，它会根据最短的那个停止生成元组。
[{name: value for name, value in zip(names, value)} for value in values]
