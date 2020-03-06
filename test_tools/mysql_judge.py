'''
Created on 2017年4月20日

@author: Jin
'''
import pymysql

def getmysqldata(hsql,hval,hdatahope):
    connect = pymysql.Connect(
        host='*.*.*.*',
        port=8066,
        user='*****',
        passwd='******$',
        db='****',
        charset='utf8'
    )#这个地址这些填自己的数据库地址哟。
    # 获取游标
    cursor = connect.cursor()
    # 查询数据
    cursor.execute(hsql ) #执行sql
    print('共查找出', cursor.rowcount, '条数据')    
    if cursor.rowcount ==0:
        print("数据库中没有找到你要的值")
        print("测试不通过")
        assert 1 ==2
    else:
        hrow = cursor.fetchone()
        print(hrow)#打印出数据库查询的数据
        hdata = hrow[hval]#提取出需要进行比对的值
        print('数据库的值:'+str(hdata))
        assert str(hdata) ==hdatahope#与预期值做对比
        print("添加或查询的结果与数据库一致！")
    cursor.close()
    connect.close()
