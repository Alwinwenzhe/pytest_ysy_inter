# -*- coding:utf-8 -*-

'''
文件名：get_excle_data.py
Created on 2017年4月20日
@author: 浪晋
'''
import xlrd, pytest

#定义一个变量用于存放测试数据的路径
file_home = r'D:\Job\python\Script\pytest_ysy_inter\test_data'
#公共数据
Testdata_p = xlrd.open_workbook(file_home+ r'\test_data_1.xlsx')#读取公共测试数据
table_p = Testdata_p.sheets()[0]#选择sheet
account = table_p.cell(2,1).value#读取测试账户
domain =table_p.cell(3,1).value#读取接口域名
header = table_p.cell(4,1).value#读取header
print(account,domain,header)
#测试流程的数据
Testdata_s = xlrd.open_workbook(file_home+r'\test_data_1.xlsx')#读取测试流程的数据
#测试模块的数据
Testdata_m = xlrd.open_workbook(file_home+r'\test_data_1.xlsx')#读取测试模块的数据

