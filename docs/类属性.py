class MyClass:
    """类属性通常用于存储与类相关的信息 这些信息对于该类的所有实例都是通用的 而不是每个实例都需要单独存储一份.
    例如可以用类属性来记录类的创建次数,所有实例共享的常量等.这样可以节省内存空间并且方便对这些共享信息进行统一的管理和维护
    """

    def __init__(self):
        pass

    @classmethod
    def define_class_attribute(cls):
        cls.class_attribute = "This is a class attribute defined in a class method"

    def access_class_attribute(self):
        print(self.class_attribute)  # 通过 self 访问类属性


# 创建类的实例
instance = MyClass()
# instance.define_class_attribute()  # 调用类方法定义类属性
instance.access_class_attribute()  # 输出: This is a class attribute defined in a class method
