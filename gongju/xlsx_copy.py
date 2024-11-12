from openpyxl import load_workbook

def duplicate_first_row(file_path, output_path):
    # 加载工作簿和工作表
    workbook = load_workbook(filename=file_path)
    sheet = workbook.active

    # 获取第二行的数据 首行是表头
    first_row_data = [cell.value for cell in sheet[2]]

    # 将第一行的数据复制到后续1999行
    for row in range(6, 2002):
        for col, value in enumerate(first_row_data, start=1):
            sheet.cell(row=row, column=col, value=value)

    # 保存修改后的工作簿
    workbook.save(output_path)


duplicate_first_row('/Users/wl/Downloads/test_bike.xlsx', './Downloads/output.xlsx' )
