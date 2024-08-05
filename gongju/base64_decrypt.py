"""Base64 编码是一种将二进制数据转换为可打印字符的编码方式。它在计算机科学和网络通信中有许多用途和好处：
1. **数据传输：** Base64 编码常用于将二进制数据在不同系统之间进行传输，特别是在网络通信中。因为某些字符在网络传输中可能会被解释为控制字符或特殊字符，使用 Base64 编码可以确保数据在不同环境中保持一致，避免数据损坏或解释错误。
2. **电子邮件附件：** 电子邮件文本仅支持 ASCII 字符，如果要将二进制文件（如图片、音频、视频等）作为邮件附件发送，可以使用 Base64 编码将其转换为可嵌入文本的形式。
3. **URL 参数：** URL 中不能直接包含一些特殊字符，例如 `/`、`?` 等。如果你需要将数据传递给 URL，可以使用 Base64 编码将其转换为安全的 URL 参数。
4. **存储敏感数据：** 尽管 Base64 编码并不加密数据，但它可以在一定程度上隐藏原始数据的内容，适用于存储一些敏感但不需要高级加密的信息，如 API 密钥或令牌。
5. **数据校验：** 通过将数据编码为 Base64，可以更轻松地执行数据校验，因为数据在不同系统中的编码始终一致，这有助于验证数据的完整性。
6. **编码可打印字符：** Base64 编码将二进制数据转换为由字母、数字和少数几个特殊字符组成的可打印字符串，这使得它适用于那些只能处理文本数据的场景。
7. **数据处理和显示：** 在某些情况下，将二进制数据转换为 Base64 编码后，可以更方便地在文本环境中处理、显示和复制粘贴数据。"""

import base64
import json


def base64_to_json(base64_str):
    try:
        decoded_data = base64.b64decode(base64_str).decode("utf-8")
        return decoded_data
    except Exception as e:
        return str(e)


def encode_to_base64(fields):
    # Base64 编码并不是加密方式，它只是一种将二进制数据转换为文本的方法，因此它并不会增加数据的安全性。
    try:
        # 将字典转为 JSON 字符串
        json_str = json.dumps(fields)

        # 对 JSON 字符串进行UTF-8编码 得到字节对象bytes
        json_data_encoded = json_str.encode("utf-8")

        # 对 UTF-8 编码后的bytes数据进行 Base64 编码
        base64_encoded = base64.b64encode(json_data_encoded).decode(
            "utf-8"
        )  # decode('utf-8') 是将字节序列转换为字符串的方法，使用 UTF-8 编码格式。

        return base64_encoded
    except Exception as e:
        print(f"Error: {e}")
        return None


def encode_image_to_base64(image_path):
    """Base64 编码是一种将二进制数据转换成文本数据的编码方式.
    在这个脚本中，encoded_image 是一个经过 Base64 编码的字符串，它的长度会比原始的二进制图像数据长，这是因为 Base64 编码是一种将二进制数据转换成文本数据的编码方式，通常会导致编码后的字符串长度增加。
    理解这个 encoded_image 字符串，可以将其看作是原始图像数据的一种文本表示形式。通过 Base64 编码，原始的二进制图像数据被转换成了由 ASCII 字符组成的字符串，这样就可以在文本协议中传输，或者嵌入到 JSON 数据中等等。因此，encoded_image 字符串可以被看作是图像的一种文本表示形式，它包含了图像的所有信息，但是以一种文本的形式呈现出来。
    至于为什么编码后的字符串看起来很长，这是因为 Base64 编码的结果会比原始的二进制数据稍微大一些，通常会增加约 33% 的长度。这是由于 Base64 编码算法的特性决定的，它将每 3 个字节的二进制数据编码成 4 个字节的 ASCII 字符，因此会导致编码后的字符串长度增加
    """
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode(
                "utf-8"
            )  # b64encode()函数对二进制图像数据进行Base64编码,编码后的Base64数据是二进制数据,decode('utf-8')将二进制数据解码为UTF-8字符串。
            return encoded_image
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    decoded_json = base64_to_json(
        "eyJuYW1lIjogIkpvaG4gRG9lIiwgImFnZSI6IDMwLCAiY2l0eSI6ICJOZXcgWW9yayJ9"
    )
    # print("解码后的JSON据:", decoded_json)

    # encoded_result = encode_to_base64({'name': 'John Doe', 'age': 30, 'city': 'New York'})
    encoded_result = encode_to_base64(
        "https://github.com/wojiaoxiaowuaaa/Baldwin/blob/master/gongju/base64_decrypt.py"
    )
    print("编码后的文本数据:", encoded_result)

    # encoded_image = encode_image_to_base64(
    #     "../config/pic/1~!!@@#11.webp"
    # )  # 这里的encoded_image 可用于在JSON 数据中嵌入图像或通过网络 API 传输图像
    # print(encoded_image)
