class Student:
    """
    变量是对内存及其地址的抽象;
    每当有一个变量名指向一块内存地址时,这个内存地址中对应内容的引用计数就会+1;
    :name/age --- 类属性

    当你运行一个 Python 脚本时,操作系统会启动一个新的进程,并在这个进程中运行 Python 解释器.这个进程的生命周期从脚本开始执行到脚本结束.有自己的内存空间和资源分配，独立于其他进程运行.
    这个进程是脚本执行的独立环境，拥有自己的地址空间、文件描述符、环境变量等资源。

    Python 脚本执行流程
    1.启动过程：
    当你通过命令行输入 python script.py 时，操作系统首先查找 python 的可执行文件。
    找到后，操作系统创建一个新的进程，并将 python 可执行文件加载到这个进程中。
    2.代码执行：
    Python 解释器开始执行 script.py 文件中的代码。
    解释器逐行解析和执行代码，可能会加载更多的模块和执行更多的函数。
    3.资源使用：
    在执行过程中，进程可能会请求操作系统提供更多资源（如内存、文件句柄等）。
    Python 的垃圾回收机制会定期清理不再使用的内存。
    4.进程结束：
    脚本执行完成后，Python 解释器会结束，操作系统会清理该进程使用的所有资源，并关闭进程.
    """

    name: str = "sale"
    age: int = 18

    def __init__(self, a: int, b: int):
        self.a = a  # 将形参 a 的值赋值给实例属性self.a
        self.b = b  # 将形参 b 的值赋值给实例属性self.b

    def func(self):
        print(
            self
        )  # <__main__.Student object at 0x1048c6d90>  与第38行的输出相同(证明self就是类实例出的对象本身)
        # print(self.aa)  #  因为init方法中没有声明self.aa这里会报错. self.aa = aa 这一行代码的作用是将传入的参数 aa 赋值给该对象实例的 aa 属性。这样，每个被创建的 Student 类的实例都会有一个 aa 属性，并且该属性的值会根据传入的参数而不同。


Student.func(
    Student(100, 200)
)  # Student(100, 200)整体,作为实例出来的对象,作为实参传递给func方法的形参self
print(Student(100, 200))  # <__main__.Student object at 0x1048c6d90>
