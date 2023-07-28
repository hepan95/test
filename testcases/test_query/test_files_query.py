import pytest
import allure

from api.query_api import ApiEpld


@allure.epic("EPLD项目")
@allure.feature("档案管理模块")
class TestFilesQuery:
    @allure.story("验证查询接口")
    @allure.title("档案管理---客户---基本信息查询接口")
    def test_001(self, login_fixture):
        result = ApiEpld.base_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---客户---联系人查询接口")
    def test_002(self, login_fixture):
        result = ApiEpld.contact_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---客户---代理跟进分配查询接口")
    def test_003(self, login_fixture):
        result = ApiEpld.client2_agent_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---客户---客服分配查询接口")
    def test_004(self, login_fixture):
        result = ApiEpld.client2_cs_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---客户---协同通知查询接口")
    def test_005(self, login_fixture):
        result = ApiEpld.client2_sn_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---客户---收发货人档案查询接口")
    def test_006(self, login_fixture):
        result = ApiEpld.factory_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("档案管理---客户---税率档案查询接口")
    def test_007(self, login_fixture):
        result = ApiEpld.tax_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---客户---开票档案查询接口")
    def test_008(self, login_fixture):
        result = ApiEpld.customerInvoice_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---客户---汇率档案查询接口")
    def test_009(self, login_fixture):
        result = ApiEpld.client_rate_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---客户---物料档案查询接口")
    def test_010(self, login_fixture):
        result = ApiEpld.material_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---客户---结算单位查询接口")
    def test_011(self, login_fixture):
        result = ApiEpld.customerClearingUnit_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("档案管理---客户---客户共享查询接口")
    def test_012(self, login_fixture):
        result = ApiEpld.clientShare_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---客户---习惯费用项查询接口")
    def test_013(self, login_fixture):
        result = ApiEpld.customerCustomaryCost_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---客户---客户端管理查询接口")
    def test_014(self, login_fixture):
        result = ApiEpld.customerTerminal_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---客户---委托模板库查询接口")
    def test_015(self, login_fixture):
        result = ApiEpld.blm_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---客户---客户地点档案查询接口")
    def test_016(self, login_fixture):
        result = ApiEpld.customerDistrict_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---供应商---基本信息查询接口")
    def test_017(self, login_fixture):
        result = ApiEpld.supplier_base_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---供应商---联系人查询接口")
    def test_018(self, login_fixture):
        result = ApiEpld.supplier_contact_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---供应商---车辆档案查询接口")
    def test_019(self, login_fixture):
        result = ApiEpld.car_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("档案管理---供应商---司机档案查询接口")
    def test_020(self, login_fixture):
        result = ApiEpld.driver_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---供应商---汇率档案查询接口")
    def test_021(self, login_fixture):
        result = ApiEpld.supplier_rate_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---供应商---税率档案查询接口")
    def test_022(self, login_fixture):
        result = ApiEpld.suptaxrate_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---供应商---仓库档案查询接口")
    def test_023(self, login_fixture):
        result = ApiEpld.tenantWarehouse_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("档案管理---供应商---地点档案查询接口")
    def test_024(self, login_fixture):
        result = ApiEpld.archiverService_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("档案管理---供应商---结算单位查询接口")
    def test_025(self, login_fixture):
        result = ApiEpld.supplierClearingUnit_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("档案管理---供应商---习惯费用项查询接口")
    def test_026(self, login_fixture):
        result = ApiEpld.supplierCustomaryCost_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---组织档案---组织机构查询接口")
    def test_027(self, login_fixture):
        result = ApiEpld.institution_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("档案管理---组织档案---内部结算查询接口")
    def test_028(self, login_fixture):
        result = ApiEpld.insideStatement_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---组织档案---利润转移设置查询接口")
    def test_029(self, login_fixture):
        result = ApiEpld.it_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---组织档案---部门档案查询接口")
    def test_030(self, login_fixture):
        result = ApiEpld.department_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---组织档案---用户档案查询接口")
    def test_031(self, login_fixture):
        result = ApiEpld.user_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---组织档案---法人档案查询接口")
    def test_032(self, login_fixture):
        result = ApiEpld.tenantCorporateInfo_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("档案管理---费用项档案查询接口")
    def test_033(self, login_fixture):
        result = ApiEpld.charge_item_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
