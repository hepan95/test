import pytest
import allure

from api.query_api import ApiEpld


@allure.epic("EPLD项目")
@allure.feature("客户与订单模块")
class TestWarehouseQuery:
    @allure.title("客户订单列表查询接口")
    def test_001(self, login_fixture):
        result = ApiEpld.customerOrder_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("INBOUND_PO列表查询接口")
    def test_002(self, login_fixture):
        result = ApiEpld.inbound_po_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("预约资源设置---预约仓库列表查询接口")
    def test_003(self, login_fixture):
        result = ApiEpld.appointWarehouse_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("预约资源设置---预约月台---月台设置列表查询接口")
    def test_004(self, login_fixture):
        result = ApiEpld.appointPlatform_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("预约资源设置---预约月台---分配客户设置列表查询接口")
    def test_005(self, login_fixture):
        result = ApiEpld.appointPlatform_allotList(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("平台预约---平台预约订单列表查询接口")
    def test_006(self, login_fixture):
        result = ApiEpld.logisticsAppointment_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("平台预约---平台预约单管理列表查询接口")
    def test_007(self, login_fixture):
        result = ApiEpld.logisticsAppointmentBooking_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("外部预约---预约订单列表查询接口")
    def test_008(self, login_fixture):
        result = ApiEpld.appointmentOrder_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("外部预约---预约订单列表查询接口")
    def test_009(self, login_fixture):
        result = ApiEpld.reservationManagement_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("仓库预约岗---预约单受理接口(查看月台使用情况)")
    def test_010(self, login_fixture):
        result = ApiEpld.acceptAppointment_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("库存管理---总库存列表查询接口")
    def test_011(self, login_fixture):
        result = ApiEpld.storageTotal_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("库存管理---库存流水列表查询接口")
    def test_012(self, login_fixture):
        result = ApiEpld.storageDetail_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("库存管理---库存流水列表查询接口")
    def test_013(self, login_fixture):
        result = ApiEpld.storageTurnover_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("库存管理---库存流水列表查询接口")
    def test_014(self, login_fixture):
        result = ApiEpld.storageCompare_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
