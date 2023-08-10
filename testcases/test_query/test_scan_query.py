import pytest
import allure

from api.query_api import ApiTms
from utils.read import base_data


@allure.epic("TMS项目")
@allure.feature("扫描管理模块")
class TestScanQuery:
    @allure.title("扫描管理-转仓（提货扫描）-上传管理页签列表查询接口")
    def test_001(self, login_fixture):
        result = ApiTms.spu_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-转仓（提货扫描）-订单汇总页签列表查询接口")
    def test_002(self, login_fixture):
        result = ApiTms.spo_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-转仓（提货扫描）-运输信息页签列表查询接口")
    def test_003(self, login_fixture):
        result = ApiTms.spt_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-分货（复核扫描）-分货&复核页签列表查询接口")
    def test_004(self, login_fixture):
        result = ApiTms.ss_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-分货（复核扫描）-箱码信息页签列表查询接口")
    def test_005(self, login_fixture):
        result = ApiTms.spi_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-分货（复核扫描）-串货记录页签列表查询接口")
    def test_006(self, login_fixture):
        result = ApiTms.spp_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-配送交接扫描页签列表查询接口")
    def test_007(self, login_fixture):
        result = ApiTms.sdl_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-退货(提货扫描)页签列表查询接口")
    def test_008(self, login_fixture):
        result = ApiTms.srl_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-正向(提货扫描)页签列表查询接口")
    def test_009(self, login_fixture):
        result = ApiTms.spl_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-HUB出入库扫描-箱码扫描记录页签列表查询接口")
    def test_010(self, login_fixture):
        result = ApiTms.shb_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("扫描管理-HUB出入库扫描-订单出入库汇总页签列表查询接口")
    def test_011(self, login_fixture):
        result = ApiTms.sho_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
