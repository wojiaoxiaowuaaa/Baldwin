from DownloadKit import DownloadKit


def download_kit_ticktock():
    # 创建下载器对象
    d = DownloadKit('/Users/wl/Desktop')

    # 遍历文件获取URL地址 传参到下载器对象进行下载
    # with open('doc/url.txt', 'r') as f:
    #     for i in f:
    #         d.download(i)
    d.download('')


if __name__ == '__main__':
    download_kit_ticktock()
