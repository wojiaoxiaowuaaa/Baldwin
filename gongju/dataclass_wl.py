from dataclasses import dataclass, asdict

"""
dataclass 是 Python 3.7 引入的一个装饰器，用于简化创建类并自动生成一些通用的特殊方法，
如 __init__.py.py、__repr__、__eq__ 等。它旨在简化数据类的定义，特别适用于用于存储数据的类。
"""


@dataclass
class Person:
    name: str
    age: int
    city: str
    amail: str = None


person = Person("小舞", 30, "New York")

# 自动生成的特殊方法   __repr__( 打印对象时调用的魔法方法)
print(person)

# 调用 __eq__
print(person == Person("John", 31, "beijing"))

# 得到字典类型的数据
data = asdict(person)
print(data)