import pytest
import allure

from api.query_api import ApiTms
from utils.read import base_data


@allure.epic("TMS项目")
@allure.feature("跟踪管控模块")
class TestTrackQuery:
    @allure.title("跟踪管控-在途跟踪列表查询接口")
    def test_001(self, login_fixture):
        result = ApiTms.ttt_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("跟踪管控-文件管理各个页签列表查询接口")
    @pytest.mark.parametrize("fileStatus", base_data.read_data()['fileStatus'])
    def test_002(self, login_fixture, fileStatus):
        result = ApiTms.tfm_list(login_fixture, fileStatus)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("跟踪管控-车辆管理各个页签列表查询接口")
    @pytest.mark.parametrize("carState", base_data.read_data()['carState'])
    def test_003(self, login_fixture, carState):
        result = ApiTms.ccm_list(login_fixture, carState)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("跟踪管控-事件异常各个页签列表查询接口")
    @pytest.mark.parametrize("abnormalStatus", base_data.read_data()['abnormalStatus'])
    def test_004(self, login_fixture, abnormalStatus):
        result = ApiTms.ccm_list(login_fixture, abnormalStatus)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("跟踪管控-预约管理各个页签列表查询接口")
    @pytest.mark.parametrize("appointmentTag", base_data.read_data()['appointmentTag'])
    def test_005(self, login_fixture, appointmentTag):
        result = ApiTms.ta_list(login_fixture, appointmentTag)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
