"""生成指定长度的随机字符串:
secrets_string = secrets.token_hex(10)  # <class 'str'>
secrets模块是 Python 标准库中的一个模块,提供了生成随机数和安全随机数的函数,用于安全敏感的密码、token、验证码等场景.
secrets 模块与 random 模块相似,但它专门用于生成安全的随机数,避免了在密码学和安全性方面的一些问题.在需要生成安全随机数的场景中,推荐使用 secrets 模块来保证随机数的安全性和可靠性"""

import asyncio
import secrets


async def secrets_str(length=10):
    return secrets.token_hex(length)


async def main():
    # 当调用 secrets_str() 函数时,会返回一个异步任务对象,你可以将其 await,以等待结果的返回.
    result = await secrets_str()
    print(result)


if __name__ == '__main__':
    # 运行主协程,从而实现了异步调用 secrets_str() 函数并打印结果.
    asyncio.run(main())

# 在Python中,await 关键字用于暂停当前协程的执行,等待另一个协程完成并返回结果.这个关键字只能在协程内部使用,它告诉事件循环event_loop暂停当前协程的执行,并执行其他协程,直到等待的协程完成并返回结果,然后再继续执行当前协程.
# 下面这行代码,await secrets_str() 位于顶级上下文中,而不是在异步函数内部.在顶级上下文中使用 await 是不允许的,因为 Python 解释器无法直接处理异步调用.而在异步函数内部,使用 await 是允许的,因为在异步函数内部可以使用异步操作.
# await secrets_str()
