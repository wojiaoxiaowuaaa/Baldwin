
# 输入你的Base64编码字符串
import json
import base64


def encode_fields_to_base64(fields):
    try:
        # 将字典转为 JSON 字符串
        json_str = json.dumps(fields)

        # 对 JSON 字符串进行UTF-8编码 得到utf-8字节对象
        json_data_encoded = json_str.encode('utf-8')

        # 对 UTF-8 编码后的数据进行 Base64 编码
        base64_encoded = base64.b64encode(json_data_encoded).decode('utf-8')

        return base64_encoded
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    fields_to_encode = {'name': 'John Doe', 'age': 30, 'city': 'New York'}

    encoded_result = encode_fields_to_base64(fields_to_encode)

    if encoded_result:
        print(encoded_result)
    else:
        print("Encoding failed.")
