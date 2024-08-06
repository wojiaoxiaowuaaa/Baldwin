import datetime
import time
from datetime import datetime, timezone, timedelta

print(
    "当前时刻的时间戳-默认单位秒:", int(time.time()), end="\n\n"
)  # current_timestamp = int(time.time()) # 当前时刻的时间戳---单位秒


def timestamp_to_beijing_time(timestamp):
    if len(str(timestamp)) == 13:
        timestamp /= 1000  # Convert milliseconds to seconds if it's in milliseconds

    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    beijing_time = utc_time.astimezone(
        timezone(timedelta(hours=8))
    )  # Convert to Beijing timezone
    return beijing_time


def beijing_time_to_timestamp(date_str, format_str="%Y-%m-%d %H:%M:%S"):
    try:
        date_time = datetime.strptime(date_str, format_str)
        timestamp = int(date_time.timestamp())  # *1000 return ms timestamp
        return timestamp
    except ValueError:
        return None


if __name__ == "__main__":
    print("输入时间戳日期为:", timestamp_to_beijing_time(1708940095494), end="\n\n")
    (
        print(
            "输入日期时间戳为(默认单位:秒)：",
            beijing_time_to_timestamp("2022-01-01 12:09:59"),
        )
        if beijing_time_to_timestamp("2022-01-01 12:09:59")
        else print("无效的日期时间格式(代码末行输出)")
    )
