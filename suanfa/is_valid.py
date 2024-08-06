def is_valid(s: str) -> bool:
    """检查字符串是否表示一个有效的括号序列。有效括号序列是指由左括号（"(", "{", "["）和相应的右括号（")", "}", "]"）组成，且左括号和右括号成对出现，没有多余的括号"""

    stack = []  # 1. 初始化一个空栈`stack`，用于存储遇到的左括号。

    mapping = {
        ")": "(",
        "}": "{",
        "]": "[",
    }  # 2. (字典的key均为右括号)创建一个映射字典，它将每个右括号映射到其对应的左括号。

    for (
        char
    ) in (
        s
    ):  # 3. 遍历输入字符串`s`中的每个字符`char`：如果`char`是一个右括号（即在`mapping`字典的键中），检查栈顶元素（如果栈不为空则弹出，否则假设为'-'） 如果栈顶元素不是与当前右括号匹配的左括号，返回`False`，因为这意味着括号不匹配。否则，`char`是一个左括号，将其压入栈中。
        if char in mapping:
            top_element = stack.pop() if stack else "-"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return (
        not stack
    )  # 遍历结束后，如果栈为空，说明所有左括号都有对应的右括号，返回`True`；否则返回`False`，因为存在未闭合的左括号。


print(is_valid("()[]{}"))
