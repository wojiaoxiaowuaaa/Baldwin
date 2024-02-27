import requests
import os
import uuid


def download_images_from_file(filename, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(filename, "r") as file:
        for line in file:
            url = line.strip()
            response = requests.get(url)
            if response.status_code == 200:
                image_name = str(uuid.uuid4()).replace("-", "") + ".webp"
                save_path = os.path.join(output_dir, image_name)
                with open(save_path, "wb") as img_file:
                    img_file.write(response.content)
                print(f"已下载图片：{save_path}")
            else:
                print(f"无法下载图片：{url}")


filename = ""
output_dir = ""
download_images_from_file(filename, output_dir)
