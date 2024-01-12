from pytube import YouTube
from time_count import calculate_execution_time


@calculate_execution_time
def download_youtube_video(url, output_path='.'):
    try:
        # 创建 YouTube 对象
        yt = YouTube(url)

        # 获取视频的最高分辨率
        video = yt.streams.get_highest_resolution()

        # 下载视频到指定路径
        video.download(output_path)

        print(f"视频 '{yt.title}' 下载完成！")
    except Exception as e:
        print(f"下载失败：{e}")


if __name__ == "__main__":
    # 替换为你要下载的 YouTube 视频的 URL
    video_url = """
        https://www.youtube.com/watch?v=055mU4f3E5A
    """

    # 替换为你想要保存视频的本地路径
    # save_path = "path/to/save"

    download_youtube_video(video_url)
