# 一般情况下，__new__ 方法不需要手动调用，因为在对象创建时，Python 解释器会自动调用它。
# __new__ 负责对象的创建和内存的分配，而 __init__ 方法则负责对象的初始化。在很多情况下，你只需要重写 __init__ 方法，因为大部分对象的创建和初始化都可以在这个方法中完成
class User:
    __instance = None  # 类变量  初始化为None  存储唯一的实例对象(重写new方法实现单例模式)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  # 重写new方法  创建实例之前检查是否已经存在实例
            cls.__instance = super().__new__(cls, *args, **kwargs)  # 调用父类的 __new__ 方法，创建一个新的实例，并将其赋值给 __instance。这里调用父类的 __new__ 方法，确保正确地创建实例。
        return cls.__instance  # 返回存储在 __instance 中的唯一实例。


def singleton(cls):
    """单例模式的装饰器写法,字典的key是类名,value是类的实例对象.
    instances = {<class '__main__.Singleton'>: <__main__.Singleton object at 0x10bc004f0>}"""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    pass


a = Singleton()
b = Singleton()
print(a is b)


class Printer:
    """使用类名创建对象时Python解释器做的事:
    1. 为对象在内存中分配空间
    2. 为对象进行初始化

    new方法在内部做了两件事:
    1. 为对象分配空间
    2. 把对象的引用返回给Python解释器
    Python解释器拿到对象的引用之后,就会把对象的引用传递给init方法的第一个参数self,init拿到对象引用之后,就可以在方法的内部,针对对象来定义实例属性, 这就是new和init的分工"""

    def __init__(self):
        print("init  初始化")

    def __new__(cls, *args, **kwargs):
        print("new___")
        instance = super().__new__(cls)
        return instance  # 重写new方法一定要返回对象的引用,否则Python解释器得不到分配了空间的对象引用,就不会调用对象的初始化方法.


obj = Printer()  # 创建对象时 new方法会被自动调用(时间上早于init方法)
print(obj)
