import requests
import os
import uuid
import shutil


def download_images_from_file(filename, output_dir):
    """根据指定文件中的URL下载图片到指定目录"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(filename, "r") as file:
        for line in file:
            url = (
                line.strip()
            )  # strip()方法移除字符串开头和结尾的指定字符(默认是空白字符、空格、换行符、制表符等)
            response = requests.get(url)
            if response.status_code == 200:
                image_name = str(uuid.uuid4()).replace("-", "") + ".webp"
                save_path = os.path.join(output_dir, image_name)
                with open(save_path, "wb") as f:
                    f.write(response.content)  # response.content 是 requests 库中的一个属性,它包含了服务器返回的原始响应数据.对于图片资源,response.content 包含的是图片的二进制数据.
                print(f"已下载图片:{save_path}")
            else:
                print(f"无法下载图片:{url}")

    # shutil.rmtree(output_dir)


if __name__ == "__main__":
    download_images_from_file("../config/url.txt", "../config/pic")
