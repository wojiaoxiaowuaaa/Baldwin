def logger(level):
    def decorate(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print("Warn Info")
            elif level == "error":
                print("error Info")
            return func(*args)

        return wrapper

    return decorate


@logger(level="error")  # 先调用了工厂函数，返回了装饰器
def myname(name="ali"):
    print("My name is %s" % name)


myname()
