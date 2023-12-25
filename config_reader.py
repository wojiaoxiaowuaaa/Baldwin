import configparser

config = configparser.ConfigParser()
config.read("/Users/wl/Desktop/ZhaoSongPy/config.ini")  # 指定配置文件路径

# 从配置文件中读取变量
filename = config["MyConfig"]["filename"]
output_dir = config["MyConfig"]["output_dir"]
desktop = config["MyConfig"]["desktop"]
save_path = config["MyConfig"]["save_path"]
