from DownloadKit import DownloadKit
from time_count import calculate_execution_time


@calculate_execution_time
def download_kit_ticktock():
    # 创建下载器对象
    d = DownloadKit()
    # 遍历文件获取URL地址 传参到下载器对象进行下载
    with open('doc/url.txt', 'r') as f:
        # for i in f:
        d.download(f.read().strip(), '/Users/wl/Desktop', )


download_kit_ticktock()
