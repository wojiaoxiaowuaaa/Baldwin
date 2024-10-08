class Student:
    """
    变量是对内存及其地址的抽象;
    每当有一个变量名指向一块内存地址时,这个内存地址中对应内容的引用计数就会+1;

    在 Python 中,方法如下面的func,属于类的命名空间,而不是实例的命名空间.这意味着方法是定义在类层面上的,所有实例共享同一个方法,而不是每个实例都有自己的方法副本.
    当你访问实例的方法时,Python 会在类的命名空间中查找该方法.因此,func 作为一个方法,存在于 Student 类的命名空间中,可以通过 Student.__dict__ 查看到,
    而不是在每个实例的 __dict__ 中.简而言之,__dict__ 属性只包含实例属性的信息,不包括类属性(如类变量和方法).
    当你运行一个 Python 脚本时,操作系统会启动一个新的进程,并在这个进程中运行 Python 解释器.这个进程的生命周期从脚本开始执行到脚本结束.
    有自己的内存空间和资源分配,独立于其他进程运行.这个进程是脚本执行的独立环境,拥有自己的地址空间、文件描述符、环境变量等资源.

    Python 脚本执行流程
    1.启动过程:
    当你通过命令行输入 python script.py 时,操作系统首先查找 python 的可执行文件.
    找到后,操作系统创建一个新的进程,并将 python 可执行文件加载到这个进程中.
    2.代码执行:
    Python 解释器开始执行 script.py 文件中的代码.
    解释器逐行解析和执行代码,可能会加载更多的模块和执行更多的函数.
    3.资源使用:
    在执行过程中,进程可能会请求操作系统提供更多资源(如内存、文件句柄等).
    Python 的垃圾回收机制会定期清理不再使用的内存.
    4.进程结束:
    脚本执行完成后,Python 解释器会结束,操作系统会清理该进程使用的所有资源,并关闭进程.
    """

    name: str = "sale"  # 类属性(类变量)

    def __init__(self, a: int, b: int):
        self.a = a  # 将形参 a 的值赋值给实例属性self.a
        self.b = b  # 实例属性
        # age = 18  # 局部变量(不会保存到__dict__中)

    def func(self):  # 类属性(或者类方法不会保存到__dict__中)
        print(self)  # <__main__.Student object at 0x1048c6d90>  与第40行的输出相同(证明self就是类实例出的对象本身)
        print(self.name)  # 在Python中,类变量是属于类的变量,它被所有该类的实例共享.当你通过实例访问一个属性时,Python会首先尝试在该实例的__dict__中查找该属性.如果没有找到,它会继续在该实例所属类的__dict__中查找,这就是为什么可以通过self引用类变量的原因.
        # print(self.aa)  #  因为init方法中没有声明self.aa这里会报错. self.aa = aa 这一行代码的作用是将传入的参数 aa 赋值给该对象实例的 aa 属性.这样,每个被创建的 Student 类的实例都会有一个 aa 属性,并且该属性的值会根据传入的参数而不同.


Student.func(Student(100, 200))  # Student(100, 200)整体,作为实例出来的对象,作为实参传递给func方法的形参self
print(Student(100, 200))  # <__main__.Student object at 0x1048c6d90>
