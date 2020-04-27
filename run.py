import pytest
# import sys
#
# origin = sys.stdout
# hlog = open('C:\\Jin\\workpase\\FreeTestGo\\test_log\\log.txt', 'w')
# sys.stdout = hlog
#
# if __name__ == '__main__':
#     args = ['-q','-s']
#     pytest.main(args)
#     sys.stdout = origin
#     hlog.close()
#     print("测试结束！")


if __name__ == '__main__':
    pytest.main(['-s','test_case_2.py','-m=webtest'])