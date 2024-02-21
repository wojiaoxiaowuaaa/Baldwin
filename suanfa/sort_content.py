from config.setting import winter_fell, net


def func(winter_fell):
    punctuations = ['（', '，', '。', '“', '、', ' ', '）', '”', '\n']
    for punctuation in punctuations:
        winter_fell = winter_fell.replace(punctuation, '')  # 替换标点符号

    hashmap = {}  # 用字典存储：字符：次数
    for word in winter_fell:
        if word in hashmap:
            hashmap[word] = hashmap[word] + 1  # 该字符第N次在字典里
        else:
            hashmap[word] = 1  # 该字符第一次在字典里
    # print(hashmap)

    fin_hashmap = list(zip(hashmap.values(), hashmap.keys()))  # 按照次数从大到小排序
    fin_hashmap.sort(reverse=True, key=lambda x: x[0])
    print(fin_hashmap)


with open(net, 'r') as f:
    content = f.read()

func(content)
