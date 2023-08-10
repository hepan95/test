import pytest
import allure

from api.query_api import ApiEpld
from utils.read import base_data


@allure.epic("EPLD项目")
@allure.feature("物流执行模块模块")
class TestExecuteQuery:
    @allure.title("物流执行---所有类型---执行中查询接口")
    @pytest.mark.parametrize("serviceTypeCode", base_data.read_data()['serviceTypeCode'])
    def test_001(self, login_fixture, serviceTypeCode):
        result = ApiEpld.dispatch_list(login_fixture, serviceTypeCode)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---所有类型---执行完成查询接口")
    @pytest.mark.parametrize("serviceTypeCode", base_data.read_data()['serviceTypeCode'])
    def test_002(self, login_fixture, serviceTypeCode):
        result = ApiEpld.dispatch_list_complete(login_fixture, serviceTypeCode)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---提单制作---国际海运---待处理查询接口")
    def test_003(self, login_fixture):
        result = ApiEpld.seaBill_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---提单制作---国际海运---已处理查询接口")
    def test_004(self, login_fixture):
        result = ApiEpld.seaBill_list_processed(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---提单制作---空运---待处理查询接口")
    def test_005(self, login_fixture):
        result = ApiEpld.airlift_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---提单制作---空运---已处理查询接口")
    def test_006(self, login_fixture):
        result = ApiEpld.airlift_list_processed(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---提单制作---铁路---待处理查询接口")
    def test_007(self, login_fixture):
        result = ApiEpld.railway_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---提单制作---铁路---已处理查询接口")
    def test_008(self, login_fixture):
        result = ApiEpld.railway_list_processed(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---提单制作---驳船---待处理查询接口")
    def test_009(self, login_fixture):
        result = ApiEpld.barge_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---提单制作---驳船---已处理查询接口")
    def test_010(self, login_fixture):
        result = ApiEpld.barge_list_processed(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("物流执行---文档管理---任务单查询接口")
    def test_011(self, login_fixture):
        result = ApiEpld.taskList_list(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"

    @allure.title("物流执行---文档管理---物流订单查询接口")
    def test_012(self, login_fixture):
        result = ApiEpld.taskList_logisticslist(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "成功"


if __name__ == '__main__':
    pytest.main()
