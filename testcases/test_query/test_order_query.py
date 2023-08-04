import pytest
import allure

from api.query_api import ApiTms


@allure.epic("EPLD项目")
@allure.feature("智能分析模块")
class TestAnalysisQuery:
    @allure.story("验证查询接口")
    @allure.title("智能分析---物流订单整审时效报表接口")
    def test_001(self, login_fixture):
        result = ApiTms.excelReport_searchList(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
