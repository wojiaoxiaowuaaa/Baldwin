# 过设置 PYTHONPATH 环境变量,你可以指定 Python 解释器在查找模块和包时应该搜索的目录.这使得你能够在自定义目录中组织和管理你的 Python 模块和包,而不需要将它们复制到标准库路径或当前脚本目录中.  export PYTHONPATH="/Users/wl/Downloads/Baldwin:$PYTHONPATH" (写到.zshrc文件中可永久生效)

# mac下的brew安装的解释器路径: /usr/local/Cellar/python@3.13/3.13.1/Frameworks/Python.framework/Versions/3.13/bin

# echo $PATH命令在Mac终端(或任何Linux系统)中用于显示当前用户的环境变量PATH的内容.PATH环境变量包含了一系列的目录,这些目录被操作系统用来搜索可执行文件.

# os.system("ls -l") 直接执行命令;home_dir = os.environ.get("HOME")获取主目录;home_dir = os.environ.get("PATH")获取环境变量;

# os.path.insert(0, "..") 添加当前脚本的上级目录到系统路径列表的开头

# only_name = str(uuid.uuid4()).replace("-", "")

# wl_dir = Path(__file__).resolve().parents[2]

# with open('config/config.toml', 'r') as f: config = toml.load(f)

# from tool import replace_punctuation_in_file
# replace_punctuation_in_file("/Users/wl/Downloads/Baldwin/wl_mt.py")  # 文件标点替换
