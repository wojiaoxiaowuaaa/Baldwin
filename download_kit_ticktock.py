from DownloadKit import DownloadKit
from gongju.time_count import calculate_execution_time

# https://g1879.gitee.io/downloadkitdocs/usage/create_object/


@calculate_execution_time
def download_kit_ticktock():
    # 创建下载器对象
    d = DownloadKit()
    with open('doc/url.txt', 'r') as f:
        d.download(f.read().strip(), '/Users/wl/Desktop', )


download_kit_ticktock()
