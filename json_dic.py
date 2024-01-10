import json
# 读取本地存储的json文件  转化为dict类型后在脚本中作数据分析用.
# json.load 用于从文件中加载 JSON 数据，接收文件对象作为参数,例如f。
# json.loads 用于从字符串中加载 JSON 数据，接收字符串作为参数例如f.read()。


def func(json_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)  # <class 'dict'>
        return data


json_file_path = '/Users/wl/Downloads/abtest埋点.json'
res = func(json_file_path)
print(res)

# for key in res:
#     print(key)
