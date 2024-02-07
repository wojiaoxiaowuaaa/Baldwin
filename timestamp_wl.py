import datetime
import time
from datetime import datetime, timezone, timedelta


def timestamp_to_beijing_time(timestamp):
    if len(str(timestamp)) == 13:
        timestamp /= 1000  # Convert milliseconds to seconds if it's in milliseconds

    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    beijing_time = utc_time.astimezone(
        timezone(timedelta(hours=8))
    )  # Convert to Beijing timezone

    return beijing_time


# 输入待转换的时间戳
input_time = 1704038400000
print("输入时间戳--->日期为:", timestamp_to_beijing_time(input_time))


def beijing_time_to_timestamp(date_str, format_str="%Y-%m-%d %H:%M:%S"):
    try:
        date_time = datetime.strptime(date_str, format_str)
        timestamp = int(date_time.timestamp() * 1000)  # *1000 return ms timestamp
        return timestamp
    except ValueError:
        return None


# 输入待转换的日期
date_time_str = "2022-01-01 12:09:59"
print("输入日期--->时间戳为：", beijing_time_to_timestamp(date_time_str)) if beijing_time_to_timestamp(date_time_str) else print("无效的日期时间格式(代码末行输出)")


# current_timestamp = int(time.time()) # 当前时刻的时间戳---单位秒
current_time_ms = int(time.time() * 1000)
print("当前时刻的时间戳-单位毫秒:", current_time_ms, end="\n\n")