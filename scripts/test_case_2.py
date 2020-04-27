import pytest

class Test_Pytest():

    # 跳过该用例，也可添加某些条件再跳过skipif
    @pytest.mark.skip
    def test_one(self,):
            print("----start------")
            pytest.xfail(reason='该功能尚未完成')
            print("test_one方法执行" )
            assert 1==1

    # 第二种跳过方法：将该用例标记成xfail失败，并且该用例中的后续代码不会执行。如功能未完成、已知有问题用例或前置条件操作失败
    @pytest.mark.xfail
    def test_four(self):
        print("test_three方法执行")
        assert 3 - 1 == 1

    # xfail的另一种使用方法：如果测试用例执行失败的则结果是xfail（不会额外显示出错误信息）；如果测试用例执行成功的则结果是xpass。
    @pytest.mark.xfail
    def test_five(self):
        print("test_three方法执行")
        assert 3 - 1 == 2

    # 给用例添加标记：webtest，执行方式：pytest.main(["-s", "test_server.py", "-m=webtest"])，-s指定文件，-m指定执行特定标记用例
    @pytest.mark.webtest
    def test_two(self):
            print("test_two方法执行" )
            assert "o" in "love"

    @pytest.mark.webtest
    def test_three(self):
            print("test_three方法执行" )
            assert 3-2==1


if __name__=="__main__":
    pytest.main(['-s','test_case_2.py','-m=webtest'])