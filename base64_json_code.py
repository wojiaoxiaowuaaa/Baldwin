import json
import base64


def json_to_base64(json_str):
    try:
        json_data = json.loads(json_str)
        encoded_data = base64.b64encode(json.dumps(json_data).encode("utf-8")).decode(
            "utf-8"
        )
        return encoded_data
    except Exception as e:
        return str(e)


# 输入你的JSON字符串
input_json = """
        {"name": "Alice", "age": 25, "city": "Beijing"}
"""

# 调用函数进行转换并打印结果
base64_result = json_to_base64(input_json)
print("Base64编码结果: ", base64_result)
