import os

# res = os.system('echo $PATH ')   会执行命令 返回值是命令的退出状态码而不是输出内容  0表示成功

path_value = os.getenv('PATH')

sansa = path_value.split(':')

for i in sansa: print(i)
