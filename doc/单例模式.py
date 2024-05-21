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


"""

class User:
    __instance = None  # 类变量  初始化为None  存储唯一的实例对象

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  # 重写new方法  创建实例之前检查是否已经存在实例
            cls.__instance = super().__new__(cls, *args, **kwargs)  # 调用父类的 __new__ 方法，创建一个新的实例，并将其赋值给 __instance。这里调用父类的 __new__ 方法，确保正确地创建实例。
        return cls.__instance  # 返回存储在 __instance 中的唯一实例。
        

一般情况下，__new__ 方法不需要手动调用，因为在对象创建时，Python 解释器会自动调用它。
总结一下，__new__ 负责对象的创建和内存的分配，而 __init__ 方法则负责对象的初始化。在很多情况下，你只需要重写 __init__ 方法，因为大部分对象的创建和初始化都可以在这个方法中完成。

"""