import pytest
import allure

from api.query_api import ApiEpld


@allure.epic("EPLD项目")
@allure.feature("计费与对账模块")
class TestChargeQuery:
    @allure.story("验证查询接口")
    @allure.title("计费与对账---应收结算---未完成页签查询接口")
    def test_001(self, login_fixture):
        result = ApiEpld.bill_receive_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收结算---已完成页签接口")
    def test_002(self, login_fixture):
        result = ApiEpld.bill_receive_list_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收改单---未完成页签接口")
    def test_003(self, login_fixture):
        result = ApiEpld.change_receive_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收改单---已完成页签接口")
    def test_004(self, login_fixture):
        result = ApiEpld.change_receive_list_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收账单---未完成页签接口")
    def test_005(self, login_fixture):
        result = ApiEpld.receivable_pay_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收账单---已审核页签接口")
    def test_006(self, login_fixture):
        result = ApiEpld.receivable_pay_list_Audited(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收账单---已开票页签接口")
    def test_007(self, login_fixture):
        result = ApiEpld.receivable_pay_list_Invoiced(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收发票接口")
    def test_008(self, login_fixture):
        result = ApiEpld.invoice_apply_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收协同账单接口")
    def test_009(self, login_fixture):
        result = ApiEpld.synergy_receive_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---合并结算---未完成页签接口")
    def test_010(self, login_fixture):
        result = ApiEpld.merge_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---合并结算---已完成页签接口")
    def test_011(self, login_fixture):
        result = ApiEpld.merge_list_Completed(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应付结算---未完成页签接口")
    def test_012(self, login_fixture):
        result = ApiEpld.pay_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应付结算---已完成页签接口")
    def test_013(self, login_fixture):
        result = ApiEpld.pay_list_Completed(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应付改单---未完成页签接口")
    def test_014(self, login_fixture):
        result = ApiEpld.change_pay_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("计费与对账---应付改单---已完成页签接口")
    def test_015(self, login_fixture):
        result = ApiEpld.change_pay_list_Completed(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "Success"

    @allure.title("计费与对账---应付账单接口")
    def test_016(self, login_fixture):
        result = ApiEpld.due_pay_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---报销结算接口")
    def test_017(self, login_fixture):
        result = ApiEpld.reimbursement_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收月账单接口")
    def test_018(self, login_fixture):
        result = ApiEpld.receiveMonthBill_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应付月账单接口")
    def test_019(self, login_fixture):
        result = ApiEpld.payMonthBill_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应付代垫费接口")
    def test_020(self, login_fixture):
        result = ApiEpld.payPrepaid_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收代垫费接口")
    def test_021(self, login_fixture):
        result = ApiEpld.receivePrepaid_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应付额外费用接口")
    def test_022(self, login_fixture):
        result = ApiEpld.payExtra_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---应收额外费用接口")
    def test_023(self, login_fixture):
        result = ApiEpld.receiveExtra_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("计费与对账---其他费用接口")
    def test_024(self, login_fixture):
        result = ApiEpld.other_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
