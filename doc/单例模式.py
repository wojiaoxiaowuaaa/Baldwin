def singleton(cls):
    """单利模式装饰器写法
    instances = {<class '__main__.Singleton'>: <__main__.Singleton object at 0x10bc004f0>}"""

    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    # print(instances)
    return get_instance


@singleton
class Singleton:
    pass


a = Singleton()
b = Singleton()
print(a is b)
