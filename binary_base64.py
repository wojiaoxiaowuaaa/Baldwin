"""
经过 Base64 编码的二进制数据可以解码成原始的数据形式，包括 JSON 数据。Base64 编码只是一种将二进制数据转换为文本的方式，而在解码时，
你可以将 Base64 编码的数据还原成原始的二进制数据，然后根据数据的格式解析。
通常情况下，如果你需要在二进制数据和文本之间进行转换，可以使用 Base64 编码和解码。例如，当你想在 JSON 数据中嵌入二进制数据（如图片、音频等）时，
可以将二进制数据进行 Base64 编码，然后将编码后的 Base64 字符串嵌入到 JSON 中。在接收端，你可以将 Base64 字符串解码成二进制数据，然后进行处理。
以下是一个简单的示例，演示了如何在 JSON 数据中嵌入经过 Base64 编码的二进制数据：
"""

import json
import base64

# 假设这是要嵌入的二进制数据.可替换为图片的绝对路径.
binary_data = b"Hello, World!"

# 将二进制数据进行 Base64 编码
base64_encoded = base64.b64encode(binary_data).decode("utf-8")

# 创建包含 Base64 编码数据的 JSON 对象
json_data = {"data": base64_encoded}

# 将 转换为 JSON 字符串
json_string = json.dumps(json_data)

# 在接收端，将 JSON 字符串转换回对象
received_json_data = json.loads(json_string)

# 获取 Base64 编码数据
received_base64_encoded = received_json_data["data"]

# 将 Base64 编码数据解码为二进制数据
decoded_binary_data = base64.b64decode(received_base64_encoded.encode("utf-8"))

# 现在你可以处理解码后的二进制数据
print(decoded_binary_data)


"""
在 Python 中，`encode('utf-8')` 和 `decode('utf-8')` 是用于字符串编码和解码的方法，用于在字节序列和 Unicode 字符串之间进行转换。这两个方法通常用于处理字符集和编码的转换，特别是在处理文本数据的时候。

- **`encode('utf-8')`：** 这个方法用于将 Unicode 字符串编码为字节序列。它接受一个参数，即要使用的字符编码。在这里，`'utf-8'` 表示使用 UTF-8 编码。UTF-8 是一种常用的字符编码，用于表示 Unicode 字符。例如：

  ```python
  unicode_string = "Hello, 你好"
  byte_sequence = unicode_string.encode('utf-8')
  print(byte_sequence)  # 输出字节序列
  ```

- **`decode('utf-8')`：** 这个方法用于将字节序列解码为 Unicode 字符串。它也接受一个参数，即要使用的字符编码。与 `encode` 方法相反，在这里，`'utf-8'` 用于表示输入字节序列的编码。例如：

  ```python
  byte_sequence = b'Hello, \xe4\xbd\xa0\xe5\xa5\xbd'
  unicode_string = byte_sequence.decode('utf-8')
  print(unicode_string)  # 输出 Unicode 字符串
  ```

需要注意以下几点：

1. `encode()` 方法将字符串编码为字节序列，输出的是 `bytes` 类型。
2. `decode()` 方法将字节序列解码为字符串，输出的是 `str` 类型。
3. 在进行编码和解码时，要确保使用相同的字符编码，否则可能会出现乱码或错误的结果。
4. UTF-8 是一种可变长度的字符编码，可以用于表示世界上大部分字符，包括拉丁字母、汉字、符号等。

总之，`encode('utf-8')` 和 `decode('utf-8')` 方法在处理文本数据时非常有用，特别是在处理多语言和多字符集的场景中。它们帮助你在字节序列和 Unicode 字符串之间进行无缝转换。
"""
