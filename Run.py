import pytest

if __name__ == '__main__':
    # pytest.main(["-vs"])

    # test="./Test_casa/test_ict_long.py"
    test = ".//testcases"
    # 执行测试用例生成测试数据，如果已经存在报告，那就先清空，然后再生成新的测试报告，使用命令： --clean-alluredir
    pytest.main(['-vs', test, '--clean-alluredir', '--alluredir', './allure-results'])