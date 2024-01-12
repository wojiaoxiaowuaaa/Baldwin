from pytube import YouTube

url = """
		https://www.youtube.com/watch?v=SomiNFCnC4c
"""

yt = YouTube(url)

# 获取视频的标题
video_title = yt.title

# 获取视频的作者
video_author = yt.author

# 获取视频的发布日期
video_publish_date = yt.publish_date

# 获取视频的描述
video_description = yt.description

print(f"标题: {video_title}")
print(f"作者: {video_author}")
print(f"发布日期: {video_publish_date}")
print(f"描述: {video_description}")


# 创建一个YouTube对象，提供视频的URL
# yt = YouTube(url)

# 获取视频的音频流
# audio_stream = yt.streams.filter(only_audio=True).first()

# 下载音频到指定的文件路径（保存为MP3文件）
# audio_stream.download(output_path='/path/to/save')
