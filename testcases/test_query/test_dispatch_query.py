import pytest
import allure

from api.query_api import ApiEpld


@allure.epic("EPLD项目")
@allure.feature("派单中心模块")
class TestDispatchQuery:
    @allure.title("派单中心---空运---待派单接口")
    def test_001(self, login_fixture):
        result = ApiEpld.air_transport_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---空运---已派单接口")
    def test_002(self, login_fixture):
        result = ApiEpld.air_transport_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---空运---已完成接口")
    def test_003(self, login_fixture):
        result = ApiEpld.air_transport_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---空运---已撤销接口")
    def test_004(self, login_fixture):
        result = ApiEpld.air_transport_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---空运---已取消查询接口")
    def test_005(self, login_fixture):
        result = ApiEpld.air_transport_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---国内运输---待派单查询接口")
    def test_006(self, login_fixture):
        result = ApiEpld.mnt_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---国内运输---已派单查询接口")
    def test_007(self, login_fixture):
        result = ApiEpld.mnt_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---国内运输---已完成查询接口")
    def test_008(self, login_fixture):
        result = ApiEpld.mnt_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---国内运输---已撤销查询接口")
    def test_009(self, login_fixture):
        result = ApiEpld.mnt_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---国内运输---已取消查询接口")
    def test_010(self, login_fixture):
        result = ApiEpld.mnt_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---保税运输---待派单查询接口")
    def test_011(self, login_fixture):
        result = ApiEpld.bt_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---保税运输---已派单查询接口")
    def test_012(self, login_fixture):
        result = ApiEpld.bt_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---保税运输---已完成查询接口")
    def test_013(self, login_fixture):
        result = ApiEpld.bt_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---保税运输---已撤销查询接口")
    def test_014(self, login_fixture):
        result = ApiEpld.bt_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---保税运输---已取消查询接口")
    def test_015(self, login_fixture):
        result = ApiEpld.bt_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---内贸运输---待派单查询接口")
    def test_016(self, login_fixture):
        result = ApiEpld.nit_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---内贸运输---已派单查询接口")
    def test_017(self, login_fixture):
        result = ApiEpld.nit_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---内贸运输---已完成查询接口")
    def test_018(self, login_fixture):
        result = ApiEpld.nit_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---内贸运输---已撤销查询接口")
    def test_019(self, login_fixture):
        result = ApiEpld.nit_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---内贸运输---已取消查询接口")
    def test_020(self, login_fixture):
        result = ApiEpld.nit_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---中港运输---待派单查询接口")
    def test_021(self, login_fixture):
        result = ApiEpld.mht_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---中港运输---已派单查询接口")
    def test_022(self, login_fixture):
        result = ApiEpld.mht_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---中港运输---已完成查询接口")
    def test_023(self, login_fixture):
        result = ApiEpld.mht_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---中港运输---已撤销查询接口")
    def test_024(self, login_fixture):
        result = ApiEpld.mht_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---中港运输---已取消查询接口")
    def test_025(self, login_fixture):
        result = ApiEpld.mht_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---跨境运输---待派单查询接口")
    def test_026(self, login_fixture):
        result = ApiEpld.mcbt_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---跨境运输---已派单查询接口")
    def test_027(self, login_fixture):
        result = ApiEpld.mcbt_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---跨境运输---已完成查询接口")
    def test_028(self, login_fixture):
        result = ApiEpld.mcbt_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---跨境运输---已取消查询接口")
    def test_029(self, login_fixture):
        result = ApiEpld.mcbt_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港口运输---待派单查询接口")
    def test_030(self, login_fixture):
        result = ApiEpld.pt_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港口运输---已派单查询接口")
    def test_031(self, login_fixture):
        result = ApiEpld.pt_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港口运输---已完成查询接口")
    def test_032(self, login_fixture):
        result = ApiEpld.pt_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港口运输---已撤销查询接口")
    def test_033(self, login_fixture):
        result = ApiEpld.pt_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港口运输---已取消查询接口")
    def test_034(self, login_fixture):
        result = ApiEpld.pt_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---香港本地运输---待派单查询接口")
    def test_035(self, login_fixture):
        result = ApiEpld.hnt_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---香港本地运输---已派单查询接口")
    def test_036(self, login_fixture):
        result = ApiEpld.hnt_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---香港本地运输---已完成查询接口")
    def test_037(self, login_fixture):
        result = ApiEpld.hnt_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---香港本地运输---已撤销查询接口")
    def test_038(self, login_fixture):
        result = ApiEpld.hnt_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---香港本地运输---已取消查询接口")
    def test_039(self, login_fixture):
        result = ApiEpld.hnt_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---装卸服务---待派单查询接口")
    def test_040(self, login_fixture):
        result = ApiEpld.lu_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---装卸服务---已派单查询接口")
    def test_041(self, login_fixture):
        result = ApiEpld.lu_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---装卸服务---已完成查询接口")
    def test_042(self, login_fixture):
        result = ApiEpld.lu_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---装卸服务---已撤销查询接口")
    def test_043(self, login_fixture):
        result = ApiEpld.lu_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港内作业---待派单查询接口")
    def test_044(self, login_fixture):
        result = ApiEpld.wp_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港内作业---已派单查询接口")
    def test_045(self, login_fixture):
        result = ApiEpld.wp_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港内作业---已完成查询接口")
    def test_046(self, login_fixture):
        result = ApiEpld.wp_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港内作业---已撤销查询接口")
    def test_047(self, login_fixture):
        result = ApiEpld.wp_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---陆运---港内作业---已取消查询接口")
    def test_048(self, login_fixture):
        result = ApiEpld.wp_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---海运---待派单查询接口")
    def test_049(self, login_fixture):
        result = ApiEpld.st_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---海运---已派单查询接口")
    def test_050(self, login_fixture):
        result = ApiEpld.st_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---海运---已完成查询接口")
    def test_051(self, login_fixture):
        result = ApiEpld.st_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---海运---已撤销查询接口")
    def test_052(self, login_fixture):
        result = ApiEpld.st_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---海运---已取消查询接口")
    def test_053(self, login_fixture):
        result = ApiEpld.st_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---代订舱---待派单查询接口")
    def test_054(self, login_fixture):
        result = ApiEpld.abs_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---代订舱---已派单查询接口")
    def test_055(self, login_fixture):
        result = ApiEpld.abs_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---代订舱---已完成查询接口")
    def test_056(self, login_fixture):
        result = ApiEpld.abs_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---代订舱---已撤销查询接口")
    def test_057(self, login_fixture):
        result = ApiEpld.abs_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---代订舱---已取消查询接口")
    def test_058(self, login_fixture):
        result = ApiEpld.abs_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---内贸海运---待派单查询接口")
    def test_059(self, login_fixture):
        result = ApiEpld.niss_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---内贸海运---已派单查询接口")
    def test_060(self, login_fixture):
        result = ApiEpld.niss_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---内贸海运---已完成查询接口")
    def test_061(self, login_fixture):
        result = ApiEpld.niss_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---海运---内贸海运---已取消查询接口")
    def test_062(self, login_fixture):
        result = ApiEpld.niss_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---快递---待派单查询接口")
    def test_063(self, login_fixture):
        result = ApiEpld.ed_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---快递---已派单查询接口")
    def test_064(self, login_fixture):
        result = ApiEpld.ed_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---快递---已完成查询接口")
    def test_065(self, login_fixture):
        result = ApiEpld.ed_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---快递---已撤销查询接口")
    def test_066(self, login_fixture):
        result = ApiEpld.ed_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---快递---已取消查询接口")
    def test_067(self, login_fixture):
        result = ApiEpld.ed_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---仓储---待派单查询接口")
    def test_068(self, login_fixture):
        result = ApiEpld.wo_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---仓储---已派单查询接口")
    def test_069(self, login_fixture):
        result = ApiEpld.wo_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---仓储---已完成查询接口")
    def test_070(self, login_fixture):
        result = ApiEpld.wo_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---仓储---已撤销查询接口")
    def test_071(self, login_fixture):
        result = ApiEpld.wo_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---仓储---已取消查询接口")
    def test_072(self, login_fixture):
        result = ApiEpld.wo_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---报关---待派单查询接口")
    def test_073(self, login_fixture):
        result = ApiEpld.cs_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---报关---已派单查询接口")
    def test_074(self, login_fixture):
        result = ApiEpld.cs_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---报关---已完成查询接口")
    def test_075(self, login_fixture):
        result = ApiEpld.cs_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---报关---已撤销查询接口")
    def test_076(self, login_fixture):
        result = ApiEpld.cs_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---报关---已取消查询接口")
    def test_077(self, login_fixture):
        result = ApiEpld.cs_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---转DO---待派单查询接口")
    def test_078(self, login_fixture):
        result = ApiEpld.td_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---转DO---已派单查询接口")
    def test_079(self, login_fixture):
        result = ApiEpld.td_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---转DO---已完成接口")
    def test_080(self, login_fixture):
        result = ApiEpld.td_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---转DO---已撤销查询接口")
    def test_081(self, login_fixture):
        result = ApiEpld.td_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---转DO---已取消查询接口")
    def test_082(self, login_fixture):
        result = ApiEpld.td_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---铁路运输---待派单查询接口")
    def test_083(self, login_fixture):
        result = ApiEpld.rt_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---铁路运输---已派单查询接口")
    def test_084(self, login_fixture):
        result = ApiEpld.rt_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---铁路运输---已完成查询接口")
    def test_085(self, login_fixture):
        result = ApiEpld.rt_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---铁路运输---已撤销查询接口")
    def test_086(self, login_fixture):
        result = ApiEpld.rt_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---铁路运输---已取消查询接口")
    def test_087(self, login_fixture):
        result = ApiEpld.rt_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---驳船运输---待派单查询接口")
    def test_088(self, login_fixture):
        result = ApiEpld.railway_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---驳船运输---已派单查询接口")
    def test_089(self, login_fixture):
        result = ApiEpld.railway_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---驳船运输---已完成查询接口")
    def test_090(self, login_fixture):
        result = ApiEpld.railway_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---驳船运输---已撤销查询接口")
    def test_091(self, login_fixture):
        result = ApiEpld.railway_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---驳船运输---已取消查询接口")
    def test_092(self, login_fixture):
        result = ApiEpld.railway_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---代办及单证服务---待派单查询接口")
    def test_093(self, login_fixture):
        result = ApiEpld.ao_pending(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---代办及单证服务---已派单查询接口")
    def test_094(self, login_fixture):
        result = ApiEpld.ao_done(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---代办及单证服务---已完成查询接口")
    def test_095(self, login_fixture):
        result = ApiEpld.ao_complete(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---代办及单证服务---已撤销查询接口")
    def test_096(self, login_fixture):
        result = ApiEpld.ao_revoke(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"

    @allure.title("派单中心---代办及单证服务---已取消查询接口")
    def test_097(self, login_fixture):
        result = ApiEpld.ao_cancel(login_fixture)
        assert result.success is True
        assert result.body["returnMsg"] == "操作成功"


if __name__ == '__main__':
    pytest.main()
