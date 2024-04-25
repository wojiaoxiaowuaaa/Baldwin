import base64


def encode_image_to_base64(image_path):
    """Base64 编码是一种将二进制数据转换成文本数据的编码方式.
    在这个脚本中，encoded_image 是一个经过 Base64 编码的字符串，它的长度会比原始的二进制图像数据长，这是因为 Base64 编码是一种将二进制数据转换成文本数据的编码方式，通常会导致编码后的字符串长度增加。
    理解这个 encoded_image 字符串，可以将其看作是原始图像数据的一种文本表示形式。通过 Base64 编码，原始的二进制图像数据被转换成了由 ASCII 字符组成的字符串，这样就可以在文本协议中传输，或者嵌入到 JSON 数据中等等。因此，encoded_image 字符串可以被看作是图像的一种文本表示形式，它包含了图像的所有信息，但是以一种文本的形式呈现出来。
    至于为什么编码后的字符串看起来很长，这是因为 Base64 编码的结果会比原始的二进制数据稍微大一些，通常会增加约 33% 的长度。这是由于 Base64 编码算法的特性决定的，它将每 3 个字节的二进制数据编码成 4 个字节的 ASCII 字符，因此会导致编码后的字符串长度增加"""
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')  # b64encode()函数对二进制图像数据进行Base64编码,编码后的Base64数据是二进制数据,decode('utf-8')将二进制数据解码为UTF-8字符串。
            return encoded_image
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    encoded_image = encode_image_to_base64('../27149/软件.png')  # 这里的encoded_image 可用于在JSON 数据中嵌入图像或通过网络 API 传输图像
    print(encoded_image)