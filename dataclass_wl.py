from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str = None


p1 = Person("是小舞", 18)
p2 = Person("不是小武", 88, "test@163.com")
print(p1)
print(p2)
print(p1 == p2)
