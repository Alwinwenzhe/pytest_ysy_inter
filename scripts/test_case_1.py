import pytest
import allure
from uti.ExcelHandler import ExcelHandler
from uti.RequestsHandler import RequestHandler
from uti.AllureHandler import AllureHandler
from uti.EmailHandler import EmailHandler
'''
1. 拿到Excel数据
2. 发请求
3. 生成测试用例报告
4. 发邮件
5. 断言

'''

class Test_case(object):

    @pytest.mark.parametrize('case', ExcelHandler().get_excel_data)         # 将获取的所有数据通过参数case，传入test_case，case作为list，会逐一传入
    def test_case(self, case):
        """  执行断言 """
        # print(case)
        # 发请求
        response = RequestHandler(case).get_response

        # 制作 allure 报告
        allure.dynamic.title(case['case_project'])
        allure.dynamic.description('<font color="red">请求URL：</font>{}<br />'
                                   '<font color="red">期望值：</font>{}'.format(case['case_url'], case['case_description']))
        allure.dynamic.feature(case['case_project'])
        allure.dynamic.story(case['case_method'])
        assert response[1] in response[0]

    def teardown_class(self):
        """  执行alllure命令 """

        AllureHandler().execute_command()
        # 发邮件  暂时使用jenkins替代
        # EmailHandler().send_email()


if __name__ == "__main__":
    rh = Test_case()
    temp = rh.test_case()
    print(temp)