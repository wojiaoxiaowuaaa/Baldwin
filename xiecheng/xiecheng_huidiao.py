# async def greet(name):
#     print(f"Hello, {name}!")
#     await asyncio.sleep(1)
#     print(f"Goodbye, {name}!")
#
#
# async def main():
#     task1 = asyncio.create_task(greet("Alice"))
#     task2 = asyncio.create_task(greet("Bob"))
#
#     await task1
#     await task2
#
#
# asyncio.run(main())


def do_operation(x, y, callback):
    # 回调函数是一种常见的编程概念，它指的是将一个函数作为参数传递给另一个函数，在特定条件满足时被调用执行。回调函数通常用于处理异步操作、事件处理和定制逻辑，允许代码更灵活地响应不同的情况。
    # 在实际应用中，回调函数可以用于处理异步操作，例如网络请求的结果、定时任务的完成等情况。通过将回调函数作为参数传递，代码可以更加模块化和灵活，适应不同的业务逻辑。
    result = x + y
    callback(str(result))


def callback_function(result):
    print("callback_function is run  result is:", result)


# 调用 do_operation 函数，并传入 callback_function 作为回调函数
if __name__ == '__main__':
    do_operation(10, 20, callback_function)



