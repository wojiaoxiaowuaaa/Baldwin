import asyncio
import secrets

"""
生成指定长度的随机字符串:
random_string = secrets.token_hex(10)  # <class 'str'>
secrets 模块是 Python 标准库中的一个模块，提供了生成随机数和安全随机数的函数，用于安全敏感的密码、token、验证码等场景。
secrets 模块与 random 模块相似，但它专门用于生成安全的随机数，避免了在密码学和安全性方面的一些问题。在需要生成安全随机数的场景中，推荐使用 secrets 模块来保证随机数的安全性和可靠性。"""


async def secrets_str(length=10):
    return secrets.token_hex(length)


async def main():
    # 当调用 secrets_str() 函数时，会返回一个异步任务对象，你可以将其 await，以等待结果的返回。
    result = await secrets_str()
    print(result)

# 运行主协程，从而实现了异步调用 secrets_str() 函数并打印结果。
asyncio.run(main())
