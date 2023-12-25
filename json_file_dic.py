import json

"""
pwd = '/Users/wl/Downloads/kswitch-online-人脸.json'

with open(pwd, 'r') as f:
    dic = json.load(f)  # <class 'dict'>
"""


def load_json_file(path):
    with open(file_path, "r") as file:
        data = json.load(file)

    return data


# 指定 JSON 文件的路径
file_path = "/Users/wl/Desktop/zzz_py/doc/res.json"

# 加载 JSON 文件并转化为字典
result = load_json_file(file_path)

# 打印结果
# print(result)

for k in result.items():
    print(k)
