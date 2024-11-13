import openpyxl


class ExcelModifier:
    def __init__(self, file_path):
        """
        :param file_path: 待处理的文件路径
        初始化方法，用于加载工作簿
        """
        self.workbook = openpyxl.load_workbook(filename=file_path)
        self.sheet = self.workbook.active

    def duplicate_first_row(self, output_path):
        """
        将第一行的数据复制到后续行.
        :param output_path: 处理后输出文件路径
        """
        first_row_data = [cell.value for cell in self.sheet[2]]

        for row in range(3, 2001):
            for col, value in enumerate(first_row_data, start=1):
                self.sheet.cell(row=row, column=col, value=value)

        # 保存修改后的工作簿
        self.workbook.save(output_path)

    def increment_first_column(self, output_path):
        """
        从第二行开始，每一行第一列的值递增
        :param output_path: 处理后输的出文件路径
        """
        start_value = 8166460001

        # 从第二行开始，每一行第一列的值递增
        for row in range(2, self.sheet.max_row + 1):
            self.sheet.cell(row=row, column=1, value=start_value)
            start_value += 1

        # 保存修改后的文件
        self.workbook.save(output_path)

if __name__ == "__main__":
    modifier = ExcelModifier("/Users/wl/Downloads/big_new_file.xlsx")
    modifier.duplicate_first_row("/Users/wl/Downloads/output.xlsx")
    modifier.increment_first_column("/Users/wl/Downloads/wl.xlsx")