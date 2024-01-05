def func(content):
    punctuations = ['（', '，', '。', '“', '、', ' ', '）', '”', '\n']
    for punctuation in punctuations:
        content = content.replace(punctuation, '')  # 替换标点符号

    hashmap = {}  # 用字典存储：字符：次数
    for word in content:
        if word in hashmap:
            hashmap[word] = hashmap[word] + 1  # 该字符第N次在字典里
        else:
            hashmap[word] = 1  # 该字符第一次在字典里
    # print(hashmap)

    fin_hashmap = list(zip(hashmap.values(), hashmap.keys()))  # 按照次数从大到小排序
    fin_hashmap.sort(reverse=True, key=lambda x: x[0])
    print(fin_hashmap)


content = '''
文本排序统计文本中的字符并降序排序:
软件测试工程师（Software Testing Engineer）指理解产品的功能要求，并对其进行测试，检查软件有没有缺陷（Bug），
测试软件是否具有稳定性（Robustness）、安全性、易操作性等性能，写出相应的测试规范和测试用例的专门工作人员。
简而言之，软件测试工程师在一家软件企业中担当的是“质量管理”角色，及时发现软件问题并及时督促更正，确保产品的正常运作。
按其级别和职位的不同，分为三类。
'''

func(content)
