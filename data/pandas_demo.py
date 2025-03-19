import pandas as pd

# 将根目录加入到系统路径中 否则下一行的导入在终端执行时会报错找不到对应的模块. BASE_PATH : /Users/wl/Downloads/Baldwin
# if (BASE_PATH := os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) not in sys.path: sys.path.insert(0, BASE_PATH)

# file_path = "/Users/wl/Documents/1675678004817.xlsx"
# df = pd.read_excel(file_path)

# 打印表头（列名）
# print("表头：", df.columns)

# 打印前几行数据
# print(df.head())

# 基本统计信息
# print("基本统计信息：")
# print(df.describe())

# 根据列进行筛选
# selected_column = 'path'
# selected_data = df[selected_column]
# print(selected_data)


# 创建一个二维数据结构:DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(data)

# 打印 DataFrame
print(df)
# to_xlsx 方法保存 DataFrame 到 Excel 文件
# df.to_csv('output.csv', index=False)
