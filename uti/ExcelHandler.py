import xlrd
import conf


class ExcelHandler(object):

    def __init__(self):
        # 私有属性
        self.__number = 0

    @property   # property装饰器就是负责把一个方法变成属性调用的
    def get_excel_data(self):
        # 获取到book对象
        book = xlrd.open_workbook(conf.TEST_CASE_PATH)
        # print(book)
        # 获取sheet对象
        sheet = book.sheet_by_index(1)
        # sheet = book.sheet_by_name('接口自动化用例')
        # sheets = book.sheets()  # 获取所有的sheet对象

        rows, cols = sheet.nrows, sheet.ncols
        l = []
        # print(sheet.row_values(0))
        title = sheet.row_values(0)
        # print(title)
        # 获取其他行
        for i in range(1, rows):
            # print(sheet.row_values(i))
            l.append(dict(zip(title, sheet.row_values(i))))
        return l

EH = ExcelHandler()
EH.get_excel_data       # 直接调用