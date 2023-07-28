import pytest
import allure

from api.query_api import ApiEpld


@allure.epic("EPLD项目")
@allure.feature("物流订单模块")
class TestOrderQuery:
    @allure.story("验证查询接口")
    @allure.title("物流订单---委托订单列表接口查询接口")
    def test_001(self, login_fixture):
        result = ApiEpld.delegation_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---PO Management---PO Management列表接口查询接口")
    def test_002(self, login_fixture):
        result = ApiEpld.po_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---PO Management---Booking Management列表接口查询接口")
    def test_003(self, login_fixture):
        result = ApiEpld.booking_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---待接订单列表查询接口")
    def test_004(self, login_fixture):
        result = ApiEpld.receive_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("物流订单---物流执行订单列表查询接口")
    def test_005(self, login_fixture):
        result = ApiEpld.logisticsExecutionOrder_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---订单录入列表查询接口")
    def test_006(self, login_fixture):
        result = ApiEpld.input_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("物流订单---订单完善列表查询接口")
    def test_007(self, login_fixture):
        result = ApiEpld.job_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("物流订单---订单汇总列表查询接口")
    def test_008(self, login_fixture):
        result = ApiEpld.all_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("物流订单---预约管理---代理预约查询接口")
    def test_009(self, login_fixture):
        result = ApiEpld.agent_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---预约管理---物流订单预约查询接口")
    def test_010(self, login_fixture):
        result = ApiEpld.logisticsBooking_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---货量拆分查询接口")
    def test_011(self, login_fixture):
        result = ApiEpld.volume_split_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---Nike报表---NIKEPI查询接口")
    def test_012(self, login_fixture):
        result = ApiEpld.nikeKpi_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---Nike报表---货物异常情况查询接口")
    def test_013(self, login_fixture):
        result = ApiEpld.nikeGoodsException_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---数据处理中心---物流执行订单处理查询接口")
    def test_014(self, login_fixture):
        result = ApiEpld.orderProcess_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---数据处理中心---处理规则配置查询接口")
    def test_015(self, login_fixture):
        result = ApiEpld.processRules_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---数据处理中心---处理记录报表查询接口")
    def test_016(self, login_fixture):
        result = ApiEpld.processReport_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流订单---数据处理中心---供应商规则配置查询接口")
    def test_017(self, login_fixture):
        result = ApiEpld.supplierRuleConfig_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
