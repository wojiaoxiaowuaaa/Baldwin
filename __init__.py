"""
Python的json模块提供了把内存中的对象序列化的方法.
dump的功能就是把Python对象encode为json对象,一个编码过程。
注意json模块提供了json.dumps和json.dump方法,区别是dump可以直接写到文件中,而dumps到一个字符串,这里的s可以理解为string。
load的功能是把json对象decode解码为Python对象.如果是文件类型使用json.load()如果是string类型则使用json.loads()
"""
