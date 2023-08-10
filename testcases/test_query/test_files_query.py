import pytest
import allure

from api.query_api import ApiTms
from utils.read import base_data


@allure.epic("TMS项目")
@allure.feature("档案管理模块")
class TestFilesQuery:
    @allure.title("档案管理-客户管理-客户档案列表查询接口")
    def test_001(self, login_fixture):
        result = ApiTms.cca_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-客户管理-联系人档案列表查询接口")
    def test_002(self, login_fixture):
        result = ApiTms.ccc_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-客户管理-客服分配列表查询接口")
    def test_003(self, login_fixture):
        result = ApiTms.ccs_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-客户管理-收发货档案列表查询接口")
    def test_004(self, login_fixture):
        result = ApiTms.ccf_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-客户管理-税率档案列表查询接口")
    def test_005(self, login_fixture):
        result = ApiTms.cct_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-客户管理-结算单位档案列表查询接口")
    def test_006(self, login_fixture):
        result = ApiTms.cccu_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-供应商管理-供应商档案列表查询接口")
    def test_007(self, login_fixture):
        result = ApiTms.csa_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-供应商管理-联系人档案列表查询接口")
    def test_008(self, login_fixture):
        result = ApiTms.csc_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-供应商管理-车辆档案列表查询接口")
    def test_009(self, login_fixture):
        result = ApiTms.csc1_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-供应商管理-司机档案列表查询接口")
    def test_010(self, login_fixture):
        result = ApiTms.csd_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-供应商管理-税率档案列表查询接口")
    def test_011(self, login_fixture):
        result = ApiTms.cst_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-内部档案-收发货档案列表查询接口")
    def test_012(self, login_fixture):
        result = ApiTms.cif_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-内部档案-自有车档案列表查询接口")
    def test_013(self, login_fixture):
        result = ApiTms.csci_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-内部档案-自有司机档案列表查询接口")
    def test_014(self, login_fixture):
        result = ApiTms.cid_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理-内部档案-汇率档案列表查询接口")
    def test_015(self, login_fixture):
        result = ApiTms.br1_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
