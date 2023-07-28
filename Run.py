import pytest

if __name__ == '__main__':
    # 执行测试用例生成测试数据，如果已经存在报告，那就先清空，然后再生成新的测试报告，使用命令： --clean-alluredir
    pytest.main(['-vs', '--clean-alluredir', '--alluredir', './report'])