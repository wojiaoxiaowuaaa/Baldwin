l = list(range(30))

chunk_size = 4  # 按照指定步长拆分列表(将列表拆分为若干个子列表 ，每个子列表的长度为chunk_size)

l = [l[i:i + chunk_size] for i in range(0, len(l), chunk_size)]  # 列表推导式

print(l)


