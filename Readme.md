# 一、概述

框架采用excle+pytest+jenkins+allure的结构，使用数据驱动方式进行开发测试。能够达到单个接口的多种测试数据的组合测试，以及基于业务流程的接口组合测试。考虑到测试人员编写测试用例的方便性，采用数据驱动的设计方式，将数据分层出来，与业务逻辑剥离。这样测试人员就可以通过数据文件专注的写测试用例，不用关注代码编写，提高了效率。通过与jenkins的集成，使用allure生成测试报告，能够一目了然的看到测试的执行情况。若开发也采用的jenkins集成环境，甚至可以达到与开发集成，自动编译、部署、测试的高度自动化流程。
本框架适用于基于HTTP的接口自动化测试。

# 二、结构说明

FreeTestGo #项目名称
FreeTestGo #项目名称
- ├─test_cass #用于存放测试用例的脚本
- │ └─init.py
- │ └─test_cass_01.py #测试用例1
- │ └─test_cass_02.py #测试用例2
- ├─test_data #用于存放测试数据
- │ └─test_data_1.xlsx #测试数据1
- │ └─test_data_2.xlsx #测试数据2
- ├─test_get_data #用于存放读取测试数据的方法
- │ └─init.py
- │ └─get_test_data_01.py #方法1
- │ └─get_test_data_02.py #方法2
- ├─test_log #用于存放测试日志
- │ └─test_log.txt
- ├─test_report #用于存放allure生成测试报告依赖的文件
- │ └─test_report.xml
- ├─test_suite #用于存放测试流程的脚本
- │ └─init.py
- │ └─test_suite_01.py #测试用例1
- │ └─test_suite_02.py #测试用例2
- ├─test_tools #用于存放封装的各种公共方法
- │ └─init.py
- │ └─test_tools.py
- ├─pytest.ini #配置文件，可配置运行的参数以及选择需要运行的用例等
- └─runtests.py #执行入口