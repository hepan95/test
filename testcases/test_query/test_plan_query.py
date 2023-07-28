import pytest
import allure

from api.query_api import ApiEpld
from utils.read import base_data


@allure.epic("EPLD项目")
@allure.feature("物流计划模块")
class TestPlanQuery:
    @allure.story("验证查询接口")
    @allure.title("物流计划---(所有类型)---待计划、配载查询接口")
    @pytest.mark.parametrize("serviceTypeCode", base_data.read_data()['serviceTypeCodePlan'])
    def test_001(self, login_fixture, serviceTypeCode):
        result = ApiEpld.plan_list(login_fixture, serviceTypeCode)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流计划---(所有类型)---已计划查询接口")
    @pytest.mark.parametrize("serviceTypeCode", base_data.read_data()['serviceTypeCodePlan'])
    def test_002(self, login_fixture, serviceTypeCode):
        result = ApiEpld.plan_list_planned(login_fixture, serviceTypeCode)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"



if __name__ == '__main__':
    pytest.main()
