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
