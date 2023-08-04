import pytest
import allure

from api.login_api import login_outcome


@allure.epic("TMS项目")
@allure.feature("登录模块")
class TestLoginCase:
    @allure.title("测试账号密码登录")
    def test_login_case(self):
        result = login_outcome.login()
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
