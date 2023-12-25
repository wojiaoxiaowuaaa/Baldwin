from pytube import YouTube
from time_count import calculate_execution_time
from config_reader import save_path


@calculate_execution_time
def download_youtube_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # 获取最高分辨率的视频流

        stream.download(output_path=save_path)  # 下载视频到指定路径

        print(f"视频已成功下载到 {save_path}")

    except Exception as e:
        print(f"下载视频时出错：{e}")


if __name__ == "__main__":
    youtube_url = """
        https://www.douyin.com/video/7285611499786079507
    """
    download_youtube_video(youtube_url, save_path)
