"""
Python的json模块提供了把内存中的对象序列化的方法.
dump的功能就是把Python对象encode为json对象,一个编码过程。
注意json模块提供了json.dumps和json.dump方法,区别是dump可以直接写到文件中,而dumps到一个字符串,这里的s可以理解为string。
load的功能是把json对象decode解码为Python对象.如果是文件类型使用json.load()如果是string类型则使用json.loads()

UTF-8 是 Unicode 字符集的一种编码方式，它定义了如何将 Unicode 中的字符以字节序列的形式存储。
Unicode 是字符集，UTF-8 是编码方式： Unicode 是一个字符集，定义了字符和其唯一代码点的对应关系。

基于指定的解释器创建虚拟环境(这里是基于pypy创建虚拟环境)
virtualenv  -p  /Users/wl/Downloads/pypy3.10-v7.3.15-macos_x86_64/bin/pypy  venv_name
激活虚拟环境
source /venv_name/bin/activate
退出虚拟环境
deactivate
"""


