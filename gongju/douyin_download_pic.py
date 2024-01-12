import os
import requests


def download_image(url, save_path):
    response = requests.get(url)

    # 获取文件名（包括扩展名）
    file_name = url.split("/")[-1]

    # 删除文件名中 ".webp" 后面的部分
    file_name = file_name.split(".webp")[0] + ".webp"

    # 去除文件名中除字母和.外的其他内容
    file_name_no_ext = "".join(filter(lambda x: x.isalpha() or x == ".", file_name))

    # 保存文件
    save_file_path = os.path.join(save_path, file_name)
    with open(save_file_path, "wb") as f:
        f.write(response.content)
    print(f"Downloaded and saved: {file_name}")


# 指定文本文件路径
url_file_path = "/Users/wl/Desktop/zzz_py/doc/url.txt"

# 指定保存图片的文件夹路径
save_folder_path = "/Users/wl/Documents/douyin_download"

# 遍历文本文件中的URL并下载图片
with open(url_file_path, "r") as file:
    urls = file.readlines()
    for url in urls:
        url = url.strip()
        download_image(url, save_folder_path)
