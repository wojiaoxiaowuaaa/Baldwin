class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    def introduce(self):
        # 实例方法中可以访问实例属性
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def get_population(cls):
        # 类方法中不能直接访问实例属性
        print(f"Total population: {cls.population}")

    @staticmethod
    def is_adult(age):
        # 静态方法中不能访问实例属性
        return age >= 18

    @classmethod
    def create_person(cls, name, age):
        # 类方法中创建实例并访问实例属性
        person = cls(name, age)
        print(f"Created a person named {person.name} who is {person.age} years old.")
        return person

# 创建对象实例
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 调用实例方法
person1.introduce()  # 输出: Hello, my name is Alice and I am 30 years old.

# 调用类方法
Person.get_population()  # 输出: Total population: 2

# 调用静态方法
print(Person.is_adult(20))  # 输出: True

# 类方法中创建对象并访问实例属性
person3 = Person.create_person("Charlie", 22)  # 输出: Created a person named Charlie who is 22 years old.
