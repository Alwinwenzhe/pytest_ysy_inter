'''
Created on 2017年4月20日
文件名：get_token.py
@author: 浪晋
'''
import json
import requests
import xlrd
from xlutils.copy import copy
from test_tools import get_excle_data       # 引入py文件

Testdata = get_excle_data.Testdata_p#获取公共表的数据
file_home = get_excle_data.file_home
table = Testdata.sheets()[0]#选择sheet
hurl = table.cell(7,1).value#读取URL

def get_token_to_data():
    '''登陆'''
    turl = hurl + table.cell(10,1).value
    hdata = {
        "username":table.cell(3,1).value,
        "password":table.cell(4,1).value,
        "otp":table.cell(5,1).value}
    headers = {'content-type': table.cell(6,1).value
       }
    r = requests.post(turl, data=json.dumps(hdata), headers=headers)
    hjson = json.loads(r.text)#获取并处理返回的json数据
    herror ="error"

    if herror in hjson:
        print("登陆失败，退出程序！")
        exit()
    else:
        hcode = str(hjson['code'])
        print('请求返回状态为：'+hcode)
        if hcode == table.cell(9,1).value:
            token = hjson['data']['token']#获取token
            print('当前token为：'+token)
            #将获取的token保存到testdata中
            oldWb = xlrd.open_workbook(file_home+'test_data_p.xls',formatting_info=True)
            newWb = copy(oldWb)
            newWs = newWb.get_sheet(0)
            newWs.write(8, 1, token)
            print ("Token写入成功")
            newWb.save(file_home+'test_data_p.xls')
            print ("test_data_p保存成功")
        else:
            print('登陆失败，程序退出')
            exit()

#get_token_to_data()
