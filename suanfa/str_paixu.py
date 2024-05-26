def count_letters(s):
    letter_dict = {}
    for char in s:
        if char.isalpha():  # 判断字符是否为字母
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    return letter_dict

# 示例字符串
input_string = "统计字符示例字符串，只计字母"

# 调用函数
result = count_letters(input_string)

# 输出结果
for letter, count in result.items():
    print(f"'{letter}': {count}")
