import pytest
import allure

from api.login_api import login_outcome


@allure.epic("EPLD项目")
@allure.feature("登录模块feature")
class TestLoginCase:
    @allure.story("验证登录接口")
    @allure.title("测试账号密码登录")
    @allure.testcase("http://epld-test.epldcloud.com", name="接口地址testcase")
    @allure.issue("http://epld-test.epldcloud.com", name="缺陷地址issue")
    @allure.link("http://epld-test.epldcloud.com", name="链接地址link")
    @allure.description("当前登录账号是px，用例描述")
    @allure.step("操作步骤")
    @allure.severity(severity_level="blocker")
    def test_login_case(self):
        result = login_outcome.login()
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
