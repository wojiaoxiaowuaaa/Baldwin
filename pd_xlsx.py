import pandas as pd

# 读取 Excel 文件
file_path = '/Users/wl/Downloads/接口请求上报量汇总前1W.xlsx'
df = pd.read_excel(file_path)

# 打印表头（列名）
# print("表头：", df.columns)

# 打印前几行数据
print(df.head())

# 基本统计信息
# print("基本统计信息：")
# print(df.describe())

# 根据列进行筛选
# selected_column = 'path'
# selected_data = df[selected_column]
# print(selected_data)
