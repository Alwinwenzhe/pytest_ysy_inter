from test_tools import get_excle_data
hurl =get_excle_data.hurl
hcontent_type =get_excle_data.content_type
htoken = get_excle_data.htoken
Testdata = get_excle_data.Testdata_m
def reviewowner_data():
    table = Testdata.sheets()[0]#选择excle表中的sheet
    htestdata = []#定义的数组，用来装测试数据
    for i in range(8,9):
        hdata = {
            "oid": table.cell(i,3).value,
            "statusAudit": table.cell(i,4).value,
            "remark": table.cell(i,5).value
        }
        headers = {
            "content-type":hcontent_type,
            'token': htoken
            }

        hremark= table.cell(i,11).value
        turl = hurl+table.cell(i,2).value
        hcodehope = table.cell(i,15).value
        hsql= table.cell(i,17).value+table.cell(i,18).value#这个是数据库的方法需要的
        hval= int(table.cell(i,19).value)   #这个是数据库的方法需要的
        hdatahope= table.cell(i,20).value   #这个是数据库的方法需要的
        valuedatas = (hremark,turl,hdata,headers,hcodehope,hsql, hval, hdatahope)
        htestdata.append(valuedatas)#添加到数组
    return htestdata
