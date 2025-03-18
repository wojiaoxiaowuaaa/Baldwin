class Singleton:
    """重写__new__方法,实现单例模式"""
    _instance = None  # 类属性,用于存储当前类的唯一实例.

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def singleton(cls):
    """单例模式的装饰器写法,字典的key是类名,value是类的实例对象.
    instances = {<class '__main__.Singleton'>: <__main__.Singleton object at 0x10bc004f0>}
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


# @singleton
# class Singleton: pass

class Printer:
    """使用类名创建对象时Python解释器做的事:
    1. 为对象在内存中分配空间
    2. 为对象进行初始化

    new方法在内部做了两件事:
    1. 为对象分配空间
    2. 把对象的引用返回给Python解释器
    Python解释器拿到对象的引用之后,就会把对象的引用传递给init方法的第一个参数self,init拿到对象引用之后,就可以在方法的内部,针对对象来定义实例属性, 这就是new和init的分工
    """

    def __init__(self):
        print("init  初始化")

    def __new__(cls, *args, **kwargs):
        print("new___")
        instance = super(Printer, cls).__new__(cls)
        return instance  # 重写new方法一定要返回对象的引用,否则Python解释器得不到分配了空间的对象引用,就不会调用对象的初始化方法.

# print(Printer())  # 创建对象时 new方法会被自动调用(时间上早于init方法)
