"""
经过 Base64 编码的二进制数据可以解码成原始的数据形式，包括 JSON 数据。Base64 编码只是一种将二进制数据转换为文本的方式，而在解码时，
你可以将 Base64 编码的数据还原成原始的二进制数据，然后根据数据的格式解析。
通常情况下，如果你需要在二进制数据和文本之间进行转换，可以使用 Base64 编码和解码。例如，当你想在 JSON 数据中嵌入二进制数据（如图片、音频等）时，
可以将二进制数据进行 Base64 编码，然后将编码后的 Base64 字符串嵌入到 JSON 中。在接收端，你可以将 Base64 字符串解码成二进制数据，然后进行处理。
以下是一个简单的示例，演示了如何在 JSON 数据中嵌入经过 Base64 编码的二进制数据：
"""
import json
import base64

# 假设这是要嵌入的二进制数据b"Hello, World!"
# 将图片读取为二进制数据 并使用海象操作符将其保存到变量binary_data中 <class 'bytes'>
with open("../config/soft.png", "rb") as f: (binary_data := f.read())

# 将二进制数据进行 Base64 编码
base64_encoded = base64.b64encode(binary_data).decode("utf-8")

# 创建包含 Base64 编码数据的 dict 对象
json_data = {"data": base64_encoded}

# 将 转换为 JSON 字符串  进行网络传输
json_string = json.dumps(json_data)

# 在接收端，将 JSON 字符串转换回对象
received_json_data = json.loads(json_string)

# 获取 Base64 编码数据
received_base64_encoded = received_json_data["data"]

# 将 Base64 编码数据解码为二进制数据
decoded_binary_data = base64.b64decode(received_base64_encoded.encode("utf-8"))

# 现在你可以处理解码后的二进制数据
print(decoded_binary_data)
