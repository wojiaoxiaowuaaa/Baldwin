from DownloadKit import DownloadKit
from time_count import calculate_execution_time


@calculate_execution_time
def download_kit_ticktock():
    # 创建下载器对象
    d = DownloadKit('/Users/wl/Desktop')

    # 遍历文件获取URL地址 传参到下载器对象进行下载
    # with open('doc/url.txt', 'r') as f:
    #     for i in f:
    #         d.download(i)
    d.download('https://v5-dy-o-abtest.zjcdn.com/2c8da0782549f27b6c3d8c8f68b2eb6f/65b3a97c/video/tos/cn/tos-cn-ve-15c001-alinc2/okVrAFNzDIPhe4yAa45qG1BVqB7APh5DfQDhEg/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1379&bt=1379&cs=0&ds=6&ft=.8lkJbPOPd82h3jVQ9L5f9CTsdg.mn2og3cAp&mime_type=video_mp4&qs=0&rc=N2llZjRoOmU1OjY7Nmc1NkBpMzRxZGk6ZmplcDMzNGkzM0BiLTMxMmAvXzQxLTM2LzMtYSNpZGxhcjRnbWlgLS1kLTBzcw%3D%3D&btag=e00010000&cc=46&dy_q=1706269530&feature_id=f0150a16a324336cda5d6dd0b69ed299&l=202401261945309DF76C529B84EA1A1A1D')


if __name__ == '__main__':
    download_kit_ticktock()
