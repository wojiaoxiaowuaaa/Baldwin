import qrcode
from matplotlib import pyplot as plt


def qr_png(data):
    """生成二维码方法
    :param data: 二维码内容"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    # img.save("qrcode.png")

    fig = plt.figure()  # 使用matplotlib展示二维码
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(img)
    ax.axis("off")  # 不显示坐标轴 使得展示的图片更加简洁
    plt.show()


qr_png("http://www.pofengqx.com/QTCX?b=8660629937_1")
