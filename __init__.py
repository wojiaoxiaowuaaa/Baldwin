# 过设置 PYTHONPATH 环境变量,你可以指定 Python 解释器在查找模块和包时应该搜索的目录.这使得你能够在自定义目录中组织和管理你的 Python 模块和包,而不需要将它们复制到标准库路径或当前脚本目录中.
# export PYTHONPATH="/Users/wl/Downloads/Baldwin:$PYTHONPATH" (写到.zshrc文件中可永久生效)

# os.path.insert(0, "..") 添加当前脚本的上级目录到系统路径列表的开头

# only_name = str(uuid.uuid4()).replace("-", "")

# wl_dir = Path(__file__).resolve().parents[2]

# python -c 'import os; print(os.getenv("CONSUL_DEMO"))'
