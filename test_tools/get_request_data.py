import json
import requests

def PostRequest(turl,hdata,headers,hcodehope):
    hr  = requests.post(turl,data=json.dumps(hdata), headers=headers)
    hjson = json.loads(hr.text)#获取并处理返回的json数据
    print('测试数据：'+str(hdata))
    print('返回的内容为:'+str(hjson))
    assert "error" not in hjson
    print('获取到的状态是：'+str(hjson['code'])+'，预期的状态是：'+hcodehope)
    assert str(hjson['code']) == hcodehope
    print('返回值对比通过')
