class Student:
    """
    变量是对内存及其地址的抽象;
    每当有一个变量名指向一块内存地址时,这个内存地址中对应内容的引用计数就会+1;
    :name/age --- 类属性
    """
    name = "sale"
    age = "18"

    def __init__(self, aa, bb):
        print("init function is run --->")
        print(aa)
        print(bb)

    def fun1(self):
        print("function 1 is run")
        print(self)  # <__main__.Student object at 0x1048c6d90>  与第22行的输出相同(证明self就是类实例出的对象本身)
        # print(self.aa)  #  因为init方法中没有声明self.aa = aa这里会报错. self.aa = aa 这一行代码的作用是将传入的参数 aa 赋值给该对象实例的 aa 属性。这样，每个被创建的 Student 类的实例都会有一个 aa 属性，并且该属性的值会根据传入的参数而不同。


Student.fun1(Student(100, 200))  # Student(100, 200)整体,作为实例出来的对象,作为实参传递给func1方法的形参self
# print(Student(100, 200))  # <__main__.Student object at 0x1048c6d90>
