import os

# res = os.system('echo $PATH ') 会执行命令,返回值是命令的退出状态码而不是输出内容.0表示成功.
# path_value用来获取当前环境中的PATH变量值。这意味着它会返回一个字符串，里面包含了所有被系统用于寻找可执行文件的目录路径。这对于确定系统如何找到和运行命令，以及如何添加或修改路径以便系统能够识别新的可执行文件位置非常重要.
path_value = os.getenv("PATH")

for i in path_value.split(":"):
    print(i)
