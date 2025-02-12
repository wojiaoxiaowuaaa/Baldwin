"""
生成器send方法和next方法唯一的区别在于:执行send方法会首先把上一次挂起的yield语句的返回值通过参数设定,从而实现与生成器方法的交互.
但是需要注意,在一个生成器对象没有执行next方法之前,由于没有yield语句被挂起,所以执行send方法会报错.例如

def MyGenerator():
    value = yield 1
    value = yield value

gen = MyGenerator()
print(gen.send(2))

我们可以将.__next__方法看作是生成器函数函数体执行的驱动器.

针对yield表达式,先执行yield i,然后才是赋值.yield把i值返回给调用者后,执行的下一步操作是赋值,本来可以好好地赋值给x,
但却因为等号右边的yield关键字而被暂停,此时生成器函数执行到赋值这一步,换句话说x = yield i这句话才执行了一半.
当调用者通过调用send(value)再次回到生成器函数时,此时是回到了之前x = yield i这个赋值表达式被暂停的那里,
刚才我们说过生成器函数执行到了赋值这一步,因此接下来就要真正开始执行赋值操作啦,也即是执行语句x = yield i的另一半过程:赋值.
这个值就是调用者通过send(value)发送进生成器的值,也即是yield i这个表达式的值.


def coroutine():
    # coroutine函数定义了一个协程,它通过一个无限循环等待从外部发送的值,并打印接收到的值.当协程被首次启动时,它会暂停在yield语句处,等待接收一个值.
    # 然后,我们通过send方法向协程发送了两个值,协程每次接收到值后都会打印出来.
    # 需要注意的是,第一次启动协程时,需要调用next(c)或者c.send(None)来启动协程,否则会抛出TypeError异常.
    while True:
        received_value = yield
        print("Received:", received_value)

# 创建一个协程对象
c = coroutine()

# 启动协程
next(c)

# 发送值给协程
c.send("Hello")

# 继续发送值给协程
c.send("World")

"""

from tool import color_print_green, color_print_red


def func():
    print(1)
    yield 2
    print(3)
    value = yield 4
    print(5)
    yield value


g = func()
print(g.__next__())
color_print_green()
print(g.send("打印了吗打印了吗打印了吗打印了吗?"))
color_print_red()
print(g.__next__())
