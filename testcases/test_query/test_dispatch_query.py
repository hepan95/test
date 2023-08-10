import pytest
import allure

from api.query_api import ApiTms
from utils.read import base_data


@allure.epic("TMS项目")
@allure.feature("配载及派单模块")
class TestAnalysisQuery:
    @allure.title("配载优化-配载列表查询接口")
    def test_001(self, login_fixture):
        result = ApiTms.lob_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("配载优化-预配载列表查询接口")
    def test_002(self, login_fixture):
        result = ApiTms.lop_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("配载优化-已配载列表查询接口")
    def test_003(self, login_fixture):
        result = ApiTms.lol_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("待办任务-待派单列表查询接口")
    def test_004(self, login_fixture):
        result = ApiTms.dispatch_todo_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("待办任务-待智能派单列表查询接口")
    def test_005(self, login_fixture):
        result = ApiTms.dispatch_todo2_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("待办任务-待司机确认列表查询接口")
    def test_006(self, login_fixture):
        result = ApiTms.dispatch_todo3_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("待办任务-待司机确认列表查询接口")
    def test_007(self, login_fixture):
        result = ApiTms.dispatch_todo4_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("待办任务-已拒绝列表查询接口")
    def test_008(self, login_fixture):
        result = ApiTms.dispatch_todo5_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("执行中任务列表查询接口")
    def test_008(self, login_fixture):
        result = ApiTms.dispatch_done_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("已完成任务列表查询接口")
    def test_008(self, login_fixture):
        result = ApiTms.dispatch_finished_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("运单跟踪-各个页签列表查询接口")
    @pytest.mark.parametrize("waybillStatus", base_data.read_data()['waybillStatus'])
    def test_008(self, login_fixture, waybillStatus):
        result = ApiTms.tft_list(login_fixture, waybillStatus)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("监理任务-各个页签列表查询接口")
    @pytest.mark.parametrize("tab", base_data.read_data()['tab'])
    def test_008(self, login_fixture, tab):
        result = ApiTms.dst_list(login_fixture, tab)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
