"""
{'data': {'traceAssetsIdList': ['106170400000001citycode250113000028', '106170400000001citycode250113000029', '106170400000001citycode250113000030', '106170400000001citycode250113000031', '106170400000001citycode250113000032', '106170400000001citycode250113000033', '106170400000001citycode250113000034', '106170400000001citycode250113000035', '106170400000001citycode250113000036']}, 'status': 1000, 'message': '请求成功'}
"""

# def func(json_file):
#     """读取本地存储的json文件,转化为dic类型
#     json.load 用于从文件中加载 JSON 数据，接收文件对象作为参数,例如f。
#     json.loads 用于从json字符串中加载 JSON 数据，接收字符串作为参数例如f.read()或变量名"""
#     with open(json_file, 'r') as f:
#         data = json.load(f)  # <class 'dict'>
#         return data
#
#
# json_file = f'{os.path.dirname(__file__)}/config/demo.json'
# data = func(json_file)
# print(data)

import json
import sys


def convert_and_print_json(s):
    try:
        # 将通过参数输入的字符串转换为字典
        input_dict = eval(s)
        # 将字典转换为格式化的 JSON 字符串，并设置 ensure_ascii=False 以正确显示非 ASCII 字符
        json_output = json.dumps(input_dict, indent=4, ensure_ascii=False)
        print()
        print(json_output)
        print()
    except (SyntaxError, NameError):
        print("输入错误，请确保输入有效的字典数据。")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 获取命令行参数中的字典数据字符串
        input_dict_str = sys.argv[1]
        convert_and_print_json(input_dict_str)
    else:
        print("请在命令行中提供要转换的字典数据。")
