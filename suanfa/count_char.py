import os


def count_characters(file_path):
    # (统计文本中字符的出现次数 排序后展示最高频的前十个)初始化一个空字典hashmap来存储字符及其出现次数
    hashmap = {}

    try:
        with open(file_path, "r") as f:
            # for line in f:
            #     for char in line:
            for char in f.read():
                if char in hashmap:
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return  # 捕获到异常后立即退出函数,防止继续执行后续代码.这有助于避免在处理错误时出现不必要的执行和潜在的错误输出.
    except (
        PermissionError
    ):  # try 语句后面可以有多个 except 块，每个 except 块可以处理不同类型的异常。这样可以针对不同的异常类型执行不同的处理逻辑。
        print(f"没有权限读取文件 {file_path}。")
        return
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return

    hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)[
        :10
    ]  # [(' ', 260), ('r', 41)]
    return dict(hashmap)


print(count_characters(os.path.abspath(__file__)))
