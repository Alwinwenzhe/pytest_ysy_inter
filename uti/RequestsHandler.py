import json
import requests
from bs4 import BeautifulSoup
from uti.LoggerHandler import logger


class RequestHandler(object):
    '''
    请求相关
    '''

    def __init__(self, case):
        self.case = case
        try:
            self.case_expect = json.loads(self.case['case_expect'])
        except:
            self.case_expect = self.case['case_expect']

    @property
    def get_response(self):
        """ 获取请求结果 """
        response = self.send_request()
        return response

    def send_request(self):
        """ 发请求 """
        try:
            response = requests.request(
                method=self.case['case_method'],
                url=self.case['case_url'],
                params=self._check_params()             # 调用私有方法，外部类不要去访问它
            )
            # ## 这里通过response返回的Content-Type，进行内容格式判断
            # content_type = response.headers['Content-Type']
            # content_type = content_type.split(";")[0].split('/')[-1] if ';' in content_type else \
            # content_type.split("/")[-1]
            # ## 判定格式后，对返回内容进行取值
            # if hasattr(self, '_check_{}_response'.format(content_type)):                # hasattr() 函数用于判断对象是否包含对应的属性
            #     response = getattr(self, '_check_{}_response'.format(content_type))(response)           # getattr() 函数用于返回一个对象属性值，，这里会跳转到_check_html_response
            # else:
            #     raise '返回类型为: {}, 无法解析'.format(content_type)
        except:
            ## 如果格式判断和取值异常，就返回固定内容，这里并不适合我们接口约定，从内容判断和取值都得修改
            logger().error({'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])})
            return {'response': "请求发送失败，详细信息： url={}".format(self.case['case_url'])}, self.case['case_expect']
        return response.text,self.case['case_expect']

    def _check_json_response(self, response):
        """  处理json类型的返回值 """
        response = response.json()  # {'success': True}
        for key in self.case_expect:
            if self.case_expect[key] != response[key]:  # 用例执行失败的
                return {key: self.case_expect[key]}, {key: response[key]}
        else:  # 执行成功
            logger("发送请求").info('{} 执行成功'.format(self.case['case_url']))
            return {key: self.case_expect[key]}, {key: response[key]}

    def _check_html_response(self, response):
        """ 校验html类型的数据"""
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        title = soup_obj.find('title').text
        return title, self.case_expect

    def _check_params(self):
        """ 整理参数 """
        if self.case['case_params']:
            """
            做扩展
            """
            return self.case['case_params']
        else:
            return {}
