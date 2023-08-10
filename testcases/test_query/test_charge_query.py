import pytest
import allure

from api.query_api import ApiTms
from utils.read import base_data


@allure.epic("TMS项目")
@allure.feature("费用管理模块")
class TestChargeQuery:
    @allure.title("费用管理-创建应收合并结算单各个页签列表查询接口")
    @pytest.mark.parametrize("incomeTag", base_data.read_data()['incomeTag'])
    def test_001(self, login_fixture, incomeTag):
        result = ApiTms.brl_list(login_fixture, incomeTag)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应收费用制作各个页签列表查询接口")
    @pytest.mark.parametrize("tab", base_data.read_data()['tab'])
    def test_002(self, login_fixture, tab):
        result = ApiTms.brl1_list(login_fixture, tab)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应收改单列表查询接口")
    def test_003(self, login_fixture):
        result = ApiTms.brc_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应收票结账单列表查询接口")
    @pytest.mark.parametrize("billStatus",base_data.read_data()['billStatus'])
    def test_004(self, login_fixture, billStatus):
        result = ApiTms.brl2_list(login_fixture, billStatus)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-月结账单列表查询接口")
    def test_005(self, login_fixture):
        result = ApiTms.brmb_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应收发票申请列表列表查询接口")
    def test_006(self, login_fixture):
        result = ApiTms.br_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应收额外费用申请各个列表列表查询接口")
    @pytest.mark.parametrize("chargeStatus", base_data.read_data()['chargeStatus'])
    def test_007(self, login_fixture, chargeStatus):
        result = ApiTms.bre_list(login_fixture, chargeStatus)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-创建应付合并结算单各个列表查询接口")
    @pytest.mark.parametrize("tabType", base_data.read_data()['tabType'])
    def test_008(self, login_fixture, tabType):
        result = ApiTms.bpcmb_list(login_fixture, tabType)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应付费用制作各个列表查询接口")
    @pytest.mark.parametrize("tab", base_data.read_data()['tab'])
    def test_009(self, login_fixture, tab):
        result = ApiTms.bpm_list(login_fixture, tab)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应付改单列表查询接口")
    def test_010(self, login_fixture):
        result = ApiTms.bpc_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应付票结账单列表查询接口")
    def test_011(self, login_fixture):
        result = ApiTms.bpb_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应付月结账单列表查询接口")
    def test_012(self, login_fixture):
        result = ApiTms.bpmb_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-应付额外费申请各个列表查询接口")
    @pytest.mark.parametrize("chargeStatus", base_data.read_data()['chargeStatus'])
    def test_013(self, login_fixture, chargeStatus):
        result = ApiTms.bpe_list(login_fixture, chargeStatus)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("费用管理-运单补录列表查询接口")
    @pytest.mark.parametrize("supplementType", base_data.read_data()['supplementType'])
    def test_014(self, login_fixture, supplementType):
        result = ApiTms.ba_list(login_fixture, supplementType)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
