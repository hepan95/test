import pytest
import allure

from api.query_api import ApiTms
from utils.read import base_data


@allure.epic("TMS项目")
@allure.feature("运输订单模块")
class TestAnalysisQuery:
    @allure.title("接入订单列表查询接口")
    def test_001(self, login_fixture):
        result = ApiTms.order_accept_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("待办任务列表查询接口")
    def test_002(self, login_fixture):
        result = ApiTms.order_pending_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("执行中任务列表查询接口")
    def test_003(self, login_fixture):
        result = ApiTms.order_complete_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("订单跟踪-订单跟踪-各个页签列表查询接口")
    @pytest.mark.parametrize("statusType", base_data.read_data()['statusType'])
    def test_004(self, login_fixture, statusType):
        result = ApiTms.track_order_list(login_fixture, statusType)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("订单汇总列表查询接口")
    def test_005(self, login_fixture):
        result = ApiTms.order_total_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

if __name__ == '__main__':
    pytest.main()
