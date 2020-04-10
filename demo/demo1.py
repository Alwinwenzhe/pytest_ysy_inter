import xlrd
import json
import requests
from bs4 import BeautifulSoup

import xlrd

# row 是行
# col 是列

def get_excel_data():
    '''
    将excel中某个sheet数据，转化为了键值对
    :return:
    '''
    file_path = r'D:\Job\python\Script\pytest_ysy_inter\demo\接口示例.xlsx'

    # 获取到book对象
    book = xlrd.open_workbook(file_path)
    # print(book)
    # 获取sheet对象
    sheet = book.sheet_by_index(0)
    # sheet = book.sheet_by_name('接口自动化用例')
    # sheets = book.sheets()  # 获取所有的sheet对象

    rows, cols = sheet.nrows, sheet.ncols       # 获取到所有的行和列 sheet.nrows方法, sheet.ncols方法
    l = []
    # print(sheet.row_values(0))
    title = sheet.row_values(0)     # 按照索引取出第一列key
    # print(title)
    # 获取其他行
    for i in range(1, rows):
        # print(sheet.row_values(i))
        l.append(dict(zip(title, sheet.row_values(i))))     # 将行和列的值拼接在一起 组合成[{},{}]的样式 zip拉在一起 dict转一下

    return l

data =get_excel_data()

# 通过爬虫库直接定位标签内容
r = requests.get('https://www.cnblogs.com/Neeo/articles/11667962.html')
s = BeautifulSoup(r.text, 'lxml')           # 通过爬虫库lxml解析器将网页转化为utf-8内容输出
                                            # lxml是python的一个解析库，支持HTML和XML的解析，支持XPath解析方式，而且解析效率非常高
print(s.find('title').text)                 # 查找标签名为title，并显示其文本内容
print("*" * 30)
# print("s:",s)
print ("type(s):",type(s))
print("*" * 30)