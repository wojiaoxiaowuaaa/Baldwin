"""
Base64 编码是一种基于64个可打印字符来表示二进制数据的编码方法.它广泛应用于需要将二进制数据转换为文本格式的场景,
如在URL、电子邮件和Web应用中传输数据.
经过 Base64 编码的二进制数据可以解码成原始的数据形式,包括 JSON 数据 Base64 编码只是一种将二进制数据转换为文本的方式,而在解码时,
你可以将 Base64 编码的数据还原成原始的二进制数据,然后根据数据的格式解析.
通常情况下,如果你需要在二进制数据和文本之间进行转换,可以使用 Base64 编码和解码.
例如,当你想在 JSON 数据中嵌入二进制数据(如图片、音频等)时,可以将二进制数据进行 Base64 编码,然后将编码后的Base64字符串嵌入到JSON中
在接收端,你可以将 Base64 字符串解码成二进制数据,然后进行处理.
以下是一个简单的示例,演示了如何在 JSON 数据中嵌入经过 Base64 编码的二进制数据:
# 假设这是要嵌入的二进制数据b"Hello, World!"
# 将图片读取为二进制数据 并使用海象操作符将其保存到变量binary_data中 <class 'bytes'>
with open("../config/soft.png", "rb") as f: (binary_data := f.read())

# 将二进制数据进行 Base64 编码
base64_encoded = base64.b64encode(binary_data).decode("utf-8")

# 创建包含 Base64 编码数据的 dict 对象
json_data = {"data": base64_encoded}

# 将 转换为 JSON 字符串  进行网络传输
json_string = json.dumps(json_data)

# 在接收端,将 JSON 字符串转换回对象
received_json_data = json.loads(json_string)

# 获取 Base64 编码数据
received_base64_encoded = received_json_data["data"]

# 将 Base64 编码数据解码为二进制数据
decoded_binary_data = base64.b64decode(received_base64_encoded.encode("utf-8"))

# 现在你可以处理解码后的二进制数据
print(decoded_binary_data)

-----------------------------
Base64 编码是一种将二进制数据转换为可打印字符的编码方式.它在计算机科学和网络通信中有许多用途和好处:
1. 数据传输:** Base64 编码常用于将二进制数据在不同系统之间进行传输,特别是在网络通信中.因为某些字符在网络传输中可能会被解释为控制字符或特殊字符,使用 Base64 编码可以确保数据在不同环境中保持一致,避免数据损坏或解释错误.
2. 电子邮件附件:** 电子邮件文本仅支持 ASCII 字符,如果要将二进制文件(如图片、音频、视频等)作为邮件附件发送,可以使用 Base64 编码将其转换为可嵌入文本的形式.
3. URL 参数:** URL 中不能直接包含一些特殊字符,例如 `/`、`?` 等.如果你需要将数据传递给 URL,可以使用 Base64 编码将其转换为安全的 URL 参数.
4. 存储敏感数据:** 尽管 Base64 编码并不加密数据,但它可以在一定程度上隐藏原始数据的内容,适用于存储一些敏感但不需要高级加密的信息,如 API 密钥或令牌.
5. 数据校验:** 通过将数据编码为 Base64,可以更轻松地执行数据校验,因为数据在不同系统中的编码始终一致,这有助于验证数据的完整性.
6. 编码可打印字符:** Base64 编码将二进制数据转换为由字母、数字和少数几个特殊字符组成的可打印字符串,这使得它适用于那些只能处理文本数据的场景.
7. 数据处理和显示:** 在某些情况下,将二进制数据转换为 Base64 编码后,可以更方便地在文本环境中处理、显示和复制粘贴数据"""

import base64
import json
import hashlib
import os
from config.setting import MD5_SALT


def base64_to_json(base64_str):
    try:
        decoded_data = base64.b64decode(base64_str).decode("utf-8")
        return decoded_data
    except Exception as e:
        return str(e)


def encode_to_base64(fields):
    # Base64 编码并不是加密方式,它只是一种将二进制数据转换为文本的方法,因此它并不会增加数据的安全性.
    try:
        # 将字典转为 JSON 字符串
        json_str = json.dumps(fields)

        # 对 JSON 字符串进行UTF-8编码 得到字节对象bytes
        json_data_encoded = json_str.encode("utf-8")

        # 对 UTF-8 编码后的bytes数据进行 Base64 编码
        base64_encoded = base64.b64encode(json_data_encoded).decode(
            "utf-8"
        )  # decode('utf-8') 是将字节序列转换为字符串的方法,使用 UTF-8 编码格式.

        return base64_encoded
    except Exception as e:
        print(f"Error: {e}")
        return None


def encode_image_to_base64(image_path):
    """Base64 编码是一种将二进制数据转换成文本数据的编码方式.
    在这个脚本中,encoded_image 是一个经过 Base64 编码的字符串,它的长度会比原始的二进制图像数据长,这是因为 Base64 编码是一种将二进制数据转换成文本数据的编码方式,通常会导致编码后的字符串长度增加.
    理解这个 encoded_image 字符串,可以将其看作是原始图像数据的一种文本表示形式.通过 Base64 编码,原始的二进制图像数据被转换成了由 ASCII 字符组成的字符串,这样就可以在文本协议中传输,或者嵌入到 JSON 数据中等等.因此,encoded_image 字符串可以被看作是图像的一种文本表示形式,它包含了图像的所有信息,但是以一种文本的形式呈现出来.
    至于为什么编码后的字符串看起来很长,这是因为 Base64 编码的结果会比原始的二进制数据稍微大一些,通常会增加约 33% 的长度.这是由于 Base64 编码算法的特性决定的,它将每 3 个字节的二进制数据编码成 4 个字节的 ASCII 字符,因此会导致编码后的字符串长度增加
    """
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode(
                "utf-8"
            )  # b64encode()函数对二进制图像数据进行Base64编码,编码后的Base64数据是二进制数据,decode('utf-8')将二进制数据解码为UTF-8字符串.
            return encoded_image
    except Exception as e:
        print(f"Error: {e}")
        return None


def calculate_md5(file_path, block_size=1024):
    md5 = hashlib.md5()
    with open(
            file_path, "rb"
    ) as file:  # 二进制模式意味着文件将以字节流的形式读取,而不是文本.
        for block in iter(
                lambda: file.read(block_size), b""
        ):  # 创建一个迭代器,该迭代器会重复调用 lambda: file.read(block_size),直到返回值为 b''(空字节串,即文件末尾)迭代器停止.
            md5.update(
                block
            )  # 这个方法会更新 MD5 对象的状态,考虑到了新的数据块.在整个文件读取过程中,这个方法会不断更新 MD5 对象,将所有的数据块一一加入计算.
    return md5.hexdigest()  # 获取 MD5 摘要的十六进制表示


def get_md5(username, str):
    """MD5加密处理"""
    str = username + str + MD5_SALT  # 把用户名也作为str加密的一部分
    md5 = hashlib.md5()  # 创建md5对象
    md5.update(str.encode("utf-8"))  # Python3中需要先转换为 bytes 类型,才能加密
    return (
        md5.hexdigest()
    )  # 计算输入数据的 MD5 哈希值,并将其以十六进制字符串的形式返回.


def video_md5(pwd):
    """获取视频的md5值 节约内存型"""
    md5_hash = hashlib.md5()
    with open(pwd, "rb") as f:
        while chunk := f.read(4096):
            md5_hash.update(chunk)
    print(md5_hash.hexdigest())


def md5_video(pwd):
    """获取视频的md5 快速型(一次性加载全部数据到内存)
    Python的内存管理是基于引用计数和垃圾回收的,一次性读取大文件可能会导致整个文件的内容都存储在内存中,占用大量的内存空间.如果文件过大,超出了系统的可用内存限制,就会导致内存溢出
    """
    with open(pwd, "rb") as f:
        md5 = hashlib.md5(f.read()).hexdigest()
    print(md5)


if __name__ == "__main__":
    encoded_result = encode_to_base64({"name": "John Doe", "age": 30, "city": "New York"})
    # print("编码后的文本数据:", encoded_result)

    # md5_value = calculate_md5(os.path.abspath(__file__))
    # print(md5_value)


