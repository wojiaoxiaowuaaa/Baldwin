import base64


def encode_image_to_base64(image_path):
    try:
        # 读取图像
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            # b64encode()函数对二进制图像数据进行Base64编码,编码后的Base64数据是二进制数据,decode('utf-8')将二进制数据解码为UTF-8字符串。
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            return encoded_image
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    image_path = '/Users/wl/Documents/代码量级.png'

    encoded_image = encode_image_to_base64(image_path)

    if encoded_image:
        # 这里的encoded_image 可用于在JSON 数据中嵌入图像或通过网络 API 传输图像
        print(encoded_image)
