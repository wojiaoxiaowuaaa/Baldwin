"""元类(metaclass)是Python中的一个高级概念,用于创建类本身.
`metaclass` 关键字:
在Python中,可以通过 `metaclass` 关键字在类定义时指定元类.如果没有指定,Python会使用内建的 `type` 作为元类.

`Singleton` 元类的作用:
`Singleton` 元类的作用是确保一个类只有一个实例.这是通过拦截类的实例化过程(即拦截 `__call__` 方法)来实现的.
当尝试创建一个实例时,`Singleton` 会检查该类的实例是否已经存在:
- 如果实例不存在,`Singleton` 会创建一个实例,并将其存储,以便后续的创建请求可以返回同一个实例.
- 如果实例已存在,直接返回存储的实例.
这样,无论何时何地尝试创建类的实例,都只会得到同一个实例对象,从而实现了单例模式.

 总结:
元类是Python中用于创建类的类.通过自定义元类,可以控制类的创建过程,实现一些高级功能,如单例模式.
`Singleton` 元类通过控制类的实例化过程,确保一个类只有一个实例,展示了元类的强大功能."""


class Singleton(type):
    __instances = {}  # __instances 是一个类变量,用于存储已创建的实例.字典的键是类,值是该类的实例.

    def __call__(cls, *args, **kwargs):  # cls-当前类.这段代码检查类是否已有实例.如果没有,创建一个新实例并存储;如果有,直接返回已存储的实例.
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]


if __name__ == '__main__':
    class My(metaclass=Singleton): pass  # noqa: E701

    a = My()
    b = My()
    
    print(a is b)
