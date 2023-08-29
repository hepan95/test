#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: test_ict_scene.py.py
# @Time:2023/4/12 15:17
# @Author:PH
import time

from Common import log_page
log = log_page.Log()
import datetime
import allure
import pytest
# from pytest_assume.plugin import assume
myskip = pytest.mark.skipif()
from Common import common_funtion as pz #获取项目地址
from Common import ict_api as ict
from Config import config as cf
from Common import common_funtion as bf
hz_host = cf.hz_host
hz_token = ict.Test_login().Test_login002()
ht_host = cf.ht_host
ht_token = ict.Test_login().Test_login001()

@allure.parent_suite('ict业务场景测试用例')  # 包的注释
@allure.suite('ict业务场景测试用例模块')  # 模块的注释
@allure.sub_suite('前置条件')      #大类的注释
# @pytest.mark.skip(reason="无理由跳过")
class Test_query002():
    # log.info("運行前置條件")
    '''大类'''
    def setup_class(self):
        '''大类前置'''
        pass
    def teardown_class(self):
        '''大类后置'''
        pass
    @allure.title("区域规则-集装箱出口运输,操作区域蛇口")   #类方法的注释
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query001(self):
        log.info("区域规则-集装箱出口运输,操作区域蛇口")
        '''用例描述'''
        with allure.step("查看区域规则-集装箱出口运输,操作区域蛇口是否存在"):
            qy_gh = ict.Test_Added01().test_Added0031(taskUnitCode="port_container_export_transport",centerName="shekou_group")
            assert qy_gh[0] =='操作成功'
            if qy_gh[1] == [] :
                with allure.step("新增集装箱出口区域规划"):
                    xz_gh = ict.Test_Added01().test_Added0032(taskUnitCode="port_container_export_transport",centerName="shekou_group",isContainer=1)
                    assert xz_gh == '操作成功'
                with allure.step("查看区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="port_container_export_transport",centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                with allure.step("启用区域规划状态"):
                    qyqy_gh = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                    assert qyqy_gh == '启用成功'
            if qy_gh[1] != [] :
                with allure.step("查看区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="port_container_export_transport",centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                    if qygh_id[1] == "enabled_type_unenabled":
                        with allure.step("未启用查看区域规划id+状态"):
                            qy_qyzx = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                            assert qy_qyzx == '启用成功'
                    if qygh_id[1] == "enabled_type_disabled":
                        with allure.step("禁用查看区域规划id+状态"):
                            qy_qyzx = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                            assert qy_qyzx == '启用成功'
                    if qygh_id[1] == "enabled_type_enabled":
                        with allure.step("集装箱出口区域规划已存在，并已启用"):
                            pass

    @allure.title("接单中心-集装箱出口运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query002(self):
        log.info("接单中心-集装箱出口运输")
        with allure.step("查看接单中心-集装箱出口运输，是否存在"):
            jd_zx = ict.Test_Added01().test_Added0035(taskUnitCode="port_container_export_transport")
            assert jd_zx[0] =='操作成功'
            if jd_zx[1] == 0 :
                with allure.step("新增集装箱出口接单中心"):
                    zxjd_zx = ict.Test_Added01().test_Added0036(taskUnitCode="port_container_export_transport",isContainer=1)
                    assert zxjd_zx == '操作成功'
                with allure.step("查看接单中心id"):
                    jdzx_id = ict.Test_Added01().test_Added0037(taskUnitCode="port_container_export_transport")
                    assert jdzx_id[0] == '操作成功'
                with allure.step("启用接单中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                    assert qy_jdzx == '启用成功'
            if jd_zx[1] != 0 :
                with allure.step("查看接单中心id"):
                    jdzx_id = ict.Test_Added01().test_Added0037(taskUnitCode="port_container_export_transport")
                    assert jdzx_id[0] == '操作成功'
                    if jdzx_id[2] == "enabled_type_unenabled":
                        with allure.step("接单中心未启用，启用接单中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jdzx_id[2] == "enabled_type_disabled":
                        with allure.step("接单中心禁用，启用接单中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jdzx_id[2] == "enabled_type_enabled":
                        with allure.step("接单中已存在，并已启用"):
                            pass

    @allure.title("计划中心-集装箱出口运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query003(self):
        log.info("计划中心-集装箱出口运输")
        with allure.step("查看计划中心-集装箱出口运输，是否存在"):
            jh_zx = ict.Test_Added01().test_Added0039(taskUnitCode="port_container_export_transport")
            assert jh_zx[0] == '操作成功'
            if jh_zx[1] == 0:
                with allure.step("新增集装箱出口计划中心"):
                    zxjh_zx = ict.Test_Added01().test_Added0040(taskUnitCode="port_container_export_transport",isContainer=1)
                    assert zxjh_zx == '操作成功'
                with allure.step("查看计划中心id"):
                    jhzx_id = ict.Test_Added01().test_Added0041(taskUnitCode="port_container_export_transport")
                    assert jhzx_id[0] == '操作成功'
                with allure.step("启用计划中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                    assert qy_jdzx == '启用成功'
            if jh_zx[1] != 0:
                with allure.step("查看计划中心id"):
                    jhzx_id = ict.Test_Added01().test_Added0041(taskUnitCode="port_container_export_transport")
                    assert jhzx_id[0] == '操作成功'
                    if jhzx_id[2] == "enabled_type_unenabled":
                        with allure.step("计划中心未启用，启用计划中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jhzx_id[2] == "enabled_type_disabled":
                        with allure.step("计划中心禁用，启用计划中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jhzx_id[2] == "enabled_type_enabled":
                        with allure.step("计划中已存在，并已启用"):
                            pass

    @allure.title("调度中心-集装箱出口运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query004(self):
        log.info("调度中心-集装箱出口运输")
        with allure.step("查看调度中心，是否存在"):
            dd_zx = ict.Test_Added01().test_Added0043(centerName="center_type_dispatch_mm02",taskUnitCode="")
            assert dd_zx[0] == '操作成功'
            data = dd_zx[1]
            res = [item[key] for item in data for key in item]
            # print(res)
            list1 = []
            list2 = []
            id = []
            for item in data:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
                    if key == "distributionChannel":
                        # print(item[key])
                        list1.append(item[key])
                    if key == "statusType":
                        list2.append(item[key])
            # print(list1)
            if 0 not in list1:  #如果0不在列表中
                with allure.step("新增调度中心-货源大厅渠道"):
                    zxdd_zx = ict.Test_Added01().test_Added0044(centerName="center_type_dispatch_mm02",distributionChannel=0,isContainer=1)
                    assert zxdd_zx == '操作成功'
                with allure.step("查看调度中心id"):
                    ddzx_id = ict.Test_Added01().test_Added0045(centerName="center_type_dispatch_mm02")
                    assert ddzx_id[0] == '操作成功'
                with allure.step("启用调度中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0046(jdzx_id=ddzx_id[1])
                    assert qy_jdzx == '启用成功'
            if 1 not in list1:  # 如果1不在列表中
                with allure.step("新增调度中心-自有车渠道"):
                    zxdd_zx = ict.Test_Added01().test_Added0044(centerName="center_type_dispatch_mm02",distributionChannel=1,isContainer=1)
                    assert zxdd_zx == '操作成功'
                with allure.step("查看调度中心id"):
                    ddzx_id = ict.Test_Added01().test_Added0045(centerName="center_type_dispatch_mm02")
                    assert ddzx_id[0] == '操作成功'
                with allure.step("启用调度中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0046(jdzx_id=ddzx_id[1])
                    assert qy_jdzx == '启用成功'
            if 2 not in list1:  # 如果2不在列表中
                with allure.step("新增调度中心-供应商渠道"):
                    zxdd_zx = ict.Test_Added01().test_Added0044(centerName="center_type_dispatch_mm02",distributionChannel=2,isContainer=1)
                    assert zxdd_zx == '操作成功'
                with allure.step("查看调度中心id"):
                    ddzx_id = ict.Test_Added01().test_Added0045(centerName="center_type_dispatch_mm02")
                    assert ddzx_id[0] == '操作成功'
                with allure.step("启用调度中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0046(jdzx_id=ddzx_id[1])
                    assert qy_jdzx == '启用成功'
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                jdzx_id = id[id2]
                with allure.step("启用调度中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0046(jdzx_id=jdzx_id)
                    assert qy_jdzx == '启用成功'

    @allure.title("货主联系人")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query005(self):
        log.info("货主联系人")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看货主联系人"):
            hz_lxr = ict.Test_Added01().test_Added0013(hz_id=hz_id[1])
            assert hz_lxr[0] == '操作成功'
            if hz_lxr[1] == 0 :
                with allure.step("新增货主联系人"):
                    xz_lxr = ict.Test_Added01().test_Added0015(hz_id=hz_id[1])
                    assert xz_lxr[0] == '操作成功'
                with allure.step("获取新增货主联系人id"):
                    lxr_id = ict.Test_Added01().test_Added0014(hz_id=hz_id[1])
                    assert lxr_id[0] == '操作成功'
                with allure.step("启用新增货主联系人"):
                    lxr_id = ict.Test_Added01().test_Added0016(lxr_id=lxr_id[3])
                    assert lxr_id[0] == '操作成功'
            if hz_lxr[1] != 0 :
                with allure.step("获取新增货主联系人id+状态"):
                    lxr_id = ict.Test_Added01().test_Added0014(hz_id=hz_id[1])
                    assert lxr_id[0] == '操作成功'
                    if lxr_id[2] == "enabled_type_unenabled" :
                        with allure.step("未启用货主联系人：启用货主联系人"):
                            lxr_id = ict.Test_Added01().test_Added0016(lxr_id=lxr_id[3])
                            assert lxr_id[0] == '操作成功'
                    if lxr_id[2] == "enabled_type_disabled" :
                        with allure.step("禁用货主联系人：启用货主联系人"):
                            lxr_id = ict.Test_Added01().test_Added0016(lxr_id=lxr_id[3])
                            assert lxr_id[0] == '操作成功'
                    if lxr_id[2] == "enabled_type_enabled" :
                        with allure.step("货主联系人已存在，并已启用"):
                            pass

    @allure.title("收发货联系人1")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query006(self):
        log.info("收发货联系人1")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看收发货联系人是否存在"):
            sfh_lxr = ict.Test_Added01().test_Added0026(hz_id=hz_id[1],zh_name="测试集装箱装货地址")
            assert sfh_lxr[0] == '操作成功'
            if sfh_lxr[1] == 0 :
                with allure.step("获取收发地省编码"):
                    sf_bm = ict.Test_Added01().test_Added0001(lx=3,name="湖南省")
                    assert sf_bm[0] == '操作成功'
                    sf_bm = sf_bm[1]
                with allure.step("获取收发地市编码"):
                    cs_bm = ict.Test_Added01().test_Added0001(lx=4,name="长沙市")
                    assert cs_bm[0] == '操作成功'
                    cs_bm = cs_bm[1]
                with allure.step("获取收发地区编码"):
                    q_bm = ict.Test_Added01().test_Added0001(lx=5,name="雨花区")
                    assert q_bm[0] == '操作成功'
                    q_bm = q_bm[1]
                with allure.step("获取收发地街道编码"):
                    jd_bm = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm[0] == '操作成功'
                    jd_bm = jd_bm[1]
                with allure.step("新增收发货联系人"):
                    sf_hr = ict.Test_Added01().test_Added0028(hz_id=hz_id[1],gj_bm=2,sf_bm=sf_bm,cs_bm=cs_bm,xzq_bm=q_bm,jd_bm=jd_bm,name="测试集装箱装货地址",address="海山街道122号")
                    assert sf_hr[0] == '操作成功'
                with allure.step("获取装货单位档案"):
                    sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id[1], zh_name="测试集装箱装货地址")
                    assert sfh_dd[0] == '操作成功'
                    if sfh_dd[6] == "enabled_type_unenabled":
                        with allure.step("启用,，装货单位名称：{}".format(sfh_dd[2])):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_enabled":
                        with allure.step("装货单位已启用"):
                            pass
            if sfh_lxr[1] != 0 :
                with allure.step("存在，获取装货单位档案"):
                    sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id[1], zh_name="测试集装箱装货地址")
                    assert sfh_dd[0] == '操作成功'
                    if sfh_dd[6] == "enabled_type_unenabled":
                        with allure.step("装货单位未启用，启用,，装货单位名称：{}".format(sfh_dd[2])):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_disabled":
                        with allure.step("装货单位禁用，启用"):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_enabled":
                        with allure.step("装货单位已存在，并已启用"):
                            pass

    @allure.title("货主合同报价--集装箱出口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query007(self):
        log.info("货主合同报价--集装箱出口")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看货主同报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0047(hz_id=hz_id[1],contractType="cargo_owner_type")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0 :
                with allure.step("新增货主合同报价单"):
                    xzbz_dd = ict.Test_Added01().test_Added0049(hz_id=hz_id[1],contractType="cargo_owner_type")
                    assert xzbz_dd[0] == '操作成功'
                with allure.step("查看新增货主同报价单id"):
                    bz_dd = ict.Test_Added01().test_Added0048(hz_id=hz_id[1],contractType= "cargo_owner_type")
                    assert bz_dd[0] == '操作成功'
                with allure.step("启用新增货主报价单:{}".format(bz_dd[3])):
                    qybz_dd = ict.Test_Added01().test_Added0050(bjd_id=bz_dd[2])
                    assert qybz_dd == '操作成功'
                with allure.step("获取港口id"):
                    gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                    assert gk_id1[0] == '操作成功'
                    gk_id = gk_id1[1]  # 港口id
                    gk_name = gk_id1[2]  # 港口名称
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("获取收发地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    jd_bm = jd_bm1[1]
                    jd_name = jd_bm1[2]
                with allure.step("新增集装箱出口运输货主合同报价:港口：{},{}{}{}{}".format(gk_name,sf_name,cs_name,q_name,jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0052(customerPriceId=bz_dd[2],taskUnitCode="port_container_export_transport",
                    taskUnitTypeName="集装箱出口运输",transportPort=gk_id,departure=jd_bm,departureProvinces=sf_bm,departureCity=cs_bm,
                    departureArea=q_bm)
                    assert xzsc_bj == '操作成功'
                with allure.step("新增集装箱出口运输货主合同报价，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0053(bjd_id=bz_dd[2],transportPort=gk_id,departure=[jd_bm],taskUnitCode="port_container_export_transport")
                    assert bjd_bm[0] == '操作成功'
                with allure.step("启用新增集装箱出口运输货主合同报价,报价单编码：{}".format(bjd_bm[3])):
                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm[1])
                    assert jd_bm == '操作成功'
            if bz_dd1[1] != 0:
                with allure.step("存在集装箱出口运输货主合同报价单，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0048(hz_id=hz_id[1],contractType= "cargo_owner_type")
                    assert bjd_bm[0] == '操作成功'
                    if bjd_bm[1] == "status_type_unenabled":
                        with allure.step("启用已存在(未启用)的集装箱出口运输货主市场报价单,报价单id：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm== '操作成功'
                    if bjd_bm[1] == "status_disabled":
                        with allure.step("启用已存在(禁用)的集装箱出口运输货主市场报价,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_type_enabled":
                        with allure.step("已存在的集装箱出口运输货主市场报价，并已启用,报价单编码：{}".format(bjd_bm[3])):
                            pass
                    with allure.step("获取港口id"):
                        gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                        assert gk_id1[0] == '操作成功'
                        gk_id = gk_id1[1]  # 港口id
                        gk_name = gk_id1[2]  # 港口名称
                    with allure.step("获取收发地街道编码"):
                        jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                        assert jd_bm1[0] == '操作成功'
                        jd_bm = jd_bm1[1]
                        jd_name = jd_bm1[2]
                    with allure.step("存在货主合同报价，查看是否存在区域报价报价单信息"):
                        bjd_bm1 = ict.Test_Added01().test_Added0051(bjd_id=bjd_bm[2],transportPort=gk_id,departure=[jd_bm],taskUnitCode="port_container_export_transport")
                        assert bjd_bm1[0] == '操作成功'
                        if  bjd_bm1[1] == [] :
                            with allure.step("获取港口id"):
                                gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                                assert gk_id1[0] == '操作成功'
                                gk_id = gk_id1[1]  # 港口id
                                gk_name = gk_id1[2]  # 港口名称
                            with allure.step("获取收发地省编码"):
                                sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                                assert sf_bm1[0] == '操作成功'
                                sf_bm = sf_bm1[1]
                                sf_name = sf_bm1[2]
                            with allure.step("获取收发地市编码"):
                                cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                                assert cs_bm1[0] == '操作成功'
                                cs_bm = cs_bm1[1]
                                cs_name = cs_bm1[2]
                            with allure.step("获取收发地区编码"):
                                q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                                assert q_bm1[0] == '操作成功'
                                q_bm = q_bm1[1]
                                q_name = q_bm1[2]
                            with allure.step("获取收发地街道编码"):
                                jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                                assert jd_bm1[0] == '操作成功'
                                jd_bm = jd_bm1[1]
                                jd_name = jd_bm1[2]
                            with allure.step(
                                    "新增货主合同集装箱出口运输报价:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name, jd_name)):
                                xzsc_bj = ict.Test_Added01().test_Added0052(customerPriceId=bjd_bm[2],taskUnitCode="port_container_export_transport",
                                                                            taskUnitTypeName="集装箱出口运输",
                                                                            transportPort=gk_id, departure=jd_bm,
                                                                            departureProvinces=sf_bm,
                                                                            departureCity=cs_bm, departureArea=q_bm,
                                                                            )
                                assert xzsc_bj == '操作成功'
                            with allure.step("查看新增集装箱出口运输货主市场报价,查看报价id"):
                                bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_bm[2], transportPort=gk_id,departure=[jd_bm],taskUnitCode="port_container_export_transport")
                                assert bjd_bm2[0] == '操作成功'
                            with allure.step("启用新增集装箱出口运输货主市场报价,报价单编码：{}".format(bjd_bm[3])):
                                jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                assert jd_bm == '操作成功'
                        if bjd_bm1[1] != []:
                            with allure.step("存在集装箱出口运输货主合同报价,查看报价id"):
                                bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_bm[2],transportPort=gk_id,departure=[jd_bm],taskUnitCode="port_container_export_transport")
                                assert bjd_bm2[0] == '操作成功'
                                if  bjd_bm2[2] == "enabled_type_unenabled":
                                    with allure.step("启用存在(未启用)集装箱出口运输货主合同报价"):
                                        jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                        assert jd_bm == '操作成功'
                                if  bjd_bm2[2] == "enabled_type_disabled":
                                    with allure.step("启用存在(禁用)集装箱出口运输货主合同报价"):
                                        jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                        assert jd_bm == '操作成功'
                                if bjd_bm2[2] == "enabled_type_enabled":
                                    with allure.step("存在集装箱出口运输货主合同报价,并已启用报价"):
                                        pass

    @allure.title("集装箱出口报价--自有车")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query008(self):
        log.info("集装箱出口报价--自有车")
        with allure.step("查看自有车报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0076(fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0 :
                with allure.step("新增自有车报价单"):
                    xzbz_dd = ict.Test_Added01().test_Added0078(fw_lx="port_container_export_transport",fw_name="集装箱出口运输")
                    assert xzbz_dd[0] == '操作成功'
                with allure.step("查看新增自有车报价单id"):
                    bz_dd = ict.Test_Added01().test_Added0079(fw_lx="port_container_export_transport")
                    assert bz_dd[0] == '操作成功'
                with allure.step("启用新增自有车报价单:{}".format(bz_dd[2])):
                    qybz_dd = ict.Test_Added01().test_Added0080(bjd_id=bz_dd[1])
                    assert qybz_dd == '操作成功'
                with allure.step("获取港口id"):
                    gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                    assert gk_id1[0] == '操作成功'
                    gk_id = gk_id1[1]  # 港口id
                    gk_name = gk_id1[2]  # 港口名称
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("获取收发地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    jd_bm = jd_bm1[1]
                    jd_name = jd_bm1[2]
                with allure.step("新增自有车报价:港口：{},{}{}{}{}".format(gk_name,sf_name,cs_name,q_name,jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0008(marketPriceId=bz_dd[1],transportPort=gk_id,departure=jd_bm,
                                                                departureProvinces=sf_bm,departureCity=cs_bm,departureArea=q_bm,
                                                                taskUnitCode="port_container_export_transport" )
                    assert xzsc_bj == '操作成功'
                with allure.step("新增自有车集装箱出口运输自有车报价，查看报价信息"):
                    bjd_bm2 = ict.Test_Added01().test_Added0081(bjd_id=bz_dd[1],transportPort=gk_id,departure=jd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    with allure.step("新增集装箱出口运输自有车报价，报价单id：{}".format(bjd_bm2[1])):
                        jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                        assert jd_bm == '操作成功'
            if bz_dd1[1] != 0 :
                with allure.step("存在报价单，查看自有车报价单信息"):
                    bz_dd = ict.Test_Added01().test_Added0079(fw_lx="port_container_export_transport")
                    assert bz_dd[0] == '操作成功'
                    if  bz_dd[3] == "status_type_unenabled" :
                        with allure.step("启用存在未启用自有车报价单:{}".format(bz_dd[2])):
                            qybz_dd = ict.Test_Added01().test_Added0080(bjd_id=bz_dd[1])
                            assert qybz_dd == '操作成功'
                    if  bz_dd[3] == "status_disabled" :
                        with allure.step("启用存在禁用自有车报价单:{}".format(bz_dd[2])):
                            qybz_dd = ict.Test_Added01().test_Added0080(bjd_id=bz_dd[1])
                            assert qybz_dd == '操作成功'
                    if  bz_dd[3] == "status_type_enabled" :
                        with allure.step("自有车报价单已存在并已启用:{}".format(bz_dd[2])):
                            pass
        with allure.step("获取港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]  # 港口id
            gk_name = gk_id1[2]  # 港口名称
        with allure.step("获取收发地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm1[0] == '操作成功'
            jd_bm = jd_bm1[1]
            jd_name = jd_bm1[2]
        with allure.step("存在报价单，查看自有车报价单信息"):
            bz_dd = ict.Test_Added01().test_Added0079(fw_lx="port_container_export_transport")
            assert bz_dd[0] == '操作成功'
        with allure.step("存在自有车集装箱出口报价单，查看是否存在区域报价报价信息"):
            bjd_bm1 = ict.Test_Added01().test_Added0082(bjd_id=bz_dd[1],transportPort=gk_id,departure=jd_bm)
            assert bjd_bm1[0] == '操作成功'
            if  bjd_bm1[1] == 0 :
                with allure.step("获取港口id"):
                    gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                    assert gk_id1[0] == '操作成功'
                    gk_id = gk_id1[1]  # 港口id
                    gk_name = gk_id1[2]  # 港口名称
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("获取收发地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    jd_bm = jd_bm1[1]
                    jd_name = jd_bm1[2]
                with allure.step(
                        "新增集装箱出口运输自有车报价1:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name, jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0008(marketPriceId=bz_dd[1],transportPort=gk_id,departure=jd_bm,
                                                                departureProvinces=sf_bm,departureCity=cs_bm,departureArea=q_bm,
                                                                taskUnitCode="port_container_export_transport" )
                    assert xzsc_bj == '操作成功'
                with allure.step("查看新增集装箱出口运输自有车报价,查看报价id"):
                    bjd_bm2 = ict.Test_Added01().test_Added0081(bjd_id=bz_dd[1],transportPort=gk_id,departure=jd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    with allure.step("新增集装箱出口运输自有车报价，报价单id：{}".format(bjd_bm2[1])):
                        jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                        assert jd_bm == '操作成功'
            if bjd_bm1[1] != 0:
                with allure.step("存在集装箱出口运输自有车报价,查看报价id"):
                    bjd_bm2 = ict.Test_Added01().test_Added0081(bjd_id=bz_dd[1],transportPort=gk_id,departure=jd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    if  bjd_bm2[2] == "enabled_type_unenabled":
                        with allure.step("启用存在(未启用)集装箱出口运输自有车报价，报价单id：{}".format(bjd_bm2[1])):
                            jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                            assert jd_bm == '操作成功'
                    if  bjd_bm2[2] == "enabled_type_disabled":
                        with allure.step("启用存在(禁用)集装箱出口运输自有车报价"):
                            jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                            assert jd_bm == '操作成功'
                    if bjd_bm2[2] == "enabled_type_enabled":
                        with allure.step("存在集装箱出口运输自有车报价,并已启用报价"):
                            pass

    @allure.title("自有车档案1")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query009(self):
        log.info("自有车档案1")
        with allure.step("查看运输公司<租户测试自有车-集1>是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0059(gys_name="租户测试自有车-集1")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0 :
                with allure.step("<租户测试自有车-集1>运输公司是不存在，查看归属法人"):
                    gs_fr = ict.Test_Added01().test_Added0060()
                    assert gs_fr[0] == '操作成功'
                    fr_id =  gs_fr[1]   #法人id
                    with allure.step("新增<租户测试自有车-集1>运输公司"):
                        xz_gys = ict.Test_Added01().test_Added0061(fr_id=fr_id,gys_name="租户测试自有车-集1",gyslx="supplier_type_car_owner")
                        assert xz_gys[0] == '操作成功'
                        with allure.step("启用<租户测试自有车-集1>运输公司：{}".format(xz_gys[4])):
                            gs_fr = ict.Test_Added01().test_Added0063(gys_id=xz_gys[1],lx="enabled_type_enabled")
                            assert gs_fr == '操作成功'
            if bz_dd1[1] != 0 :
                with allure.step("<租户测试自有车-集1>查看运输公司档案"):
                    gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
                    assert gys_da[0] == '操作成功'
                    if  gys_da[3] == "enabled_type_unenabled" :
                        with allure.step("<租户测试自有车-集1>启用未启用运输公司：{}".format(gys_da[4])):
                            gs_fr = ict.Test_Added01().test_Added0063(gys_id=gys_da[1],lx="enabled_type_enabled")
                            assert gs_fr == '操作成功'
                    if  gys_da[3] == "enabled_type_disabled" :
                        with allure.step("<租户测试自有车-集1>启用禁用运输公司：{}".format(gys_da[4])):
                            gs_fr = ict.Test_Added01().test_Added0063(gys_id=gys_da[1],lx="enabled_type_enabled")
                            assert gs_fr == '操作成功'
                    if gys_da[3] == "enabled_type_enabled":
                        with allure.step("<租户测试自有车-集1>运输公司已存在，并已启用".format(gys_da[4])):
                            pass
        with allure.step("查看司机档案否存在"):
            sj_da = ict.Test_Added01().test_Added0064(sj_name="测试自有车-集1")
            assert sj_da[0] == '操作成功'
        with allure.step("查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            if sj_da[1] == 0 :
                with allure.step("司机档案不存在,新增司机档案1"):
                    xz_sj = ict.Test_Added01().test_Added0065(gys_id=gys_da[1],sj_name="测试自有车-集1",fulx="container_type")
                    assert xz_sj[0] == '操作成功'
                with allure.step("启用司机档案"):
                    gys_da = ict.Test_Added01().test_Added0067(lb_id=xz_sj[1],lx="enabled_type_enabled")
                    assert gys_da == '操作成功'
            if sj_da[1] != 0 :
                with allure.step("司机档案存在,查看司机档案1"):
                    xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
                    assert xz_sj[0] == '操作成功'
                    if xz_sj[3] == "enabled_type_unenabled" :
                        with allure.step("启用(未启用)司机档案"):
                            gys_da = ict.Test_Added01().test_Added0067(lb_id=xz_sj[1],lx="enabled_type_enabled")
                            assert gys_da == '操作成功'
                    if xz_sj[3] == "enabled_type_disabled" :
                        with allure.step("启用(禁用)司机档案"):
                            gys_da = ict.Test_Added01().test_Added0067(lb_id=xz_sj[1],lx="enabled_type_enabled")
                            assert gys_da == '操作成功'
                    if xz_sj[3] == "enabled_type_enabled" :
                        with allure.step("司机档案已存在，并已启用"):
                            pass
        with allure.step("查看粤ZZ0001车辆档案否存在"):
            sj_da = ict.Test_Added01().test_Added0068(gys_da[1],cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            if sj_da[1] == 0 :
                with allure.step("查看司机档案"):
                    xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
                    assert xz_sj[0] == '操作成功'
                with allure.step("车辆档案不存在,新增车辆档案"):
                    xz_sj = ict.Test_Added01().test_Added0069(gys_id=gys_da[1],sjda_id=xz_sj[1],
                       cz_qy="shekou_group",fw_lx="container_type",cp_hao="粤ZZ0001")
                    assert xz_sj[0] == '操作成功'
                with allure.step("启用车辆档案"):
                    gys_da = ict.Test_Added01().test_Added0071(lb_id=xz_sj[1],lx="enabled_type_enabled")
                    assert gys_da == '操作成功'
            if sj_da[1] != 0 :
                sj_da1 = ict.Test_Added01().test_Added0070(gys_da[1], cp_hao="粤ZZ0001")
                assert sj_da1[0] == '操作成功'
                if  sj_da1[5] == "enabled_type_unenabled" :
                    with allure.step("启用(未启用)粤ZZ0001车辆档案"):
                        gys_da = ict.Test_Added01().test_Added0071(lb_id=sj_da1[1], lx="enabled_type_enabled")
                        assert gys_da == '操作成功'
                if  sj_da1[5] == "enabled_type_disabled" :
                    with allure.step("启用(禁用)粤ZZ0001车辆档案"):
                        gys_da = ict.Test_Added01().test_Added0071(lb_id=sj_da1[1], lx="enabled_type_enabled")
                        assert gys_da == '操作成功'
                if  sj_da1[5] == "enabled_type_enabled" :
                    with allure.step("粤ZZ0001车辆档案已存在，并已启用"):
                        pass

    @allure.title("自有车档案2")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query010(self):
        log.info("自有车档案2")
        with allure.step("查看运输公司<租户测试自有车-集2>是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0059(gys_name="租户测试自有车-集2")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0 :
                with allure.step("<租户测试自有车-集2>运输公司是不存在，查看归属法人"):
                    gs_fr = ict.Test_Added01().test_Added0060()
                    assert gs_fr[0] == '操作成功'
                    fr_id =  gs_fr[1]   #法人id
                    with allure.step("新增<租户测试自有车-集2>运输公司"):
                        xz_gys = ict.Test_Added01().test_Added0061(fr_id=fr_id,gys_name="租户测试自有车-集2",gyslx="supplier_type_car_owner")
                        assert xz_gys[0] == '操作成功'
                        with allure.step("启用<租户测试自有车-集2>运输公司：{}".format(xz_gys[4])):
                            gs_fr = ict.Test_Added01().test_Added0063(gys_id=xz_gys[1],lx="enabled_type_enabled")
                            assert gs_fr == '操作成功'
            if bz_dd1[1] != 0 :
                with allure.step("<租户测试自有车-集2>查看运输公司档案"):
                    gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集2")
                    assert gys_da[0] == '操作成功'
                    if  gys_da[3] == "enabled_type_unenabled" :
                        with allure.step("<租户测试自有车-集2>启用未启用运输公司：{}".format(gys_da[4])):
                            gs_fr = ict.Test_Added01().test_Added0063(gys_id=gys_da[1],lx="enabled_type_enabled")
                            assert gs_fr == '操作成功'
                    if  gys_da[3] == "enabled_type_disabled" :
                        with allure.step("<租户测试自有车-集2>启用禁用运输公司：{}".format(gys_da[4])):
                            gs_fr = ict.Test_Added01().test_Added0063(gys_id=gys_da[1],lx="enabled_type_enabled")
                            assert gs_fr == '操作成功'
                    if gys_da[3] == "enabled_type_enabled":
                        with allure.step("<租户测试自有车-集2>运输公司已存在，并已启用".format(gys_da[4])):
                            pass
        with allure.step("查看司机档案2否存在"):
            sj_da = ict.Test_Added01().test_Added0064(sj_name="测试自有车-集2")
            assert sj_da[0] == '操作成功'
        with allure.step("查看运输公司档案2"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集2")
            assert gys_da[0] == '操作成功'
            if sj_da[1] == 0 :
                with allure.step("司机档案不存在,新增司机档案2"):
                    xz_sj = ict.Test_Added01().test_Added0065(gys_id=gys_da[1],sj_name="测试自有车-集2",fulx="container_type")
                    assert xz_sj[0] == '操作成功'
                with allure.step("启用司机档案2"):
                    gys_da = ict.Test_Added01().test_Added0067(lb_id=xz_sj[1],lx="enabled_type_enabled")
                    assert gys_da == '操作成功'
            if sj_da[1] != 0 :
                with allure.step("司机档案存在,查看司机档案2"):
                    xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集2")
                    assert xz_sj[0] == '操作成功'
                    if xz_sj[3] == "enabled_type_unenabled" :
                        with allure.step("启用(未启用)司机档案2"):
                            gys_da = ict.Test_Added01().test_Added0067(lb_id=xz_sj[1],lx="enabled_type_enabled")
                            assert gys_da == '操作成功'
                    if xz_sj[3] == "enabled_type_disabled" :
                        with allure.step("启用(禁用)司机档案2"):
                            gys_da = ict.Test_Added01().test_Added0067(lb_id=xz_sj[1],lx="enabled_type_enabled")
                            assert gys_da == '操作成功'
                    if xz_sj[3] == "enabled_type_enabled" :
                        with allure.step("司机档案已存在2，并已启用"):
                            pass
        with allure.step("查看粤B7788车辆档案否存在"):
            sj_da = ict.Test_Added01().test_Added0068(gys_da[1],cp_hao="粤B7788")
            assert sj_da[0] == '操作成功'
            if sj_da[1] == 0 :
                with allure.step("查看司机档案2"):
                    xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集2")
                    assert xz_sj[0] == '操作成功'
                with allure.step("车辆档案不存在,新增车辆档案"):
                    xz_sj = ict.Test_Added01().test_Added0069(gys_id=gys_da[1],sjda_id=xz_sj[1],
                       cz_qy="shekou_group",fw_lx="container_type",cp_hao="粤B7788")
                    assert xz_sj[0] == '操作成功'
                with allure.step("启用车辆档案粤B7788"):
                    gys_da = ict.Test_Added01().test_Added0071(lb_id=xz_sj[1],lx="enabled_type_enabled")
                    assert gys_da == '操作成功'
            if sj_da[1] != 0 :
                sj_da1 = ict.Test_Added01().test_Added0070(gys_da[1],cp_hao="粤B7788")
                assert sj_da1[0] == '操作成功'
                if  sj_da1[5] == "enabled_type_unenabled" :
                    with allure.step("启用(未启用)粤B7788车辆档案"):
                        gys_da = ict.Test_Added01().test_Added0071(lb_id=sj_da1[1],lx="enabled_type_enabled")
                        assert gys_da == '操作成功'
                if  sj_da1[5] == "enabled_type_disabled" :
                    with allure.step("启用(禁用)粤B7788车辆档案"):
                        gys_da = ict.Test_Added01().test_Added0071(lb_id=sj_da1[1],lx="enabled_type_enabled")
                        assert gys_da == '操作成功'
                if  sj_da1[5] == "enabled_type_enabled" :
                    with allure.step("粤B7788车辆档案已存在，并已启用"):
                        pass

    @allure.title("收发货联系人2")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query011(self):
        log.info("收发货联系人2")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看收发货联系人是否存在"):
            sfh_lxr = ict.Test_Added01().test_Added0026(hz_id=hz_id[1],zh_name="厢式车装货地址1")
            assert sfh_lxr[0] == '操作成功'
            if sfh_lxr[1] == 0 :
                with allure.step("获取收发地省编码"):
                    sf_bm = ict.Test_Added01().test_Added0001(lx=3,name="广东省")
                    assert sf_bm[0] == '操作成功'
                    sf_bm = sf_bm[1]
                with allure.step("获取收发地市编码"):
                    cs_bm = ict.Test_Added01().test_Added0001(lx=4,name="深圳市")
                    assert cs_bm[0] == '操作成功'
                    cs_bm = cs_bm[1]
                with allure.step("获取收发地区编码"):
                    q_bm = ict.Test_Added01().test_Added0001(lx=5,name="盐田区")
                    assert q_bm[0] == '操作成功'
                    q_bm = q_bm[1]
                with allure.step("获取收发地街道编码"):
                    jd_bm = ict.Test_Added01().test_Added0001(lx=6,name="海山街道")
                    assert jd_bm[0] == '操作成功'
                    jd_bm = jd_bm[1]
                with allure.step("新增收发货联系人"):
                    sf_hr = ict.Test_Added01().test_Added0028(hz_id=hz_id[1],gj_bm=2,sf_bm=sf_bm,cs_bm=cs_bm,xzq_bm=q_bm,jd_bm=jd_bm,name="厢式车装货地址1",address="海山大道99号")
                    assert sf_hr[0] == '操作成功'
                with allure.step("获取装货单位档案"):
                    sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id[1], zh_name="厢式车装货地址1")
                    assert sfh_dd[0] == '操作成功'
                    if sfh_dd[6] == "enabled_type_unenabled":
                        with allure.step("启用,，装货单位名称：{}".format(sfh_dd[2])):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_enabled":
                        with allure.step("装货单位已启用"):
                            pass
            if sfh_lxr[1] != 0 :
                with allure.step("存在，获取装货单位档案"):
                    sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id[1], zh_name="厢式车装货地址1")
                    assert sfh_dd[0] == '操作成功'
                    if sfh_dd[6] == "enabled_type_unenabled":
                        with allure.step("装货单位未启用，启用,，装货单位名称：{}".format(sfh_dd[2])):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_disabled":
                        with allure.step("装货单位禁用，启用"):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_enabled":
                        with allure.step("装货单位已存在，并已启用"):
                            pass

    @allure.title("收发货联系人3")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query012(self):
        log.info("收发货联系人3")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看收发货联系人是否存在"):
            sfh_lxr = ict.Test_Added01().test_Added0026(hz_id=hz_id[1],zh_name="厢式车装货地址2")
            assert sfh_lxr[0] == '操作成功'
            if sfh_lxr[1] == 0 :
                with allure.step("获取收发地省编码"):
                    sf_bm = ict.Test_Added01().test_Added0001(lx=3,name="广东省")
                    assert sf_bm[0] == '操作成功'
                    sf_bm = sf_bm[1]
                with allure.step("获取收发地市编码"):
                    cs_bm = ict.Test_Added01().test_Added0001(lx=4,name="深圳市")
                    assert cs_bm[0] == '操作成功'
                    cs_bm = cs_bm[1]
                with allure.step("获取收发地区编码"):
                    q_bm = ict.Test_Added01().test_Added0001(lx=5,name="盐田区")
                    assert q_bm[0] == '操作成功'
                    q_bm = q_bm[1]
                with allure.step("获取收发地街道编码"):
                    jd_bm = ict.Test_Added01().test_Added0001(lx=6,name="海山街道")
                    assert jd_bm[0] == '操作成功'
                    jd_bm = jd_bm[1]
                with allure.step("新增收发货联系人"):
                    sf_hr = ict.Test_Added01().test_Added0028(hz_id=hz_id[1],gj_bm=2,sf_bm=sf_bm,cs_bm=cs_bm,xzq_bm=q_bm,jd_bm=jd_bm,name="厢式车装货地址2",address="海山街道100号")
                    assert sf_hr[0] == '操作成功'
                with allure.step("获取装货单位档案"):
                    sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id[1], zh_name="厢式车装货地址1")
                    assert sfh_dd[0] == '操作成功'
                    if sfh_dd[6] == "enabled_type_unenabled":
                        with allure.step("启用,，装货单位名称：{}".format(sfh_dd[2])):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_enabled":
                        with allure.step("装货单位已启用"):
                            pass
            if sfh_lxr[1] != 0 :
                with allure.step("存在，获取装货单位档案"):
                    sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id[1], zh_name="厢式车装货地址2")
                    assert sfh_dd[0] == '操作成功'
                    if sfh_dd[6] == "enabled_type_unenabled":
                        with allure.step("装货单位未启用，启用,，装货单位名称：{}".format(sfh_dd[2])):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_disabled":
                        with allure.step("装货单位禁用，启用"):
                            qy_jdzx = ict.Test_Added01().test_Added0030(zhdw_id=sfh_dd[1])
                            assert qy_jdzx == '操作成功'
                    if sfh_dd[6] == "enabled_type_enabled":
                        with allure.step("装货单位已存在，并已启用"):
                            pass

    @allure.title("货主市场报价--厢式车内陆运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query013(self):
        log.info("货主市场报价--厢式车内陆运输")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看货主同报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0047(hz_id=hz_id[1],contractType="cargo_owner_type")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0:
                with allure.step("新增货主合同报价单"):
                    xzbz_dd = ict.Test_Added01().test_Added0049(hz_id=hz_id[1],contractType="cargo_owner_type")
                    assert xzbz_dd[0] == '操作成功'
                with allure.step("查看新增货主同报价单id"):
                    bz_dd = ict.Test_Added01().test_Added0048(hz_id=hz_id[1],contractType= "cargo_owner_type")
                    assert bz_dd[0] == '操作成功'
                with allure.step("启用新增货主报价单:{}".format(bz_dd[3])):
                    qybz_dd = ict.Test_Added01().test_Added0050(bjd_id=bz_dd[2])
                    assert qybz_dd == '操作成功'
                with allure.step("获取卸货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    xsf_bm = sf_bm1[1]
                    xsf_name = sf_bm1[2]
                with allure.step("获取卸货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    xcs_bm = cs_bm1[1]
                    xcs_name = cs_bm1[2]
                with allure.step("获取卸货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    xq_bm = q_bm1[1]
                    xq_name = q_bm1[2]
                with allure.step("获取卸货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    xjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]

                with allure.step("获取装货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
                    assert sf_bm1[0] == '操作成功'
                    zsf_bm = sf_bm1[1]
                    zsf_name = sf_bm1[2]
                with allure.step("获取装货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
                    assert cs_bm1[0] == '操作成功'
                    zcs_bm = cs_bm1[1]
                    zcs_name = cs_bm1[2]
                with allure.step("获取装货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
                    assert q_bm1[0] == '操作成功'
                    zq_bm = q_bm1[1]
                    zq_name = q_bm1[2]
                with allure.step("获取装货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
                    assert jd_bm1[0] == '操作成功'
                    zjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]
                with allure.step("新增厢式车运输货主合同报价，"):
                    xz_bj = ict.Test_Added01().test_Added0100(customerPriceId=bz_dd[2],taskUnitCode="bulkcargo_transport",taskUnitTypeName="厢式车运输",
                            departure=zjd_bm,departureProvinces=zsf_bm,departureCity=zcs_bm,departureArea=zq_bm,
                            destination=xjd_bm,destinationProvinces=xsf_bm,destinationCity=xcs_bm,destinationArea=xq_bm)
                    assert xz_bj == '操作成功'
                with allure.step("新增厢式车运输货主合同报价，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0101(bjd_id=bz_dd[2],taskUnitCode="bulkcargo_transport",jd_bm=[zjd_bm])
                    assert bjd_bm[0] == '操作成功'
                    bj_id =  bjd_bm[2][0]["id"]
                with allure.step("启用新增厢式车运输货主合同报价,报价单编码：{}".format(bz_dd[3])):
                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                    assert jd_bm == '操作成功'
            if bz_dd1[1] != 0:
                with allure.step("存在货主合同报价单，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0048(hz_id=hz_id[1],contractType= "cargo_owner_type")
                    assert bjd_bm[0] == '操作成功'
                    if bjd_bm[1] == "status_type_unenabled":
                        with allure.step("启用已存在(未启用)的集装箱出口运输货主市场报价单,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_disabled":
                        with allure.step("启用已存在(禁用)的集装箱出口运输货主市场报价,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_type_enabled":
                        with allure.step("已存在货主市场报价单，并已启用,报价单编码：{}".format(bjd_bm[3])):
                            pass
        with allure.step("获取装货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
            assert jd_bm1[0] == '操作成功'
            zjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]
        with allure.step("查看是否存在厢式车运输货主合同报价"):
            bjd_bm3 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=[zjd_bm])
            assert bjd_bm3[0] == '操作成功'
            if bjd_bm3[1] == 0 :
                with allure.step("获取卸货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    xsf_bm = sf_bm1[1]
                    xsf_name = sf_bm1[2]
                with allure.step("获取卸货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    xcs_bm = cs_bm1[1]
                    xcs_name = cs_bm1[2]
                with allure.step("获取卸货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    xq_bm = q_bm1[1]
                    xq_name = q_bm1[2]
                with allure.step("获取卸货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    xjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]
                with allure.step("获取装货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
                    assert sf_bm1[0] == '操作成功'
                    zsf_bm = sf_bm1[1]
                    zsf_name = sf_bm1[2]
                with allure.step("获取装货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
                    assert cs_bm1[0] == '操作成功'
                    zcs_bm = cs_bm1[1]
                    zcs_name = cs_bm1[2]
                with allure.step("获取装货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
                    assert q_bm1[0] == '操作成功'
                    zq_bm = q_bm1[1]
                    zq_name = q_bm1[2]
                with allure.step("获取装货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
                    assert jd_bm1[0] == '操作成功'
                    zjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]
                with allure.step("新增厢式车运输货主合同报价，"):
                    xz_bj = ict.Test_Added01().test_Added0100(customerPriceId=bjd_bm[2],
                                                              taskUnitCode="bulkcargo_transport",
                                                              taskUnitTypeName="厢式车运输",
                                                              departure=zjd_bm, departureProvinces=zsf_bm,
                                                              departureCity=zcs_bm, departureArea=zq_bm,
                                                              destination=xjd_bm,
                                                              destinationProvinces=xsf_bm,
                                                              destinationCity=xcs_bm, destinationArea=xq_bm)
                    assert xz_bj == '操作成功'
                with allure.step("新增厢式车运输货主合同报价，查看报价单信息"):
                    bjd_bm5 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=[zjd_bm])
                    assert bjd_bm5[0] == '操作成功'
                    bj_id = bjd_bm5[2][0]["id"]
                with allure.step("启用新增厢式车运输货主合同报价,报价单编码：{},{}".format(bjd_bm[3],bj_id)):
                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                    assert jd_bm == '操作成功'
            if bjd_bm3[1] != 0:
                    with allure.step("存在厢式车运输货主合同报价，查看报价单信息"):
                            bjd_bm4 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=[zjd_bm])
                            assert bjd_bm4[0] == '操作成功'
                            bj_id = bjd_bm4[2][0]["id"]
                            bjd_zt = bjd_bm4[2][0]["enabledType"]
                            if bjd_zt == "enabled_type_unenabled":
                                with allure.step("启用存在(未启用)厢式车运输货主合同报价"):
                                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                                    assert jd_bm == '操作成功'
                            if bjd_zt == "enabled_type_disabled":
                                with allure.step("启用存在(禁用)厢式车运输货主合同报价"):
                                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                                    assert jd_bm == '操作成功'
                            if bjd_zt == "enabled_type_enabled":
                                with allure.step("存在厢式车货主合同报价,并已启用报价"):
                                    pass

    @allure.title("区域规则-厢式车运输,操作区域蛇口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query014(self):
        log.info("区域规则-厢式车运输,操作区域蛇口")
        '''用例描述'''
        with allure.step("查看区域规则-厢式车运输,操作区域蛇口是否存在"):
            qy_gh = ict.Test_Added01().test_Added0031(taskUnitCode="bulkcargo_transport",centerName="shekou_group")
            assert qy_gh[0] =='操作成功'
            if qy_gh[1] == [] :
                with allure.step("新增厢式车运输区域规划"):
                    xz_gh = ict.Test_Added01().test_Added0032(taskUnitCode="bulkcargo_transport",centerName="shekou_group",isContainer=0)
                    assert xz_gh == '操作成功'
                with allure.step("查看厢式车运输区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="bulkcargo_transport",centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                with allure.step("启用厢式车运输区域规划状态"):
                    qyqy_gh = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                    assert qyqy_gh == '启用成功'
            if qy_gh[1] != [] :
                with allure.step("查看厢式车运输区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="bulkcargo_transport",centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                    if qygh_id[1] == "enabled_type_unenabled":
                        with allure.step("未启用厢式车运输查看区域规划id+状态"):
                            qy_qyzx = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                            assert qy_qyzx == '启用成功'
                    if qygh_id[1] == "enabled_type_disabled":
                        with allure.step("禁用厢式车运输查看区域规划id+状态"):
                            qy_qyzx = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                            assert qy_qyzx == '启用成功'
                    if qygh_id[1] == "enabled_type_enabled":
                        with allure.step("厢式车运输区域规划已存在，并已启用"):
                            pass

    @allure.title("接单中心-厢式车运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query015(self):
        log.info("接单中心-厢式车运输")
        with allure.step("查看接单中心-厢式车运输，是否存在"):
            jd_zx = ict.Test_Added01().test_Added0035(taskUnitCode="bulkcargo_transport")
            assert jd_zx[0] =='操作成功'
            if jd_zx[1] == 0 :
                with allure.step("新增厢式车接单中心"):
                    zxjd_zx = ict.Test_Added01().test_Added0036(taskUnitCode="bulkcargo_transport",isContainer=0)
                    assert zxjd_zx == '操作成功'
                with allure.step("查看厢式车接单中心id"):
                    jdzx_id = ict.Test_Added01().test_Added0037(taskUnitCode="bulkcargo_transport")
                    assert jdzx_id[0] == '操作成功'
                with allure.step("启用厢式车接单中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                    assert qy_jdzx == '启用成功'
            if jd_zx[1] != 0 :
                with allure.step("查看厢式车接单中心id"):
                    jdzx_id = ict.Test_Added01().test_Added0037(taskUnitCode="bulkcargo_transport")
                    assert jdzx_id[0] == '操作成功'
                    if jdzx_id[2] == "enabled_type_unenabled":
                        with allure.step("接单中心厢式车未启用，启用接单中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jdzx_id[2] == "enabled_type_disabled":
                        with allure.step("接单中心厢式车禁用，启用接单中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jdzx_id[2] == "enabled_type_enabled":
                        with allure.step("厢式车接单中已存在，并已启用"):
                            pass

    @allure.title("计划中心-厢式车运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query016(self):
        log.info("计划中心-厢式车运输")
        with allure.step("查看计划中心-厢式车运输运输，是否存在"):
            jh_zx = ict.Test_Added01().test_Added0039(taskUnitCode="bulkcargo_transport")
            assert jh_zx[0] == '操作成功'
            if jh_zx[1] == 0:
                with allure.step("新增厢式车运输计划中心"):
                    zxjh_zx = ict.Test_Added01().test_Added0040(taskUnitCode="bulkcargo_transport",isContainer=0)
                    assert zxjh_zx == '操作成功'
                with allure.step("查看厢式车运输计划中心id"):
                    jhzx_id = ict.Test_Added01().test_Added0041(taskUnitCode="bulkcargo_transport")
                    assert jhzx_id[0] == '操作成功'
                with allure.step("启用厢式车运输计划中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                    assert qy_jdzx == '启用成功'
            if jh_zx[1] != 0:
                with allure.step("查看厢式车运输计划中心id"):
                    jhzx_id = ict.Test_Added01().test_Added0041(taskUnitCode="bulkcargo_transport")
                    assert jhzx_id[0] == '操作成功'
                    if jhzx_id[2] == "enabled_type_unenabled":
                        with allure.step("厢式车运输计划中心未启用，启用计划中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jhzx_id[2] == "enabled_type_disabled":
                        with allure.step("厢式车运输计划中心禁用，启用计划中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jhzx_id[2] == "enabled_type_enabled":
                        with allure.step("厢式车运输计划中已存在，并已启用"):
                            pass

    @allure.title("运输公司合同报价--厢式车内陆运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query017(self):
        log.info("运输公司合同报价--厢式车内陆运输")
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看运输公司合同报价是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0047(hz_id=gys_id[1],contractType="transportation_company_type")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0:
                with allure.step("新增运输公司合同报价厢式车"):
                    xzbz_dd = ict.Test_Added01().test_Added0049(hz_id=gys_id[1],contractType="transportation_company_type")
                    assert xzbz_dd[0] == '操作成功'
                with allure.step("查看新增运输公司合同报价厢式车id"):
                    bz_dd = ict.Test_Added01().test_Added0048(hz_id=gys_id[1],contractType= "transportation_company_type")
                    assert bz_dd[0] == '操作成功'
                with allure.step("启用新增运输公司合同报价厢式车:{}".format(bz_dd[3])):
                    qybz_dd = ict.Test_Added01().test_Added0050(bjd_id=bz_dd[2])
                    assert qybz_dd == '操作成功'
                with allure.step("获取卸货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    xsf_bm = sf_bm1[1]
                    xsf_name = sf_bm1[2]
                with allure.step("获取卸货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    xcs_bm = cs_bm1[1]
                    xcs_name = cs_bm1[2]
                with allure.step("获取卸货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    xq_bm = q_bm1[1]
                    xq_name = q_bm1[2]
                with allure.step("获取卸货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    xjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]

                with allure.step("获取装货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
                    assert sf_bm1[0] == '操作成功'
                    zsf_bm = sf_bm1[1]
                    zsf_name = sf_bm1[2]
                with allure.step("获取装货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
                    assert cs_bm1[0] == '操作成功'
                    zcs_bm = cs_bm1[1]
                    zcs_name = cs_bm1[2]
                with allure.step("获取装货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
                    assert q_bm1[0] == '操作成功'
                    zq_bm = q_bm1[1]
                    zq_name = q_bm1[2]
                with allure.step("获取装货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
                    assert jd_bm1[0] == '操作成功'
                    zjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]
                with allure.step("新增厢式车运输公司合同报价，"):
                    xz_bj = ict.Test_Added01().test_Added0100(customerPriceId=bz_dd[2],
                                                              taskUnitCode="bulkcargo_transport",
                                                              taskUnitTypeName="厢式车运输",
                                                              departure=zjd_bm, departureProvinces=zsf_bm,
                                                              departureCity=zcs_bm, departureArea=zq_bm,
                                                              destination=xjd_bm, destinationProvinces=xsf_bm,
                                                              destinationCity=xcs_bm, destinationArea=xq_bm)
                    assert xz_bj == '操作成功'
                with allure.step("新增厢式车运输公司合同报价，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0101(bjd_id=bz_dd[2],taskUnitCode="bulkcargo_transport",jd_bm=[zjd_bm])
                    assert bjd_bm[0] == '操作成功'
                    bj_id = bjd_bm[2][0]["id"]
                with allure.step("启用新增厢式车运输公司合同报价,报价单编码：{}".format(bz_dd[3])):
                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                    assert jd_bm == '操作成功'
            if bz_dd1[1] != 0:
                with allure.step("存在运输公司厢式车合同报价，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0048(hz_id=gys_id[1],contractType= "transportation_company_type")
                    assert bjd_bm[0] == '操作成功'
                    if bjd_bm[1] == "status_type_unenabled":
                        with allure.step("启用已存在(未启用)运输公司厢式车报价单,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_disabled":
                        with allure.step("启用已存在(禁用)运输公司厢式车报价单,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_type_enabled":
                        with allure.step("已存在运输公司厢式车报价单，并已启用,报价单编码：{}".format(bjd_bm[3])):
                            pass
                    with allure.step("获取装货地街道编码"):
                        jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
                        assert jd_bm1[0] == '操作成功'
                        zjd_bm = jd_bm1[1]
                        xjd_name = jd_bm1[2]
                    with allure.step("查看是否存在厢式车运输运输公司合同报价"):
                        bjd_bm3 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=[zjd_bm])
                        assert bjd_bm3[0] == '操作成功'
                        if bjd_bm3[1] == 0:
                            with allure.step("获取卸货地省编码"):
                                sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                                assert sf_bm1[0] == '操作成功'
                                xsf_bm = sf_bm1[1]
                                xsf_name = sf_bm1[2]
                            with allure.step("获取卸货地市编码"):
                                cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                                assert cs_bm1[0] == '操作成功'
                                xcs_bm = cs_bm1[1]
                                xcs_name = cs_bm1[2]
                            with allure.step("获取卸货地区编码"):
                                q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                                assert q_bm1[0] == '操作成功'
                                xq_bm = q_bm1[1]
                                xq_name = q_bm1[2]
                            with allure.step("获取卸货地街道编码"):
                                jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                                assert jd_bm1[0] == '操作成功'
                                xjd_bm = jd_bm1[1]
                                xjd_name = jd_bm1[2]
                            with allure.step("获取装货地省编码"):
                                sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
                                assert sf_bm1[0] == '操作成功'
                                zsf_bm = sf_bm1[1]
                                zsf_name = sf_bm1[2]
                            with allure.step("获取装货地市编码"):
                                cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
                                assert cs_bm1[0] == '操作成功'
                                zcs_bm = cs_bm1[1]
                                zcs_name = cs_bm1[2]
                            with allure.step("获取装货地区编码"):
                                q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
                                assert q_bm1[0] == '操作成功'
                                zq_bm = q_bm1[1]
                                zq_name = q_bm1[2]
                            with allure.step("获取装货地街道编码"):
                                jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
                                assert jd_bm1[0] == '操作成功'
                                zjd_bm = jd_bm1[1]
                                xjd_name = jd_bm1[2]
                            with allure.step("新增厢式车运输运输公司合同报价，"):
                                xz_bj = ict.Test_Added01().test_Added0100(customerPriceId=bjd_bm[2],
                                                                          taskUnitCode="bulkcargo_transport",
                                                                          taskUnitTypeName="厢式车运输",
                                                                          departure=zjd_bm, departureProvinces=zsf_bm,
                                                                          departureCity=zcs_bm, departureArea=zq_bm,
                                                                          destination=xjd_bm,
                                                                          destinationProvinces=xsf_bm,
                                                                          destinationCity=xcs_bm, destinationArea=xq_bm)
                                assert xz_bj == '操作成功'
                            with allure.step("新增厢式车运输公司合同报价，查看报价单信息{}".format(bjd_bm[2])):
                                bjd_bm1 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=[zjd_bm])
                                assert bjd_bm1[0] == '操作成功'
                                bj_id = bjd_bm1[2][0]["id"]
                            with allure.step("启用新增厢式车运输公司合同报价,报价单编码：{}".format(bjd_bm[3])):
                                jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                                assert jd_bm == '操作成功'
                        if bjd_bm3[1] != 0:
                            with allure.step("存在厢式车运输运输公司合同报价，查看报价单信息"):
                                bjd_bm4 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=[zjd_bm])
                                assert bjd_bm4[0] == '操作成功'
                                bj_id = bjd_bm4[2][0]["id"]
                                bjd_zt = bjd_bm4[2][0]["enabledType"]
                                if bjd_zt == "enabled_type_unenabled":
                                    with allure.step("启用存在(未启用)厢式车运输公司合同报价"):
                                        jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                                        assert jd_bm == '操作成功'
                                if bjd_zt == "enabled_type_disabled":
                                    with allure.step("启用存在(禁用)厢式车运输公司合同报价"):
                                        jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                                        assert jd_bm == '操作成功'
                                if bjd_zt == "enabled_type_enabled":
                                    with allure.step("存在厢式车运输公司合同报价,并已启用报价"):
                                        pass

    @allure.title("运输公司车辆司机档案")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query018(self):
        log.info("运输公司车辆司机档案")
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看司机是否存在"):
            siji_da = ict.Test_transport_company01().test_transport0003(siji_name="测试运输公司司机1",gys_id=gys_id[1])
            assert siji_da[0] == '操作成功'
            if siji_da[1] == 0 :
                with allure.step("新增司机档案"):
                    xz_shiji = ict.Test_transport_company01().test_transport0004(gys_id=gys_id[1],shiji_name="测试运输公司司机1",siji_dh="15252545555")
                    assert xz_shiji == '操作成功'
            if siji_da[1] != 0 :
                with allure.step("司机档案存在，查看司机状态"):
                    siji_zt = siji_da[2][0]["enabledType"]
                    siji_id = siji_da[2][0]["id"]
                    if  siji_zt == "enabled_type_disabled":
                        with allure.step("司机档案存在被禁用，启用司机状态"):
                            qy_siji = ict.Test_transport_company01().test_transport0005(siji_id=siji_id)
                            assert qy_siji == '操作成功'
                    if  siji_zt == "enabled_type_unenabled":
                        with allure.step("司机档案存在未启用，启用司机状态"):
                            qy_siji = ict.Test_transport_company01().test_transport0005(siji_id=siji_id)
                            assert qy_siji == '操作成功'
                    if siji_zt == "enabled_type_enabled":
                        with allure.step("司机档案存在且已启用"):
                            pass
        with allure.step("查看车辆是否存在"):
            cl_da = ict.Test_transport_company01().test_transport0007(c_pai="粤A6688",gys_id=gys_id[1])
            assert cl_da[0] == '操作成功'
        with allure.step("查看司机ID"):
            siji_da = ict.Test_transport_company01().test_transport0003(siji_name="", gys_id=gys_id[1])
            assert siji_da[0] == '操作成功'
            siji_id =  siji_da[2][0]["id"]
            if cl_da[1] == 0:
                with allure.step("新增车辆档案"):
                    xz_cl = ict.Test_transport_company01().test_transport0006(gys_id=gys_id[1],
                                                                                 c_pai="粤A6688",siji_id=siji_id)
                    assert xz_cl == '操作成功'
            if cl_da[1] != 0:
                with allure.step("车辆档案存在，查看车辆状态"):
                    cl_zt = siji_da[2][0]["enabledType"]
                    cl_id = siji_da[2][0]["id"]
                    if cl_zt == "enabled_type_disabled":
                        with allure.step("车辆档案存在被禁用，启用司机状态"):
                            qy_siji = ict.Test_transport_company01().test_transport0008(cl_id=cl_id)
                            assert qy_siji == '操作成功'
                    if cl_zt == "enabled_type_unenabled":
                        with allure.step("车辆档案存在未启用，启用司机状态"):
                            qy_siji = ict.Test_transport_company01().test_transport0008(cl_id=cl_id)
                            assert qy_siji == '操作成功'
                    if cl_zt == "enabled_type_enabled":
                        with allure.step("车辆档案存在且已启用"):
                            pass

    @allure.title("费用项档案")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query019(self):
        log.info("费用项档案")
        with allure.step("查看'报关费'费用项档案是否存在"):
            fy_lx = ict.Test_Added01().test_Added0111(fyx_name="报关费")
            assert fy_lx[0] == '操作成功'
            if fy_lx[1] == 0 :
                with allure.step("新增'报关费'费用项档案"):
                    xz_fylx = ict.Test_Added01().test_Added0112(fyx_name="报关费")
                    assert xz_fylx == '操作成功'
            if  fy_lx[1] != 0 :
                fy_zt = fy_lx[2][0]["active"]
                fyx_id = fy_lx[2][0]["id"]
                if fy_zt ==  "active_invalid" :
                    with allure.step("激活'报关费'费用项档案"):
                        jh_fylx = ict.Test_Added01().test_Added0113(fyx_id=fyx_id)
                        assert jh_fylx == '操作成功'
                else:
                    with allure.step("'报关费'费用项档案,已存在，并已启用"):
                        pass

    @allure.title("司机市场报价--集装箱出口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query020(self):
        log.info("司机市场报价--集装箱出口")
        with allure.step("查看司机市场报价报价单是否存在"):
            sj_bjd = ict.Test_Added01().test_Added0115(fy_lx="port_container_export_transport")
            assert sj_bjd[0] == '操作成功'
            if  sj_bjd[1] == 0 :
                with allure.step("新增司机市场报价报价单"):
                    xz_bjd = ict.Test_Added01().test_Added0116(fy_lx="port_container_export_transport",fy_name="集装箱出口运输")
                    assert xz_bjd == '操作成功'
                with allure.step("查看司机市场报价报价单id"):
                    ck_bjd = ict.Test_Added01().test_Added0115(fy_lx="port_container_export_transport")
                    assert ck_bjd[0] == '操作成功'
                    bjd_id = ck_bjd[2][0]["id"]
                with allure.step("启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                    qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                    assert qy_bjd == '操作成功'
            if  sj_bjd[1] != 0 :
                bjd_id = sj_bjd[2][0]["id"]
                bjd_zt = sj_bjd[2][0]["statusType"]
                if bjd_zt == "status_type_unenabled" :
                    with allure.step("报价单未启用，启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                        qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                        assert qy_bjd == '操作成功'
                if bjd_zt == "status_disabled" :
                    with allure.step("报价单已禁用，启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                        qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                        assert qy_bjd == '操作成功'
                if bjd_zt == "status_type_enabled" :
                    with allure.step("司机市场报价报价单已存在并已启用，报价单id{}".format(bjd_id)):
                        pass
        with allure.step("查看司机市场报价报价单id"):
            sj_bjd = ict.Test_Added01().test_Added0115(fy_lx="port_container_export_transport")
            assert sj_bjd[0] == '操作成功'
            bjd_id = sj_bjd[2][0]["id"]
        with allure.step("获取港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]  # 港口id
            gk_name = gk_id1[2]  # 港口名称
        with allure.step("获取收发地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm1[0] == '操作成功'
            jd_bm = jd_bm1[1]
            jd_name = jd_bm1[2]
        with allure.step("查看是否存在司机市场区域报价报价单信息"):
            bjd_bm1 = ict.Test_Added01().test_Added0082(bjd_id=bjd_id,transportPort=gk_id,departure=jd_bm)
            assert bjd_bm1[0] == '操作成功'
            if  bjd_bm1[1] == 0 :
                with allure.step("获取港口id"):
                    gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                    assert gk_id1[0] == '操作成功'
                    gk_id = gk_id1[1]  # 港口id
                    gk_name = gk_id1[2]  # 港口名称
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("获取收发地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    jd_bm = jd_bm1[1]
                    jd_name = jd_bm1[2]
                with allure.step(
                        "新增司机市场集装箱出口运输报价:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name, jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0008(marketPriceId=bjd_id, transportPort=gk_id,
                                                                departure=jd_bm,
                                                                departureProvinces=sf_bm, departureCity=cs_bm,
                                                                departureArea=q_bm,
                                                                taskUnitCode="port_container_export_transport")
                    assert xzsc_bj == '操作成功'
                with allure.step("查看新增集装箱出口运输货主市场报价,查看报价id"):
                    bjd_bm2 = ict.Test_Added01().test_Added0081(bjd_id=bjd_id,transportPort=gk_id,departure=jd_bm)
                    assert bjd_bm2[0] == '操作成功'
                with allure.step("启用新增集装箱出口运输货主市场报价,报价单编码：{}".format(bjd_id)):
                    jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                    assert jd_bm == '操作成功'
            if bjd_bm1[1] != 0:
                with allure.step("存在集装箱出口运输司机市场报价,查看报价id"):
                    bjd_bm2 = ict.Test_Added01().test_Added0081(bjd_id=bjd_id, transportPort=gk_id, departure=jd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    if bjd_bm2[2] == "enabled_type_unenabled":
                        with allure.step("启用存在(未启用)集装箱出口运输司机市场报价"):
                            jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                            assert jd_bm == '操作成功'
                    if bjd_bm2[2] == "enabled_type_disabled":
                        with allure.step("启用存在(禁用)集装箱出口运输司机市场报价"):
                            jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                            assert jd_bm == '操作成功'
                    if bjd_bm2[2] == "enabled_type_enabled":
                        with allure.step("存在集装箱出口运输司机市场报价,并已启用报价"):
                            pass

    @allure.title("监理档案")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query021(self):
        log.info("监理档案")
        with allure.step("查看监理是否存在"):
            jl_da = ict.Test_Added01().test_Added0125(jl_name="毛敏监理01")
            assert jl_da[0] == '操作成功'
            if jl_da[2] == 0 :
                with allure.step("获取供应商ID"):
                    gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
                    assert gys_id[0] == '操作成功'
                with allure.step("新增监理档案"):
                    xz_jlda = ict.Test_Added01().test_Added0127(gys_id=gys_id[1])
                    assert xz_jlda == '操作成功'
                with allure.step("查看监理档案ID"):
                    jl_da = ict.Test_Added01().test_Added0125(jl_name="毛敏监理01")
                    assert jl_da[0] == '操作成功'
                    ji_id = jl_da[1][0]["id"]
                with allure.step("激活监理档案"):
                    jh_jlda = ict.Test_Added01().test_Added0126(jl_id=ji_id)
                    assert jh_jlda == '操作成功'
            if jl_da[2] != 0 :
                with allure.step("存在，获取监理档案"):
                    jl_zt = jl_da[1][0]["active"]
                    ji_id = jl_da[1][0]["id"]
                    if jl_zt == "active_unactivated" :
                        with allure.step("存在》未激活，激活监理档案"):
                            jh_jlda = ict.Test_Added01().test_Added0126(jl_id=ji_id)
                            assert jh_jlda == '操作成功'
                    if jl_zt == "active_invalid" :
                        with allure.step("存在》失效，激活监理档案"):
                            jh_jlda = ict.Test_Added01().test_Added0126(jl_id=ji_id)
                            assert jh_jlda == '操作成功'
                    if jl_zt == "active_activated" :
                        with allure.step("存在》并已经激活监理档案"):
                           pass

    @allure.title("区域规则-集装箱进口运输,操作区域蛇口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query022(self):
        log.info("区域规则-集装箱进口运输,操作区域蛇口")
        '''用例描述'''
        with allure.step("查看区域规则-集装箱进口运输,操作区域蛇口是否存在"):
            qy_gh = ict.Test_Added01().test_Added0031(taskUnitCode="port_container_import_transport",
                                                      centerName="shekou_group")
            assert qy_gh[0] == '操作成功'
            if qy_gh[1] == []:
                with allure.step("新增集装箱进口区域规划"):
                    xz_gh = ict.Test_Added01().test_Added0032(taskUnitCode="port_container_import_transport",
                                                              centerName="shekou_group", isContainer=1)
                    assert xz_gh == '操作成功'
                with allure.step("查看区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="port_container_import_transport",
                                                                centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                with allure.step("启用区域规划状态"):
                    qyqy_gh = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                    assert qyqy_gh == '启用成功'
            if qy_gh[1] != []:
                with allure.step("查看区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="port_container_import_transport",
                                                                centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                    if qygh_id[1] == "enabled_type_unenabled":
                        with allure.step("未启用查看区域规划id+状态"):
                            qy_qyzx = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                            assert qy_qyzx == '启用成功'
                    if qygh_id[1] == "enabled_type_disabled":
                        with allure.step("禁用查看区域规划id+状态"):
                            qy_qyzx = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                            assert qy_qyzx == '启用成功'
                    if qygh_id[1] == "enabled_type_enabled":
                        with allure.step("集装箱进口区域规划已存在，并已启用"):
                            pass

    @allure.title("接单中心-集装箱进口运输")
    # @pytest.mark.skip(reason="无理由跳")
    def test_query023(self):
        log.info("接单中心-集装箱进口运输")
        with allure.step("查看接单中心-集装箱进口运输，是否存在"):
            jd_zx = ict.Test_Added01().test_Added0035(taskUnitCode="port_container_import_transport")
            assert jd_zx[0] == '操作成功'
            if jd_zx[1] == 0:
                with allure.step("新增集装箱进口接单中心"):
                    zxjd_zx = ict.Test_Added01().test_Added0036(taskUnitCode="port_container_import_transport",
                                                                isContainer=1)
                    assert zxjd_zx == '操作成功'
                with allure.step("查看接单中心id"):
                    jdzx_id = ict.Test_Added01().test_Added0037(taskUnitCode="port_container_import_transport")
                    assert jdzx_id[0] == '操作成功'
                with allure.step("启用接单中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                    assert qy_jdzx == '启用成功'
            if jd_zx[1] != 0:
                with allure.step("查看接单中心id"):
                    jdzx_id = ict.Test_Added01().test_Added0037(taskUnitCode="port_container_import_transport")
                    assert jdzx_id[0] == '操作成功'
                    if jdzx_id[2] == "enabled_type_unenabled":
                        with allure.step("接单中心未启用，启用接单中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jdzx_id[2] == "enabled_type_disabled":
                        with allure.step("接单中心禁用，启用接单中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jdzx_id[2] == "enabled_type_enabled":
                        with allure.step("接单中已存在，并已启用"):
                            pass

    @allure.title("计划中心-集装箱进口运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query024(self):
        log.info("计划中心-集装箱进口运输")
        with allure.step("查看计划中心-集装箱进口运输，是否存在"):
            jh_zx = ict.Test_Added01().test_Added0039(taskUnitCode="port_container_import_transport")
            assert jh_zx[0] == '操作成功'
            if jh_zx[1] == 0:
                with allure.step("新增集装箱进口计划中心"):
                    zxjh_zx = ict.Test_Added01().test_Added0040(taskUnitCode="port_container_import_transport",
                                                                isContainer=1)
                    assert zxjh_zx == '操作成功'
                with allure.step("查看计划中心id"):
                    jhzx_id = ict.Test_Added01().test_Added0041(taskUnitCode="port_container_import_transport")
                    assert jhzx_id[0] == '操作成功'
                with allure.step("启用计划中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                    assert qy_jdzx == '启用成功'
            if jh_zx[1] != 0:
                with allure.step("查看计划中心id"):
                    jhzx_id = ict.Test_Added01().test_Added0041(taskUnitCode="port_container_import_transport")
                    assert jhzx_id[0] == '操作成功'
                    if jhzx_id[2] == "enabled_type_unenabled":
                        with allure.step("计划中心未启用，启用计划中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jhzx_id[2] == "enabled_type_disabled":
                        with allure.step("计划中心禁用，启用计划中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jhzx_id[2] == "enabled_type_enabled":
                        with allure.step("计划中已存在，并已启用"):
                            pass

    @allure.title("货主市场报价--集装箱进口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query025(self):
        log.info("货主市场报价--集装箱进口")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看货主同报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0047(hz_id=hz_id[1], contractType="cargo_owner_type")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0:
                with allure.step("新增货主合同报价单"):
                    xzbz_dd = ict.Test_Added01().test_Added0049(hz_id=hz_id[1], contractType="cargo_owner_type")
                    assert xzbz_dd[0] == '操作成功'
                with allure.step("查看新增货主同报价单id"):
                    bz_dd = ict.Test_Added01().test_Added0048(hz_id=hz_id[1], contractType="cargo_owner_type")
                    assert bz_dd[0] == '操作成功'
                with allure.step("启用新增货主报价单:{}".format(bz_dd[3])):
                    qybz_dd = ict.Test_Added01().test_Added0050(bjd_id=bz_dd[2])
                    assert qybz_dd == '操作成功'
                with allure.step("获取港口id"):
                    gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                    assert gk_id1[0] == '操作成功'
                    gk_id = gk_id1[1]  # 港口id
                    gk_name = gk_id1[2]  # 港口名称
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("获取收发地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    jd_bm = jd_bm1[1]
                    jd_name = jd_bm1[2]
                with allure.step("新增集装箱进口运输货主合同报价:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name, jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0158(customerPriceId=bz_dd[2],
                                                                taskUnitCode="port_container_import_transport",
                                                                taskUnitTypeName="集装箱进口运输", transportPort=gk_id,
                                                                departure=jd_bm, departureProvinces=sf_bm,
                                                                departureCity=cs_bm,
                                                                departureArea=q_bm)
                    assert xzsc_bj[0] == '操作成功'
                with allure.step("新增集装箱进口运输货主合同报价，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0053(bjd_id=bz_dd[2],transportPort=gk_id,departure=[],taskUnitCode="port_container_import_transport")
                    assert bjd_bm[0] == '操作成功'
                with allure.step("启用新增集装箱进口运输货主合同报价,报价单编码：{}".format(bjd_bm[3])):
                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm[1])
                    assert jd_bm == '操作成功'
            if bz_dd1[1] != 0:
                with allure.step("存在集装箱进口运输货主合同报价单，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0048(hz_id=hz_id[1], contractType="cargo_owner_type")
                    assert bjd_bm[0] == '操作成功'
                    if bjd_bm[1] == "status_type_unenabled":
                        with allure.step("启用已存在(未启用)的集装箱出口运输货主市场报价单,报价单id：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_disabled":
                        with allure.step("启用已存在(禁用)的集装箱出口运输货主市场报价,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_type_enabled":
                        with allure.step("已存在的集装箱出口运输货主市场报价，并已启用,报价单编码：{}".format(bjd_bm[3])):
                            pass
                    with allure.step("获取港口id"):
                        gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                        assert gk_id1[0] == '操作成功'
                        gk_id = gk_id1[1]  # 港口id
                        gk_name = gk_id1[2]  # 港口名称
                    with allure.step("获取收发地街道编码"):
                        jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                        assert jd_bm1[0] == '操作成功'
                        jd_bm = jd_bm1[1]
                        jd_name = jd_bm1[2]
                    with allure.step("存在货主合同报价，查看是否存在区域报价报价单信息"):
                        bjd_bm1 = ict.Test_Added01().test_Added0051(bjd_id=bjd_bm[2], transportPort=gk_id,
                                                                    departure=[],
                                                                    taskUnitCode="port_container_import_transport")
                        assert bjd_bm1[0] == '操作成功'
                        if bjd_bm1[1] == []:
                            with allure.step("获取港口id"):
                                gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                                assert gk_id1[0] == '操作成功'
                                gk_id = gk_id1[1]  # 港口id
                                gk_name = gk_id1[2]  # 港口名称
                            with allure.step("获取收发地省编码"):
                                sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                                assert sf_bm1[0] == '操作成功'
                                sf_bm = sf_bm1[1]
                                sf_name = sf_bm1[2]
                            with allure.step("获取收发地市编码"):
                                cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                                assert cs_bm1[0] == '操作成功'
                                cs_bm = cs_bm1[1]
                                cs_name = cs_bm1[2]
                            with allure.step("获取收发地区编码"):
                                q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                                assert q_bm1[0] == '操作成功'
                                q_bm = q_bm1[1]
                                q_name = q_bm1[2]
                            with allure.step("获取收发地街道编码"):
                                jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                                assert jd_bm1[0] == '操作成功'
                                jd_bm = jd_bm1[1]
                                jd_name = jd_bm1[2]
                            with allure.step(
                                    "新增货主合同集装箱进口运输报价:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name,
                                                                            jd_name)):
                                xzsc_bj = ict.Test_Added01().test_Added0158(customerPriceId=bjd_bm[2],
                                                                            taskUnitCode="port_container_import_transport",
                                                                            taskUnitTypeName="集装箱进口运输",
                                                                            transportPort=gk_id, departure=jd_bm,
                                                                            departureProvinces=sf_bm,
                                                                            departureCity=cs_bm, departureArea=q_bm,
                                                                            )
                                assert xzsc_bj == '操作成功'
                            with allure.step("查看新增集装箱进口运输货主市场报价,查看报价id"):
                                bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_bm[2], transportPort=gk_id,
                                                                            departure=[],taskUnitCode="port_container_import_transport")
                                assert bjd_bm2[0] == '操作成功'
                            with allure.step("启用新增集装箱进口运输货主市场报价,报价单编码：{}".format(bjd_bm[3])):
                                jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                assert jd_bm == '操作成功'
                        if bjd_bm1[1] != []:
                            with allure.step("存在集装箱进口运输货主合同报价,查看报价id"):
                                bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_bm[2], transportPort=gk_id,
                                                                            departure=[],taskUnitCode="port_container_import_transport")
                                assert bjd_bm2[0] == '操作成功'
                                if bjd_bm2[2] == "enabled_type_unenabled":
                                    with allure.step("启用存在(未启用)集装箱进口运输货主合同报价"):
                                        jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                        assert jd_bm == '操作成功'
                                if bjd_bm2[2] == "enabled_type_disabled":
                                    with allure.step("启用存在(禁用)集装箱进口运输货主合同报价"):
                                        jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                        assert jd_bm == '操作成功'
                                if bjd_bm2[2] == "enabled_type_enabled":
                                    with allure.step("存在集装箱进口运输货主合同报价,并已启用报价"):
                                        pass

    @allure.title("自有司机报价--集装箱进口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query026(self):
        log.info("自有司机报价--集装箱进口")
        with allure.step("查看自有车报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0076(fw_lx="port_container_import_transport")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0 :
                with allure.step("新增自有车报价单"):
                    xzbz_dd = ict.Test_Added01().test_Added0078(fw_lx="port_container_import_transport",fw_name="集装箱进口运输")
                    assert xzbz_dd[0] == '操作成功'
                with allure.step("查看新增自有车报价单id"):
                    bz_dd = ict.Test_Added01().test_Added0079(fw_lx="port_container_import_transport")
                    assert bz_dd[0] == '操作成功'
                with allure.step("启用新增自有车报价单:{}".format(bz_dd[2])):
                    qybz_dd = ict.Test_Added01().test_Added0080(bjd_id=bz_dd[1])
                    assert qybz_dd == '操作成功'
            if bz_dd1[1] != 0 :
                with allure.step("存在报价单，查看自有车报价单信息"):
                    bz_dd = ict.Test_Added01().test_Added0079(fw_lx="port_container_import_transport")
                    assert bz_dd[0] == '操作成功'
                    if  bz_dd[3] == "status_type_unenabled" :
                        with allure.step("启用存在未启用自有车报价单:{}".format(bz_dd[2])):
                            qybz_dd = ict.Test_Added01().test_Added0080(bjd_id=bz_dd[1])
                            assert qybz_dd == '操作成功'
                    if  bz_dd[3] == "status_disabled" :
                        with allure.step("启用存在禁用自有车报价单:{}".format(bz_dd[2])):
                            qybz_dd = ict.Test_Added01().test_Added0080(bjd_id=bz_dd[1])
                            assert qybz_dd == '操作成功'
                    if  bz_dd[3] == "status_type_enabled" :
                        with allure.step("自有车报价单已存在并已启用:{}".format(bz_dd[2])):
                            pass
        with allure.step("获取港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]  # 港口id
            gk_name = gk_id1[2]  # 港口名称
        with allure.step("获取收发地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6,name="洞井街道")
            assert jd_bm1[0] == '操作成功'
            jd_bm = jd_bm1[1]
            jd_name = jd_bm1[2]
        with allure.step("存在报价单，查看自有车报价单信息"):
            bz_dd = ict.Test_Added01().test_Added0079(fw_lx="port_container_import_transport")
            assert bz_dd[0] == '操作成功'
        with allure.step("存在自有车集装箱进口报价单，查看是否存在区域报价报价信息"):
            bjd_bm1 = ict.Test_Added01().test_Added0167(bjd_id=bz_dd[1],transportPort=gk_id,departure=jd_bm)
            assert bjd_bm1[0] == '操作成功'
            if  bjd_bm1[1] == 0 :
                with allure.step("获取港口id"):
                    gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                    assert gk_id1[0] == '操作成功'
                    gk_id = gk_id1[1]  # 港口id
                    gk_name = gk_id1[2]  # 港口名称
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("获取收发地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6,name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    jd_bm = jd_bm1[1]
                    jd_name = jd_bm1[2]
                with allure.step("新增自有车报价:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name, jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0166(marketPriceId=bz_dd[1], transportPort=gk_id,
                                                                departure=jd_bm,
                                                                departureProvinces=sf_bm, departureCity=cs_bm,
                                                                departureArea=q_bm,
                                                                taskUnitCode="port_container_import_transport")
                    assert xzsc_bj == '操作成功'
                with allure.step("新增自有车集装箱进口运输自有车报价，查看报价信息"):
                    bjd_bm2 = ict.Test_Added01().test_Added0167(bjd_id=bz_dd[1],transportPort=gk_id,departure=jd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    bz_id =  bjd_bm2[2][0]["id"]
                    with allure.step("启用新增集装箱进口运输自有车报价，报价单id：{}".format(bjd_bm2[1])):
                        jd_bm = ict.Test_Added01().test_Added0011(bz_id=bz_id)
                        assert jd_bm == '操作成功'


            if bjd_bm1[1] != 0:
                with allure.step("存在集装箱进口运输自有车报价,查看报价id"):
                    bjd_bm2 = ict.Test_Added01().test_Added0167(bjd_id=bz_dd[1],transportPort=gk_id,departure=jd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    bz_zt =  bjd_bm2[2][0]["enabledType"]
                    if  bz_zt == "enabled_type_unenabled":
                        with allure.step("启用存在(未启用)集装箱进口运输自有车报价，报价单id：{}".format(bjd_bm2[1])):
                            jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                            assert jd_bm == '操作成功'
                    if  bz_zt == "enabled_type_disabled":
                        with allure.step("启用存在(禁用)集装箱进口运输自有车报价"):
                            jd_bm = ict.Test_Added01().test_Added0011(bz_id=bjd_bm2[1])
                            assert jd_bm == '操作成功'
                    if bz_zt == "enabled_type_enabled":
                        with allure.step("存在集装箱进口运输自有车报价,并已启用报价"):
                            pass

    @allure.title("司机市场报价--厢式车进口运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query027(self):
        log.info("司机市场报价--厢式车进口运输")
        with allure.step("查看厢式车进口司机市场报价是否存在"):
            sj_bjd = ict.Test_Added01().test_Added0115(fy_lx="port_container_import_transport")
            assert sj_bjd[0] == '操作成功'
            if  sj_bjd[1] == 0 :
                with allure.step("新增司机市场报价报价单"):
                    xz_bjd = ict.Test_Added01().test_Added0116(fy_lx="port_container_import_transport",fy_name="集装箱进口运输")
                    assert xz_bjd == '操作成功'
                with allure.step("查看司机市场报价报价单id"):
                    ck_bjd = ict.Test_Added01().test_Added0115(fy_lx="port_container_import_transport")
                    assert ck_bjd[0] == '操作成功'
                    bjd_id = ck_bjd[2][0]["id"]
                with allure.step("启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                    qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                    assert qy_bjd == '操作成功'
            if  sj_bjd[1] != 0 :
                bjd_id = sj_bjd[2][0]["id"]
                bjd_zt = sj_bjd[2][0]["statusType"]
                if bjd_zt == "status_type_unenabled" :
                    with allure.step("报价单未启用，启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                        qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                        assert qy_bjd == '操作成功'
                if bjd_zt == "status_disabled" :
                    with allure.step("报价单已禁用，启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                        qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                        assert qy_bjd == '操作成功'
                if bjd_zt == "status_type_enabled" :
                    with allure.step("司机市场报价报价单已存在并已启用，报价单id{}".format(bjd_id)):
                        pass
        with allure.step("查看厢式车进口司机市场报价id"):
            sj_bjd = ict.Test_Added01().test_Added0115(fy_lx="port_container_import_transport")
            assert sj_bjd[0] == '操作成功'
            bjd_id = sj_bjd[2][0]["id"]
        with allure.step("获取港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]  # 港口id
            gk_name = gk_id1[2]  # 港口名称
        with allure.step("获取卸货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
            assert jd_bm1[0] == '操作成功'
            zjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]
        with allure.step("存在厢式车进口司机市场报价单，查看是否存在区域报价报价信息"):
            bjd_bm1 = ict.Test_Added01().test_Added0167(bjd_id=bjd_id,transportPort=gk_id,departure=zjd_bm)
            assert bjd_bm1[0] == '操作成功'
            if  bjd_bm1[1] == 0 :
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("新增厢式车进口司机市场报价:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name,xjd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0166(marketPriceId=bjd_id, transportPort=gk_id,
                                                                departure=zjd_bm,
                                                                departureProvinces=sf_bm, departureCity=cs_bm,
                                                                departureArea=q_bm,
                                                                taskUnitCode="port_container_import_transport")
                    assert xzsc_bj == '操作成功'
                with allure.step("新增厢式车进口司机市场报价，查看报价信息"):
                    bjd_bm2 = ict.Test_Added01().test_Added0167(bjd_id=bjd_id,transportPort=gk_id,departure=zjd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    bz_id =  bjd_bm2[2][0]["id"]
                    with allure.step("启用新增厢式车进口司机市场报价，报价单id：{}".format(bjd_bm2[1])):
                        jd_bm = ict.Test_Added01().test_Added0011(bz_id=bz_id)
                        assert jd_bm == '操作成功'

            if bjd_bm1[1] != 0:
                with allure.step("存在厢式车进口司机市场报价,查看报价id"):
                    bjd_bm2 = ict.Test_Added01().test_Added0167(bjd_id=bjd_id,transportPort=gk_id,departure=zjd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    bz_zt =  bjd_bm2[2][0]["enabledType"]
                    bz_id =  bjd_bm2[2][0]["id"]
                    if  bz_zt == "enabled_type_unenabled":
                        with allure.step("启用存在(未启用)厢式车进口司机市场报价，报价单id：{}".format(bz_id)):
                            jd_bm = ict.Test_Added01().test_Added0011(bz_id=bz_id)
                            assert jd_bm == '操作成功'
                    if  bz_zt == "enabled_type_disabled":
                        with allure.step("启用存在(禁用)厢式车进口司机市场报价"):
                            jd_bm = ict.Test_Added01().test_Added0011(bz_id=bz_id)
                            assert jd_bm == '操作成功'
                    if bz_zt == "enabled_type_enabled":
                        with allure.step("存在厢式车进口司机市场报价,并已启用报价"):
                            pass

    @allure.title("司机市场报价--厢式车内陆运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query028(self):
        log.info("司机市场报价--厢式车内陆运输")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看厢式车司机市场报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0115(fy_lx="bulkcargo_transport")
            assert bz_dd1[0] == '操作成功'
            if  bz_dd1[1] == 0 :
                with allure.step("新增司机市场报价报价单"):
                    xz_bjd = ict.Test_Added01().test_Added0116(fy_lx="bulkcargo_transport",fy_name="厢式车运输")
                    assert xz_bjd == '操作成功'
                with allure.step("查看司机市场报价报价单id"):
                    ck_bjd = ict.Test_Added01().test_Added0115(fy_lx="bulkcargo_transport")
                    assert ck_bjd[0] == '操作成功'
                    bjd_id = ck_bjd[2][0]["id"]
                with allure.step("启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                    qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                    assert qy_bjd == '操作成功'
            if  bz_dd1[1] != 0 :
                bjd_id = bz_dd1[2][0]["id"]
                bjd_zt = bz_dd1[2][0]["statusType"]
                if bjd_zt == "status_type_unenabled" :
                    with allure.step("报价单未启用，启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                        qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                        assert qy_bjd == '操作成功'
                if bjd_zt == "status_disabled" :
                    with allure.step("报价单已禁用，启用司机市场报价报价单，报价单id{}".format(bjd_id)):
                        qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                        assert qy_bjd == '操作成功'
                if bjd_zt == "status_type_enabled" :
                    with allure.step("司机市场报价报价单已存在并已启用，报价单id{}".format(bjd_id)):
                        pass
        with allure.step("查看厢式车司机市场报价单ID"):
            bz_dd1 = ict.Test_Added01().test_Added0115(fy_lx="bulkcargo_transport")
            assert bz_dd1[0] == '操作成功'
            bjd_id = bz_dd1[2][0]["id"]
        with allure.step("获取装货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
            assert jd_bm1[0] == '操作成功'
            zjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]
        with allure.step("查看是否存在厢式车司机市场报价"):
            bjd_bm3 = ict.Test_Added01().test_Added0169(bjd_id=bjd_id,departure=zjd_bm)
            assert bjd_bm3[0] == '操作成功'
            if bjd_bm3[1] == 0 :
                with allure.step("获取卸货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    xsf_bm = sf_bm1[1]
                    xsf_name = sf_bm1[2]
                with allure.step("获取卸货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    xcs_bm = cs_bm1[1]
                    xcs_name = cs_bm1[2]
                with allure.step("获取卸货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    xq_bm = q_bm1[1]
                    xq_name = q_bm1[2]
                with allure.step("获取卸货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    xjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]
                with allure.step("获取装货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
                    assert sf_bm1[0] == '操作成功'
                    zsf_bm = sf_bm1[1]
                    zsf_name = sf_bm1[2]
                with allure.step("获取装货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
                    assert cs_bm1[0] == '操作成功'
                    zcs_bm = cs_bm1[1]
                    zcs_name = cs_bm1[2]
                with allure.step("获取装货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
                    assert q_bm1[0] == '操作成功'
                    zq_bm = q_bm1[1]
                    zq_name = q_bm1[2]
                with allure.step("获取装货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
                    assert jd_bm1[0] == '操作成功'
                    zjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]
                with allure.step("新增厢式车司机市场报价"):
                    xzsc_bj = ict.Test_Added01().test_Added0170(bjd_id=bjd_id,zh_jd=zjd_bm, zh_s=zsf_bm,zh_cs=zcs_bm, zh_q=zq_bm,
                                                                xh_jd=xjd_bm,xh_s=xsf_bm,xh_cs=xcs_bm,xh_q=xq_bm,fu_lx="bulkcargo_transport")
                    assert xzsc_bj == '操作成功'
                with allure.step("新增厢式车司机市场报价，查看报价信息"):
                    bjd_bm2 = ict.Test_Added01().test_Added0169(bjd_id=bjd_id,departure=zjd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    bz_id = bjd_bm2[2][0]["id"]
                    with allure.step("启用新增厢式车进口司机市场报价，报价单id：{}".format(bjd_bm2[1])):
                        jd_bm = ict.Test_Added01().test_Added0011(bz_id=bz_id)
                        assert jd_bm == '操作成功'
            if bjd_bm3[1] != 0:
                    with allure.step("存在厢式车司机市场报价，查看报价单信息"):
                        bjd_bm2 = ict.Test_Added01().test_Added0169(bjd_id=bjd_id, departure=zjd_bm)
                        assert bjd_bm2[0] == '操作成功'
                        bj_id = bjd_bm2[2][0]["id"]
                        bjd_zt = bjd_bm2[2][0]["enabledType"]
                        if bjd_zt == "enabled_type_unenabled":
                            with allure.step("启用存在(未启用)厢式车司机市场报价"):
                                jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                                assert jd_bm == '操作成功'
                        if bjd_zt == "enabled_type_disabled":
                            with allure.step("启用存在(禁用)厢式车司机市场报价"):
                                jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                                assert jd_bm == '操作成功'
                        if bjd_zt == "enabled_type_enabled":
                            with allure.step("存在厢式车司机市场报价,并已启用报价"):
                                pass

    @allure.title("自有司机报价--厢式车内陆运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query029(self):
        log.info("自有司机报价--厢式车内陆运输")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看厢式车自有司机报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0076(fw_lx="bulkcargo_transport")
            assert bz_dd1[0] == '操作成功'
            if  bz_dd1[1] == 0 :
                with allure.step("新增厢式车自有司机报价单"):
                    xz_bjd = ict.Test_Added01().test_Added0078(fw_lx="bulkcargo_transport",fw_name="厢式车运输")
                    assert xz_bjd[0] == '操作成功'
                with allure.step("查看厢式车自有司机报价单id"):
                    ck_bjd = ict.Test_Added01().test_Added0079(fw_lx="bulkcargo_transport")
                    assert ck_bjd[0] == '操作成功'
                    bjd_id = ck_bjd[1]
                with allure.step("启用厢式车自有司机报价单，报价单id{}".format(bjd_id)):
                    qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                    assert qy_bjd == '操作成功'
            if  bz_dd1[1] != 0 :
                with allure.step("查看厢式车自有司机报价单id"):
                    ck_bjd = ict.Test_Added01().test_Added0079(fw_lx="bulkcargo_transport")
                    assert ck_bjd[0] == '操作成功'
                    bjd_id = ck_bjd[1]
                    bjd_zt = ck_bjd[3]
                    if bjd_zt == "status_type_unenabled" :
                        with allure.step("厢式车自有司机报价单未启用，启用报价单id{}".format(bjd_id)):
                            qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                            assert qy_bjd == '操作成功'
                    if bjd_zt == "status_disabled" :
                        with allure.step("厢式车自有司机报价单已禁用，启用报价单，报价单id{}".format(bjd_id)):
                            qy_bjd = ict.Test_Added01().test_Added0005(bjd_id=bjd_id)
                            assert qy_bjd == '操作成功'
                    if bjd_zt == "status_type_enabled" :
                        with allure.step("厢式车自有司机报价单已存在并已启用，报价单id{}".format(bjd_id)):
                            pass
        with allure.step("查看厢式车自有司机报价单id"):
            ck_bjd = ict.Test_Added01().test_Added0079(fw_lx="bulkcargo_transport")
            assert ck_bjd[0] == '操作成功'
            bjd_id = ck_bjd[1]
        with allure.step("获取装货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
            assert jd_bm1[0] == '操作成功'
            zjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]
        with allure.step("查看是否存在自有司机厢式车报价"):
            bjd_bm3 = ict.Test_Added01().test_Added0169(bjd_id=bjd_id,departure=zjd_bm)
            assert bjd_bm3[0] == '操作成功'
            if bjd_bm3[1] == 0 :
                with allure.step("获取卸货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    xsf_bm = sf_bm1[1]
                    xsf_name = sf_bm1[2]
                with allure.step("获取卸货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    xcs_bm = cs_bm1[1]
                    xcs_name = cs_bm1[2]
                with allure.step("获取卸货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    xq_bm = q_bm1[1]
                    xq_name = q_bm1[2]
                with allure.step("获取卸货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    xjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]
                with allure.step("获取装货地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
                    assert sf_bm1[0] == '操作成功'
                    zsf_bm = sf_bm1[1]
                    zsf_name = sf_bm1[2]
                with allure.step("获取装货地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
                    assert cs_bm1[0] == '操作成功'
                    zcs_bm = cs_bm1[1]
                    zcs_name = cs_bm1[2]
                with allure.step("获取装货地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
                    assert q_bm1[0] == '操作成功'
                    zq_bm = q_bm1[1]
                    zq_name = q_bm1[2]
                with allure.step("获取装货地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
                    assert jd_bm1[0] == '操作成功'
                    zjd_bm = jd_bm1[1]
                    xjd_name = jd_bm1[2]
                with allure.step("新增自有司机厢式车报价"):
                    xzsc_bj = ict.Test_Added01().test_Added0170(bjd_id=bjd_id,zh_jd=zjd_bm, zh_s=zsf_bm,zh_cs=zcs_bm, zh_q=zq_bm,
                                                                xh_jd=xjd_bm,xh_s=xsf_bm,xh_cs=xcs_bm,xh_q=xq_bm,fu_lx="bulkcargo_transport")
                    assert xzsc_bj == '操作成功'
                with allure.step("新增自有司机厢式车，查看报价信息"):
                    bjd_bm2 = ict.Test_Added01().test_Added0169(bjd_id=bjd_id,departure=zjd_bm)
                    assert bjd_bm2[0] == '操作成功'
                    bz_id = bjd_bm2[2][0]["id"]
                    with allure.step("启用自有司机厢式车报价单，报价单id：{}".format(bjd_bm2[1])):
                        jd_bm = ict.Test_Added01().test_Added0011(bz_id=bz_id)
                        assert jd_bm == '操作成功'
            if bjd_bm3[1] != 0:
                    with allure.step("存在自有司机厢式车报价，查看报价单信息"):
                        bjd_bm2 = ict.Test_Added01().test_Added0169(bjd_id=bjd_id,departure=zjd_bm)
                        assert bjd_bm2[0] == '操作成功'
                        bj_id = bjd_bm2[2][0]["id"]
                        bjd_zt = bjd_bm2[2][0]["enabledType"]
                        if bjd_zt == "enabled_type_unenabled":
                            with allure.step("启用存在(未启用)自有司机厢式车报价"):
                                jd_bm = ict.Test_Added01().test_Added0011(bz_id=bj_id)
                                assert jd_bm == '操作成功'
                        if bjd_zt == "enabled_type_disabled":
                            with allure.step("启用存在(禁用)自有司机厢式车报价"):
                                jd_bm = ict.Test_Added01().test_Added0011(bz_id=bj_id)
                                assert jd_bm == '操作成功'
                        if bjd_zt == "enabled_type_enabled":
                            with allure.step("存在自有司机厢式车报价,并已启用报价"):
                                pass

    @allure.title("客户文件配置--厢式车")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query029(self):
        log.info("客户文件配置--厢式车")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看厢式车客户文件配置是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0177(hz_id=hz_id[1],fw_lx="van_type")
            assert bz_dd1[0] == '操作成功'
            if  bz_dd1[1] == 0 :
                with allure.step("不存在客户文件配置--厢式车》新增"):
                    xz_pz = ict.Test_Added01().test_Added0176(hz_id=hz_id[1])
                    assert xz_pz == '操作成功'
                with allure.step("查看厢式车客户文件配置id"):
                    da_id = ict.Test_Added01().test_Added0177(hz_id=hz_id[1])
                    assert da_id[0] == '操作成功'
                with allure.step("启用厢式车客户文件配置"):
                    qy_da = ict.Test_Added01().test_Added0178(da_id=da_id[2][0]["id"])
                    assert qy_da == '操作成功'

            if bz_dd1[1] != 0:
                dd_zt =  bz_dd1[2][0]["statusType"]
                dd_id = bz_dd1[2][0]["id"]
                if dd_zt == "enabled_type_unenabled":
                    with allure.step("启用存在(未启用)厢式车客户文件配置"):
                        jd_bm = ict.Test_Added01().test_Added0178(da_id=dd_id)
                        assert jd_bm == '操作成功'
                if dd_zt == "enabled_type_disabled":
                    with allure.step("启用存在(禁用)厢式车客户文件配置"):
                        jd_bm = ict.Test_Added01().test_Added0178(da_id=dd_id)
                        assert jd_bm == '操作成功'
                if dd_zt == "enabled_type_enabled":
                    with allure.step("存在厢式车客户文件配置,并已启用"):
                        pass

    @allure.title("接单中心-危险品运输出口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query030(self):
        log.info("接单中心-危险品运输出口")
        with allure.step("查看接单中心-危险品运输出口，是否存在"):
            jd_zx = ict.Test_Added01().test_Added0035(taskUnitCode="dangerous_cargo_export_transport")
            assert jd_zx[0] =='操作成功'
            if jd_zx[1] == 0 :
                with allure.step("新增危险品运输出口接单中心"):
                    zxjd_zx = ict.Test_Added01().test_Added0036(taskUnitCode="dangerous_cargo_export_transport",isContainer=1)
                    assert zxjd_zx == '操作成功'
                with allure.step("查看危险品运输出口接单中心id"):
                    jdzx_id = ict.Test_Added01().test_Added0037(taskUnitCode="dangerous_cargo_export_transport")
                    assert jdzx_id[0] == '操作成功'
                with allure.step("启用危险品运输出口接单中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                    assert qy_jdzx == '启用成功'
            if jd_zx[1] != 0 :
                with allure.step("查看危险品运输出口接单中心id"):
                    jdzx_id = ict.Test_Added01().test_Added0037(taskUnitCode="dangerous_cargo_export_transport")
                    assert jdzx_id[0] == '操作成功'
                    if jdzx_id[2] == "enabled_type_unenabled":
                        with allure.step("危险品运输出口接单中心未启用，启用接单中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jdzx_id[2] == "enabled_type_disabled":
                        with allure.step("危险品运输出口接单中心禁用，启用接单中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0038(jdzx_id=jdzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jdzx_id[2] == "enabled_type_enabled":
                        with allure.step("危险品运输出口接单中已存在，并已启用"):
                            pass

    @allure.title("区域规则-危险品出口运输,操作区域蛇口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query031(self):
        log.info("区域规则-危险品出口运输,操作区域蛇口")
        '''用例描述'''
        with allure.step("查看区域规则-危险品出口运输,操作区域蛇口是否存在"):
            qy_gh = ict.Test_Added01().test_Added0031(taskUnitCode="dangerous_cargo_export_transport",centerName="shekou_group")
            assert qy_gh[0] =='操作成功'
            if qy_gh[1] == [] :
                with allure.step("新增危险品出口运输区域规划"):
                    xz_gh = ict.Test_Added01().test_Added0032(taskUnitCode="dangerous_cargo_export_transport",centerName="shekou_group",isContainer=1)
                    assert xz_gh == '操作成功'
                with allure.step("查看危险品出口运输区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="dangerous_cargo_export_transport",centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                with allure.step("启用危险品出口运输区域规划状态"):
                    qyqy_gh = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                    assert qyqy_gh == '启用成功'
            if qy_gh[1] != [] :
                with allure.step("查看危险品出口运输区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="dangerous_cargo_export_transport",centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                    if qygh_id[1] == "enabled_type_unenabled":
                        with allure.step("未启用查，启用危险品出口运输"):
                            qy_qyzx = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                            assert qy_qyzx == '启用成功'
                    if qygh_id[1] == "enabled_type_disabled":
                        with allure.step("禁用，启用危险品出口运输"):
                            qy_qyzx = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                            assert qy_qyzx == '启用成功'
                    if qygh_id[1] == "enabled_type_enabled":
                        with allure.step("危险品出口运输区域规划已存在，并已启用"):
                            pass

    @allure.title("计划中心-危险品出口运输")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query032(self):
        log.info("计划中心-危险品出口运输")
        with allure.step("查看计划中心-危险品出口运输，是否存在"):
            jh_zx = ict.Test_Added01().test_Added0039(taskUnitCode="dangerous_cargo_export_transport")
            assert jh_zx[0] == '操作成功'
            if jh_zx[1] == 0:
                with allure.step("新增危险品出口运输计划中心"):
                    zxjh_zx = ict.Test_Added01().test_Added0040(taskUnitCode="dangerous_cargo_export_transport",isContainer=1)
                    assert zxjh_zx == '操作成功'
                with allure.step("查看危险品出口运输计划中心id"):
                    jhzx_id = ict.Test_Added01().test_Added0041(taskUnitCode="dangerous_cargo_export_transport")
                    assert jhzx_id[0] == '操作成功'
                with allure.step("启用危险品出口运输计划中心"):
                    qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                    assert qy_jdzx == '启用成功'
            if jh_zx[1] != 0:
                with allure.step("查看危险品出口运输计划中心id"):
                    jhzx_id = ict.Test_Added01().test_Added0041(taskUnitCode="dangerous_cargo_export_transport")
                    assert jhzx_id[0] == '操作成功'
                    if jhzx_id[2] == "enabled_type_unenabled":
                        with allure.step("危险品出口运输计划中心未启用，启用计划中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jhzx_id[2] == "enabled_type_disabled":
                        with allure.step("危险品出口运输计划中心禁用，启用计划中心"):
                            qy_jdzx = ict.Test_Added01().test_Added0042(jdzx_id=jhzx_id[1])
                            assert qy_jdzx == '启用成功'
                    if jhzx_id[2] == "enabled_type_enabled":
                        with allure.step("危险品出口运输计划中已存在，并已启用"):
                            pass

    @allure.title("货主合同报价--危险品出口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query033(self):
        log.info("货主合同报价--危险品出口")
        with allure.step("查看货主id"):
            hz_id = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id[0] == '操作成功'
        with allure.step("查看货主同报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0047(hz_id=hz_id[1],contractType="cargo_owner_type")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0 :
                with allure.step("新增货主合同报价单"):
                    xzbz_dd = ict.Test_Added01().test_Added0049(hz_id=hz_id[1],contractType="cargo_owner_type")
                    assert xzbz_dd[0] == '操作成功'
                with allure.step("查看新增货主同报价单id"):
                    bz_dd = ict.Test_Added01().test_Added0048(hz_id=hz_id[1],contractType= "cargo_owner_type")
                    assert bz_dd[0] == '操作成功'
                with allure.step("启用新增货主报价单:{}".format(bz_dd[3])):
                    qybz_dd = ict.Test_Added01().test_Added0050(bjd_id=bz_dd[2])
                    assert qybz_dd == '操作成功'
                with allure.step("获取港口id"):
                    gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                    assert gk_id1[0] == '操作成功'
                    gk_id = gk_id1[1]  # 港口id
                    gk_name = gk_id1[2]  # 港口名称
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("获取收发地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    jd_bm = jd_bm1[1]
                    jd_name = jd_bm1[2]
                with allure.step("新增危险品出口货主合同报价:港口：{},{}{}{}{}".format(gk_name,sf_name,cs_name,q_name,jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0052(customerPriceId=bz_dd[2],taskUnitCode="dangerous_cargo_export_transport",
                    taskUnitTypeName="危险品出口运输",transportPort=gk_id,departure=jd_bm,departureProvinces=sf_bm,departureCity=cs_bm,
                    departureArea=q_bm)
                    assert xzsc_bj == '操作成功'
                with allure.step("新增危险品出口运输货主合同报价，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0053(bjd_id=bz_dd[2],transportPort=gk_id,departure=[jd_bm],taskUnitCode="dangerous_cargo_export_transport")
                    assert bjd_bm[0] == '操作成功'
                with allure.step("启用危险品出口运输运输货主合同报价,报价单编码：{}".format(bjd_bm[3])):
                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm[1])
                    assert jd_bm == '操作成功'
            if bz_dd1[1] != 0:
                with allure.step("存在集装箱出口运输货主合同报价单，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0048(hz_id=hz_id[1],contractType= "cargo_owner_type")
                    assert bjd_bm[0] == '操作成功'
                    if bjd_bm[1] == "status_type_unenabled":
                        with allure.step("启用已存在(未启用)的危险品出口运输运输货主市场报价单,报价单id：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm== '操作成功'
                    if bjd_bm[1] == "status_disabled":
                        with allure.step("启用已存在(禁用)危险品出口运输集装箱出口运输货主市场报价,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_type_enabled":
                        with allure.step("已存在的危险品出口运输运输货主市场报价，并已启用,报价单编码：{}".format(bjd_bm[3])):
                            pass
                    with allure.step("获取港口id"):
                        gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                        assert gk_id1[0] == '操作成功'
                        gk_id = gk_id1[1]  # 港口id
                        gk_name = gk_id1[2]  # 港口名称
                    with allure.step("获取收发地街道编码"):
                        jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                        assert jd_bm1[0] == '操作成功'
                        jd_bm = jd_bm1[1]
                        jd_name = jd_bm1[2]
                    with allure.step("存在货主合同报价，查看是否存在危险品出口运输区域报价报价单信息"):
                        bjd_bm1 = ict.Test_Added01().test_Added0051(bjd_id=bjd_bm[2],transportPort=gk_id,departure=[jd_bm],taskUnitCode="dangerous_cargo_export_transport")
                        assert bjd_bm1[0] == '操作成功'
                        if  bjd_bm1[1] == [] :
                            with allure.step("获取港口id"):
                                gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                                assert gk_id1[0] == '操作成功'
                                gk_id = gk_id1[1]  # 港口id
                                gk_name = gk_id1[2]  # 港口名称
                            with allure.step("获取收发地省编码"):
                                sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                                assert sf_bm1[0] == '操作成功'
                                sf_bm = sf_bm1[1]
                                sf_name = sf_bm1[2]
                            with allure.step("获取收发地市编码"):
                                cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                                assert cs_bm1[0] == '操作成功'
                                cs_bm = cs_bm1[1]
                                cs_name = cs_bm1[2]
                            with allure.step("获取收发地区编码"):
                                q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                                assert q_bm1[0] == '操作成功'
                                q_bm = q_bm1[1]
                                q_name = q_bm1[2]
                            with allure.step("获取收发地街道编码"):
                                jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                                assert jd_bm1[0] == '操作成功'
                                jd_bm = jd_bm1[1]
                                jd_name = jd_bm1[2]
                            with allure.step(
                                    "新增货主合同危险品出口运输报价:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name, jd_name)):
                                xzsc_bj = ict.Test_Added01().test_Added0052(customerPriceId=bjd_bm[2],taskUnitCode="dangerous_cargo_export_transport",
                                                                            taskUnitTypeName="集装箱出口运输",
                                                                            transportPort=gk_id, departure=jd_bm,
                                                                            departureProvinces=sf_bm,
                                                                            departureCity=cs_bm, departureArea=q_bm,
                                                                            )
                                assert xzsc_bj == '操作成功'
                            with allure.step("查看新增危险品出口运输货主市场报价,查看报价id"):
                                bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_bm[2], transportPort=gk_id,departure=[jd_bm],taskUnitCode="dangerous_cargo_export_transport")
                                assert bjd_bm2[0] == '操作成功'
                            with allure.step("启用新增危险品出口运输货主市场报价,报价单编码：{}".format(bjd_bm[3])):
                                jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                assert jd_bm == '操作成功'
                        if bjd_bm1[1] != []:
                            with allure.step("存在危险品出口运输货主合同报价,查看报价id"):
                                bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_bm[2],transportPort=gk_id,departure=[jd_bm],taskUnitCode="dangerous_cargo_export_transport")
                                assert bjd_bm2[0] == '操作成功'
                                if  bjd_bm2[2] == "enabled_type_unenabled":
                                    with allure.step("启用存在(未启用)危险品出口运输货主合同报价"):
                                        jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                        assert jd_bm == '操作成功'
                                if  bjd_bm2[2] == "enabled_type_disabled":
                                    with allure.step("启用存在(禁用)危险品出口运输货主合同报价"):
                                        jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                        assert jd_bm == '操作成功'
                                if bjd_bm2[2] == "enabled_type_enabled":
                                    with allure.step("存在危险品出口运输货主合同报价,并已启用报价"):
                                        pass

    @allure.title("运输公司合同报价--危险品出口")
    # @pytest.mark.skip(reason="无理由跳过")
    def test_query034(self):
        log.info("运输公司合同报价--危险品出口")
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看运输公司合同报价是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0047(hz_id=gys_id[1],contractType="transportation_company_type")
            assert bz_dd1[0] == '操作成功'
            if bz_dd1[1] == 0:
                with allure.step("新增运输公司合同报价"):
                    xzbz_dd = ict.Test_Added01().test_Added0049(hz_id=gys_id[1],contractType="transportation_company_type")
                    assert xzbz_dd[0] == '操作成功'
                with allure.step("查看新增运输公司合同报价id"):
                    bz_dd = ict.Test_Added01().test_Added0048(hz_id=gys_id[1],contractType= "transportation_company_type")
                    assert bz_dd[0] == '操作成功'
                with allure.step("启用新增运输公司合同报价:{}".format(bz_dd[3])):
                    qybz_dd = ict.Test_Added01().test_Added0050(bjd_id=bz_dd[2])
                    assert qybz_dd == '操作成功'
            if bz_dd1[1] != 0:
                with allure.step("存在运输公司合同报价，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0048(hz_id=gys_id[1],contractType= "transportation_company_type")
                    assert bjd_bm[0] == '操作成功'
                    if bjd_bm[1] == "status_type_unenabled":
                        with allure.step("启用已存在(未启用)运输公司报价单,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_disabled":
                        with allure.step("启用已存在(禁用)运输公司报价单,报价单编码：{}".format(bjd_bm[3])):
                            jd_bm = ict.Test_Added01().test_Added0050(bjd_id=bjd_bm[2])
                            assert jd_bm == '操作成功'
                    if bjd_bm[1] == "status_type_enabled":
                        with allure.step("已存在运输公司报价单，并已启用,报价单编码：{}".format(bjd_bm[3])):
                            pass
        with allure.step("获取装货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
            assert jd_bm1[0] == '操作成功'
            zjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]
        with allure.step("查看是否存在危险品出口运输运输公司合同报价"):
            bjd_bm3 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="dangerous_cargo_export_transport",jd_bm=[])
            assert bjd_bm3[0] == '操作成功'
            if bjd_bm3[1] == 0:
                with allure.step("获取港口id"):
                    gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
                    assert gk_id1[0] == '操作成功'
                    gk_id = gk_id1[1]  # 港口id
                    gk_name = gk_id1[2]  # 港口名称
                with allure.step("获取收发地省编码"):
                    sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
                    assert sf_bm1[0] == '操作成功'
                    sf_bm = sf_bm1[1]
                    sf_name = sf_bm1[2]
                with allure.step("获取收发地市编码"):
                    cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
                    assert cs_bm1[0] == '操作成功'
                    cs_bm = cs_bm1[1]
                    cs_name = cs_bm1[2]
                with allure.step("获取收发地区编码"):
                    q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
                    assert q_bm1[0] == '操作成功'
                    q_bm = q_bm1[1]
                    q_name = q_bm1[2]
                with allure.step("获取收发地街道编码"):
                    jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
                    assert jd_bm1[0] == '操作成功'
                    jd_bm = jd_bm1[1]
                    jd_name = jd_bm1[2]
                with allure.step(
                        "新增危险品出口货主合同报价:港口：{},{}{}{}{}".format(gk_name, sf_name, cs_name, q_name, jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0052(customerPriceId=bjd_bm[2],
                                                                taskUnitCode="dangerous_cargo_export_transport",
                                                                taskUnitTypeName="危险品出口运输",
                                                                transportPort=gk_id, departure=jd_bm,
                                                                departureProvinces=sf_bm,
                                                                departureCity=cs_bm,
                                                                departureArea=q_bm)
                    assert xzsc_bj == '操作成功'
                with allure.step("新增危险品出口运输货主合同报价，查看报价单信息"):
                    bjd_bm4 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="dangerous_cargo_export_transport",jd_bm=[])
                    assert bjd_bm4[0] == '操作成功'
                    bj_id = bjd_bm4[2][0]["id"]
                with allure.step("启用危险品出口运输运输货主合同报价,报价单编码：{}".format(bjd_bm[3])):
                    jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                    assert jd_bm == '操作成功'
            if bjd_bm3[1] != 0:
                with allure.step("存在危险品出口运输运输公司合同报价，查看报价单信息"):
                    bjd_bm4 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="dangerous_cargo_export_transport",jd_bm=[])
                    assert bjd_bm4[0] == '操作成功'
                    bj_id = bjd_bm4[2][0]["id"]
                    bjd_zt = bjd_bm4[2][0]["enabledType"]
                    if bjd_zt == "enabled_type_unenabled":
                        with allure.step("启用存在(未启用)危险品出口运输公司合同报价"):
                            jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                            assert jd_bm == '操作成功'
                    if bjd_zt == "enabled_type_disabled":
                        with allure.step("启用存在(禁用)危险品出口运输公司合同报价"):
                            jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                            assert jd_bm == '操作成功'
                    if bjd_zt == "enabled_type_enabled":
                        with allure.step("存在危险品出口运输公司合同报价,并已启用报价"):
                            pass



@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景一 集装箱出口')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso1():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景一 集装箱出口（测试点：重复派车自有车应付费用生成五条明细)")
    def test_business_scenario001(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]    #货主联系人id
            lxr_name = lxr_name1[3]  #货主联系人名称
            lxr_hm = lxr_name1[4]    #货主联系人号码
        with allure.step("港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]   #港口id
        with allure.step("获取收发地省编码"):
            sf_bm = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm[0] == '操作成功'
            sf_bm = sf_bm[1]
        with allure.step("获取收发地市编码"):
            cs_bm = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm[0] == '操作成功'
            cs_bm = cs_bm[1]
        with allure.step("获取收发地区编码"):
            q_bm = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm[0] == '操作成功'
            q_bm = q_bm[1]
        with allure.step("获取收发地街道编码"):
            jd_bm = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm[0] == '操作成功'
            jd_bm = jd_bm[1]
        with allure.step("获取装货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            zhdw_id = sfh_dd[1]         #装货单位id
            zhdw_name = sfh_dd[2]       #装货单位名称
            zhdw_lxr =  sfh_dd[3]       #装货联系人
            zhdw_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time9 =time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  #订舱号
        with allure.step("集装箱出口运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0055(taskUnitCode="port_container_export_transport",customerId=hz_id,
                                                        transportPort=gk_id,provinces=sf_bm,city=cs_bm,area=q_bm,
                                                        street=jd_bm,consigneeConsignorId=zhdw_id,pickupTime=time2,carModeId="20GP")
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("新增集装箱出口订单"):
            newly_order = ict.Test_Added01().test_Added02100(customerId=hz_id,customerContact=lxr_name,customerContactPhone=lxr_hm,
                        customerServiceId=kf_id,transportPort=gk_id,departureProvinces=sf_bm,departureCity=cs_bm,departureArea=q_bm,
                        departure=jd_bm,cyCutOffTime=time3,consignorId=zhdw_id,consignorName=zhdw_name,consignorContact=zhdw_lxr,
                        consignorContactPhone=zhdw_xlrdh,consignorContactAddr=zhdw_xxdz,provinces=sf_bm,city=cs_bm,district=q_bm,
                        street=jd_bm,pickupTime=time2,bookingNumber=SSS,customerDelegateCode=time9,baseAmount=bjd_je,price=bjd_je,
                        customerPricePropertyId=bjd_id,matchKey=jd_bm)
            assert newly_order == '操作成功'
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'

        '''集装箱出口订单分单管理》分自有车'''
        with allure.step("计划管理，分单查询，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                print(id2)
                fd_id = id[id2]
                with allure.step("分单，分派自有车,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che=fd_id,gys="",hy_dt="")
                    assert qy_jdzx == '操作成功'

        '''集装箱出口订单派自有车A'''
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[3][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[3][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[2]    #订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')   #装货时间  年月日
        with allure.step("查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]   #司机id
            sj_name = xz_sj[4]   #司机名称
            sj_haoma = xz_sj[5]   #司机号码
        with allure.step("查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]   #车辆id
            cp_hao = sj_da[2]    #车牌号
            cl_name = sj_da[4]  #车辆名称
            cz_qy = sj_da[6]    # 操作区域
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0 :
                with allure.step("出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type",cz_qy=cz_qy,tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0 :
                with allure.step("出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤ZZ0001",zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'

        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'

        with allure.step("应付费用基本信息明细，订单:{}".format(dd_hao)):
            jb_xx = ict.Test_Added01().test_Added0087(dd_id=dd_id)
            pytest.assume(jb_xx[0] == '操作成功')
            zd_id =jb_xx[1]["chargeInfo"][0]["id"]  # 账单ID
            cp_hao = jb_xx[1]["supplierTransportOrderVo"]["mainlandLicensePlateNumber"]  # 车牌号
            sj_name1 = jb_xx[1]["supplierTransportOrderVo"]["driverName"]  # 司机姓名

        with allure.step("应付费用费用信息明细，订单:{}".format(dd_hao)):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            # zd_id = fy_xx[1][0]["id"]   #账单ID
            dd_hao = fy_xx[1][0]["orderNumber"]    #订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][0]["statusType"]    #明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            js_dw = fy_xx[1][0]["balanceId"]["title"] #结算单位

        with allure.step("断言车牌号:{},司机名称:{},结算单位:{},费用明细状态:{}".format(cp_hao,sj_name1,js_dw,zd_zt)):
            pytest.assume(cp_hao == cc_xx[4])
            pytest.assume(sj_name1 == sj_name)
            pytest.assume(js_dw == gyl_name)
            pytest.assume(zd_zt == "status_check_awaiting")
        with allure.step("手动录入柜号，订单:{}".format(dd_hao)):
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            # g_hao = ict.Test_Added01().test_Added0089(x_hao=x_hao,kg_z=kg_z,dd_id=dd_id,ft_hao=ft_hao)
            # pytest.assume(g_hao == '操作成功')

        with allure.step("获取节点ID，订单:{}".format(dd_hao)):
            jd_id = ict.Test_Added01().test_Added0124(dd_id=dd_id)
            pytest.assume(jd_id[0] == '操作成功')
            g_hao = ict.Test_Added01().test_Added0123(dd_id=dd_id,g_hao=x_hao,ft_hao=ft_hao,k_gz=kg_z,time1=zh_time,jd_id=jd_id[1])
            pytest.assume(g_hao == '操作成功')

        with allure.step("跟踪管理查看柜号，订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
        with allure.step("跟踪管理查看提柜节点时间跟踪点亮，订单:{}".format(dd_hao)):
            dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
            pytest.assume(dl_time[0]  == '操作成功')
            taskTypeName = dl_time[1][2]["taskTypeName"]
            finishTime = dl_time[1][2]["finishTime"]
            pytest.assume(taskTypeName == '离开提柜地')    #节点名称
            pytest.assume(finishTime != [])               #节点时间

        '''集装箱出口订单撤销派自有车A'''
        with allure.step("自有车撤销派单，订单号:{}".format(dd_hao)):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        with allure.step("跟踪管理查看柜号不清空，订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)   #断言柜号
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)       #断言封条号
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)      #断言空柜重
            allure.attach(ck_g_hao[1][0]["containerNumber"], name="断言柜号：FSCU5130217", attachment_type=allure.attachment_type.TEXT)
            allure.attach(ck_g_hao[1][0]["sealNumber"], name="断言封条号：CAAU5507656", attachment_type=allure.attachment_type.TEXT)
            allure.attach(ck_g_hao[1][0]["cabinetWeight"], name="断言柜重：2580", attachment_type=allure.attachment_type.TEXT)
        with allure.step("跟踪管理查看提柜节点时间跟踪清空，订单:{}".format(dd_hao)):
            dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
            pytest.assume(dl_time[0]  == '操作成功')
            taskTypeName = dl_time[1][2]["taskTypeName"]
            pytest.assume(taskTypeName  == '离开提柜地')      ##节点名称
            allure.attach(body=taskTypeName, name="断言节点名称：离开提柜地", attachment_type=allure.attachment_type.TEXT)
            time1= dl_time[1][2]
            list22 = []
            for key in time1:
                # print(key)
                if key == "finishTime":
                    # print(time1[key])
                    list22.append(key)
            pytest.assume(list22 == [])      #断言节点时间key不存在
        with allure.step("断言应付费用列表清空，订单:{}".format(dd_hao)):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(fy_lb[0] ==  '操作成功')
            allure.attach(body=fy_lb[0], name="接口响应", attachment_type=allure.attachment_type.TEXT)
            pytest.assume(fy_lb[2]["driverName"] != "测试自有车-集1" )      #断言司机名称
            allure.attach(body=fy_lb[2]["driverName"], name="断言司机名称为空", attachment_type=allure.attachment_type.TEXT)
            pytest.assume(fy_lb[2]["mainlandLicensePlateNumber"] != "粤ZZ0001")      #断言车牌号
            allure.attach(body=fy_lb[2]["mainlandLicensePlateNumber"], name="断言车牌号为空", attachment_type=allure.attachment_type.TEXT)
            list11 = []
            time1 = fy_lb[2]
            for key in time1:
                # print(key)
                if key == "supplierId":
                    # print(time1[key])
                    list11.append(time1[key])
            pytest.assume(list11 == [])      #断言结算单位为空
            pytest.assume(fy_lb[2]["orderStatus"] == "status_waiting_dispatch" )      #断言运单状态=待派单
            pytest.assume(fy_lb[2]["baseAmount"] == 0 )      #断言应付运费0
            pytest.assume(fy_lb[2]["otherAmount"] == 0 )      #断言其它应付费用0


        '''集装箱出口订单派自有车B'''
        with allure.step("查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集2")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]   #司机id
            sj_name = xz_sj[4]   #司机名称
            sj_haoma = xz_sj[5]   #司机号码
        with allure.step("查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集2")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤B7788")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]   #车辆id
            cp_hao = sj_da[2]    #车牌号
            cl_name = sj_da[4]  #车辆名称
            cz_qy = sj_da[6]    # 操作区域
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤B7788",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0 :
                with allure.step("出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type",cz_qy=cz_qy,tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0 :
                with allure.step("出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤B7788",zh_time=time2)
                    assert cc_dd[0] == '操作成功'
                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'

        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤B7788",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'

        with allure.step("应付费用基本信息明细，订单:{}".format(dd_hao)):
            jb_xx = ict.Test_Added01().test_Added0087(dd_id=dd_id)
            pytest.assume(jb_xx[0] == '操作成功')
            zd_id =jb_xx[1]["chargeInfo"][0]["id"]  # 账单ID
            cp_hao = jb_xx[1]["supplierTransportOrderVo"]["mainlandLicensePlateNumber"]  # 车牌号
            sj_name1 = jb_xx[1]["supplierTransportOrderVo"]["driverName"]  # 司机姓名

        with allure.step("应付费用费用信息明细，订单:{}".format(dd_hao)):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            zd_id = fy_xx[1][0]["id"]   #账单ID
            dd_hao = fy_xx[1][0]["orderNumber"]    #订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][0]["statusType"]    #明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            js_dw = fy_xx[1][0]["balanceId"]["title"] #结算单位

        with allure.step("断言车牌号:{},司机名称:{},结算单位:{},费用明细状态:{}".format(cp_hao,sj_name1,js_dw,zd_zt)):
            pytest.assume(cp_hao == cc_xx[4])
            pytest.assume(sj_name1 == sj_name)
            pytest.assume(js_dw == gyl_name)
            pytest.assume(zd_zt == "status_check_awaiting")
        with allure.step("应付费用费用明细审核，订单:{}".format(dd_hao)):
            mx_sh = ict.Test_Added01().test_Added0095(mx_id=zd_id)
            pytest.assume(mx_sh == '操作成功')
        with allure.step("应付费用费用信息明细状态，订单:{}".format(dd_hao)):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')  #订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][0]["statusType"]    #明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            pytest.assume(zd_zt == "status_check_completed")

        # with allure.step("跟踪管理查看柜号，订单:{}".format(dd_hao)):
        #     x_hao = "FSCU5130217"
        #     ft_hao = "CAAU5507656"
        #     kg_z = "2580"
        #     ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
        #     pytest.assume(ck_g_hao[0] == '操作成功')
        #     pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
        #     pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
        #     pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
        # with allure.step("跟踪管理查看提柜节点时间跟踪点亮，订单:{}".format(dd_hao)):
        #     dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
        #     pytest.assume(dl_time[0]  == '操作成功')
        #     taskTypeName = dl_time[1][2]["taskTypeName"]
        #     pytest.assume(taskTypeName == '离开提柜地')    #节点名称
        #     time1= dl_time[1][2]
        #     list22 = []
        #     for key in time1:
        #         # print(key)
        #         if key == "finishTime":
        #             # print(time1[key])
        #             list22.append(key)
        #     pytest.assume(list22 != [])      #断言节点时间key存在

        '''集装箱出口订单撤销派自有车B'''
        with allure.step("自有车撤销派单，订单号:{}".format(dd_hao)):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        with allure.step("跟踪管理查看柜号不清空，订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
            allure.attach(ck_g_hao[1][0]["containerNumber"], name="断言柜号：FSCU5130217", attachment_type=allure.attachment_type.TEXT)
            allure.attach(ck_g_hao[1][0]["sealNumber"], name="断言封条号：CAAU5507656", attachment_type=allure.attachment_type.TEXT)
            allure.attach(ck_g_hao[1][0]["cabinetWeight"], name="断言柜重：2580", attachment_type=allure.attachment_type.TEXT)
        with allure.step("跟踪管理查看提柜节点时间跟踪清空，订单:{}".format(dd_hao)):
            dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
            pytest.assume(dl_time[0]  == '操作成功')
            taskTypeName = dl_time[1][2]["taskTypeName"]
            pytest.assume(taskTypeName  == '离开提柜地')      ##节点名称
            allure.attach(body=taskTypeName, name="断言节点名称：离开提柜地", attachment_type=allure.attachment_type.TEXT)
            time1= dl_time[1][2]
            list22 = []
            for key in time1:
                # print(key)
                if key == "finishTime":
                    # print(time1[key])
                    list22.append(key)
            pytest.assume(list22 == [])      #断言节点时间key不存在
        with allure.step("断言应付费用列表清空，订单:{}".format(dd_hao)):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(fy_lb[0] ==  '操作成功')
            allure.attach(body=fy_lb[0], name="接口响应", attachment_type=allure.attachment_type.TEXT)
            pytest.assume(fy_lb[2]["driverName"] != "测试自有车-集2" )      #断言司机名称
            allure.attach(body=fy_lb[2]["driverName"], name="断言司机名称为空", attachment_type=allure.attachment_type.TEXT)
            pytest.assume(fy_lb[2]["mainlandLicensePlateNumber"] != "粤B7788")      #断言车牌号
            allure.attach(body=fy_lb[2]["mainlandLicensePlateNumber"], name="断言车牌号为空", attachment_type=allure.attachment_type.TEXT)
            list11 = []
            time1 = fy_lb[2]
            for key in time1:
                # print(key)
                if key == "supplierId":
                    # print(time1[key])
                    list11.append(time1[key])
            pytest.assume(list11 == [])      #断言结算单位为空
            pytest.assume(fy_lb[2]["baseAmount"] == 0 )      #断言应付运费0
            pytest.assume(fy_lb[2]["otherAmount"] == 0 )      #断言其它应付费用0

        '''集装箱出口订单派自有车c'''
        with allure.step("查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]  # 司机id
            sj_name = xz_sj[4]  # 司机名称
            sj_haoma = xz_sj[5]  # 司机号码
        with allure.step("查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  # 供应商id
            gyl_name = gys_da[4]  # 供应商名称
        with allure.step("查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]  # 车辆id
            cp_hao = sj_da[2]  # 车牌号
            cl_name = sj_da[4]  # 车辆名称
            cz_qy = sj_da[6]  # 操作区域
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤ZZ0001", zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0:
                with allure.step("出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type", cz_qy=cz_qy, tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0:
                with allure.step("出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001", zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if j == "car_dispatch_undistribute":
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'



        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001", zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id = cc_xx[1]  # 出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2, fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id, driverId=sj_id, supplierId=gys_id,
                                                     mainlandLicensePlateNumber=cp_hao,
                                                     orderNumber=dd_hao, pickupTime=zh_time,
                                                     transportType="transport_type_one_one",
                                                     mainlandLicensePlate=cl_id, driverName=sj_name,
                                                     mainlandPhone=sj_haoma, supplierName=gyl_name,
                                                     carDispatchId=ccb_id)
            assert pzyc == '操作成功'

        with allure.step("应付费用基本信息明细，订单:{}".format(dd_hao)):
            jb_xx = ict.Test_Added01().test_Added0087(dd_id=dd_id)
            pytest.assume(jb_xx[0] == '操作成功')
            zd_id = jb_xx[1]["chargeInfo"][0]["id"]  # 账单ID
            cp_hao = jb_xx[1]["supplierTransportOrderVo"]["mainlandLicensePlateNumber"]  # 车牌号
            sj_name1 = jb_xx[1]["supplierTransportOrderVo"]["driverName"]  # 司机姓名

        with allure.step("应付费用费用信息明细，订单:{}".format(dd_hao)):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            zd_id1 = fy_xx[1][2]["id"]   #账单ID
            dd_hao = fy_xx[1][2]["orderNumber"]  # 订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][2]["statusType"]  # 明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            js_dw = fy_xx[1][2]["balanceId"]["title"]  # 结算单位
        with allure.step("断言车牌号:{},司机名称:{},结算单位:{},费用明细状态:{}".format(cp_hao, sj_name1, js_dw, zd_zt)):
            pytest.assume(cp_hao == cc_xx[4])
            pytest.assume(sj_name1 == sj_name)
            pytest.assume(js_dw == gyl_name)
            pytest.assume(zd_zt == "status_check_awaiting")

        with allure.step("应付费用B费用信息明细生成负数并明细已审核，订单:{}".format(dd_hao)):
            zd_zt1 = fy_xx[1][0]["statusType"]
            zd_zt2 = fy_xx[1][1]["statusType"]
            je1 = fy_xx[1][0]["price"]
            je2 = fy_xx[1][1]["price"]
            pytest.assume(zd_zt1 == "status_check_completed")
            pytest.assume(zd_zt2 == "status_check_completed")
            pytest.assume(je1 == 3500)
            pytest.assume(je2 == -3500)
        # with allure.step("跟踪管理查看柜号，订单:{}".format(dd_hao)):
        #     ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao, fw_lx="port_container_export_transport")
        #     x_hao = "FSCU5130217"
        #     ft_hao = "CAAU5507656"
        #     kg_z = "2580"
        #     pytest.assume(ck_g_hao[0] == '操作成功')
        #     pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
        #     pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
        #     pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
        # with allure.step("跟踪管理查看提柜节点时间跟踪点亮，订单:{}".format(dd_hao)):
        #     dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
        #     pytest.assume(dl_time[0] == '操作成功')
        #     taskTypeName = dl_time[1][2]["taskTypeName"]
        #     finishTime = dl_time[1][2]["finishTime"]
        #     pytest.assume(taskTypeName == '离开提柜地')  # 节点名称
        #     pytest.assume(finishTime != [])  # 节点时间
        with allure.step("应付费用费用明细审核，订单:{}".format(dd_hao)):
            mx_sh = ict.Test_Added01().test_Added0095(mx_id=zd_id1)
            pytest.assume(mx_sh == '操作成功')
        with allure.step("应付费用费用整审，订单:{}".format(dd_hao)):
            fy_zs = ict.Test_Added01().test_Added0096(dd_id=dd_id)
            pytest.assume(fy_zs == '操作成功')
        with allure.step("断言应付费用列表订单费用状态已完成，订单:{}".format(dd_hao)):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_hao, fw_lx="port_container_export_transport")
            pytest.assume(fy_lb[0] == '操作成功')
            pytest.assume(fy_lb[2]["chargeStatus"] == "status_check_all_completed")  # 断言订单费用状态已整审

        '''集装箱出口订单撤销派自有车c'''
        with allure.step("自有车撤销派单，订单号:{}".format(dd_hao)):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        with allure.step("跟踪管理查看柜号不清空，订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao, fw_lx="port_container_export_transport")
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
            allure.attach(ck_g_hao[1][0]["containerNumber"], name="断言柜号：FSCU5130217",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(ck_g_hao[1][0]["sealNumber"], name="断言封条号：CAAU5507656",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(ck_g_hao[1][0]["cabinetWeight"], name="断言柜重：2580",
                          attachment_type=allure.attachment_type.TEXT)
        with allure.step("跟踪管理查看提柜节点时间跟踪清空，订单:{}".format(dd_hao)):
            dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
            pytest.assume(dl_time[0] == '操作成功')
            taskTypeName = dl_time[1][2]["taskTypeName"]
            pytest.assume(taskTypeName == '离开提柜地')  ##节点名称
            allure.attach(body=taskTypeName, name="断言节点名称：离开提柜地", attachment_type=allure.attachment_type.TEXT)
            time1 = dl_time[1][2]
            list22 = []
            for key in time1:
                # print(key)
                if key == "finishTime":
                    # print(time1[key])
                    list22.append(key)
            pytest.assume(list22 == [])  # 断言节点时间key不存在
        with allure.step("断言应付费用列表清空，订单:{}".format(dd_hao)):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_hao, fw_lx="port_container_export_transport")
            pytest.assume(fy_lb[0] == '操作成功')
            allure.attach(body=fy_lb[0], name="接口响应", attachment_type=allure.attachment_type.TEXT)
            pytest.assume(fy_lb[2]["driverName"] != "测试自有车-集1")  # 断言司机名称
            allure.attach(body=fy_lb[2]["driverName"], name="断言司机名称为空", attachment_type=allure.attachment_type.TEXT)
            pytest.assume(fy_lb[2]["mainlandLicensePlateNumber"] != "粤ZZ0001")  # 断言车牌号
            allure.attach(body=fy_lb[2]["mainlandLicensePlateNumber"], name="断言车牌号为空",
                          attachment_type=allure.attachment_type.TEXT)
            list11 = []
            time1 = fy_lb[2]
            for key in time1:
                # print(key)
                if key == "supplierId":
                    # print(time1[key])
                    list11.append(time1[key])
            pytest.assume(list11 == [])  # 断言结算单位为空
            pytest.assume(fy_lb[2]["orderStatus"] == "status_waiting_dispatch")  # 断言运单状态=待派单
            pytest.assume(fy_lb[2]["baseAmount"] == 0 )          #断言应付运费0
            pytest.assume(fy_lb[2]["otherAmount"] == 0 )         #断言其它应付费用0


        '''集装箱出口订单派自有车D'''
        with allure.step("查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集2")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]   #司机id
            sj_name = xz_sj[4]   #司机名称
            sj_haoma = xz_sj[5]   #司机号码
        with allure.step("查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集2")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤B7788")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]   #车辆id
            cp_hao = sj_da[2]    #车牌号
            cl_name = sj_da[4]  #车辆名称
            cz_qy = sj_da[6]    # 操作区域
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤B7788",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0 :
                with allure.step("出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type",cz_qy=cz_qy,tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0 :
                with allure.step("出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤B7788",zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if j == "car_dispatch_undistribute":
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤B7788",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'
        # with allure.step("跟踪管理查看柜号，订单:{}".format(dd_hao)):
        #     x_hao = "FSCU5130217"
        #     ft_hao = "CAAU5507656"
        #     kg_z = "2580"
        #     ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
        #     pytest.assume(ck_g_hao[0] == '操作成功')
        #     pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
        #     pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
        #     pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
        # with allure.step("跟踪管理查看提柜节点时间跟踪点亮，订单:{}".format(dd_hao)):
        #     dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
        #     pytest.assume(dl_time[0]  == '操作成功')
        #     taskTypeName = dl_time[1][2]["taskTypeName"]
        #     pytest.assume(taskTypeName == '离开提柜地')    #节点名称
        #     time1= dl_time[1][2]
        #     list22 = []
        #     for key in time1:
        #         # print(key)
        #         if key == "finishTime":
        #             # print(time1[key])
        #             list22.append(key)
        #     pytest.assume(list22 != [])      #断言节点时间key存在
        with allure.step("应付费用改单查询，订单:{}".format(dd_hao)):
            yf_gd = ict.Test_Added01().test_Added0097(dd_hao=dd_hao)
            pytest.assume(yf_gd[0]  == '操作成功')
            pytest.assume(yf_gd[1][0]["renewalReason"]  == '海格原因')  #断言改单原因
            pytest.assume(yf_gd[1][0]["statusType"]  == 'status_submit_awaiting')  #断言改单状态》待提交



            zd_id = yf_gd[1][0]["id"]
        with allure.step("应付费用改单详情页，订单:{},{}".format(dd_hao,zd_id)):
            gd_xx = ict.Test_Added01().test_Added0183(zd_id=zd_id)
            # print(dd_xx)
            pytest.assume(gd_xx[0]  == '操作成功')
            title1 = ict.get_k(gd_xx[1]["title"])
            details1 = ict.get_k(gd_xx[1]["details"][4])
            # print(details1)
            title1.update([("chargeDirection",1)])
            details1.update([("salesPrice",3500),("salesAmount",3500),("salesNumber",1)])
        with allure.step("应付费用改单提交，订单:{}".format(dd_hao)):
            gd_tj = ict.Test_Added01().test_Added0098(title=title1,detail=details1)
            pytest.assume(gd_tj  == '操作成功')




        with allure.step("应付费用改单审核，订单:{}".format(dd_hao)):
            gd_sh = ict.Test_Added01().test_Added0099(gd_id=yf_gd[1][0]["id"])
            pytest.assume(gd_sh  == '操作成功')
        with allure.step("应付费用费用信息明细，订单:{}".format(dd_hao)):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            # zd_id = fy_xx[1][0]["id"]   #账单ID
            dd_hao = fy_xx[1][4]["orderNumber"]    #订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][4]["statusType"]    #明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            js_dw = fy_xx[1][4]["balanceId"]["title"] #结算单位
            gd_bh = fy_xx[1][4]["renewalNumber"] #改单编号
            gd_yy = fy_xx[1][4]["renewalReason"] #调整原因
            pytest.assume(gd_bh != [])           #改单编号
            pytest.assume(gd_yy == "海格原因")      #调整原因
            pytest.assume(zd_zt == "status_check_all_completed")  #费用状态


        with allure.step("断言应付费用费用信息明细全部撤销账单结算单位明细，订单:{}".format(dd_hao)):
            js_dw0 = fy_xx[1][0]["balanceId"]["title"]  # 结算单位
            js_dw1 = fy_xx[1][1]["balanceId"]["title"]  # 结算单位
            js_dw2 = fy_xx[1][2]["balanceId"]["title"]  # 结算单位
            js_dw3 = fy_xx[1][3]["balanceId"]["title"]  # 结算单位
            js_dw4 = fy_xx[1][4]["balanceId"]["title"]  # 结算单位
            pytest.assume(js_dw0 == "租户测试自有车-集2") #派B车账单
            pytest.assume(js_dw1 == "租户测试自有车-集2") #派B车账单
            pytest.assume(js_dw2 == "租户测试自有车-集1") #派C车账单
            pytest.assume(js_dw3 == "租户测试自有车-集1") #派C车账单
            pytest.assume(js_dw4 == "租户测试自有车-集2") #派D车账单
        with allure.step("断言应付费用费用信息明细全部撤销账单结金额明细，订单:{}".format(dd_hao)):
            je1 = fy_xx[1][0]["price"]
            je2 = fy_xx[1][1]["price"]
            je3 = fy_xx[1][2]["price"]
            je4 = fy_xx[1][3]["price"]
            je5 = fy_xx[1][4]["price"]
            pytest.assume(je1 == 3500)
            pytest.assume(je2 == -3500)
            pytest.assume(je3 == 3500)
            pytest.assume(je4 == -3500)
            pytest.assume(je5 == 3500)


        '''取消订单'''
        with allure.step("调度管理》撤销派单/车，订单号：{}".format(dd_hao)):
            cx_pc = ict.Test_Added01().test_Added0156(dd_id=dd_id)
            assert cx_pc == '操作成功'
        with allure.step("计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("撤销分单,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("集装箱运输》取消订单，订单号：{}".format(dd_xx1[2])):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=dd_xx[6]["id"])
            assert qx_dd == '操作成功'
        with allure.step("订单管理》集装箱运输》查看订单状态，订单号：{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode="")
            assert jzx_ys[0] == '操作成功'
            assert jzx_ys[1][0]["orderStatus"] == 'status_undo_completed'

@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景二 厢式车多装一卸')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso2():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景二 厢式车多装一卸（测试点：重复派车运输公司应付费用生成五条明细）")
    def test_business_scenario001(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]    #货主联系人id
            lxr_name = lxr_name1[3]  #货主联系人名称
            lxr_hm = lxr_name1[4]    #货主联系人号码
        with allure.step("获取卸货地省编码"):
            sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm1[0] == '操作成功'
            xsf_bm = sf_bm1[1]
            xsf_name = sf_bm1[2]
        with allure.step("获取卸货地市编码"):
            cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm1[0] == '操作成功'
            xcs_bm = cs_bm1[1]
            xcs_name = cs_bm1[2]
        with allure.step("获取卸货地区编码"):
            q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm1[0] == '操作成功'
            xq_bm = q_bm1[1]
            xq_name = q_bm1[2]
        with allure.step("获取卸货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm1[0] == '操作成功'
            xjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]

        with allure.step("获取装货地省编码"):
            sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
            assert sf_bm1[0] == '操作成功'
            zsf_bm = sf_bm1[1]
            zsf_name = sf_bm1[2]
        with allure.step("获取装货地市编码"):
            cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
            assert cs_bm1[0] == '操作成功'
            zcs_bm = cs_bm1[1]
            zcs_name = cs_bm1[2]
        with allure.step("获取装货地区编码"):
            q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
            assert q_bm1[0] == '操作成功'
            zq_bm = q_bm1[1]
            zq_name = q_bm1[2]
        with allure.step("获取装货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
            assert jd_bm1[0] == '操作成功'
            zjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]


        with allure.step("获取装货单位1档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="厢式车装货地址1")
            assert sfh_dd[0] == '操作成功'
            zhdw1_id = sfh_dd[1]         #装货单位id
            zhdw1_name = sfh_dd[2]       #装货单位名称
            zhdw1_lxr =  sfh_dd[3]       #装货联系人
            zhdw1_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw1_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取装货单位2档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="厢式车装货地址2")
            assert sfh_dd[0] == '操作成功'
            zhdw2_id = sfh_dd[1]         #装货单位id
            zhdw2_name = sfh_dd[2]       #装货单位名称
            zhdw2_lxr =  sfh_dd[3]       #装货联系人
            zhdw2_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw2_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取卸货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            xhdw_id = sfh_dd[1]         #装货单位id
            xhdw_name = sfh_dd[2]       #装货单位名称
            xhdw_lxr =  sfh_dd[3]       #装货联系人
            xhdw_xlrdh = sfh_dd[4]      #装货联系电话
            xhdw_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 =time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 =time1[5]  # +50天  年月日
            time7 =time1[6]  # +100天  年月日
            time8 =time1[7]  # +200天  年月日
            time9 =time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  #订舱号
        with allure.step("厢式车运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0102(customerId=hz_id,provinces=xsf_bm,city=xcs_bm,area=xq_bm,street=xjd_bm,provinces1=zsf_bm,city1=zcs_bm,area1=zq_bm,street1=zjd_bm,consigneeConsignorId1=zhdw1_id,consigneeConsignorId2=zhdw2_id)
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("新增厢式车运输"):
            xz_xsc =  ict.Test_Added01().test_Added02101(customerId=hz_id,customerContact=lxr_name,customerContactPhone=lxr_hm,customerServiceId=kf_id,consigneeId=xhdw_id,consigneeName=xhdw_name,consigneeContact=xhdw_lxr,
                        consigneeContactPhone=xhdw_xlrdh,consigneeContactAddr=xhdw_xxdz,xh_sf=xsf_bm,xh_cs=xcs_bm,xh_q=xq_bm,xh_jd=xjd_bm,zh_sf=zsf_bm,zh_cs=zcs_bm,zh_q=zq_bm,zh_jd=zjd_bm,zh_dz1id=zhdw1_id,zh_dz1name=zhdw1_name,zh_dz1lxr=zhdw1_lxr,
                        zh_dz1lxrdh=zhdw1_xlrdh,zh_dz1=zhdw1_xxdz,zh_dz2id=zhdw2_id,zh_dz2name=zhdw2_name,zh_dz2lxr=zhdw2_lxr,zh_dz2lxrdh=zhdw2_xlrdh,zh_dz2=zhdw2_xxdz,zh_time=time2,jc_time=time3,bj_je=bjd_je,bj_id=bjd_id,kh_hao=time9)
            assert xz_xsc == '操作成功'
        with allure.step("查询新增厢式车多装一卸订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            dd_hao =  dd_xx[3]

        '''厢式车订单分单管理》分供应'''
        with allure.step("计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 1
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("分单，分派供应商,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che="", gys=fd_id, hy_dt="")
                    assert qy_jdzx == '操作成功'

        '''厢式车订单派供应商A：手工报价'''
        with allure.step("计划管理，获取订单ID，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys2_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr =  gys_xx[2]
            gys_lxrdh =  gys_xx[3]
        with allure.step("派供应商A"):
            gys_xx = ict.Test_Added01().test_Added0106(dd_id=dd_id,gys_lxr=gys_lxr,gys_lxrdh=gys_lxrdh,gys_id=gys_id[1],je=2500)
            assert gys_xx == '操作成功'

        '''厢式车订单派供应商A：应付费用断言'''
        with allure.step("应付费用基本信息明细，订单:{}".format(dd_hao)):
            jb_xx = ict.Test_Added01().test_Added0087(dd_id=dd_id)
            pytest.assume(jb_xx[0] == '操作成功')
            zd_id =jb_xx[1]["chargeInfo"][0]["id"]  # 账单ID
        with allure.step("应付费用费用信息明细，订单:{}".format(dd_hao)):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            # zd_id = fy_xx[1][0]["id"]   #账单ID
            dd_hao = fy_xx[1][0]["orderNumber"]    #订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][0]["statusType"]    #明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            js_dw = fy_xx[1][0]["balanceId"]["title"] #结算单位
        with allure.step("结算单位:{},费用明细状态:{}".format(js_dw,zd_zt)):
            pytest.assume(js_dw == cf.gys2_name)
            pytest.assume(zd_zt == "status_check_awaiting")
        with allure.step("应付列表，司机，车牌号断言为空".format(js_dw,zd_zt)):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=(dd_xx[3]), fw_lx="")
            pytest.assume(fy_lb[0] == '操作成功')
            allure.attach(body=fy_lb[0], name="接口响应", attachment_type=allure.attachment_type.TEXT)
            list11 = []
            time1 = fy_lb[2]
            for key in time1:
                # print(key)
                if key == "driverName":
                    # print(time1[key])
                    list11.append(time1[key])
            pytest.assume(list11 == [])  # 断言司机key不存在
            list22 = []
            time1 = fy_lb[2]
            for key in time1:
                # print(key)
                if key == "mainlandLicensePlateNumber":
                    # print(time1[key])
                    list22.append(time1[key])
            pytest.assume(list11 == [])  # 断言车牌号key不存在


        '''厢式车订单改派供应商B：合同报价'''
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr =  gys_xx[2]
            gys_lxrdh =  gys_xx[3]
        with allure.step("派供应商B"):
            gys_xx = ict.Test_Added01().test_Added0107(dd_id=dd_id,gys_lxr=gys_lxr,gys_lxrdh=gys_lxrdh,gys_id=gys_id[1])
            assert gys_xx == '操作成功'

        '''供应商B接单，并指派车辆'''
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("供应商接单"):
            gys_id1 = ict.Test_transport_company01().test_transport0002(dd_id=dd_id)
            assert gys_id1== '操作成功'
        with allure.step("查看司机ID"):
            siji_da = ict.Test_transport_company01().test_transport0003(siji_name="测试运输公司司机1",gys_id=gys_id[1])
            assert siji_da[0] == '操作成功'
            siji_id =  siji_da[2][0]["id"]
            siji_name = siji_da[2][0]["driverName"]
            siji_dh = siji_da[2][0]["driverMobilePhone"]
        with allure.step("查看车辆档案"):
            cl_da = ict.Test_transport_company01().test_transport0007(c_pai="粤A6688",gys_id=gys_id[1])
            assert cl_da[0] == '操作成功'
            cl_id =  cl_da[2][0]["id"]
            c_pai = cl_da[2][0]["carNumber"]
        with allure.step("供应商指派车辆"):
            zp_cl = ict.Test_transport_company01().test_transport0009(dd_id=dd_id,shiji_dh=siji_dh,cl_id=cl_id,siji_id=siji_id,
                                                                      c_pai=c_pai,siji_name=siji_name)
            assert zp_cl == '操作成功'

        with allure.step("应付费用基本信息明细，订单:{}".format(dd_hao)):
            jb_xx = ict.Test_Added01().test_Added0087(dd_id=dd_id)
            pytest.assume(jb_xx[0] == '操作成功')
            zd_id = jb_xx[1]["chargeInfo"][0]["id"]  # 账单ID
            cp_hao1 = jb_xx[1]["supplierTransportOrderVo"]["mainlandLicensePlateNumber"]  # 车牌号
            sj_name1 = jb_xx[1]["supplierTransportOrderVo"]["driverName"]  # 司机姓名

        with allure.step("应付费用费用信息明细，订单:{}".format(dd_xx[3])):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            zd_id = fy_xx[1][0]["id"]  # 账单ID
            dd_hao = fy_xx[1][0]["orderNumber"]  # 订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][0]["statusType"]  # 明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            js_dw = fy_xx[1][0]["balanceId"]["title"]  # 结算单位

        with allure.step("断言存在车牌号:{},司机名称:{},结算单位:{},费用明细状态:{}".format(cp_hao1,sj_name1,js_dw, zd_zt)):
            pytest.assume(cp_hao1 == c_pai)
            pytest.assume(sj_name1 == siji_name)
            pytest.assume(js_dw == cf.gys1_name)
            pytest.assume(zd_zt == "status_check_awaiting")
        with allure.step("应付费用费用明细审核，订单:{}".format(dd_hao)):
            mx_sh = ict.Test_Added01().test_Added0095(mx_id=zd_id)
            pytest.assume(mx_sh == '操作成功')
        with allure.step("应付费用费用信息明细状态，订单:{}".format(dd_hao)):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')  # 订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][0]["statusType"]  # 明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            pytest.assume(zd_zt == "status_check_completed")

        '''厢式车订单改派供应商C：手工报价'''
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys2_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr = gys_xx[2]
            gys_lxrdh = gys_xx[3]
        with allure.step("派供应商c，订单ID：{}，联系人：{}，电话：{},供应商ID：{}".format(dd_id,gys_lxr,gys_lxrdh,gys_id[1])):
            gys_xx = ict.Test_Added01().test_Added0109(dd_id=dd_id, gys_lxr=gys_lxr, gys_lxrdh=gys_lxrdh,
                                                       gys_id=gys_id[1])
            assert gys_xx == '操作成功'


        with allure.step("应付费用费用信息明细，订单:{}".format(dd_hao)):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            zd_id1 = fy_xx[1][2]["id"]  # 账单ID
            dd_hao = fy_xx[1][2]["orderNumber"]  # 订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][2]["statusType"]  # 明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            js_dw0 = fy_xx[1][0]["balanceId"]["title"]  # 结算单位
            js_dw1 = fy_xx[1][1]["balanceId"]["title"]  # 结算单位
            js_dw2 = fy_xx[1][2]["balanceId"]["title"]  # 结算单位

        with allure.step("断言订单现有结算单位:{},费用明细状态:{}".format(js_dw2,zd_zt)):
            pytest.assume(js_dw2 == cf.gys2_name)
            pytest.assume(zd_zt == "status_check_awaiting")

        with allure.step("断言订单原有结算单位，应付费用B费用信息明细生成负数并明细已审核，订单:{}".format(dd_hao)):
            zd_zt1 = fy_xx[1][0]["statusType"]
            zd_zt2 = fy_xx[1][1]["statusType"]
            je1 = fy_xx[1][0]["price"]
            je2 = fy_xx[1][1]["price"]
            pytest.assume(zd_zt1 == "status_check_completed")
            pytest.assume(zd_zt2 == "status_check_completed")
            pytest.assume(je1 == 5000)
            pytest.assume(je2 == -5000)
            pytest.assume(js_dw0 == cf.gys1_name)
            pytest.assume(js_dw1 == cf.gys1_name)
        with allure.step("应付列表，司机，车牌号断言为空".format(js_dw2,zd_zt)):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=(dd_xx[3]), fw_lx="")
            pytest.assume(fy_lb[0] == '操作成功')
            allure.attach(body=fy_lb[0], name="接口响应", attachment_type=allure.attachment_type.TEXT)
            list11 = []
            time1 = fy_lb[2]
            for key in time1:
                # print(key)
                if key == "driverName":
                    # print(time1[key])
                    list11.append(time1[key])
            pytest.assume(list11 == [])  # 断言司机key不存在
            list22 = []
            time1 = fy_lb[2]
            for key in time1:
                # print(key)
                if key == "mainlandLicensePlateNumber":
                    # print(time1[key])
                    list22.append(time1[key])
            pytest.assume(list11 == [])  # 断言车牌号key不存在
        with allure.step("应付费用费用明细审核，订单:{}".format(dd_hao)):
                mx_sh = ict.Test_Added01().test_Added0095(mx_id=zd_id1)
                pytest.assume(mx_sh == '操作成功')
        with allure.step("应付费用费用整审，订单:{}".format(dd_hao)):
            fy_zs = ict.Test_Added01().test_Added0096(dd_id=dd_id)
            pytest.assume(fy_zs == '操作成功')
        with allure.step("断言应付费用列表订单费用状态已完成，订单:{}".format(dd_hao)):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_hao, fw_lx="")
            pytest.assume(fy_lb[0] == '操作成功')
            allure.attach(body=fy_lb[0], name="接口响应", attachment_type=allure.attachment_type.TEXT)
            pytest.assume(fy_lb[2]["chargeStatus"] == "status_check_all_completed")  # 断言订单费用状态已整审

        '''厢式车订单改派供应商D：合同报价'''
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr =  gys_xx[2]
            gys_lxrdh =  gys_xx[3]
        with allure.step("派供应商D"):
            gys_xx = ict.Test_Added01().test_Added0107(dd_id=dd_id,gys_lxr=gys_lxr,gys_lxrdh=gys_lxrdh,gys_id=gys_id[1])
            assert gys_xx == '操作成功'

        '''供应商D接单，并指派车辆'''
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("供应商接单"):
            gys_id1 = ict.Test_transport_company01().test_transport0002(dd_id=dd_id)
            assert gys_id1== '操作成功'
        with allure.step("查看司机ID"):
            siji_da = ict.Test_transport_company01().test_transport0003(siji_name="测试运输公司司机1",gys_id=gys_id[1])
            assert siji_da[0] == '操作成功'
            siji_id =  siji_da[2][0]["id"]
            siji_name = siji_da[2][0]["driverName"]
            siji_dh = siji_da[2][0]["driverMobilePhone"]
        with allure.step("查看车辆档案"):
            cl_da = ict.Test_transport_company01().test_transport0007(c_pai="粤A6688",gys_id=gys_id[1])
            assert cl_da[0] == '操作成功'
            cl_id =  cl_da[2][0]["id"]
            c_pai = cl_da[2][0]["carNumber"]
        with allure.step("供应商指派车辆"):
            zp_cl = ict.Test_transport_company01().test_transport0009(dd_id=dd_id,shiji_dh=siji_dh,cl_id=cl_id,siji_id=siji_id,
                                                                      c_pai=c_pai,siji_name=siji_name)
            assert zp_cl == '操作成功'
        with allure.step("断言应付费用插入改单明细信息，订单:{}".format(dd_hao)):
            yf_gd = ict.Test_Added01().test_Added0097(dd_hao=dd_hao)
            pytest.assume(yf_gd[0] == '操作成功')
            pytest.assume(yf_gd[1][0]["renewalReason"] == '海格原因')  # 断言改单原因
            pytest.assume(yf_gd[1][0]["statusType"] == 'status_submit_awaiting')  # 断言改单状态

            zd_id = yf_gd[1][0]["id"]
        with allure.step("应付费用改单详情页，订单:{},{}".format(dd_hao,zd_id)):
            gd_xx = ict.Test_Added01().test_Added0183(zd_id=zd_id)
            pytest.assume(gd_xx[0]  == '操作成功')
            title1 = ict.get_k(gd_xx[1]["title"])
            details1 = ict.get_k(gd_xx[1]["details"][4])
            title1.update([("chargeDirection",1)])
            details1.update([("salesPrice",3500),("salesAmount",3500),("salesNumber",1)])
        with allure.step("应付费用改单提交，订单:{}".format(dd_xx[3])):
            gd_tj = ict.Test_Added01().test_Added0098(title=title1,detail=details1)
            pytest.assume(gd_tj  == '操作成功')


        with allure.step("应付费用改单审核，订单:{}".format(dd_hao)):
            gd_sh = ict.Test_Added01().test_Added0099(gd_id=yf_gd[1][0]["id"])
            pytest.assume(gd_sh == '操作成功')
        with allure.step("断言改单明细插入应付账单，订单:{}".format(dd_hao)):  #断言的是改单明细是否插入应付账单
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            # zd_id = fy_xx[1][0]["id"]   #账单ID
            dd_hao = fy_xx[1][4]["orderNumber"]  # 订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][4]["statusType"]  # 明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
            js_dw = fy_xx[1][4]["balanceId"]["title"]  # 结算单位
            gd_bh = fy_xx[1][4]["renewalNumber"]  # 改单编号
            gd_yy = fy_xx[1][4]["renewalReason"]  # 调整原因
            pytest.assume(gd_bh != [])  # 改单编号
            pytest.assume(gd_yy == "海格原因")  # 调整原因
            pytest.assume(zd_zt == "status_check_all_completed")  # 费用状态
        with allure.step("断言应付费用费用信息明细全部撤销账单结算单位明细，订单:{}".format(dd_hao)):
            js_dw0 = fy_xx[1][0]["balanceId"]["title"]  # 结算单位
            js_dw1 = fy_xx[1][1]["balanceId"]["title"]  # 结算单位
            js_dw2 = fy_xx[1][2]["balanceId"]["title"]  # 结算单位
            js_dw3 = fy_xx[1][3]["balanceId"]["title"]  # 结算单位
            js_dw4 = fy_xx[1][4]["balanceId"]["title"]  # 结算单位
            pytest.assume(js_dw0 == cf.gys1_name) #派B车账单
            pytest.assume(js_dw1 == cf.gys1_name) #派B车账单
            pytest.assume(js_dw2 == cf.gys2_name) #派C车账单
            pytest.assume(js_dw3 == cf.gys2_name) #派C车账单
            pytest.assume(js_dw4 == cf.gys1_name) #派D车账单
        with allure.step("断言应付费用费用信息明细全部撤销账单结金额明细，订单:{}".format(dd_hao)):
            je1 = fy_xx[1][0]["price"]
            je2 = fy_xx[1][1]["price"]
            je3 = fy_xx[1][2]["price"]
            je4 = fy_xx[1][3]["price"]
            je5 = fy_xx[1][4]["price"]
            pytest.assume(je1 == 5000)
            pytest.assume(je2 == -5000)
            pytest.assume(je3 == 4500)
            pytest.assume(je4 == -4500)
            pytest.assume(je5 == 5000)

        '''取消订单'''
        with allure.step("调度管理》撤销派单/车，订单号：{}".format(dd_hao)):
            cx_pc = ict.Test_Added01().test_Added0156(dd_id=dd_id)
            assert cx_pc == '操作成功'
        with allure.step("计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("撤销分单,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("集装箱运输》取消订单，订单号：{}".format(dd_hao)):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=dd_xx[6]["id"])
            assert qx_dd == '操作成功'
        with allure.step("订单管理》集装箱运输》查看订单状态，订单号：{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0168(orderNumber=dd_hao)
            assert jzx_ys[0] == '操作成功'
            assert jzx_ys[1][0]["orderStatus"] == 'status_undo_completed'

@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景四 集装箱出口')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso3():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景四 集装箱出口（测试点：柜号多路径同步）")
    def test_business_scenario001(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]    #货主联系人id
            lxr_name = lxr_name1[3]  #货主联系人名称
            lxr_hm = lxr_name1[4]    #货主联系人号码
        with allure.step("港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]   #港口id
        with allure.step("获取收发地省编码"):
            sf_bm = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm[0] == '操作成功'
            sf_bm = sf_bm[1]
        with allure.step("获取收发地市编码"):
            cs_bm = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm[0] == '操作成功'
            cs_bm = cs_bm[1]
        with allure.step("获取收发地区编码"):
            q_bm = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm[0] == '操作成功'
            q_bm = q_bm[1]
        with allure.step("获取收发地街道编码"):
            jd_bm = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm[0] == '操作成功'
            jd_bm = jd_bm[1]
        with allure.step("获取装货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            zhdw_id = sfh_dd[1]         #装货单位id
            zhdw_name = sfh_dd[2]       #装货单位名称
            zhdw_lxr =  sfh_dd[3]       #装货联系人
            zhdw_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 =time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 =time1[5]  # +50天  年月日
            time7 =time1[6]  # +100天  年月日
            time8 =time1[7]  # +200天  年月日
            time9 =time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  #订舱号
        with allure.step("集装箱出口运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0055(taskUnitCode="port_container_export_transport",customerId=hz_id,
                                                        transportPort=gk_id,provinces=sf_bm,city=cs_bm,area=q_bm,
                                                        street=jd_bm,consigneeConsignorId=zhdw_id,pickupTime=time2,carModeId="20GP")
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("新增集装箱出口订单"):
                xzjzx_ck = ict.Test_Added01().test_Added02100(customerId=hz_id,customerContact=lxr_name,customerContactPhone=lxr_hm,
                            customerServiceId=kf_id,transportPort=gk_id,departureProvinces=sf_bm,departureCity=cs_bm,departureArea=q_bm,
                            departure=jd_bm,cyCutOffTime=time3,consignorId=zhdw_id,consignorName=zhdw_name,consignorContact=zhdw_lxr,
                            consignorContactPhone=zhdw_xlrdh,consignorContactAddr=zhdw_xxdz,provinces=sf_bm,city=cs_bm,district=q_bm,
                            street=jd_bm,pickupTime=time2,bookingNumber=SSS,customerDelegateCode=time9,baseAmount=bjd_je,price=bjd_je,
                            customerPricePropertyId=bjd_id,matchKey=jd_bm)
                assert xzjzx_ck == '操作成功'
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            dd_hao = dd_xx[3]
            orde_id = dd_xx[6]["id"]
        '''集装箱出口订单分单管理》分自有车'''
        with allure.step("集装箱出口订单分单管理》分自有车>计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("集装箱出口订单分单管理》分自有车>分单，分派自有车,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che=fd_id,gys="",hy_dt="")
                    assert qy_jdzx == '操作成功'

        '''集装箱出口订单派自有车A，并审核应付明细'''
        with allure.step("集装箱出口订单派自有车A，并审核应付明细>查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[3][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[3][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[2]    #订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')   #装货时间  年月日
        with allure.step("集装箱出口订单派自有车A，并审核应付明细>查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]   #司机id
            sj_name = xz_sj[4]   #司机名称
            sj_haoma = xz_sj[5]   #司机号码
        with allure.step("集装箱出口订单派自有车A，并审核应付明细>查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("集装箱出口订单派自有车A，并审核应付明细>查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]   #车辆id
            cp_hao = sj_da[2]    #车牌号
            cl_name = sj_da[4]  #车辆名称
            cz_qy = sj_da[6]    # 操作区域
        with allure.step("集装箱出口订单派自有车A，并审核应付明细>维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0 :
                with allure.step("集装箱出口订单派自有车A，并审核应付明细>出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type",cz_qy=cz_qy,tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0 :
                with allure.step("集装箱出口订单派自有车A，并审核应付明细>出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤ZZ0001",zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'
        with allure.step("集装箱出口订单派自有车A，并审核应付明细>维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("集装箱出口订单派自有车A，并审核应付明细>调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("集装箱出口订单派自有车A，并审核应付明细>调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'


        '''跟踪管理，集装箱运输》柜号录入'''
        with allure.step("跟踪管理，集装箱运输》柜号录入>手动录入柜号，订单:{}".format(dd_hao)):
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            g_hao = ict.Test_Added01().test_Added0089(x_hao=x_hao,kg_z=kg_z,dd_id=dd_id,ft_hao=ft_hao)
            pytest.assume(g_hao == '操作成功')
        with allure.step("跟踪管理，集装箱运输》柜号录入》跟踪管理查看柜号，订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)

        '''柜号录入，查看柜号同步'''
        x_hao = "FSCU5130217"
        ft_hao = "CAAU5507656"
        kg_zl = "2580"
        with allure.step("柜号录入，查看柜号同步》订单管理》订单录入列表，查看同步柜号"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            xianghao1 =  dd_xx[6]["containerNumber"]
            fengtiao1 =  dd_xx[6]["sealNumber"]
            konggui1 = dd_xx[6]["cabinetWeight"]
            pytest.assume(x_hao == xianghao1)
            pytest.assume(ft_hao == fengtiao1)
            pytest.assume(2580 == konggui1)

        with allure.step("号录入，查看柜号同步》订单管理》集装箱运输列表，查看同步柜号,订单号：{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert jzx_ys[0] == '操作成功'
            xianghao2 =  jzx_ys[1][0]["containerNumber"]
            fengtiao2 =  jzx_ys[1][0]["sealNumber"]
            konggui2 = jzx_ys[1][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao2)
            pytest.assume(ft_hao == fengtiao2)
            pytest.assume(2580 == konggui2)

        with allure.step("号录入，查看柜号同步》运单管理>计划管理>集装箱>订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            xianghao3 =  fd_xx[2][0]["containerNumber"]
            fengtiao3 =  fd_xx[2][0]["sealNumber"]
            konggui3 = fd_xx[2][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao3)
            pytest.assume(ft_hao == fengtiao3)
            pytest.assume( kg_zl == konggui3)

            xianghao4 =  fd_xx[2][1]["containerNumber"]
            fengtiao4 =  fd_xx[2][1]["sealNumber"]
            konggui4 = fd_xx[2][1]["cabinetWeight"]
            pytest.assume(x_hao == xianghao4)
            pytest.assume(ft_hao == fengtiao4)
            pytest.assume( kg_zl == konggui4)
            xianghao5 =  fd_xx[2][2]["containerNumber"]
            fengtiao5 =  fd_xx[2][2]["sealNumber"]
            konggui5 = fd_xx[2][2]["cabinetWeight"]
            pytest.assume(x_hao == xianghao5)
            pytest.assume(ft_hao == fengtiao5)
            pytest.assume( kg_zl == konggui5)
            xianghao6 =  fd_xx[2][3]["containerNumber"]
            fengtiao6 =  fd_xx[2][3]["sealNumber"]
            konggui6 = fd_xx[2][3]["cabinetWeight"]
            pytest.assume(x_hao == xianghao6)
            pytest.assume(ft_hao == fengtiao6)
            pytest.assume( kg_zl == konggui6)

        with allure.step("号录入，查看柜号同步》运单管理>调度管理>集装箱>订单号：{}".format(dd_hao)):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="")
            assert dd_xx1[0] == '操作成功'
            xianghao7 = dd_xx1[3][0]["containerNumber"]
            fengtiao7 = dd_xx1[3][0]["sealNumber"]
            konggui7 = dd_xx1[3][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)

            xianghao8 = dd_xx1[3][1]["containerNumber"]
            fengtiao8 = dd_xx1[3][1]["sealNumber"]
            konggui8 = dd_xx1[3][1]["cabinetWeight"]
            pytest.assume(x_hao == xianghao8)
            pytest.assume(ft_hao == fengtiao8)
            pytest.assume(kg_zl == konggui8)

            xianghao9 = dd_xx1[3][2]["containerNumber"]
            fengtiao9 = dd_xx1[3][2]["sealNumber"]
            konggui9 = dd_xx1[3][2]["cabinetWeight"]
            pytest.assume(x_hao == xianghao9)
            pytest.assume(ft_hao == fengtiao9)
            pytest.assume(kg_zl == konggui9)

            xianghao11 = dd_xx1[3][3]["containerNumber"]
            fengtiao11 = dd_xx1[3][3]["sealNumber"]
            konggui11 = dd_xx1[3][3]["cabinetWeight"]
            pytest.assume(x_hao == xianghao11)
            pytest.assume(ft_hao == fengtiao11)
            pytest.assume(kg_zl == konggui11)



        with allure.step("号录入，查看柜号同步》运单管理>监理管理>订单号：{}".format(dd_hao)):
            jl_gl = ict.Test_Added01().test_Added0118(dd_hao=dd_hao)
            assert jl_gl[0] == '操作成功'
            xianghao7 = jl_gl[1][0]["containerNumber"]
            fengtiao7 = jl_gl[1][0]["sealNumber"]
            konggui7 = jl_gl[1][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)

        with allure.step("号录入，查看柜号同步》运单管理>报关管理>订单号：{}".format(dd_hao)):
            bg_gl = ict.Test_Added01().test_Added0119(dd_hao=dd_hao)
            assert bg_gl[0] == '操作成功'
            xianghao7 = bg_gl[1][0]["containerNumber"]
            fengtiao7 = bg_gl[1][0]["sealNumber"]
            konggui7 = bg_gl[1][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)


        with allure.step("号录入，查看柜号同步》跟踪管理>集装箱>订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_zl)
            pytest.assume(ck_g_hao[1][1]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][1]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][1]["cabinetWeight"] == kg_zl)
            pytest.assume(ck_g_hao[1][2]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][2]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][2]["cabinetWeight"] == kg_zl)
            pytest.assume(ck_g_hao[1][3]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][3]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][3]["cabinetWeight"] == kg_zl)

        with allure.step("号录入，查看柜号同步》跟踪管理>监理管理>订单号：{}".format(dd_hao)):
            gz_jl = ict.Test_Added01().test_Added0120(dd_hao=dd_hao)
            assert gz_jl[0] == '操作成功'
            data7 = gz_jl[1]
            xianghao7 = data7[0]["containerNumber"]
            fengtiao7 = data7[0]["sealNumber"]
            konggui7 = data7[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)

        with allure.step("号录入，查看柜号同步》跟踪管理>报关管理>订单号：{}".format(dd_hao)):
            gz_bg = ict.Test_Added01().test_Added0121(dd_hao=dd_hao)
            assert gz_bg[0] == '操作成功'
            data8 = gz_bg[1]
            xianghao7 = data8[0]["containerNumber"]
            fengtiao7 = data8[0]["sealNumber"]
            konggui7 = data8[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)


        with allure.step("号录入，查看柜号同步》应收费用制作>订单号：{}".format(dd_hao)):
            ys_fy = ict.Test_Added01().test_Added0086(dd_hao=dd_hao)
            assert ys_fy[0] == '操作成功'
            data9 = ys_fy[1]
            xianghao7 = data9[0]["containerNumber"]
            fengtiao7 = data9[0]["sealNumber"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)


        with allure.step("号录入，查看柜号同步》应付费用制作>订单号：{}".format(dd_hao)):
            yf_fy = ict.Test_Added01().test_Added0094(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            assert yf_fy[0] == '操作成功'
            xianghao7 = yf_fy[2]["containerNumber"]
            fengtiao7 = yf_fy[2]["sealNumber"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)

        '''柜号录入》跟踪管理》集装箱运输》清除柜号'''
        with allure.step("后台跟踪管理》集装箱运输》清除柜号，订单号{}".format(dd_hao)):
            cc_gh = ict.Test_Added01().test_Added0122(dd_id=dd_id)
            assert cc_gh == '操作成功'

        '''柜号录入>查看柜号为空'''
        with allure.step("柜号录入>查看柜号为空》订单管理》订单录入列表，查看同步柜号"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            data01 =  dd_xx[6]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("柜号录入>查看柜号为空》订单管理》集装箱运输列表，查看同步柜号,订单号：{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert jzx_ys[0] == '操作成功'
            data01 =  jzx_ys[1]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("柜号录入>查看柜号为空》运单管理>计划管理>集装箱>订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            data01 = fd_xx[2][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])


            data01 = fd_xx[2][1]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = fd_xx[2][2]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])


            data01 = fd_xx[2][3]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("柜号录入>查看柜号为空》运单管理>调度管理>集装箱>订单号：{}".format(dd_hao)):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="")
            assert dd_xx1[0] == '操作成功'
            data01 = dd_xx1[3][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = dd_xx1[3][1]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = dd_xx1[3][2]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = dd_xx1[3][3]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("柜号录入>查看柜号为空》运单管理>监理管理>订单号：{}".format(dd_hao)):
            jl_gl = ict.Test_Added01().test_Added0118(dd_hao=dd_hao)
            assert jl_gl[0] == '操作成功'
            data01 = jl_gl[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])


        with allure.step("柜号录入>查看柜号为空》运单管理>报关管理>订单号：{}".format(dd_hao)):
            bg_gl = ict.Test_Added01().test_Added0119(dd_hao=dd_hao)
            assert bg_gl[0] == '操作成功'
            data01 = bg_gl[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("柜号录入>查看柜号为空》跟踪管理>集装箱>订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="")
            pytest.assume(ck_g_hao[0] == '操作成功')
            data01 = ck_g_hao[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = ck_g_hao[1][1]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = ck_g_hao[1][2]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = ck_g_hao[1][3]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])


        with allure.step("柜号录入>查看柜号为空》跟踪管理>监理管理>订单号：{}".format(dd_hao)):
            gz_jl = ict.Test_Added01().test_Added0120(dd_hao=dd_hao)
            assert gz_jl[0] == '操作成功'

            data01 =   gz_jl[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("柜号录入>查看柜号为空》跟踪管理>报关管理>订单号：{}".format(dd_hao)):
            gz_bg = ict.Test_Added01().test_Added0121(dd_hao=dd_hao)
            assert gz_bg[0] == '操作成功'
            data01 = gz_bg[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("柜号录入>查看柜号为空》应收费用制作>订单号：{}".format(dd_hao)):
            ys_fy = ict.Test_Added01().test_Added0086(dd_hao=dd_hao)
            assert ys_fy[0] == '操作成功'
            data01 =  ys_fy[1][0]
            xianghao1 = []
            fengtiao1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])


        with allure.step("柜号录入>查看柜号为空》应付费用制作>订单号：{}".format(dd_hao)):
            yf_fy = ict.Test_Added01().test_Added0094(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            assert yf_fy[0] == '操作成功'
            data01 =  yf_fy[2]
            xianghao1 = []
            fengtiao1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])


        '''运单管理，调度管理》集装箱运输》节点跟踪'''
        with allure.step("获取节点ID，订单:{}".format(dd_hao)):
            jd_id = ict.Test_Added01().test_Added0124(dd_id=dd_id)
            pytest.assume(jd_id[0] == '操作成功')

        with allure.step("运单管理，调度管理》集装箱运输》节点跟踪》手动录入柜号，订单:{}".format(dd_hao)):
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            g_hao = ict.Test_Added01().test_Added0123(dd_id=dd_id,g_hao=x_hao,ft_hao=ft_hao,k_gz=kg_z,time1=zh_time,jd_id=jd_id[1])
            pytest.assume(g_hao == '操作成功')

        '''节点跟踪>查看柜号同步'''

        x_hao = "FSCU5130217"
        ft_hao = "CAAU5507656"
        kg_zl = "2580"
        with allure.step("节点跟踪>查看柜号同步》订单管理》订单录入列表，查看同步柜号"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            xianghao1 =  dd_xx[6]["containerNumber"]
            fengtiao1 =  dd_xx[6]["sealNumber"]
            konggui1 = dd_xx[6]["cabinetWeight"]
            pytest.assume(x_hao == xianghao1)
            pytest.assume(ft_hao == fengtiao1)
            pytest.assume(2580 == konggui1)

        with allure.step("节点跟踪>查看柜号同步》订单管理》集装箱运输列表，查看同步柜号,订单号：{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert jzx_ys[0] == '操作成功'
            xianghao2 =  jzx_ys[1][0]["containerNumber"]
            fengtiao2 =  jzx_ys[1][0]["sealNumber"]
            konggui2 = jzx_ys[1][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao2)
            pytest.assume(ft_hao == fengtiao2)
            pytest.assume(2580 == konggui2)

        with allure.step("节点跟踪>查看柜号同步》运单管理>计划管理>集装箱>订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            xianghao3 =  fd_xx[2][0]["containerNumber"]
            fengtiao3 =  fd_xx[2][0]["sealNumber"]
            konggui3 = fd_xx[2][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao3)
            pytest.assume(ft_hao == fengtiao3)
            pytest.assume( kg_zl == konggui3)

            xianghao4 =  fd_xx[2][1]["containerNumber"]
            fengtiao4 =  fd_xx[2][1]["sealNumber"]
            konggui4 = fd_xx[2][1]["cabinetWeight"]
            pytest.assume(x_hao == xianghao4)
            pytest.assume(ft_hao == fengtiao4)
            pytest.assume( kg_zl == konggui4)
            xianghao5 =  fd_xx[2][2]["containerNumber"]
            fengtiao5 =  fd_xx[2][2]["sealNumber"]
            konggui5 = fd_xx[2][2]["cabinetWeight"]
            pytest.assume(x_hao == xianghao5)
            pytest.assume(ft_hao == fengtiao5)
            pytest.assume( kg_zl == konggui5)
            xianghao6 =  fd_xx[2][3]["containerNumber"]
            fengtiao6 =  fd_xx[2][3]["sealNumber"]
            konggui6 = fd_xx[2][3]["cabinetWeight"]
            pytest.assume(x_hao == xianghao6)
            pytest.assume(ft_hao == fengtiao6)
            pytest.assume( kg_zl == konggui6)

        with allure.step("节点跟踪>查看柜号同步》运单管理>调度管理>集装箱>订单号：{}".format(dd_hao)):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="")
            assert dd_xx1[0] == '操作成功'
            xianghao7 = dd_xx1[3][0]["containerNumber"]
            fengtiao7 = dd_xx1[3][0]["sealNumber"]
            konggui7 = dd_xx1[3][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)

            xianghao8 = dd_xx1[3][1]["containerNumber"]
            fengtiao8 = dd_xx1[3][1]["sealNumber"]
            konggui8 = dd_xx1[3][1]["cabinetWeight"]
            pytest.assume(x_hao == xianghao8)
            pytest.assume(ft_hao == fengtiao8)
            pytest.assume(kg_zl == konggui8)

            xianghao9 = dd_xx1[3][2]["containerNumber"]
            fengtiao9 = dd_xx1[3][2]["sealNumber"]
            konggui9 = dd_xx1[3][2]["cabinetWeight"]
            pytest.assume(x_hao == xianghao9)
            pytest.assume(ft_hao == fengtiao9)
            pytest.assume(kg_zl == konggui9)

            xianghao11 = dd_xx1[3][3]["containerNumber"]
            fengtiao11 = dd_xx1[3][3]["sealNumber"]
            konggui11 = dd_xx1[3][3]["cabinetWeight"]
            pytest.assume(x_hao == xianghao11)
            pytest.assume(ft_hao == fengtiao11)
            pytest.assume(kg_zl == konggui11)



        with allure.step("节点跟踪>查看柜号同步》运单管理>监理管理>订单号：{}".format(dd_hao)):
            jl_gl = ict.Test_Added01().test_Added0118(dd_hao=dd_hao)
            assert jl_gl[0] == '操作成功'
            xianghao7 = jl_gl[1][0]["containerNumber"]
            fengtiao7 = jl_gl[1][0]["sealNumber"]
            konggui7 = jl_gl[1][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)

        with allure.step("节点跟踪>查看柜号同步》运单管理>报关管理>订单号：{}".format(dd_hao)):
            bg_gl = ict.Test_Added01().test_Added0119(dd_hao=dd_hao)
            assert bg_gl[0] == '操作成功'
            xianghao7 = bg_gl[1][0]["containerNumber"]
            fengtiao7 = bg_gl[1][0]["sealNumber"]
            konggui7 = bg_gl[1][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)


        with allure.step("节点跟踪>查看柜号同步》跟踪管理>集装箱>订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_zl)
            pytest.assume(ck_g_hao[1][1]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][1]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][1]["cabinetWeight"] == kg_zl)
            pytest.assume(ck_g_hao[1][2]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][2]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][2]["cabinetWeight"] == kg_zl)
            pytest.assume(ck_g_hao[1][3]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][3]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][3]["cabinetWeight"] == kg_zl)

        with allure.step("节点跟踪>查看柜号同步》跟踪管理>监理管理>订单号：{}".format(dd_hao)):
            gz_jl = ict.Test_Added01().test_Added0120(dd_hao=dd_hao)
            assert gz_jl[0] == '操作成功'
            data7 = gz_jl[1]
            xianghao7 = data7[0]["containerNumber"]
            fengtiao7 = data7[0]["sealNumber"]
            konggui7 = data7[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)

        with allure.step("节点跟踪>查看柜号同步》跟踪管理>报关管理>订单号：{}".format(dd_hao)):
            gz_bg = ict.Test_Added01().test_Added0121(dd_hao=dd_hao)
            assert gz_bg[0] == '操作成功'
            data8 = gz_bg[1]
            xianghao7 = data8[0]["containerNumber"]
            fengtiao7 = data8[0]["sealNumber"]
            konggui7 = data8[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_zl == konggui7)


        with allure.step("节点跟踪>查看柜号同步》应收费用制作>订单号：{}".format(dd_hao)):
            ys_fy = ict.Test_Added01().test_Added0086(dd_hao=dd_hao)
            assert ys_fy[0] == '操作成功'
            data9 = ys_fy[1]
            xianghao7 = data9[0]["containerNumber"]
            fengtiao7 = data9[0]["sealNumber"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)


        with allure.step("节点跟踪>查看柜号同步》应付费用制作>订单号：{}".format(dd_hao)):
            yf_fy = ict.Test_Added01().test_Added0094(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            assert yf_fy[0] == '操作成功'
            xianghao7 = yf_fy[2]["containerNumber"]
            fengtiao7 = yf_fy[2]["sealNumber"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)


        '''节点跟踪>跟踪管理》集装箱运输》清除柜号'''
        with allure.step("后台跟踪管理》集装箱运输》清除柜号，订单号{}".format(dd_hao)):
            cc_gh = ict.Test_Added01().test_Added0122(dd_id=dd_id)
            assert cc_gh == '操作成功'


        '''节点跟踪>查看柜号为空'''
        with allure.step("节点跟踪>查看柜号为空》订单管理》订单录入列表，查看同步柜号"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            data01 =  dd_xx[6]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("节点跟踪>查看柜号为空》订单管理》集装箱运输列表，查看同步柜号,订单号：{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert jzx_ys[0] == '操作成功'
            data01 =  jzx_ys[1]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("节点跟踪>查看柜号为空》运单管理>计划管理>集装箱>订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            data01 = fd_xx[2][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])


            data01 = fd_xx[2][1]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = fd_xx[2][2]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])


            data01 = fd_xx[2][3]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("节点跟踪>查看柜号为空》运单管理>调度管理>集装箱>订单号：{}".format(dd_hao)):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="")
            assert dd_xx1[0] == '操作成功'
            data01 = dd_xx1[3][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = dd_xx1[3][1]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = dd_xx1[3][2]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = dd_xx1[3][3]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("节点跟踪>查看柜号为空》运单管理>监理管理>订单号：{}".format(dd_hao)):
            jl_gl = ict.Test_Added01().test_Added0118(dd_hao=dd_hao)
            assert jl_gl[0] == '操作成功'
            data01 = jl_gl[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])


        with allure.step("节点跟踪>查看柜号为空》运单管理>报关管理>订单号：{}".format(dd_hao)):
            bg_gl = ict.Test_Added01().test_Added0119(dd_hao=dd_hao)
            assert bg_gl[0] == '操作成功'
            data01 = bg_gl[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("节点跟踪>查看柜号为空》跟踪管理>集装箱>订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="")
            pytest.assume(ck_g_hao[0] == '操作成功')
            data01 = ck_g_hao[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = ck_g_hao[1][1]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = ck_g_hao[1][2]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

            data01 = ck_g_hao[1][3]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])


        with allure.step("节点跟踪>查看柜号为空》跟踪管理>监理管理>订单号：{}".format(dd_hao)):
            gz_jl = ict.Test_Added01().test_Added0120(dd_hao=dd_hao)
            assert gz_jl[0] == '操作成功'

            data01 =   gz_jl[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("节点跟踪>查看柜号为空》跟踪管理>报关管理>订单号：{}".format(dd_hao)):
            gz_bg = ict.Test_Added01().test_Added0121(dd_hao=dd_hao)
            assert gz_bg[0] == '操作成功'
            data01 = gz_bg[1][0]
            xianghao1 = []
            fengtiao1 = []
            konggui1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
                if key == "cabinetWeight":
                    # print(time1[key])
                    konggui1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])
            pytest.assume(konggui1 == [])

        with allure.step("节点跟踪>查看柜号为空》应收费用制作>订单号：{}".format(dd_hao)):
            ys_fy = ict.Test_Added01().test_Added0086(dd_hao=dd_hao)
            assert ys_fy[0] == '操作成功'
            data01 =  ys_fy[1][0]
            xianghao1 = []
            fengtiao1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])


        with allure.step("节点跟踪>查看柜号为空》应付费用制作>订单号：{}".format(dd_hao)):
            yf_fy = ict.Test_Added01().test_Added0094(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            assert yf_fy[0] == '操作成功'
            data01 =  yf_fy[2]
            xianghao1 = []
            fengtiao1 = []
            for key in data01:
                # print(key)
                if key == "containerNumber":
                    # print(time1[key])
                    xianghao1.append(key)
                if key == "sealNumber":
                    # print(time1[key])
                    fengtiao1.append(key)
            pytest.assume(xianghao1 == [])
            pytest.assume(fengtiao1 == [])

        '''取消订单'''
        with allure.step("取消订单》调度管理》撤销派单/车，订单号：{}".format(dd_hao)):
            cx_pc = ict.Test_Added01().test_Added0156(dd_id=dd_id)
            assert cx_pc == '操作成功'
        with allure.step("取消订单》计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("取消订单》撤销分单,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("取消订单》集装箱运输》取消订单，订单号：{}".format(dd_hao)):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=orde_id)
            assert qx_dd == '操作成功'
        with allure.step("取消订单》订单管理》集装箱运输》查看订单状态，订单号：{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert jzx_ys[0] == '操作成功'
            assert jzx_ys[1][0]["orderStatus"] == 'status_undo_completed'

@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景五 集装箱出口')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso4():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("（测试点：应收应付费用制作+改单+收款+新增异常+异常处置）（测试点：应收应付费用制作+改单+收款+新增异常+异常处置）")
    def test_business_scenario001(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]    #货主联系人id
            lxr_name = lxr_name1[3]  #货主联系人名称
            lxr_hm = lxr_name1[4]    #货主联系人号码
        with allure.step("港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]   #港口id
        with allure.step("获取收发地省编码"):
            sf_bm = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm[0] == '操作成功'
            sf_bm = sf_bm[1]
        with allure.step("获取收发地市编码"):
            cs_bm = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm[0] == '操作成功'
            cs_bm = cs_bm[1]
        with allure.step("获取收发地区编码"):
            q_bm = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm[0] == '操作成功'
            q_bm = q_bm[1]
        with allure.step("获取收发地街道编码"):
            jd_bm = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm[0] == '操作成功'
            jd_bm = jd_bm[1]
        with allure.step("获取装货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            zhdw_id = sfh_dd[1]         #装货单位id
            zhdw_name = sfh_dd[2]       #装货单位名称
            zhdw_lxr =  sfh_dd[3]       #装货联系人
            zhdw_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 =time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 =time1[5]  # +50天  年月日
            time7 =time1[6]  # +100天  年月日
            time8 =time1[7]  # +200天  年月日
            time9 =time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  #订舱号
        with allure.step("集装箱出口运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0055(taskUnitCode="port_container_export_transport",customerId=hz_id,
                                                        transportPort=gk_id,provinces=sf_bm,city=cs_bm,area=q_bm,
                                                        street=jd_bm,consigneeConsignorId=zhdw_id,pickupTime=time2,carModeId="20GP")
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("新增集装箱出口订单"):
                xzjzx_ck = ict.Test_Added01().test_Added02100(customerId=hz_id,customerContact=lxr_name,customerContactPhone=lxr_hm,
                            customerServiceId=kf_id,transportPort=gk_id,departureProvinces=sf_bm,departureCity=cs_bm,departureArea=q_bm,
                            departure=jd_bm,cyCutOffTime=time3,consignorId=zhdw_id,consignorName=zhdw_name,consignorContact=zhdw_lxr,
                            consignorContactPhone=zhdw_xlrdh,consignorContactAddr=zhdw_xxdz,provinces=sf_bm,city=cs_bm,district=q_bm,
                            street=jd_bm,pickupTime=time2,bookingNumber=SSS,customerDelegateCode=time9,baseAmount=bjd_je,price=bjd_je,
                            customerPricePropertyId=bjd_id,matchKey=jd_bm)
                assert xzjzx_ck == '操作成功'
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            dd_hao = dd_xx[3]

        '''集装箱出口订单分单管理》分自有车'''
        with allure.step("集装箱出口订单分单管理》分自有车>计划管理，分单，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("分单，分派自有车,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che=fd_id,gys="",hy_dt="")
                    assert qy_jdzx == '操作成功'


        '''集装箱出口订单派自有车A'''
        with allure.step("集装箱出口订单派自有车A>查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[3][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[3][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[2]    #订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')   #装货时间  年月日
        with allure.step("集装箱出口订单派自有车A>查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]   #司机id
            sj_name = xz_sj[4]   #司机名称
            sj_haoma = xz_sj[5]   #司机号码
        with allure.step("集装箱出口订单派自有车A>查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("集装箱出口订单派自有车A>查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]   #车辆id
            cp_hao = sj_da[2]    #车牌号
            cl_name = sj_da[4]  #车辆名称
            cz_qy = sj_da[6]    # 操作区域
        with allure.step("集装箱出口订单派自有车A>维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0 :
                with allure.step("集装箱出口订单派自有车A>出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type",cz_qy=cz_qy,tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0 :
                with allure.step("集装箱出口订单派自有车A>出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤ZZ0001",zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'

        with allure.step("集装箱出口订单派自有车A>维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("集装箱出口订单派自有车A>调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("集装箱出口订单派自有车A>调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'

        '''派监理'''
        with allure.step("派监理>查询监理ID"):
            jl_da = ict.Test_Added01().test_Added0125(jl_name="毛敏监理01")
            assert jl_da[0] == '操作成功'
            jl_id = jl_da[1][0]["id"]
            jl_dh = jl_da[1][0]["supervisionPhone"]
        with allure.step("派监理>查询监理订单ID"):
            jlyd_id = ict.Test_Added01().test_Added0118(dd_hao=dd_hao)
            assert jlyd_id[0] == '操作成功'
            yd_id = jlyd_id[1][0]["id"]
            orderId = jlyd_id[1][0]["orderId"]
            orderNumber = jlyd_id[1][0]["orderNumber"]
        with allure.step("派监理>获取供应商ID"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("派监理>派监理，订单号：{}".format(dd_hao)):
            p_jl = ict.Test_Added01().test_Added0128(ji_id=jl_id,ji_dh=jl_dh,jldd_id=yd_id,orderId=orderId,gys_id=gys_id[1],jl_name="毛敏监理01")
            assert p_jl == '操作成功'
        with allure.step("派监理>获取图片地址"):
            tu_dz = pz.Common_page().projects_path() + r"\Common\picture\2.02 MB.JPG"  # 图片地址
            # print(tu_dz)
        with allure.step("派监理>上传图片，获取图片id"):
            tp_id = ict.Test_Added01().test_Added0129(tp_lj=tu_dz)     # 获取图片id
            assert tp_id[1] == "success"
        with allure.step("派监理>监理管理》上传附件，订单号{}".format(dd_hao)):
            sc_tp = ict.Test_Added01().test_Added0130(jldd_id=yd_id,tp_name="2.02 MB.JPG",tp_id=tp_id[0])
            assert sc_tp == "操作成功"
        with allure.step("派监理>监理管理》审核文件，订单号{}".format(dd_hao)):
            sc_wj = ict.Test_Added01().test_Added0131(jlyd_id=yd_id)
            assert sc_wj == "操作成功"
        with allure.step("派监理>查看监理运单状态，订单号{}".format(dd_hao)):
            jlyd_zt = ict.Test_Added01().test_Added0118(dd_hao=dd_hao)
            assert jlyd_zt[0] == '操作成功'
            yd_id = jlyd_zt[1][0]["orderStatus"]
            pytest.assume(yd_id == "status_completed")

        '''跟踪管理，集装箱运输》柜号录入'''
        with allure.step("跟踪管理，集装箱运输》柜号录入》手动录入柜号，订单:{}".format(dd_hao)):
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            g_hao = ict.Test_Added01().test_Added0089(x_hao=x_hao,kg_z=kg_z,dd_id=dd_id,ft_hao=ft_hao)
            pytest.assume(g_hao == '操作成功')
        with allure.step("跟踪管理，集装箱运输》柜号录入》跟踪管理查看柜号"):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)

        '''派报关订单'''
        with allure.step("派报关订单>查询报关订单ID"):
            bgyd_id = ict.Test_Added01().test_Added0119(dd_hao=dd_hao)
            assert bgyd_id[0] == '操作成功'
            yd_id = bgyd_id[1][0]["id"]
            yd_hao = bgyd_id[1][0]["orderNumber"]
        with allure.step("派报关订单>获取报关供应商ID"):
            gys_id = ict.Test_Added01().test_Added0132()
            assert gys_id[0] == '操作成功'
        with allure.step("派报关订单>查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr = gys_xx[2]
            gys_lxrdh = gys_xx[3]
        with allure.step("派报关订单>报关单派供应商,運单号{}".format(yd_hao)):
            p_bgd = ict.Test_Added01().test_Added0133(bbd_id=yd_id,gys_id=gys_id[1],gys_lxr=gys_lxr,lx_dh=gys_lxrdh)
            assert p_bgd == '操作成功'
        with allure.step("派报关订单>查看派报关订单推送日志"):
            gys_id = ict.Test_Added01().test_Added0134(dd_id=yd_hao)
            assert gys_id[0] == '操作成功'


        '''跟踪管理》新增异常'''
        with allure.step("跟踪管理》新增异常>跟踪管理》集装箱运输查询，订单号{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            assert jzx_ys[0] == '操作成功'
            pytest.assume(jzx_ys[1] != [])
        with allure.step("跟踪管理》新增异常>跟踪管理》监理管理，订单号{}".format(dd_hao)):
            jl_gl = ict.Test_Added01().test_Added0120(dd_hao=dd_hao)
            assert jl_gl[0] == '操作成功'
            pytest.assume(jl_gl[1] != [])
        with allure.step("跟踪管理》新增异常>跟踪管理》订单号{}".format(dd_hao)):
            bg_gl = ict.Test_Added01().test_Added0120(dd_hao=dd_hao)
            assert bg_gl[0] == '操作成功'
            pytest.assume(bg_gl[1] != [])
        with allure.step("跟踪管理》新增异常>跟踪管理》新增异常"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[9]  # +当天 年月日时分秒
            xz_yc = ict.Test_Added01().test_Added0135(dd_id=dd_id,dd_hao=dd_hao,yc_time=time2)
            assert xz_yc == '操作成功'
        with allure.step("跟踪管理》新增异常>跟踪管理》集装箱运输异常标识出现"):
            yc_bs = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            assert yc_bs[0] == '操作成功'
            pytest.assume(yc_bs[1][0]["tags"] == "异常")

        '''异常管理》异常处置'''
        with allure.step("异常管理》异常处置>查询异常状态,订单号{}".format(dd_hao)):
            yc_zt = ict.Test_Added01().test_Added0136(dd_hao=dd_hao)
            assert yc_zt[0] == '操作成功'
            cy_id =yc_zt[1][0]["id"]
            yc_dhao = yc_zt[1][0]["exceptionCode"]
            pytest.assume(yc_zt[1][0]["exceptionLogList"][0]["status"] ==  "待处理")
        with allure.step("异常管理》异常处置>查询监理ID"):
            jl_da = ict.Test_Added01().test_Added0125(jl_name="毛敏监理01")
            assert jl_da[0] == '操作成功'
            jl_id = jl_da[1][0]["id"]
            jl_dh = jl_da[1][0]["supervisionPhone"]
        with allure.step("异常管理》异常处置>异常处理,异常单号{}".format(yc_dhao)):
            time1 = bf.Common_page().get_today001()
            time2 = time1[9]  # +当天 年月日时分秒
            jl_da = ict.Test_Added01().test_Added0137(cy_id=cy_id,dd_id=dd_id,cy_dhao=yc_dhao,dd_hao=dd_xx[3],yc_time=time2,gjr=jl_id)
            assert jl_da == '操作成功'
        with allure.step("异常管理》异常处置>异常处理完成"):
            jl_da = ict.Test_Added01().test_Added0138(cy_id=cy_id)
            assert jl_da == '操作成功'
        with allure.step("异常管理》异常处置>查询异常状态"):
            yc_zt = ict.Test_Added01().test_Added0136(dd_hao=dd_hao)
            assert yc_zt[0] == '操作成功'
            pytest.assume(yc_zt[1][0]["exceptionLogList"][0]["status"] ==  "已提交")
        with allure.step("异常管理》异常处置>跟踪管理》集装箱运输异常标识消失"):
            yc_bs = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            assert yc_bs[0] == '操作成功'
            data1 = yc_bs[1][0]
            tags = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "tags":
                        # print(item[key])
                        tags.append(item[key])
            pytest.assume(tags == [])

        '''应收费用制作,明细审核+整审'''
        with allure.step("应收费用制作,明细审核+整审>应收费用制作查询运单基本信息(费用明细)"):
            ys_lb = ict.Test_Added01().test_Added0086(dd_hao=dd_hao)
            assert ys_lb[0] == '操作成功'
            yszd_id =  ys_lb[1][0]["id"]
            yszd_zt = ys_lb[1][0]["chargeStatus"]
            pytest.assume(yszd_zt == "status_check_awaiting")
        with allure.step("应收费用制作,明细审核+整审>应收费用制作查询运单费用明细信息(费用明细)"):
            zd_xx = ict.Test_Added01().test_Added0139(fy_id=yszd_id)
            assert zd_xx[0] == '操作成功'
            zt_id = zd_xx[1][0]["id"]
            zd_zt =  zd_xx[1][0]["statusType"]
            pytest.assume(zd_zt == "status_check_awaiting")
        with allure.step("应收费用制作,明细审核+整审>审核应收明细,账单id：{}".format(zt_id)):
            sh_mx = ict.Test_Added01().test_Added0141(zd_id=zt_id)
            assert sh_mx == '操作成功'
        with allure.step("应收费用制作,明细审核+整审>账单整审,订单号：{}".format(dd_hao)):
            sh_zd = ict.Test_Added01().test_Added0142(zd_id=yszd_id)
            assert sh_zd == '操作成功'
        with allure.step(" 应收费用制作,明细审核+整审>应收费用制作查询运单费用明细信息(费用明细)"):
            zd_xx = ict.Test_Added01().test_Added0139(fy_id=yszd_id)
            assert zd_xx[0] == '操作成功'
            zd_zt =  zd_xx[1][0]["statusType"]
            pytest.assume(zd_zt == "status_check_all_completed")


        with allure.step("查看派报关订单推送日志"):
            gys_id = ict.Test_Added01().test_Added0134(dd_id=dd_hao)
            assert gys_id[0] == '操作成功'
            dd_hao = gys_id[2][0]["showContent"]
            jk_name =  gys_id[2][0]["interfaceRuleName"]
            pytest.assume(dd_hao == dd_xx[3])
            pytest.assume(jk_name == "FSC接收一体化审核的应收费用明细")

        '''应收费用改单+改单审核'''
        with allure.step("应收费用改单+改单审核>应收费用制作查询运单基本信息(费用明细)"):
            ys_lb = ict.Test_Added01().test_Added0145(dd_hao=dd_hao)
            assert ys_lb[0] == '操作成功'
            yszd_id =  ys_lb[1][0]["id"]
            yszd_zt = ys_lb[1][0]["chargeStatus"]
        with allure.step("应收费用改单+改单审核>查询费用项档案"):
            fy_dd = ict.Test_Added01().test_Added0143()
            assert fy_dd[0] == '操作成功'
            fy_dw = fy_dd[1]
            fy_id = fy_dd[2]
            fy_lx = fy_dd[3]
        with allure.step("应收费用改单+改单审核>新增应收改单提交"):
            xx_gd = ict.Test_Added01().test_Added0144(dd_hao=dd_hao,hz_id=hz_id,dd_id=yszd_id,fy_id=fy_id,fy_lx=fy_lx,fy_dw=fy_dw,gdlx=0)
            assert xx_gd == '操作成功'
        with allure.step("应收费用改单+改单审核>改单列表查询，获取改单ID"):
            gd_lb = ict.Test_Added01().test_Added0146(dd_hao=dd_hao)
            assert gd_lb[0] == '操作成功'
            gd_id = gd_lb[1][0]["id"]

        with allure.step("应收费用改单+改单审核>改单审核,订单号：{}".format(dd_hao)):
            gd_sh = ict.Test_Added01().test_Added0147(gd_id=gd_id)
            assert gd_sh == '操作成功'
        with allure.step("应收费用改单+改单审核>改单列表查询，获取改单状态"):
            gd_lb = ict.Test_Added01().test_Added0146(dd_hao=dd_hao)
            assert gd_lb[0] == '操作成功'
            gd_zt = gd_lb[1][0]["statusType"]
            pytest.assume(gd_zt == "status_check_completed")


        '''应收费用对账单提交+生成月结账单+收款'''
        with allure.step("应收费用对账单提交+生成月结账单+收款>应收对账单》待生成对账单列表"):
            ys_lb = ict.Test_Added01().test_Added0149(dd_hao=dd_hao)
            assert ys_lb[0] == '操作成功'
            yszd_id =  ys_lb[1][0]["id"]
        with allure.step("应收费用对账单提交+生成月结账单+收款>对账单按单提交，订单号：{}".format(dd_hao)):
            tj_zd = ict.Test_Added01().test_Added0148(zd_id=yszd_id)
            assert tj_zd == '操作成功'
        with allure.step("应收费用对账单提交+生成月结账单+收款>应收对账单》对账单合计列表"):
            ys_lb = ict.Test_Added01().test_Added0151(dd_hao=dd_hao)
            assert ys_lb[0] == '操作成功'
            dzd_id =  ys_lb[1][0]["id"]
            dzd_zt = ys_lb[1][0]["statusType"]
            dzd_hao =  ys_lb[1][0]["billOrderNumber"]
            pytest.assume(dzd_zt == "status_bill_awaiting" )
        with allure.step("应收费用对账单提交+生成月结账单+收款>确认对账,对账单号：{}".format(dzd_hao)):
            qr_dz = ict.Test_Added01().test_Added0150(zd_id=dzd_id)
            assert qr_dz == '操作成功'

        with allure.step("应收费用对账单提交+生成月结账单+收款>生成结算单"):
            sc_jsd = ict.Test_Added01().test_Added0152(zd_id=dzd_id)
            assert sc_jsd == '操作成功'

        with allure.step("应收费用对账单提交+生成月结账单+收款>获取图片地址"):
            tu_dz = pz.Common_page().projects_path() + r"\Common\picture\2.02 MB.JPG"  # 图片地址
            # print(tu_dz)
        with allure.step("应收费用对账单提交+生成月结账单+收款>上传图片，获取图片id"):
            tp_id = ict.Test_Added01().test_Added0129(tp_lj=tu_dz)  # 获取图片id
            assert tp_id[1] == "success"
        with allure.step("应收费用对账单提交+生成月结账单+收款>查看对账单状态"):
            yy_zt = ict.Test_Added01().test_Added0154(zd_hao=dzd_hao)
            assert yy_zt[0] == "操作成功"
            id = yy_zt[1][0]["id"]
        with allure.step("应收费用对账单提交+生成月结账单+收款>确认收款"):
            qr_sk = ict.Test_Added01().test_Added0153(zd_id=id,tp_name="2.02 MB.JPG",tp_id=tp_id[0])  # 获取图片id
            assert qr_sk == "操作成功"
        with allure.step("应收费用对账单提交+生成月结账单+收款>查看对账单状态"):
            dzd_zt = ict.Test_Added01().test_Added0154(zd_hao=dzd_hao)
            assert dzd_zt[0] == "操作成功"
            pytest.assume(dzd_zt[1][0]["statusType"] == "status_all_pay_amount_comfirm" )

        '''应付费用制作,明细审核+整审'''
        with allure.step("应付费用制作,明细审核+整审>应付费用列表订单id，订单:{}".format(dd_hao)):
            lb_xx = ict.Test_Added01().test_Added0094(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(lb_xx[0] == '操作成功')
            dd_id = lb_xx[2]["id"]
        with allure.step("应付费用制作,明细审核+整审>应付费用费用信息明细"):
            fy_xx = ict.Test_Added01().test_Added0088(dd_id=dd_id)
            pytest.assume(fy_xx[0] == '操作成功')
            zd_id1 = fy_xx[1][0]["id"]  # 账单ID
            dd_hao = fy_xx[1][0]["orderNumber"]  # 订单号    明细已审核：status_check_completed
            zd_zt = fy_xx[1][0]["statusType"]  # 明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
        with allure.step("应付费用制作,明细审核+整审>应付费用费用明细审核"):
            mx_sh = ict.Test_Added01().test_Added0095(mx_id=zd_id1)
            pytest.assume(mx_sh == '操作成功')
        with allure.step("应付费用制作,明细审核+整审>应付费用费用整审"):
            fy_zs = ict.Test_Added01().test_Added0096(dd_id=dd_id)
            pytest.assume(fy_zs == '操作成功')
        with allure.step("应付费用制作,明细审核+整审>断言应付费用列表订单费用状态已完成"):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_hao, fw_lx="port_container_export_transport")
            pytest.assume(fy_lb[0] == '操作成功')
            pytest.assume(fy_lb[2]["chargeStatus"] == "status_check_all_completed")  # 断言订单费用状态已整审

        '''应付费用改单+改单审核'''
        with allure.step("应付费用改单+改单审核>应付费用列表订单id，订单:{}".format(dd_hao)):
            lb_xx = ict.Test_Added01().test_Added0094(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(lb_xx[0] == '操作成功')
            yszd_id = lb_xx[2]["id"]
            cp_hao = lb_xx[2]["mainlandLicensePlateNumber"]
        with allure.step("应付费用改单+改单审核查询费用项档案"):
            fy_dd = ict.Test_Added01().test_Added0143()
            assert fy_dd[0] == '操作成功'
            fy_dw = fy_dd[1]
            fy_id = fy_dd[2]
            fy_lx = fy_dd[3]
        with allure.step("应付费用改单+改单审核查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("应付费用改单+改单审核新增应收改单提交"):
            xx_gd = ict.Test_Added01().test_Added0155(dd_hao=dd_hao, hz_id=hz_id, dd_id=yszd_id, fy_id=fy_id,
                                                      fy_lx=fy_lx, fy_dw=fy_dw, gdlx=1,gys_id=gys_id,cp_hao=cp_hao)
            assert xx_gd == '操作成功'
        with allure.step("应付费用改单+改单审核应付改单列表查询，获取改单ID"):
            gd_lb = ict.Test_Added01().test_Added0097(dd_hao=dd_hao)
            assert gd_lb[0] == '操作成功'
            gd_id = gd_lb[1][0]["id"]

        with allure.step("应付费用改单+改单审核改单审核,订单号：{}".format(dd_hao)):
            gd_sh = ict.Test_Added01().test_Added0099(gd_id=gd_id)
            assert gd_sh == '操作成功'
        with allure.step("应付费用改单+改单审核改单列表查询，获取改单状态"):
            gd_lb = ict.Test_Added01().test_Added0097(dd_hao=dd_hao)
            assert gd_lb[0] == '操作成功'
            gd_zt = gd_lb[1][0]["statusType"]
            pytest.assume(gd_zt == "status_check_completed")

        '''取消订单'''
        with allure.step("取消订单>查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
        with allure.step("取消订单>调度管理》撤销派车"):
            cx_pc = ict.Test_Added01().test_Added0156(dd_id=dd_id)
            assert cx_pc == '操作成功'
        with allure.step("取消订单>计划管理，分单查询"):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("撤销分单,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("取消订单>集装箱运输》取消订单，订单号：{}".format(dd_hao)):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=dd_xx[6]["id"])
            assert qx_dd == '操作成功'

@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景六 集装箱进口')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso5():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景六 集装箱进口（测试点：派自有车+通改+改派供应商+供应商手工报价）")
    def test_business_scenario001(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]  # 货主联系人id
            lxr_name = lxr_name1[3]  # 货主联系人名称
            lxr_hm = lxr_name1[4]  # 货主联系人号码
        with allure.step("港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]  # 港口id
        with allure.step("获取发货地省编码"):
            sf_bm = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm[0] == '操作成功'
            sf_bm = sf_bm[1]
        with allure.step("获取发货地市编码"):
            cs_bm = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm[0] == '操作成功'
            cs_bm = cs_bm[1]
        with allure.step("获取发货地区编码"):
            q_bm = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm[0] == '操作成功'
            q_bm = q_bm[1]
        with allure.step("获取发货地街道编码"):
            jd_bm = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm[0] == '操作成功'
            jd_bm = jd_bm[1]
        with allure.step("获取装货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            zhdw_id = sfh_dd[1]  # 装货单位id
            zhdw_name = sfh_dd[2]  # 装货单位名称
            zhdw_lxr = sfh_dd[3]  # 装货联系人
            zhdw_xlrdh = sfh_dd[4]  # 装货联系电话
            zhdw_xxdz = sfh_dd[5]  # 装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 = time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 = time1[5]  # +50天  年月日
            time7 = time1[6]  # +100天  年月日
            time8 = time1[7]  # +200天  年月日
            time9 = time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  # 订舱号
        with allure.step("集装箱进口运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0159(taskUnitCode="port_container_import_transport",
                                                        customerId=hz_id,
                                                        transportPort=gk_id, provinces=sf_bm, city=cs_bm, area=q_bm,
                                                        street=jd_bm, consigneeConsignorId=zhdw_id, pickupTime=time2,
                                                        carModeId="20GP")
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("新增集装箱进口订单"):
            xzjzx_ck = ict.Test_Added01().test_Added02102(customerId=hz_id, customerContact=lxr_name,
                                                          customerContactPhone=lxr_hm,
                                                          customerServiceId=kf_id, transportPort=gk_id,
                                                          departureProvinces=sf_bm, departureCity=cs_bm,
                                                          departureArea=q_bm,
                                                          departure=jd_bm, cyCutOffTime=time3, consignorId=zhdw_id,
                                                          consignorName=zhdw_name, consignorContact=zhdw_lxr,
                                                          consignorContactPhone=zhdw_xlrdh,
                                                          consignorContactAddr=zhdw_xxdz, provinces=sf_bm, city=cs_bm,
                                                          district=q_bm,
                                                          street=jd_bm, pickupTime=time2, bookingNumber=SSS,
                                                          customerDelegateCode=time9, baseAmount=bjd_je, price=bjd_je,
                                                          customerPricePropertyId=bjd_id, matchKey=jd_bm)
            assert xzjzx_ck == '操作成功'
        with allure.step("查询新增集装箱进口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'


        '''集装箱进口通改'''
        with allure.step("查询集装箱进口运输订单信息{}".format(dd_xx[3])):
            dd_hao = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_hao[0] == '操作成功'
            id = dd_hao[1][0]["id"]
            pytest.assume(dd_hao[1][0]["orderStatus"] == "status_execution")
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 = time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 = time1[5]  # +50天  年月日
            time7 = time1[6]  # +100天  年月日
            time8 = time1[7]  # +200天  年月日
            time9 = time1[8]  # 按时间年月日时分秒生成数组-客户委托号
        with allure.step("集装箱运输》查看订单详情页，货主：{},{}".format(cf.hz_name,id)):
            dd_xx = ict.Test_Added01().test_Added0162(dd_id=id)
            assert dd_xx[0] == '操作成功'
            data1 = dd_xx[1]
            dd_hao = dd_xx[1]["baseInfo"]["orderNumber"]
            dd_id =  dd_xx[1]["baseInfo"]["id"]
            baseInfo = data1["baseInfo"]
            addrList = data1["addrList"]
            costList = data1["costList"]
            goodsList = data1["goodsList"]
            priceList = data1["priceList"]
            baseInfo.update([('orderStatus','status_execution'),("customerDelegateCode",time9)]) #修改状态+客户委托号
            data = {"baseInfo":baseInfo,"addrList":addrList,"costList":costList,"goodsList":goodsList,"priceList":priceList}
            # print(str(data))
        with allure.step("修改订单，订单号：{}".format(dd_hao)):
            dd_xg = ict.Test_Added01().test_Added0160(data1=data,id=dd_id)
            assert dd_xg == '操作成功'
        with allure.step("查询集装箱进口运输订单状态"):
            dd_zt = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode="")
            assert dd_zt[0] == '操作成功'
            pytest.assume(dd_zt[1][0]["orderStatus"] == "status_edit_handling_awaiting")
        with allure.step("查询计划管理》集装箱出现修改申请标识"):
            jx_gl = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert jx_gl[0] == '操作成功'
        with allure.step("获取改单详情页信息"):
            gd_xx = ict.Test_Added01().test_Added0164(dd_id=dd_id)
            assert gd_xx[3] == '操作成功'
            baseInfo1 = ict.get_k(gd_xx[1]['baseInfo'])
            addrList1 = ict.get_k(gd_xx[1]['addrList'][0])
            costList1 = ict.get_k(gd_xx[1]['costList'][0])
            id = gd_xx[2]["id"]
            editType = gd_xx[2]["editType"]
            editRemark = gd_xx[2]["editRemark"]
        with allure.step("审核改单申请"):
            data1 = {"baseInfo":baseInfo1,"addrList":[addrList1],"costList":[costList1]}
            sh_gd = ict.Test_Added01().test_Added0163(dd_hao=dd_hao,data=data1,dd_id=id,editType=editType,editRemark=editRemark,changeList=[])
            assert sh_gd == '操作成功'
        with allure.step("查询计划管理》集装箱出现通改标识"):
            jx_gl = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert jx_gl[0] == '操作成功'
            pytest.assume(jx_gl[2][0]["tags"] == "通改")
        with allure.step("计划管理》通改确认"):
            tg_qr = ict.Test_Added01().test_Added0165(customerOrderId=jx_gl[2][0]["customerOrderId"])
            assert tg_qr == '操作成功'

        '''集装箱出口订单分单管理》分自有车'''
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，分单查询，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("分单，分派自有车,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che=fd_id, gys="", hy_dt="")
                    assert qy_jdzx == '操作成功'

        '''集装箱进口订单派自有车A，撤销派车变更分单，派供应商'''
        with allure.step("查询调度管理集装箱出口运输订单信息,订单号：{}".format(dd_xx[3])):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_import_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id = dd_xx1[1]  # 订单id
            zh_time = dd_xx1[3][0]["pickupTime"]  # 装货时间  年月日时分秒
            cz_qy = dd_xx1[3][0]["operationGroup"]  # 操作区域
            dd_hao = dd_xx1[2]  # 订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')  # 装货时间  年月日
        with allure.step("查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]  # 司机id
            sj_name = xz_sj[4]  # 司机名称
            sj_haoma = xz_sj[5]  # 司机号码
        with allure.step("查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  # 供应商id
            gyl_name = gys_da[4]  # 供应商名称
        with allure.step("查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]  # 车辆id
            cp_hao = sj_da[2]  # 车牌号
            cl_name = sj_da[4]  # 车辆名称
            cz_qy = sj_da[6]  # 操作区域
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤ZZ0001", zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0:
                with allure.step("出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type", cz_qy=cz_qy, tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0:
                with allure.step("出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001", zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'
        with allure.step("获取出车表ID"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id = cc_xx[1]  # 出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_import_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{},".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,
                                                     mainlandLicensePlateNumber=cp_hao,
                                                     orderNumber=dd_hao,pickupTime=zh_time,
                                                     transportType="transport_type_one_one",
                                                     mainlandLicensePlate=cl_id, driverName=sj_name,
                                                     mainlandPhone=sj_haoma, supplierName=gyl_name,
                                                     carDispatchId=ccb_id)
            assert pzyc == '操作成功'
        with allure.step("断言分单渠道"):
            fd_qd = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="port_container_import_transport")
            assert fd_qd[0] == '操作成功'
            pytest.assume("自有运力" == fd_qd[3][0]["distributeChannel"])
            pytest.assume("status_container_awaiting" == fd_qd[3][0]["orderStatus"])
        with allure.step("自有车撤销派单，订单号:{}".format(dd_xx1[2])):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        with allure.step("变更分单，订单号:{}".format(dd_xx1[2])):
            bg_fd = ict.Test_Added01().test_Added0114(dd_id=dd_id,isSubmit=1)
            pytest.assume(bg_fd == '操作成功')


        '''进口订单派供应商A：手工报价'''
        with allure.step("查询调度管理集装箱出口运输订单信息,订单号：{}".format(dd_xx[3])):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_import_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id = dd_xx1[1]  # 订单id
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr =  gys_xx[2]
            gys_lxrdh =  gys_xx[3]
        with allure.step("派供应商A"):
            gys_xx = ict.Test_Added01().test_Added0106(dd_id=dd_id,gys_lxr=gys_lxr,gys_lxrdh=gys_lxrdh,gys_id=gys_id[1],je=2500)
            assert gys_xx == '操作成功'

        '''取消订单'''
        with allure.step("查询集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
        with allure.step("查询调度管理集装箱出口运输订单信息,订单号：{}".format(dd_xx[3])):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_import_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id = dd_xx1[1]  # 订单id
        with allure.step("调度管理》撤销派单/车，订单号：{}".format(dd_xx1[2])):
            cx_pc = ict.Test_Added01().test_Added0156(dd_id=dd_id)
            assert cx_pc == '操作成功'
        with allure.step("计划管理，分单查询，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("撤销分单,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("集装箱运输》取消订单，订单号：{}".format(dd_xx1[2])):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=dd_xx[6]["id"])
            assert qx_dd == '操作成功'
        with allure.step("订单管理》集装箱运输》查看订单状态，订单号：{}".format(dd_xx1[2])):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode="")
            assert jzx_ys[0] == '操作成功'
            assert jzx_ys[1][0]["orderStatus"] == 'status_undo_completed'

@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景七 厢式车多装一卸')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso6():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景七 厢式车多装一卸（测试点：执改+派货源大厅+文件回收+改派自有车+改派供应商）")
    def test_business_scenario001(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]    #货主联系人id
            lxr_name = lxr_name1[3]  #货主联系人名称
            lxr_hm = lxr_name1[4]    #货主联系人号码
        with allure.step("获取卸货地省编码"):
            sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm1[0] == '操作成功'
            xsf_bm = sf_bm1[1]
            xsf_name = sf_bm1[2]
        with allure.step("获取卸货地市编码"):
            cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm1[0] == '操作成功'
            xcs_bm = cs_bm1[1]
            xcs_name = cs_bm1[2]
        with allure.step("获取卸货地区编码"):
            q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm1[0] == '操作成功'
            xq_bm = q_bm1[1]
            xq_name = q_bm1[2]
        with allure.step("获取卸货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm1[0] == '操作成功'
            xjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]

        with allure.step("获取装货地省编码"):
            sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
            assert sf_bm1[0] == '操作成功'
            zsf_bm = sf_bm1[1]
            zsf_name = sf_bm1[2]
        with allure.step("获取装货地市编码"):
            cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
            assert cs_bm1[0] == '操作成功'
            zcs_bm = cs_bm1[1]
            zcs_name = cs_bm1[2]
        with allure.step("获取装货地区编码"):
            q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
            assert q_bm1[0] == '操作成功'
            zq_bm = q_bm1[1]
            zq_name = q_bm1[2]
        with allure.step("获取装货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
            assert jd_bm1[0] == '操作成功'
            zjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]


        with allure.step("获取装货单位1档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="厢式车装货地址1")
            assert sfh_dd[0] == '操作成功'
            zhdw1_id = sfh_dd[1]         #装货单位id
            zhdw1_name = sfh_dd[2]       #装货单位名称
            zhdw1_lxr =  sfh_dd[3]       #装货联系人
            zhdw1_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw1_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取装货单位2档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="厢式车装货地址2")
            assert sfh_dd[0] == '操作成功'
            zhdw2_id = sfh_dd[1]         #装货单位id
            zhdw2_name = sfh_dd[2]       #装货单位名称
            zhdw2_lxr =  sfh_dd[3]       #装货联系人
            zhdw2_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw2_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取卸货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            xhdw_id = sfh_dd[1]         #装货单位id
            xhdw_name = sfh_dd[2]       #装货单位名称
            xhdw_lxr =  sfh_dd[3]       #装货联系人
            xhdw_xlrdh = sfh_dd[4]      #装货联系电话
            xhdw_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 =time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 =time1[5]  # +50天  年月日
            time7 =time1[6]  # +100天  年月日
            time8 =time1[7]  # +200天  年月日
            time9 =time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  #订舱号
        with allure.step("厢式车运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0102(customerId=hz_id,provinces=xsf_bm,city=xcs_bm,area=xq_bm,street=xjd_bm,provinces1=zsf_bm,city1=zcs_bm,area1=zq_bm,street1=zjd_bm,consigneeConsignorId1=zhdw1_id,consigneeConsignorId2=zhdw2_id)
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("新增厢式车运输"):
            xz_xsc =  ict.Test_Added01().test_Added02101(customerId=hz_id,customerContact=lxr_name,customerContactPhone=lxr_hm,customerServiceId=kf_id,consigneeId=xhdw_id,consigneeName=xhdw_name,consigneeContact=xhdw_lxr,
                        consigneeContactPhone=xhdw_xlrdh,consigneeContactAddr=xhdw_xxdz,xh_sf=xsf_bm,xh_cs=xcs_bm,xh_q=xq_bm,xh_jd=xjd_bm,zh_sf=zsf_bm,zh_cs=zcs_bm,zh_q=zq_bm,zh_jd=zjd_bm,zh_dz1id=zhdw1_id,zh_dz1name=zhdw1_name,zh_dz1lxr=zhdw1_lxr,
                        zh_dz1lxrdh=zhdw1_xlrdh,zh_dz1=zhdw1_xxdz,zh_dz2id=zhdw2_id,zh_dz2name=zhdw2_name,zh_dz2lxr=zhdw2_lxr,zh_dz2lxrdh=zhdw2_xlrdh,zh_dz2=zhdw2_xxdz,zh_time=time2,jc_time=time3,bj_je=bjd_je,bj_id=bjd_id,kh_hao=time9)
            assert xz_xsc == '操作成功'
        with allure.step("查询新增厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            dd_hao = dd_xx[3]
            orde_id = dd_xx[6]["id"]

        '''厢式车执改'''
        with allure.step("厢式车执改>查询厢式车订单信息"):
            dd_hao = ict.Test_Added01().test_Added0168(orderNumber=dd_hao)
            assert dd_hao[0] == '操作成功'
            id = dd_hao[1][0]["id"]
            pytest.assume(dd_hao[1][0]["orderStatus"] == "status_execution")
        with allure.step("厢式车执改>获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 = time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 = time1[5]  # +50天  年月日
            time7 = time1[6]  # +100天  年月日
            time8 = time1[7]  # +200天  年月日
            time9 = time1[8]  # 按时间年月日时分秒生成数组-客户委托号
        with allure.step("厢式车执改>查看订单详情页，货主：{},{}".format(cf.hz_name,id)):
            dd_xx = ict.Test_Added01().test_Added0162(dd_id=id)
            assert dd_xx[0] == '操作成功'
            data1 = dd_xx[1]
            dd_hao = dd_xx[1]["baseInfo"]["orderNumber"]
            dd_id =  dd_xx[1]["baseInfo"]["id"]
            baseInfo = data1["baseInfo"]
            addrList = data1["addrList"]
            costList = data1["costList"]
            goodsList = data1["goodsList"]
            priceList = data1["priceList"]
            baseInfo.update([('orderStatus','status_execution'),("carModeId",'10T')]) #修改状态+车型
            data = {"baseInfo":baseInfo,"addrList":addrList,"costList":costList,"goodsList":goodsList,"priceList":priceList}
            # print(str(data))
        with allure.step("厢式车执改>修改订单，订单号：{}".format(dd_hao)):
            dd_xg = ict.Test_Added01().test_Added0160(data1=data,id=dd_id)
            assert dd_xg == '操作成功'
        with allure.step("厢式车执改>查询厢式车运输列表订单状态"):
            dd_zt = ict.Test_Added01().test_Added0168(orderNumber=dd_hao)
            assert dd_zt[0] == '操作成功'
            pytest.assume(dd_zt[1][0]["orderStatus"] == "status_edit_handling_awaiting") #订单状态修改待处理
        with allure.step("厢式车执改>获取改单详情页信息"):
            gd_xx = ict.Test_Added01().test_Added0164(dd_id=dd_id)
            assert gd_xx[3] == '操作成功'
            baseInfo1 = ict.get_k(gd_xx[1]['baseInfo'])
            addrList1 = ict.get_k(gd_xx[1]['addrList'][0])
            costList1 = ict.get_k(gd_xx[1]['costList'][0])
            id = gd_xx[2]["id"]
            editType = gd_xx[2]["editType"]
            editRemark = gd_xx[2]["editRemark"]
        with allure.step("厢式车执改>审核改单申请"):
            data1 = {"baseInfo":baseInfo1,"addrList":[addrList1],"costList":[costList1]}
            sh_gd = ict.Test_Added01().test_Added0163(dd_hao=dd_hao,data=data1,dd_id=id,editType=editType,editRemark=editRemark,changeList=[])
            assert sh_gd == '操作成功'
        with allure.step("厢式车执改>查询计划管理》出现通改标识"):
            jx_gl = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert jx_gl[0] == '操作成功'
            pytest.assume(jx_gl[2][0]["tags"] == "执改")
        with allure.step("厢式车执改>计划管理》通改确认"):
            tg_qr = ict.Test_Added01().test_Added0165(customerOrderId=jx_gl[2][0]["customerOrderId"])
            assert tg_qr == '操作成功'


        '''厢式车订单分单管理》分货源大厅，发布抢单'''
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 1
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>分单，分派供应商,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che="", gys="", hy_dt=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>查询货源大厅订单状态"):
            hy_dt = ict.Test_Added01().test_Added0171(dd_hao=dd_hao)
            assert hy_dt[0] == '操作成功'
            pytest.assume(hy_dt[1]== 1 ) #订单是否存在
            pytest.assume(hy_dt[2][0]["orderStatus"] == "status_waiting_dispatch") #运单状态= 待派单
            pytest.assume(hy_dt[2][0]["cargoShowStatus"] == "status_send_awaiting") #订单状态=待发布
            dd_id = hy_dt[2][0]["id"]
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[10]  # +今天今时 年月日时分秒
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>货源大厅抢单发布"):
            qd_fb = ict.Test_Added01().test_Added0172(dd_id=dd_id,sendStartTime=time2)
            assert qd_fb == '操作成功'
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>查询货源大厅订单状态"):
            hy_dt = ict.Test_Added01().test_Added0171(dd_hao=dd_hao)
            assert hy_dt[0] == '操作成功'
            pytest.assume(hy_dt[2][0]["cargoShowStatus"] == "status_send_completed") #订单状态=已发送
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>货源大厅撤销发布"):
            cx_fb = ict.Test_Added01().test_Added0173(dd_id=dd_id)
            assert cx_fb == '操作成功'
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>查询货源大厅订单状态"):
            hy_dt = ict.Test_Added01().test_Added0171(dd_hao=dd_hao)
            assert hy_dt[0] == '操作成功'
            pytest.assume(hy_dt[2][0]["cargoShowStatus"] == "status_send_cancel") #订单状态=已撤销发布
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>货源大厅回退计划管理"):
            ht_jh = ict.Test_Added01().test_Added0174(dd_id=dd_id)
            assert ht_jh == '操作成功'
        with allure.step("厢式车订单分单管理》分货源大厅，发布抢单>计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            dd_zt = fd_xx[2][0]["orderStatus"]
            pytest.assume(dd_zt == "status_waiting_distribute") #订单状态=待分单

        '''厢式车订单分单管理》分供应商'''
        with allure.step("厢式车订单分单管理》分供应商>计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 1
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("厢式车订单分单管理》分供应商>分单，分派供应商,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che=fd_id, gys="", hy_dt="")
                    assert qy_jdzx == '操作成功'

        '''派自有车A，撤销派车变更分单，派供应商'''
        with allure.step("派自有车A，撤销派车变更分单，派供应商>查询调度管理订单信息,订单号：{}".format(dd_hao)):
            dd_xx1 = ict.Test_Added01().test_Added0175(dd_hao=dd_hao,ht_host=ht_host,token=ht_token)
            assert dd_xx1[0] == '操作成功'
            dd_id = dd_xx1[1]  # 订单id
            zh_time = dd_xx1[3][0]["pickupTime"]  # 装货时间  年月日时分秒
            cz_qy = dd_xx1[3][0]["operationGroup"]  # 操作区域
            dd_hao = dd_xx1[2]  # 订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')  # 装货时间  年月日
        with allure.step("派自有车A，撤销派车变更分单，派供应商>查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]  # 司机id
            sj_name = xz_sj[4]  # 司机名称
            sj_haoma = xz_sj[5]  # 司机号码
        with allure.step("派自有车A，撤销派车变更分单，派供应商>查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  # 供应商id
            gyl_name = gys_da[4]  # 供应商名称
        with allure.step("派自有车A，撤销派车变更分单，派供应商>查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]  # 车辆id
            cp_hao = sj_da[2]  # 车牌号
            cl_name = sj_da[4]  # 车辆名称
            cz_qy = sj_da[6]  # 操作区域
        with allure.step("派自有车A，撤销派车变更分单，派供应商>维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id,cp_hao="粤ZZ0001", zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0:
                with allure.step("派自有车A，撤销派车变更分单，派供应商>出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type", cz_qy=cz_qy, tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0:
                with allure.step("派自有车A，撤销派车变更分单，派供应商>出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001", zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'
        with allure.step("派自有车A，撤销派车变更分单，派供应商>获取出车表ID"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id = cc_xx[1]  # 出车表ID
        with allure.step("派自有车A，撤销派车变更分单，派供应商>调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_import_transport")
            assert bz_dd1[0] == '操作成功'
        with allure.step("派自有车A，撤销派车变更分单，派供应商>调度管理，派自有车，订单号：{},".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,
                                                     mainlandLicensePlateNumber=cp_hao,
                                                     orderNumber=dd_hao,pickupTime=zh_time,
                                                     transportType="transport_type_many_one",
                                                     mainlandLicensePlate=cl_id, driverName=sj_name,
                                                     mainlandPhone=sj_haoma, supplierName=gyl_name,
                                                     carDispatchId=ccb_id)
            assert pzyc == '操作成功'
        with allure.step("派自有车A，撤销派车变更分单，派供应商>断言分单渠道"):
            fd_qd = ict.Test_Added01().test_Added0175(dd_hao=dd_hao,ht_host=ht_host,token=ht_token)
            assert fd_qd[0] == '操作成功'
            pytest.assume("自有运力" == fd_qd[3][0]["distributeChannel"])
            pytest.assume("status_node_awaiting" == fd_qd[3][0]["orderStatus"])
        with allure.step("自有车撤销派单，订单号:{}".format(dd_hao)):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        with allure.step("派自有车A，撤销派车变更分单，派供应商>变更分单，订单号:{}".format(dd_hao)):
            bg_fd = ict.Test_Added01().test_Added0114(dd_id=dd_id,isSubmit=1)
            pytest.assume(bg_fd == '操作成功')

        '''厢式车订单派供应商A：手工报价'''
        with allure.step("派自有车A，撤销派车变更分单，派供应商>>计划管理，获取订单ID，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
        with allure.step("派自有车A，撤销派车变更分单，派供应商>查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys2_name)
            assert gys_id[0] == '操作成功'
        with allure.step("派自有车A，撤销派车变更分单，派供应商>查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr =  gys_xx[2]
            gys_lxrdh =  gys_xx[3]
        with allure.step("派自有车A，撤销派车变更分单，派供应商>派供应商A"):
            gys_xx = ict.Test_Added01().test_Added0106(dd_id=dd_id,gys_lxr=gys_lxr,gys_lxrdh=gys_lxrdh,gys_id=gys_id[1],je=2500)
            assert gys_xx == '操作成功'

        '''厢式车文件管理》回收文件'''
        with allure.step("厢式车文件管理》回收文件>计划管理，获取订单ID，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
            dd_hao =  fd_xx[2][0]["orderNumber"]
        with allure.step("厢式车文件管理》回收文件>文件管理》查询订单状态，订单号{}".format(dd_hao)):
            dd_info = ict.Test_Added01().test_Added0180(dd_hao=dd_hao)
            assert dd_info[0] == "操作成功"
            pytest.assume("file_status_un_recycled" == dd_info[1][0]["fileStatus"])  #文件回收状态》待回收
        with allure.step("厢式车文件管理》回收文件>获取图片地址"):
            tu_dz = pz.Common_page().projects_path() + r"\Common\picture\2.02 MB.JPG"  # 图片地址
            # print(tu_dz)
        with allure.step("厢式车文件管理》回收文件>上传图片，获取图片id"):
            tp_id = ict.Test_Added01().test_Added0129(tp_lj=tu_dz)     # 获取图片id
            assert tp_id[1] == "success"
        with allure.step("厢式车文件管理》回收文件>文件管理》上传附件，订单号{}".format(dd_hao)):
            sc_tp = ict.Test_Added01().test_Added0179(dd_id=dd_id,tp_name="2.02 MB.JPG",tp_id=tp_id[0])
            assert sc_tp == "操作成功"
        with allure.step("厢式车文件管理》回收文件>文件管理》确实回收文件，订单号{}".format(dd_hao)):
            qs_hs = ict.Test_Added01().test_Added0181(dd_id=dd_id)
            assert qs_hs == "操作成功"
        with allure.step("厢式车文件管理》回收文件>文件管理》查询订单状态，订单号{}".format(dd_hao)):
            dd_info = ict.Test_Added01().test_Added0180(dd_hao=dd_hao)
            assert dd_info[0] == "操作成功"
            pytest.assume("file_status_pending_review" == dd_info[1][0]["fileStatus"])  #文件回收状态》待审核
        with allure.step("厢式车文件管理》回收文件>文件管理》审核文件，订单号{}".format(dd_hao)):
            sh_wj = ict.Test_Added01().test_Added0182(dd_id=dd_id)
            assert sh_wj == "操作成功"
        with allure.step("厢式车文件管理》回收文件>文件管理》查询订单状态，订单号{}".format(dd_hao)):
            dd_info = ict.Test_Added01().test_Added0180(dd_hao=dd_hao)
            assert dd_info[0] == "操作成功"
            pytest.assume("file_status_done" == dd_info[1][0]["fileStatus"])  #文件回收状态》已审核

        '''取消订单'''
        with allure.step("取消订单>计划管理，获取订单ID，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
        with allure.step("取消订单>调度管理》撤销派单/车，订单号：{}".format(dd_hao)):
            cx_pc = ict.Test_Added01().test_Added0156(dd_id=dd_id)
            assert cx_pc == '操作成功'
        with allure.step("取消订单>计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("取消订单>撤销分单,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("取消订单>集装箱运输》取消订单，订单号：{}".format(dd_hao)):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=orde_id)
            assert qx_dd == '操作成功'
        with allure.step("取消订单>订单管理》集装箱运输》查看订单状态，订单号：{}".format(dd_hao)):
            jzx_ys = ict.Test_Added01().test_Added0168(orderNumber=dd_hao)
            assert jzx_ys[0] == '操作成功'
            assert jzx_ys[1][0]["orderStatus"] == 'status_undo_completed'

@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景八 危险品出口')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso7():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景八 危险品出口（测试点：订单自动分单派单+海事报关自动派单+海事申报自动派供应商,派自有车无报价，派货源大厅无报价）")
    def test_business_scenario001(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]  # 货主联系人id
            lxr_name = lxr_name1[3]  # 货主联系人名称
            lxr_hm = lxr_name1[4]  # 货主联系人号码
        with allure.step("港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]  # 港口id
        with allure.step("提柜还柜港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="盐田港")
            assert gk_id1[0] == '操作成功'
            zxgk_id = gk_id1[1]  # 港口id
        with allure.step("获取发货地省编码"):
            sf_bm = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm[0] == '操作成功'
            sf_bm = sf_bm[1]
        with allure.step("获取发货地市编码"):
            cs_bm = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm[0] == '操作成功'
            cs_bm = cs_bm[1]
        with allure.step("获取发货地区编码"):
            q_bm = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm[0] == '操作成功'
            q_bm = q_bm[1]
        with allure.step("获取发货地街道编码"):
            jd_bm = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm[0] == '操作成功'
            jd_bm = jd_bm[1]
        with allure.step("获取装货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            zhdw_id = sfh_dd[1]  # 装货单位id
            zhdw_name = sfh_dd[2]  # 装货单位名称
            zhdw_lxr = sfh_dd[3]  # 装货联系人
            zhdw_xlrdh = sfh_dd[4]  # 装货联系电话
            zhdw_xxdz = sfh_dd[5]  # 装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 = time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 = time1[5]  # +50天  年月日
            time7 = time1[6]  # +100天  年月日
            time8 = time1[7]  # +200天  年月日
            time9 = time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  # 订舱号
        with allure.step("集装箱进口运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0055(taskUnitCode="dangerous_cargo_export_transport",
                                                        customerId=hz_id,
                                                        transportPort=gk_id, provinces=sf_bm, city=cs_bm, area=q_bm,
                                                        street=jd_bm, consigneeConsignorId=zhdw_id, pickupTime=time2,
                                                        carModeId="20GP")
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("新增危险品出口订单"):
            xzjzx_ck = ict.Test_Added01().test_Added02103(customerId=hz_id, customerContact=lxr_name,
                                                          customerContactPhone=lxr_hm,
                                                          customerServiceId=kf_id, transportPort=gk_id,
                                                          cyCutOffTime=time3,isCustoms=1, customsType="Customs_Type_002",marineApplyType="marine_type_haige",
                                                          consignorId=zhdw_id,
                                                          consignorName=zhdw_name, consignorContact=zhdw_lxr,
                                                          consignorContactPhone=zhdw_xlrdh,
                                                          consignorContactAddr=zhdw_xxdz, provinces=sf_bm, city=cs_bm,
                                                          district=q_bm,
                                                          street=jd_bm, pickupTime=time2, bookingNumber=SSS,
                                                          customerDelegateCode=time9,pickupContainer=zxgk_id,price=bjd_je,customerPricePropertyId=bjd_id)
            assert xzjzx_ck == '操作成功'
        with allure.step("查询新增危险品出口订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            dd_hao = dd_xx[3]
            orde_id = dd_xx[6]["id"]

        '''录入柜号，报关订单自动派单，订单撤销派供应商'''
        with allure.step("录入柜号，报关订单自动派单，订单撤销派供应商>查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="dangerous_cargo_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[3][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[3][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[2]    #订单号
        with allure.step("录入柜号，报关订单自动派单，订单撤销派供应商>手动录入柜号，订单:{}".format(dd_hao)):
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            g_hao = ict.Test_Added01().test_Added0089(x_hao=x_hao,kg_z=kg_z,dd_id=dd_id,ft_hao=ft_hao)
            pytest.assume(g_hao == '操作成功')
        with allure.step("录入柜号，报关订单自动派单，订单撤销派供应商>跟踪管理查看柜号"):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="dangerous_cargo_export_transport")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
        with allure.step("录入柜号，报关订单自动派单，订单撤销派供应商>查询危险品出口自动派报关订单,自动派单成功"):
            zd_bg = ict.Test_Added01().test_Added0119(dd_hao=dd_hao)
            assert zd_bg[0] == '操作成功'
            # pytest.assume(zd_bg[1][0]["orderStatus"] == "status_pending")  #报关订单状态=已派单  计划8.4上生产
            pytest.assume(zd_bg[1][0]["orderStatus"] == "status_completed_dispatch")  #报关订单状态=已派单  生产环境
        with allure.step("查询危险品出口，自动分单供应商成功，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            fd_id = fd_xx[2][0]["id"]
            pytest.assume(fd_xx[2][0]["distributeChannel"] == "供应商")  #分单渠道=供应商
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="dangerous_cargo_export_transport")
            assert dd_xx1[0] == '操作成功'
            pytest.assume(dd_xx1[3][0]["orderStatus"] == "status_pending")  #运单订单状态=待派单
            # print("这个是运单状态{}".format(dd_xx1[3][0]["orderStatus"]))

        with allure.step("调度管理》撤销派单/车，订单号：{}".format(dd_hao)):
            cx_pc = ict.Test_Added01().test_Added0156(dd_id=fd_id)
            assert cx_pc == '操作成功'
        with allure.step("撤销分单,分单号：{}".format(dd_hao)):
            qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
            assert qy_jdzx == '操作成功'




        '''集装箱出口订单派自有车A，无报价'''
        with allure.step("集装箱出口订单派自有车A，无报价>计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            fd_id = fd_xx[2][0]["id"]
        with allure.step("集装箱出口订单派自有车A，无报价>分单，分派自有车,订单号：{}".format(dd_hao)):
            qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che=fd_id, gys="", hy_dt="")
            assert qy_jdzx == '操作成功'
        with allure.step("集装箱出口订单派自有车A，无报价>查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_hao,lx="dangerous_cargo_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[3][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[3][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[2]    #订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')   #装货时间  年月日

        with allure.step("集装箱出口订单派自有车A，无报价>查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]   #司机id
            sj_name = xz_sj[4]   #司机名称
            sj_haoma = xz_sj[5]   #司机号码
        with allure.step("集装箱出口订单派自有车A，无报价>查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("集装箱出口订单派自有车A，无报价>查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]   #车辆id
            cp_hao = sj_da[2]    #车牌号
            cl_name = sj_da[4]  #车辆名称
            cz_qy = sj_da[6]    # 操作区域
        with allure.step("集装箱出口订单派自有车A，无报价>维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0 :
                with allure.step("集装箱出口订单派自有车A，无报价>出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type",cz_qy=cz_qy,tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0 :
                with allure.step("集装箱出口订单派自有车A，无报价>出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤ZZ0001",zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'
        with allure.step("集装箱出口订单派自有车A，无报价>维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("集装箱出口订单派自有车A，无报价>调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="dangerous_cargo_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []



        with allure.step("查看厢式车自有司机报价单是否存在"):
            bz_dd1 = ict.Test_Added01().test_Added0076(fw_lx="dangerous_cargo_export_transport")
            assert bz_dd1[0] == '操作成功'
            if  bz_dd1[1] == 0 :
                pass
            if bz_dd1[1] != 0:
                status = bz_dd1[2][0]["statusType"]
                quotation_id = bz_dd1[2][0]["id"]
                if status == "status_type_enabled" :
                    with allure.step("存在启用的危险品出口自有车报价单，禁用报价单"):
                        forbidden =   ict.Test_Added01().test_Added0006(bjd_id =quotation_id)
                        assert forbidden == '操作成功'
        with allure.step("集装箱出口订单派自有车A，无报价>调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="dangerous_cargo_export_transport",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            # print("这个是无报价报错{}".format(pzyc))
            assert pzyc == '{}:未匹配到报价'.format(dd_hao)

        with allure.step("集装箱出口订单派自有车A，无报价>撤销分单,分单号：{}".format(dd_hao)):
            qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=dd_id)
            assert qy_jdzx == '操作成功'

        '''集装箱出口订单派货源大厅无报价'''
        with allure.step("集装箱出口订单派货源大厅无报价>计划管理，分单查询，订单号：{}".format(dd_hao)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_hao)
            assert fd_xx[0] == '操作成功'
            fd_id = fd_xx[2][0]["id"]

        with allure.step("集装箱出口订单派货源大厅无报价>分单，分派自有车,订单号：{}".format(dd_hao)):
            qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che="", gys="", hy_dt=fd_id)
            assert qy_jdzx == '获取报价信息异常[没有获取到任何市场报价]'

        with allure.step("取消订单>集装箱运输》取消订单，订单号：{}".format(dd_hao)):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=orde_id)
            assert qx_dd == '操作成功'
        with allure.step("取消订单>订单管理》集装箱运输》查看订单状态，订单号：{}".format(dd_hao)):
            dd_hao = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode="")
            assert dd_hao[0] == '操作成功'
            assert dd_hao[1][0]["orderStatus"] == 'status_undo_completed'

'''后台查询接口'''
@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景九,后台查询接口')
# @pytest.mark.skip(reason="无理由跳过")
class Test_query01():
    '''大类'''
    def setup_class(self):
        '''大类前置'''
        pass
    def teardown_class(self):
        '''大类后置'''
        pass
    # def setup(self):
    #     '''方法的前置'''
    #     pass
    # def teardown(self):
    #     '''方法的后置'''
    #     pass

    @allure.title("后台工作看板》客户数据")   #类方法的注释
    def test_query001(self):
        '''用例描述'''
        with allure.step("后台工作看板客户数据获取操作成功"):
            cf=ict.Test_query01().test_query001()
            allure.attach(body=cf[1], name="请求地址", attachment_type=allure.attachment_type.TEXT)
            # allure.attach(body=cf[2], name="请求头", attachment_type=allure.attachment_type.TEXT)
            assert cf[0] =='操作成功'
    @allure.title("后台工作看板》供应商数据")   #类方法的注释
    def test_query002(self):
        '''用例描述'''
        with allure.step("后台工作看板供应商数据获取操作成功"):
            cf=ict.Test_query01().test_query002()
            assert cf =='操作成功'
    @allure.title("后台工作看板》个体司机数据")   #类方法的注释
    def test_query003(self):
        '''用例描述'''
        with allure.step("后台工作看板个体司机数据获取操作成功"):
            cf=ict.Test_query01().test_query003()
            assert cf =='操作成功'
    @allure.title("后台工作看板》客户结算方式数据")   #类方法的注释
    def test_query004(self):
        '''用例描述'''
        with allure.step("后台工作看板客户结算方式数据获取操作成功"):
            cf=ict.Test_query01().test_query004()
            assert cf =='操作成功'
    @allure.title("后台工作看板》平台管理数据")   #类方法的注释
    def test_query005(self):
        '''用例描述'''
        with allure.step("后台工作看板平台管理数据获取操作成功"):
            cf=ict.Test_query01().test_query005()
            assert cf =='操作成功'
    @allure.title("后台工作看板》坪山项目日报表")   #类方法的注释
    def test_query006(self):
        '''用例描述'''
        with allure.step("后台工作看板坪山项目日报表数据获取操作成功"):
            cf=ict.Test_query01().test_query006()
            assert cf =='操作成功'
    @allure.title("后台工作看板》订单录入查询》危险品出口")   #类方法的注释
    def test_query007(self):
        '''用例描述'''
        with allure.step("后台订单录入查询获取"):
            cf=ict.Test_query01().test_query007()
            assert cf =='操作成功'
    @allure.title("后台工作看板》集装箱运输查询")  # 类方法的注释
    def test_query008(self):
        '''用例描述'''
        with allure.step("集装箱运输查询"):
            cf = ict.Test_query01().test_query008()
            assert cf == '操作成功'
    @allure.title("后台工作看板》厢式车运输查询")  # 类方法的注释
    def test_query009(self):
        '''用例描述'''
        with allure.step("厢式车运输查询"):
            cf = ict.Test_query01().test_query009()
            assert cf == '操作成功'
    @allure.title("后台配载计划》查询")  # 类方法的注释
    def test_query010(self):
        '''用例描述'''
        with allure.step("后台配载计划查询"):
            cf = ict.Test_query01().test_query010()
            assert cf == '操作成功'
    @allure.title("后台运单管理》计划管理集装箱查询")  # 类方法的注释
    def test_query011(self):
        '''用例描述'''
        with allure.step("计划管理集装箱查询"):
            cf = ict.Test_query01().test_query011()
            assert cf == '操作成功'
    @allure.title("后台运单管理》计划管理厢式车查询")  # 类方法的注释
    def test_query012(self):
        '''用例描述'''
        with allure.step("计划管理厢式车查询"):
            cf = ict.Test_query01().test_query012()
            assert cf == '操作成功'
    @allure.title("后台运单管理》调度管理集装箱查询")  # 类方法的注释
    def test_query013(self):
        '''用例描述'''
        with allure.step("调度管理集装箱查询"):
            cf = ict.Test_query01().test_query013()
            assert cf == '操作成功'
    @allure.title("后台运单管理》调度管理厢式车查询")  # 类方法的注释
    def test_query014(self):
        '''用例描述'''
        with allure.step("调度管理厢式车查询"):
            cf = ict.Test_query01().test_query014()
            assert cf == '操作成功'
    @allure.title("后台运单管理》出车表信息查询")  # 类方法的注释
    def test_query015(self):
        '''用例描述'''
        with allure.step("出车表信息查询"):
            cf = ict.Test_query01().test_query015()
            assert cf == '操作成功'
    @allure.title("后台运单管理》监理管理信息查询")  # 类方法的注释
    def test_query016(self):
        '''用例描述'''
        with allure.step("监理管理信息查询"):
            cf = ict.Test_query01().test_query016()
            assert cf == '操作成功'
    @allure.title("后台运单管理》报关管理信息查询")  # 类方法的注释
    def test_query017(self):
        '''用例描述'''
        with allure.step("报关管理信息查询"):
            cf = ict.Test_query01().test_query017()
            assert cf == '操作成功'
    @allure.title("后台运单管理》路桥费借款表信息查询")  # 类方法的注释
    def test_query018(self):
        '''用例描述'''
        with allure.step("路桥费借款表信息查询"):
            cf = ict.Test_query01().test_query018()
            assert cf == '操作成功'
    @allure.title("后台运单管理》路桥费维护表信息查询")  # 类方法的注释
    def test_query019(self):
        '''用例描述'''
        with allure.step("路桥费维护表信息查询"):
            cf = ict.Test_query01().test_query019()
            assert cf == '操作成功'
    @allure.title("后台跟踪管理》集装箱运输查询")  # 类方法的注释
    def test_query020(self):
        '''用例描述'''
        with allure.step("集装箱运输查询"):
            cf = ict.Test_query01().test_query020()
            assert cf == '操作成功'
    @allure.title("后台跟踪管理》厢式车运输查询")  # 类方法的注释
    def test_query021(self):
        '''用例描述'''
        with allure.step("厢式车运输查询"):
            cf = ict.Test_query01().test_query021()
            assert cf == '操作成功'
    @allure.title("后台跟踪管理》监理管理查询")  # 类方法的注释
    def test_query022(self):
        '''用例描述'''
        with allure.step("监理管理查询"):
            cf = ict.Test_query01().test_query022()
            assert cf == '操作成功'
    @allure.title("后台跟踪管理》报关管理查询")  # 类方法的注释
    def test_query023(self):
        '''用例描述'''
        with allure.step("报关管理查询"):
            cf = ict.Test_query01().test_query023()
            assert cf == '操作成功'
    @allure.title("后台跟踪管理》异常管理查询")  # 类方法的注释
    def test_query024(self):
        '''用例描述'''
        with allure.step("异常管理查询"):
            cf = ict.Test_query01().test_query024()
            assert cf == '操作成功'
    @allure.title("后台文件管理》文件管理查询")  # 类方法的注释
    def test_query025(self):
        '''用例描述'''
        with allure.step("文件管理查询"):
            cf = ict.Test_query01().test_query025()
            assert cf == '操作成功'
    @allure.title("后台货源大厅》货源大厅订单管理查询")  # 类方法的注释
    def test_query026(self):
        '''用例描述'''
        with allure.step("货源大厅订单管理查询"):
            cf = ict.Test_query01().test_query026()
            assert cf == '操作成功'
    @allure.title("应收管理》应收费用制作")  # 类方法的注释
    def test_query027(self):
        '''用例描述'''
        with allure.step("应收费用制作"):
            cf = ict.Test_query02().test_query027()
            assert cf == '操作成功'
    @allure.title("应收管理》应收改单数据获取")  # 类方法的注释
    def test_query028(self):
        '''用例描述'''
        with allure.step("应收改单数据获取"):
            cf = ict.Test_query02().test_query028()
            assert cf == '操作成功'
    @allure.title("应收管理》待生成对账单数据获取")  # 类方法的注释
    def test_query029(self):
        '''用例描述'''
        with allure.step("待生成对账单数据获取"):
            cf = ict.Test_query02().test_query029()
            assert cf == '操作成功'
    @allure.title("应收管理》对账单合计数据获取")  # 类方法的注释
    def test_query030(self):
        '''用例描述'''
        with allure.step("对账单合计数据获取"):
            cf = ict.Test_query02().test_query030()
            assert cf == '操作成功'
    @allure.title("应收管理》应收票结账单")  # 类方法的注释
    def test_query031(self):
        '''用例描述'''
        with allure.step("应收票结账单"):
            cf = ict.Test_query02().test_query031()
            assert cf == '操作成功'
    @allure.title("应收管理》应收月结账单")  # 类方法的注释
    def test_query032(self):
        '''用例描述'''
        with allure.step("应收月结账单"):
            cf = ict.Test_query02().test_query032()
            assert cf == '操作成功'
    @allure.title("应收管理》应收发票管理")  # 类方法的注释
    def test_query033(self):
        '''用例描述'''
        with allure.step("应收发票管理"):
            cf = ict.Test_query02().test_query033()
            assert cf == '操作成功'
    @allure.title("应付管理》应付费用制作查询")  # 类方法的注释
    def test_query034(self):
        '''用例描述'''
        with allure.step("应付费用制作查询"):
            cf = ict.Test_query02().test_query034()
            assert cf == '操作成功'
    @allure.title("应付管理》应付改单查询")  # 类方法的注释
    def test_query035(self):
        '''用例描述'''
        with allure.step("应付改单查询"):
            cf = ict.Test_query02().test_query035()
            assert cf == '操作成功'
    @allure.title("应付管理》应付月结账单查询")  # 类方法的注释
    def test_query036(self):
        '''用例描述'''
        with allure.step("应付月结账单查询"):
            cf = ict.Test_query02().test_query036()
            assert cf == '操作成功'
    @allure.title("认证审核》货主认证审核获取")  # 类方法的注释
    def test_query037(self):
        '''用例描述'''
        with allure.step("货主认证审核获取"):
            cf = ict.Test_query03().test_query037()
            assert cf == '操作成功'
    @allure.title("认证审核》运输公司认证获取")  # 类方法的注释
    def test_query038(self):
        '''用例描述'''
        with allure.step("运输公司认证获取"):
            cf = ict.Test_query03().test_query038()
            assert cf == '操作成功'
    @allure.title("认证审核》个人司机认证获取")  # 类方法的注释
    def test_query039(self):
        '''用例描述'''
        with allure.step("个人司机认证获取"):
            cf = ict.Test_query03().test_query039()
            assert cf == '操作成功'
    @allure.title("认证审核》车老板审核获取")  # 类方法的注释
    def test_query040(self):
        '''用例描述'''
        with allure.step("车老板审核获取"):
            cf = ict.Test_query03().test_query040()
            assert cf == '操作成功'
    @allure.title("认证审核》司机证件变更管理获取")  # 类方法的注释
    def test_query041(self):
        '''用例描述'''
        with allure.step("司机证件变更管理获取"):
            cf = ict.Test_query03().test_query041()
            assert cf == '操作成功'
    @allure.title("认证审核》司机证件监控列表获取")  # 类方法的注释
    def test_query042(self):
        '''用例描述'''
        with allure.step("司机证件监控列表获取"):
            cf = ict.Test_query03().test_query042()
            assert cf == '操作成功'
    @allure.title("认证审核》货主提额管理获取")  # 类方法的注释
    def test_query043(self):
        '''用例描述'''
        with allure.step("货主提额管理获取"):
            cf = ict.Test_query03().test_query043()
            assert cf == '操作成功'
    @allure.title("报价管理》货主市场报价获取")  # 类方法的注释
    def test_query044(self):
        '''用例描述'''
        with allure.step("货主市场报价获取"):
            cf = ict.Test_query03().test_query044()
            assert cf == '操作成功'
    @allure.title("报价管理》司机市场报价获取")  # 类方法的注释
    def test_query045(self):
        '''用例描述'''
        with allure.step("司机市场报价获取"):
            cf = ict.Test_query03().test_query045()
            assert cf == '操作成功'
    @allure.title("报价管理》货主合同报价获取")  # 类方法的注释
    def test_query046(self):
        '''用例描述'''
        with allure.step("货主合同报价获取"):
            cf = ict.Test_query03().test_query046()
            assert cf == '操作成功'
    @allure.title("报价管理》服务类型报价说明")  # 类方法的注释
    def test_query047(self):
        '''用例描述'''
        with allure.step("服务类型报价说明"):
            cf = ict.Test_query03().test_query047()
            assert cf == '操作成功'
    @allure.title("报价管理》服务类型港口报价说明")  # 类方法的注释
    def test_query048(self):
        '''用例描述'''
        with allure.step("服务类型港口报价说明"):
            cf = ict.Test_query03().test_query048()
            assert cf == '操作成功'
    @allure.title("报价管理》职业监理报价获取")  # 类方法的注释
    def test_query049(self):
        '''用例描述'''
        with allure.step("职业监理报价获取"):
            cf = ict.Test_query03().test_query049()
            assert cf == '操作成功'
    @allure.title("报价管理》司机监理报价获取")  # 类方法的注释
    def test_query050(self):
        '''用例描述'''
        with allure.step("司机监理报价获取"):
            cf = ict.Test_query03().test_query050()
            assert cf == '操作成功'
    @allure.title("报价管理》运输公司合同报价获取")  # 类方法的注释
    def test_query051(self):
        '''用例描述'''
        with allure.step("运输公司合同报价获取"):
            cf = ict.Test_query03().test_query051()
            assert cf == '操作成功'
    @allure.title("报价管理》自有司机报价获取")  # 类方法的注释
    def test_query052(self):
        '''用例描述'''
        with allure.step("自有司机报价获取"):
            cf = ict.Test_query03().test_query052()
            assert cf == '操作成功'
    @allure.title("报价管理》附加费获取")  # 类方法的注释
    def test_query053(self):
        '''用例描述'''
        with allure.step("附加费获取"):
            cf = ict.Test_query03().test_query053()
            assert cf == '操作成功'
    @allure.title("智能分析》Excel获取")  # 类方法的注释
    def test_query054(self):
        '''用例描述'''
        with allure.step("Excel获取"):
            cf = ict.Test_query04().test_query054()
            assert cf == '操作成功'
    @allure.title("智能分析》订阅计划获取")  # 类方法的注释
    def test_query055(self):
        '''用例描述'''
        with allure.step("订阅计划获取"):
            cf = ict.Test_query04().test_query055()
            assert cf == '操作成功'
    @allure.title("市场活动》激励卷档案获取")  # 类方法的注释
    def test_query056(self):
        '''用例描述'''
        with allure.step("激励卷档案获取"):
            cf = ict.Test_query05().test_query056()
            assert cf == '操作成功'
    @allure.title("市场活动》营销活动管理获取")  # 类方法的注释
    def test_query057(self):
        '''用例描述'''
        with allure.step("营销活动管理获取"):
            cf = ict.Test_query05().test_query057()
            assert cf == '操作成功'
    @allure.title("市场活动》营销活动分析获取")  # 类方法的注释
    def test_query058(self):
        '''用例描述'''
        with allure.step("营销活动分析获取"):
            cf = ict.Test_query05().test_query058()
            assert cf == '操作成功'
    @allure.title("市场活动》红包每日汇总提现列表获取")  # 类方法的注释
    def test_query059(self):
        '''用例描述'''
        with allure.step("红包每日汇总提现列表获取"):
            cf = ict.Test_query05().test_query059()
            assert cf == '操作成功'
    @allure.title("市场活动》司机收入提现列表获取")  # 类方法的注释
    def test_query060(self):
        '''用例描述'''
        with allure.step("司机收入提现列表获取"):
            cf = ict.Test_query05().test_query060()
            assert cf == '操作成功'
    @allure.title("推广活动》推广活动档案获取")  # 类方法的注释
    def test_query061(self):
        '''用例描述'''
        with allure.step("推广活动档案获取"):
            cf = ict.Test_query05().test_query061()
            assert cf == '操作成功'
    @allure.title("推广活动》推广奖励明细列表获取")  # 类方法的注释
    def test_query062(self):
        '''用例描述'''
        with allure.step("推广奖励明细列表获取"):
            cf = ict.Test_query05().test_query062()
            assert cf == '操作成功'
    @allure.title("推广活动》推广汇总列表获取")  # 类方法的注释
    def test_query063(self):
        '''用例描述'''
        with allure.step("推广汇总列表获取"):
            cf = ict.Test_query05().test_query063()
            assert cf == '操作成功'
    @allure.title("推广活动》推广发放列表获取")  # 类方法的注释
    def test_query064(self):
        '''用例描述'''
        with allure.step("推广发放列表获取"):
            cf = ict.Test_query05().test_query064()
            assert cf == '操作成功'
    @allure.title("接口日志》推送日志获取")  # 类方法的注释
    def test_query065(self):
        '''用例描述'''
        with allure.step("推送日志获取"):
            cf = ict.Test_query06().test_query065()
            assert cf == '操作成功'
    @allure.title("接口日志》接收日志获取")  # 类方法的注释
    def test_query066(self):
        '''用例描述'''
        with allure.step("接收日志获取"):
            cf = ict.Test_query06().test_query066()
            assert cf == '操作成功'
    @allure.title("货主交易日志》充值日志获取")  # 类方法的注释
    def test_query067(self):
        '''用例描述'''
        with allure.step("充值日志获取"):
            cf = ict.Test_query06().test_query067()
            assert cf == '操作成功'
    @allure.title("货主交易日志》提现日志获取")  # 类方法的注释
    def test_query068(self):
        '''用例描述'''
        with allure.step("提现日志获取"):
            cf = ict.Test_query06().test_query068()
            assert cf == '操作成功'
    @allure.title("供应商运单》供应商运单获取")  # 类方法的注释
    def test_query069(self):
        '''用例描述'''
        with allure.step("供应商运单获取"):
            cf = ict.Test_query06().test_query069()
            assert cf == '操作成功'
    @allure.title("跟进管理》操作日志")  # 类方法的注释
    def test_query070(self):
        '''用例描述'''
        with allure.step("操作日志"):
            cf = ict.Test_query06().test_query070()
            assert cf == '操作成功'
    @allure.title("咨询投诉列表")  # 类方法的注释
    def test_query071(self):
        '''用例描述'''
        with allure.step("咨询投诉列表"):
            cf = ict.Test_query06().test_query071()
            assert cf == '操作成功'
    @allure.title("标准档案》系统字典获取")  # 类方法的注释
    def test_query072(self):
        '''用例描述'''
        with allure.step("系统字典获取"):
            cf = ict.Test_query07().test_query072()
            assert cf == '操作成功'
    @allure.title("标准档案》车辆档案获取")  # 类方法的注释
    def test_query073(self):
        '''用例描述'''
        with allure.step("车辆档案获取"):
            cf = ict.Test_query07().test_query073()
            assert cf == '操作成功'
    @allure.title("标准档案》内部档案获取")  # 类方法的注释
    def test_query074(self):
        '''用例描述'''
        with allure.step("内部档案获取"):
            cf = ict.Test_query07().test_query074()
            assert cf == '操作成功'
    @allure.title("系统规则》系统配置获取")  # 类方法的注释
    def test_query075(self):
        '''用例描述'''
        with allure.step("系统配置获取"):
            cf = ict.Test_query07().test_query075()
            assert cf == '操作成功'
    @allure.title("系统规则》邮箱配置获取")  # 类方法的注释
    def test_query076(self):
        '''用例描述'''
        with allure.step("邮箱配置获取"):
            cf = ict.Test_query07().test_query076()
            assert cf == '操作成功'
    @allure.title("系统规则》邮箱接收配置获取")  # 类方法的注释
    def test_query077(self):
        '''用例描述'''
        with allure.step("邮箱接收配置获取"):
            cf = ict.Test_query07().test_query077()
            assert cf == '操作成功'
    @allure.title("系统规则》邮箱接收日志获取")  # 类方法的注释
    def test_query078(self):
        '''用例描述'''
        with allure.step("邮箱接收日志获取"):
            cf = ict.Test_query07().test_query078()
            assert cf == '操作成功'
    @allure.title("系统规则》表单号设置获取")  # 类方法的注释
    def test_query079(self):
        '''用例描述'''
        with allure.step("表单号设置获取"):
            cf = ict.Test_query07().test_query079()
            assert cf == '操作成功'
    @allure.title("系统规则》服务类型节点设置获取")  # 类方法的注释
    def test_query080(self):
        '''用例描述'''
        with allure.step("服务类型节点设置获取"):
            cf = ict.Test_query07().test_query080()
            assert cf == '操作成功'
    @allure.title("系统规则》币种设置获取")  # 类方法的注释
    def test_query081(self):
        '''用例描述'''
        with allure.step("币种设置获取"):
            cf = ict.Test_query07().test_query081()
            assert cf == '操作成功'
    @allure.title("系统规则》Excel配置库获取")  # 类方法的注释
    def test_query082(self):
        '''用例描述'''
        with allure.step("Excel配置库获取"):
            cf = ict.Test_query07().test_query082()
            assert cf == '操作成功'
    @allure.title("系统规则》报表模板设计获取")  # 类方法的注释
    def test_query083(self):
        '''用例描述'''
        with allure.step("报表模板设计获取"):
            cf = ict.Test_query07().test_query083()
            assert cf == '操作成功'
    @allure.title("系统规则》模板制作获取")  # 类方法的注释
    def test_query084(self):
        '''用例描述'''
        with allure.step("模板制作获取"):
            cf = ict.Test_query07().test_query084()
            assert cf == '操作成功'
    @allure.title("系统规则》通知账号配置获取")  # 类方法的注释
    def test_query085(self):
        '''用例描述'''
        with allure.step("通知账号配置获取"):
            cf = ict.Test_query07().test_query085()
            assert cf == '操作成功'
    @allure.title("系统规则》接口接收设置获取")  # 类方法的注释
    def test_query086(self):
        '''用例描述'''
        with allure.step("接口接收设置获取"):
            cf = ict.Test_query07().test_query086()
            assert cf == '操作成功'
    @allure.title("系统规则》接收消息分配获取")  # 类方法的注释
    def test_query087(self):
        '''用例描述'''
        with allure.step("接收消息分配获取"):
            cf = ict.Test_query07().test_query087()
            assert cf == '操作成功'
    @allure.title("系统规则》内容管理获取")  # 类方法的注释
    def test_query088(self):
        '''用例描述'''
        with allure.step("内容管理获取"):
            cf = ict.Test_query07().test_query088()
            assert cf == '操作成功'
    @allure.title("系统规则》短信模板获取")  # 类方法的注释
    def test_query089(self):
        '''用例描述'''
        with allure.step("短信模板获取"):
            cf = ict.Test_query07().test_query089()
            assert cf == '操作成功'
    @allure.title("系统规则》虚拟账号配置获取")  # 类方法的注释
    def test_query090(self):
        '''用例描述'''
        with allure.step("虚拟账号配置获取"):
            cf = ict.Test_query07().test_query090()
            assert cf == '操作成功'
    @allure.title("系统规则》角色权限分配获取")  # 类方法的注释
    def test_query091(self):
        '''用例描述'''
        with allure.step("角色权限分配获取"):
            cf = ict.Test_query07().test_query091()
            assert cf == '操作成功'
    @allure.title("系统规则》用户角色分配获取")  # 类方法的注释
    def test_query092(self):
        '''用例描述'''
        with allure.step("用户角色分配获取"):
            cf = ict.Test_query07().test_query092()
            assert cf == '操作成功'
    @allure.title("系统规则》用户数据权限分配获取")  # 类方法的注释
    def test_query093(self):
        '''用例描述'''
        with allure.step("用户数据权限分配获取"):
            cf = ict.Test_query07().test_query093()
            assert cf == '操作成功'
    @allure.title("用户设置》默认输出模板获取")  # 类方法的注释
    def test_query094(self):
        '''用例描述'''
        with allure.step("默认输出模板获取"):
            cf = ict.Test_query07().test_query094()
            assert cf == '操作成功'
    @allure.title("用户设置》常用输出模板获取")  # 类方法的注释
    def test_query095(self):
        '''用例描述'''
        with allure.step("常用输出模板获取"):
            cf = ict.Test_query07().test_query095()
            assert cf == '操作成功'
    @allure.title("组织档案》组织机构获取")  # 类方法的注释
    def test_query096(self):
        '''用例描述'''
        with allure.step("组织机构获取"):
            cf = ict.Test_query07().test_query096()
            assert cf == 'Success'
    @allure.title("组织档案》用户档案获取")  # 类方法的注释
    def test_query097(self):
        '''用例描述'''
        with allure.step("用户档案获取"):
            cf = ict.Test_query07().test_query097()
            assert cf == '操作成功'
    @allure.title("基础档案》标准汇率获取")  # 类方法的注释
    def test_query098(self):
        '''用例描述'''
        with allure.step("标准汇率获取"):
            cf = ict.Test_query07().test_query098()
            assert cf == '操作成功'
    @allure.title("基础档案》客户汇率获取")  # 类方法的注释
    def test_query099(self):
        '''用例描述'''
        with allure.step("客户汇率获取"):
            cf = ict.Test_query07().test_query099()
            assert cf == '操作成功'
    @allure.title("基础档案》费用项档案获取")  # 类方法的注释
    def test_query100(self):
        '''用例描述'''
        with allure.step("费用项档案获取"):
            cf = ict.Test_query07().test_query100()
            assert cf == '操作成功'
    @allure.title("基础档案》货主档案获取")  # 类方法的注释
    def test_query101(self):
        '''用例描述'''
        with allure.step("货主档案获取"):
            cf = ict.Test_query07().test_query101()
            assert cf == '操作成功'
    @allure.title("基础档案》二级客户获取")  # 类方法的注释
    def test_query102(self):
        '''用例描述'''
        with allure.step("二级客户获取"):
            cf = ict.Test_query07().test_query102()
            assert cf == '操作成功'
    @allure.title("基础档案》收发货人档案获取")  # 类方法的注释
    def test_query103(self):
        '''用例描述'''
        with allure.step("收发货人档案获取"):
            cf = ict.Test_query07().test_query103()
            assert cf == '操作成功'
    @allure.title("基础档案》货主联系人档案获取")  # 类方法的注释
    def test_query104(self):
        '''用例描述'''
        with allure.step("货主联系人档案获取"):
            cf = ict.Test_query07().test_query104()
            assert cf == '操作成功'
    @allure.title("基础档案》对账单发票档案获取")  # 类方法的注释
    def test_query105(self):
        '''用例描述'''
        with allure.step("对账单发票档案获取"):
            cf = ict.Test_query07().test_query105()
            assert cf == '操作成功'
    @allure.title("基础档案》开票档案获取")  # 类方法的注释
    def test_query106(self):
        '''用例描述'''
        with allure.step("开票档案获取"):
            cf = ict.Test_query07().test_query106()
            assert cf == '操作成功'
    @allure.title("基础档案》运输公司档案获取")  # 类方法的注释
    def test_query107(self):
        '''用例描述'''
        with allure.step("运输公司档案获取"):
            cf = ict.Test_query07().test_query107()
            assert cf == '操作成功'
    @allure.title("基础档案》运输公司联系人档案获取")  # 类方法的注释
    def test_query108(self):
        '''用例描述'''
        with allure.step("运输公司联系人档案获取"):
            cf = ict.Test_query07().test_query108()
            assert cf == '操作成功'
    @allure.title("基础档案》车辆档案获取")  # 类方法的注释
    def test_query109(self):
        '''用例描述'''
        with allure.step("车辆档案获取"):
            cf = ict.Test_query07().test_query109()
            assert cf == '操作成功'
    @allure.title("基础档案》司机档案获取")  # 类方法的注释
    def test_query110(self):
        '''用例描述'''
        with allure.step("司机档案获取"):
            cf = ict.Test_query07().test_query110()
            assert cf == '操作成功'
    @allure.title("基础档案》监理档案获取")  # 类方法的注释
    def test_query111(self):
        '''用例描述'''
        with allure.step("监理档案获取"):
            cf = ict.Test_query07().test_query111()
            assert cf == '操作成功'
    @allure.title("基础档案》船公司档案获取")  # 类方法的注释
    def test_query112(self):
        '''用例描述'''
        with allure.step("船公司档案获取"):
            cf = ict.Test_query07().test_query112()
            assert cf == '操作成功'
    @allure.title("基础档案》客服人员分配档案获取")  # 类方法的注释
    def test_query113(self):
        '''用例描述'''
        with allure.step("客服人员分配档案获取"):
            cf = ict.Test_query07().test_query113()
            assert cf == '操作成功'
    @allure.title("基础档案》客户税率档案获取")  # 类方法的注释
    def test_query114(self):
        '''用例描述'''
        with allure.step("客户税率档案获取"):
            cf = ict.Test_query07().test_query114()
            assert cf == '操作成功'
    @allure.title("基础档案》供应商税率档案获取")  # 类方法的注释
    def test_query115(self):
        '''用例描述'''
        with allure.step("供应商税率档案获取"):
            cf = ict.Test_query07().test_query115()
            assert cf == '操作成功'
    @allure.title("基础档案》个体司机税率档案获取")  # 类方法的注释
    def test_query116(self):
        '''用例描述'''
        with allure.step("个体司机税率档案获取"):
            cf = ict.Test_query07().test_query116()
            assert cf == '操作成功'
    @allure.title("基础档案》自有车税率档案获取")  # 类方法的注释
    def test_query117(self):
        '''用例描述'''
        with allure.step("自有车税率档案获取"):
            cf = ict.Test_query07().test_query117()
            assert cf == '操作成功'
    @allure.title("运营策略》装载量策略获取")  # 类方法的注释
    def test_query118(self):
        '''用例描述'''
        with allure.step("装载量策略获取"):
            cf = ict.Test_query07().test_query118()
            assert cf == '操作成功'
    @allure.title("运营策略》通用设置获取")  # 类方法的注释
    def test_query119(self):
        '''用例描述'''
        with allure.step("通用设置获取"):
            cf = ict.Test_query07().test_query119()
            assert cf == '操作成功'
    @allure.title("运营策略》线路范围设置获取")  # 类方法的注释
    def test_query120(self):
        '''用例描述'''
        with allure.step("通用设置获取"):
            cf = ict.Test_query07().test_query120()
            assert cf == '操作成功'
    @allure.title("运营策略》项目管控获取")  # 类方法的注释
    def test_query121(self):
        '''用例描述'''
        with allure.step("项目管控获取"):
            cf = ict.Test_query07().test_query121()
            assert cf == '操作成功'
    @allure.title("运营策略》接单中心获取")  # 类方法的注释
    def test_query122(self):
        '''用例描述'''
        with allure.step("接单中心获取"):
            cf = ict.Test_query07().test_query122()
            assert cf == '操作成功'
    @allure.title("运营策略》计划中心获取")  # 类方法的注释
    def test_query123(self):
        '''用例描述'''
        with allure.step("计划中心获取"):
            cf = ict.Test_query07().test_query123()
            assert cf == '操作成功'
    @allure.title("运营策略》调度中心获取")  # 类方法的注释
    def test_query124(self):
        '''用例描述'''
        with allure.step("调度中心获取"):
            cf = ict.Test_query07().test_query124()
            assert cf == '操作成功'
    @allure.title("运营策略》区域规划获取")  # 类方法的注释
    def test_query125(self):
        '''用例描述'''
        with allure.step("区域规划获取"):
            cf = ict.Test_query07().test_query125()
            assert cf == '操作成功'
    @allure.title("运营策略》应付额外费用审核配置获取")  # 类方法的注释
    def test_query126(self):
        '''用例描述'''
        with allure.step("应付额外费用审核配置获取"):
            cf = ict.Test_query07().test_query126()
            assert cf == '操作成功'
    @allure.title("运营策略》每日产表维护表获取")  # 类方法的注释
    def test_query127(self):
        '''用例描述'''
        with allure.step("每日产表维护表获取"):
            cf = ict.Test_query07().test_query127()
            assert cf == '操作成功'
    @allure.title("运营策略》虚拟产值基础表获取")  # 类方法的注释
    def test_query128(self):
        '''用例描述'''
        with allure.step("虚拟产值基础表获取"):
            cf = ict.Test_query07().test_query128()
            assert cf == '操作成功'
    @allure.title("运营策略》实际产值优惠表获取")  # 类方法的注释
    def test_query129(self):
        '''用例描述'''
        with allure.step("实际产值优惠表获取"):
            cf = ict.Test_query07().test_query129()
            assert cf == '操作成功'
    @allure.title("运营策略》自动分单规则列表获取")  # 类方法的注释
    def test_query130(self):
        '''用例描述'''
        with allure.step("自动分单规则列表获取"):
            cf = ict.Test_query07().test_query130()
            assert cf == '操作成功'
    @allure.title("运营策略》分单渠道份额设置获取")  # 类方法的注释
    def test_query131(self):
        '''用例描述'''
        with allure.step("分单渠道份额设置获取"):
            cf = ict.Test_query07().test_query131()
            assert cf == '操作成功'
    @allure.title("运营策略》客户文件配置管理获取")  # 类方法的注释
    def test_query132(self):
        '''用例描述'''
        with allure.step("客户文件配置管理获取"):
            cf = ict.Test_query07().test_query132()
            assert cf == '操作成功'
    @allure.title("运营策略》待办预警阈值获取")  # 类方法的注释
    def test_query133(self):
        '''用例描述'''
        with allure.step("待办预警阈值获取"):
            cf = ict.Test_query07().test_query133()
            assert cf == '操作成功'
    @allure.title("运营策略》拆子任务规则获取")  # 类方法的注释
    def test_query134(self):
        '''用例描述'''
        with allure.step("拆子任务规则获取"):
            cf = ict.Test_query07().test_query134()
            assert cf == '操作成功'
    @allure.title("消息》系统消息》发信箱获取")  # 类方法的注释
    def test_query135(self):
        '''用例描述'''
        with allure.step("发信箱获取"):
            cf = ict.Test_query08().test_query135()
            assert cf == '操作成功'
    @allure.title("消息》系统消息》收信箱获取")  # 类方法的注释
    def test_query136(self):
        '''用例描述'''
        with allure.step("收信箱获取"):
            cf = ict.Test_query08().test_query136()
            assert cf == '操作成功'
    @allure.title("消息》系统消息》收信箱获取")  # 类方法的注释
    def test_query136(self):
        '''用例描述'''
        with allure.step("收信箱获取"):
            cf = ict.Test_query08().test_query136()
            assert cf == '操作成功'
    @allure.title("消息》业务消息》收信箱获取")  # 类方法的注释
    def test_query137(self):
        '''用例描述'''
        with allure.step("收信箱获取"):
            cf = ict.Test_query08().test_query137()
            assert cf == '操作成功'
    @allure.title("消息》业务消息》发信箱获取")  # 类方法的注释
    def test_query138(self):
        '''用例描述'''
        with allure.step("发信箱获取"):
            cf = ict.Test_query08().test_query138()
            assert cf == '操作成功'
    @allure.title("消息》进度消息获取")  # 类方法的注释
    def test_query139(self):
        '''用例描述'''
        with allure.step("进度消息获取"):
            cf = ict.Test_query08().test_query139()
            assert cf == '操作成功'
    @allure.title("消息》WEB消息订阅获取")  # 类方法的注释
    def test_query140(self):
        '''用例描述'''
        with allure.step("WEB消息订阅获取"):
            cf = ict.Test_query08().test_query140()
            assert cf == '操作成功'
    @allure.title("通知》短信日志获取")  # 类方法的注释
    def test_query141(self):
        '''用例描述'''
        with allure.step("短信日志获取"):
            cf = ict.Test_query08().test_query141()
            assert cf == '操作成功'
    @allure.title("通知》邮件日志获取")  # 类方法的注释
    def test_query142(self):
        '''用例描述'''
        with allure.step("邮件日志获取"):
            cf = ict.Test_query08().test_query142()
            assert cf == '操作成功'
    @allure.title("通知》微信日志获取")  # 类方法的注释
    def test_query143(self):
        '''用例描述'''
        with allure.step("微信日志获取"):
            cf = ict.Test_query08().test_query143()
            assert cf == '操作成功'

'''货主查询接口'''
@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景九,货主的查询接口')
# @pytest.mark.skip(reason="无理由跳过")
class Test_query02():
    '''大类'''
    def setup_class(self):
        '''大类前置'''
        pass
    def teardown_class(self):
        '''大类后置'''
        pass
    @allure.title("查询报价》集装箱出口运输报价获取")   #类方法的注释
    def test_query144(self):
        '''用例描述'''
        with allure.step("集装箱出口运输报价获取"):
            cf=ict.Test_query09().test_query144()
            assert cf =='操作成功'
    @allure.title("查询报价》集装箱进口运输报价获取")  # 类方法的注释
    def test_query145(self):
        '''用例描述'''
        with allure.step("集装箱进口运输报价获取"):
            cf = ict.Test_query09().test_query145()
            assert cf == '操作成功'
    @allure.title("查询报价》厢式车运输报价获取")  # 类方法的注释
    def test_query146(self):
        '''用例描述'''
        with allure.step("厢式车运输报价获取"):
            cf = ict.Test_query09().test_query146()
            assert cf == '操作成功'
    @allure.title("询价管理》询价管理查询获取")  # 类方法的注释
    def test_query147(self):
        '''用例描述'''
        with allure.step("询价管理查询获取"):
            cf = ict.Test_query09().test_query147()
            assert cf == '操作成功'
    @allure.title("订单管理》订单管理查询获取")  # 类方法的注释
    def test_query148(self):
        '''用例描述'''
        with allure.step("订单管理查询获取"):
            cf = ict.Test_query09().test_query148()
            assert cf == '操作成功'
    @allure.title("费用中心》费用查询获取")  # 类方法的注释
    def test_query149(self):
        '''用例描述'''
        with allure.step("费用查询获取"):
            cf = ict.Test_query09().test_query149()
            assert cf == '操作成功'
    @allure.title("费用中心》应付账单查询获取")  # 类方法的注释
    def test_query150(self):
        '''用例描述'''
        with allure.step("应付账单查询获取"):
            cf = ict.Test_query09().test_query150()
            assert cf == '操作成功'
    @allure.title("费用中心》应收发票查询获取")  # 类方法的注释
    def test_query151(self):
        '''用例描述'''
        with allure.step("应收发票查询获取"):
            cf = ict.Test_query09().test_query151()
            assert cf == '操作成功'
    @allure.title("费用中心》月账单查询获取")  # 类方法的注释
    def test_query152(self):
        '''用例描述'''
        with allure.step("月账单查询获取"):
            cf = ict.Test_query09().test_query152()
            assert cf == '操作成功'
    @allure.title("费用中心》对账单查询获取")  # 类方法的注释
    def test_query153(self):
        '''用例描述'''
        with allure.step("对账单查询获取"):
            cf = ict.Test_query09().test_query153()
            assert cf == '操作成功'
    @allure.title("档案管理》收发货人查询获取")  # 类方法的注释
    def test_query154(self):
        '''用例描述'''
        with allure.step("收发货人查询获取"):
            cf = ict.Test_query09().test_query154()
            assert cf == '操作成功'
    @allure.title("档案管理》联系人档案查询获取")  # 类方法的注释
    def test_query155(self):
        '''用例描述'''
        with allure.step("联系人档案查询获取"):
            cf = ict.Test_query09().test_query155()
            assert cf == '操作成功'
    @allure.title("档案管理》结算信息档案查询获取")  # 类方法的注释
    def test_query156(self):
        '''用例描述'''
        with allure.step("结算信息档案查询获取"):
            cf = ict.Test_query09().test_query156()
            assert cf == '操作成功'
    @allure.title("档案管理》合同报价查询获取")  # 类方法的注释
    def test_query157(self):
        '''用例描述'''
        with allure.step("合同报价查询获取"):
            cf = ict.Test_query09().test_query157()
            assert cf == '操作成功'
    @allure.title("智能分析》Excel报表查询获取")  # 类方法的注释
    def test_query158(self):
        '''用例描述'''
        with allure.step("Excel报表查询获取"):
            cf = ict.Test_query09().test_query158()
            assert cf == '操作成功'
    @allure.title("用户中心》账号交易充值记录查询获取")  # 类方法的注释
    def test_query160(self):
        '''用例描述'''
        with allure.step("账号交易充值记录查询获取"):
            cf = ict.Test_query09().test_query160()
            assert cf == '操作成功'
    @allure.title("用户中心》账号交易提现记录查询获取")  # 类方法的注释
    def test_query161(self):
        '''用例描述'''
        with allure.step("账号交易提现记录查询获取"):
            cf = ict.Test_query09().test_query161()
            assert cf == '操作成功'
    @allure.title("用户中心》咨询投诉查询获取")  # 类方法的注释
    def test_query162(self):
        '''用例描述'''
        with allure.step("咨询投诉查询获取"):
            cf = ict.Test_query09().test_query162()
            assert cf == '操作成功'
    @allure.title("用户中心》权限管理用户管理查询获取")  # 类方法的注释
    def test_query163(self):
        '''用例描述'''
        with allure.step("权限管理用户管理查询获取"):
            cf = ict.Test_query09().test_query163()
            assert cf == '操作成功'
    @allure.title("用户中心》权限管理角色管理查询获取")  # 类方法的注释
    def test_query164(self):
        '''用例描述'''
        with allure.step("权限管理角色管理查询获取"):
            cf = ict.Test_query09().test_query164()
            assert cf == '操作成功'

'''运输公司查询接口'''
@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景九,运输公司查询接口')
# @pytest.mark.skip(reason="无理由跳过")
class Test_query03():
    '''大类'''
    def setup_class(self):
        '''大类前置'''
        pass
    def teardown_class(self):
        '''大类后置'''
        pass
    @allure.title("运单管理》集装箱运输获取")   #类方法的注释
    def test_query165(self):
        '''用例描述'''
        with allure.step("集装箱运输获取"):
            cf=ict.Test_query10().test_query165()
            assert cf =='操作成功'
    @allure.title("运单管理》厢式车运输获取")  # 类方法的注释
    def test_query166(self):
        '''用例描述'''
        with allure.step("厢式车运输获取"):
            cf = ict.Test_query10().test_query166()
            assert cf == '操作成功'
    @allure.title("运单管理》车辆档案获取")  # 类方法的注释
    def test_query167(self):
        '''用例描述'''
        with allure.step("车辆档案获取"):
            cf = ict.Test_query10().test_query167()
            assert cf == '操作成功'
    @allure.title("运单管理》司机档案获取")  # 类方法的注释
    def test_query168(self):
        '''用例描述'''
        with allure.step("司机档案获取"):
            cf = ict.Test_query10().test_query168()
            assert cf == '操作成功'
    @allure.title("excel报表》excel报表获取")  # 类方法的注释
    def test_query169(self):
        '''用例描述'''
        with allure.step("excel报表获取"):
            cf = ict.Test_query10().test_query169()
            assert cf == '操作成功'
    @allure.title("excel报表》订阅计划获取")  # 类方法的注释
    def test_query170(self):
        '''用例描述'''
        with allure.step("订阅计划获取"):
            cf = ict.Test_query10().test_query170()
            assert cf == '操作成功'
    @allure.title("费用中心》月账单获取")  # 类方法的注释
    def test_query171(self):
        '''用例描述'''
        with allure.step("月账单获取"):
            cf = ict.Test_query10().test_query171()
            assert cf == '操作成功'
    @allure.title("用户中心》基础信息获取")  # 类方法的注释
    def test_query172(self):
        '''用例描述'''
        with allure.step("基础信息获取"):
            cf = ict.Test_query10().test_query172()
            assert cf == '操作成功'
    @allure.title("用户中心》咨询投诉获取")  # 类方法的注释
    def test_query173(self):
        '''用例描述'''
        with allure.step("咨询投诉获取"):
            cf = ict.Test_query10().test_query173()
            assert cf == '操作成功'
    @allure.title("权限管理》用户管理获取")  # 类方法的注释
    def test_query174(self):
        '''用例描述'''
        with allure.step("用户管理获取"):
            cf = ict.Test_query10().test_query174()
            assert cf == '操作成功'
    @allure.title("用户中心》角色管理获取")  # 类方法的注释
    def test_query175(self):
        '''用例描述'''
        with allure.step("角色管理获取"):
            cf = ict.Test_query10().test_query175()
            assert cf == '操作成功'


@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景十四 报关订单（测试点：报关订单+海格申报+改派其他供应商）')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso8():
    log.info("开始运行，业务场景十四,报关订单")
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("新增报关订单")
    def test_business_scenario001(self):
        log.info("查看货主id，货主：{}".format(cf.hz_name))
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        log.info("获取货主联系人")
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]  # 货主联系人id
            lxr_name = lxr_name1[3]  # 货主联系人名称
            lxr_hm = lxr_name1[4]  # 货主联系人号码
        log.info("获取港口id")
        with allure.step("港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]  # 港口id
        log.info("获取时间")
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time9 = time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  # 订舱号
            containerNumber = "TRLU7360789"   #柜号
        log.info("新增报关订单")
        with allure.step("新增报关订单"):
            xzjzx_ck = ict.Test_Added01().test_Added02104(customerId=hz_id, customerContact=lxr_name,
                                                          customerContactPhone=lxr_hm,customsAddr=gk_id,
                                                          customerServiceId=kf_id,bookingNumber=SSS,
                                                          customerDelegateCode=time9,containerNumber=containerNumber)
            assert xzjzx_ck == '操作成功'
        time.sleep(5)
        log.info("查询报关订单信息")
        with allure.step("查询报关订单信息"):
            dd_xx = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            dd_hao = dd_xx[1][0]["orderNumber"]
            order_id = dd_xx[1][0]["id"]
        log.info("报关订单號:{}".format(dd_hao))
        log.info("接口推送日志")
        time.sleep(5)
        with allure.step("关务OMS接收一体化推单,接口推送日志报关订单号：{}".format(dd_hao)):
            log_01 = ict.Test_Added01().test_Added0134(dd_id=dd_hao)
            assert log_01[0] == '操作成功'
            pytest.assume(log_01[1] != 0 )


        with allure.step("集装箱运输》查看订单详情页，订单号：{}".format(dd_hao)):
            dd_xx = ict.Test_Added01().test_Added0162(dd_id=order_id)
            assert dd_xx[0] == '操作成功'
            data1 = dd_xx[1]
            dd_hao = dd_xx[1]["baseInfo"]["orderNumber"]
            dd_id =  dd_xx[1]["baseInfo"]["id"]
            baseInfo = data1["baseInfo"]
            goodsList = data1["goodsList"]
            priceList = data1["priceList"]
            baseInfo.update([('containerNumber','TRLU7360790')]) #修改状态+柜号
            data = {"baseInfo":baseInfo,"goodsList":goodsList,"priceList":priceList}
            # print(str(data))
        with allure.step("修改订单，订单号：{}".format(dd_hao)):
            dd_xg = ict.Test_Added01().test_Added0160(data1=data,id=dd_id)
            assert dd_xg == '操作成功'

        with allure.step("获取改单详情页信息"):
            gd_xx = ict.Test_Added01().test_Added0164(dd_id=dd_id)
            assert gd_xx[3] == '操作成功'
            baseInfo1 = ict.get_k(gd_xx[1]['baseInfo'])
            costList = []
            addrList = []
            changeList = gd_xx[2]['changeList']
            id = gd_xx[2]["id"]
            editType = gd_xx[2]["editType"]
            editRemark = gd_xx[2]["editRemark"]
            baseInfo1.update([("containerNumber","TRLU7360790")])
            # print(baseInfo1)
        with allure.step("审核改单申请"):
            data1 = {"baseInfo":baseInfo1,"addrList":addrList,"costList":costList}
            sh_gd = ict.Test_Added01().test_Added0163(dd_hao=dd_hao,data=data1,dd_id=id,editType=editType,editRemark=editRemark,changeList=changeList)
            assert sh_gd == '操作成功'

        with allure.step("报关订单>待接单》执改确认"):
            tg_qr = ict.Test_Added01().test_Added0165(customerOrderId=id)
            assert tg_qr == '操作成功'
        # time.sleep(4)
        # log.info("接口推送日志,报关订单號:{}".format(dd_hao))
        # with allure.step("关务OMS接收一体化推单,接口推送日志报关订单号：{}".format(dd_hao)):
        #     log_01 = ict.Test_Added01().test_Added0134(dd_id=dd_hao)
        #     assert log_01[0] == '操作成功'
        #     pytest.assume(log_01[1] == 2 )

        with allure.step("取消订单>集装箱运输》取消订单，订单号：{}".format(dd_hao)):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=id)
            assert qx_dd == '操作成功'
        with allure.step("取消订单>订单管理》集装箱运输》查看订单状态，订单号：{}".format(dd_hao)):
            dd_hao = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode="")
            assert dd_hao[0] == '操作成功'
            assert dd_hao[1][0]["orderStatus"] == 'status_undo_completed'


@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('业务场景十五 货主端下单+FBA配置计划')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso9():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景十五 集装箱出口（测试点：货主端下单，集装箱出口")
    def test_business_scenario001(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]    #货主联系人id
            lxr_name = lxr_name1[3]  #货主联系人名称
            lxr_hm = lxr_name1[4]    #货主联系人号码
        with allure.step("港口id"):
            gk_id1 = ict.Test_Added01().test_Added000(placeName="BREMERHAVEN")
            assert gk_id1[0] == '操作成功'
            gk_id = gk_id1[1]   #港口id
        with allure.step("获取收发地省编码"):
            sf_bm = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm[0] == '操作成功'
            sf_bm = sf_bm[1]
        with allure.step("获取收发地市编码"):
            cs_bm = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm[0] == '操作成功'
            cs_bm = cs_bm[1]
        with allure.step("获取收发地区编码"):
            q_bm = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm[0] == '操作成功'
            q_bm = q_bm[1]
        with allure.step("获取收发地街道编码"):
            jd_bm = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm[0] == '操作成功'
            jd_bm = jd_bm[1]
        with allure.step("获取装货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            zhdw_id = sfh_dd[1]         #装货单位id
            zhdw_name = sfh_dd[2]       #装货单位名称
            zhdw_lxr =  sfh_dd[3]       #装货联系人
            zhdw_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time9 =time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  #订舱号
        with allure.step("集装箱出口运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0055(taskUnitCode="port_container_export_transport",customerId=hz_id,
                                                        transportPort=gk_id,provinces=sf_bm,city=cs_bm,area=q_bm,
                                                        street=jd_bm,consigneeConsignorId=zhdw_id,pickupTime=time2,carModeId="20GP")
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("货主新增集装箱出口订单"):
            newly_order = ict.Shipperapi().test_Added014(hz_host=hz_host,token=hz_token,customerId=hz_id,customerContact=lxr_name,customerContactPhone=lxr_hm,
                        customerServiceId=kf_id,transportPort=gk_id,departureProvinces=sf_bm,departureCity=cs_bm,departureArea=q_bm,
                        departure=jd_bm,cyCutOffTime=time3,consignorId=zhdw_id,consignorName=zhdw_name,consignorContact=zhdw_lxr,
                        consignorContactPhone=zhdw_xlrdh,consignorContactAddr=zhdw_xxdz,provinces=sf_bm,city=cs_bm,district=q_bm,
                        street=jd_bm,pickupTime=time2,bookingNumber=SSS,customerDelegateCode=time9,baseAmount=bjd_je,price=bjd_je,
                        customerPricePropertyId=bjd_id,matchKey=jd_bm)
            assert newly_order == '操作成功'
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            order_id = dd_xx[1][0]["id"]
            orderNumber = dd_xx[1][0]["orderNumber"]
            pytest.assume(dd_xx[1][0]["orderStatus"] == "status_pending")  #订单状态= 待接单
        with allure.step("集装箱出口运输审核下发"):
            audit_issue = ict.Test_Added01().test_Added0196(ht_host=ht_host,token=ht_token,order_id=order_id)
            assert audit_issue == '操作成功'
        with allure.step("审核下发，查看订单状态"):
            dd_xx = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode=time9)
            assert dd_xx[0] == '操作成功'
            pytest.assume(dd_xx[1][0]["orderStatus"] == "status_execution")  #订单状态= 执行中



        '''集装箱出口订单分单管理》分自有车'''
        with allure.step("计划管理，分单查询，订单号：{}".format(orderNumber)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=orderNumber)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                print(id2)
                fd_id = id[id2]
                with allure.step("分单，分派自有车,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che=fd_id,gys="",hy_dt="")
                    assert qy_jdzx == '操作成功'

        '''集装箱出口订单派自有车A'''
        with allure.step("集装箱出口订单派自有车A》查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=orderNumber,lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[3][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[3][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[2]    #订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')   #装货时间  年月日
        with allure.step("查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集1")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]   #司机id
            sj_name = xz_sj[4]   #司机名称
            sj_haoma = xz_sj[5]   #司机号码
        with allure.step("查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集1")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤ZZ0001")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]   #车辆id
            cp_hao = sj_da[2]    #车牌号
            cl_name = sj_da[4]  #车辆名称
            cz_qy = sj_da[6]    # 操作区域
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0 :
                with allure.step("出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type",cz_qy=cz_qy,tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0 :
                with allure.step("出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤ZZ0001",zh_time=time2)
                    assert cc_dd[0] == '操作成功'

                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'

        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{}".format(orderNumber)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=orderNumber,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'

        '''集装箱出口订单撤销派自有车A'''
        with allure.step("自有车撤销派单，订单号:{}".format(orderNumber)):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')

        '''集装箱出口订单派自有车B'''
        with allure.step("集装箱出口订单派自有车B》查看司机档案"):
            xz_sj = ict.Test_Added01().test_Added0066(sj_name="测试自有车-集2")
            assert xz_sj[0] == '操作成功'
            sj_id = xz_sj[1]   #司机id
            sj_name = xz_sj[4]   #司机名称
            sj_haoma = xz_sj[5]   #司机号码
        with allure.step("查看运输公司档案"):
            gys_da = ict.Test_Added01().test_Added0062(gys_name="租户测试自有车-集2")
            assert gys_da[0] == '操作成功'
            gys_id = gys_da[1]  #供应商id
            gyl_name =  gys_da[4]  #供应商名称
        with allure.step("查看车辆档案"):
            sj_da = ict.Test_Added01().test_Added0070(gys_id=gys_id, cp_hao="粤B7788")
            assert sj_da[0] == '操作成功'
            cl_id = sj_da[1]   #车辆id
            cp_hao = sj_da[2]    #车牌号
            cl_name = sj_da[4]  #车辆名称
            cz_qy = sj_da[6]    # 操作区域
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0072(sj_id=sj_id, cp_hao="粤B7788",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            if cc_xx[1] == 0 :
                with allure.step("出车表不存在，生成出车表"):
                    xx_ccb = ict.Test_Added01().test_Added0073(fw_lx="container_type",cz_qy=cz_qy,tims=time2)
                    assert xx_ccb == '操作成功'
            if cc_xx[1] != 0 :
                with allure.step("出车表存在，查看出车表信息"):
                    cc_dd = ict.Test_Added01().test_Added0074(sj_id=sj_id,cp_hao="粤B7788",zh_time=time2)
                    assert cc_dd[0] == '操作成功'
                    data1 = cc_dd[5]
                    list11 = []
                    for i in data1:
                        # print(i)
                        n = ict.get_k(i)
                        # print(n)
                        for key in n.keys():
                            if key == "status":
                                list11.append(key)
                                list11.append(n[key])
                    # print(list11)
                    for j in list11:
                        list22 = []
                        if  j =="car_dispatch_undistribute" :
                            list22.append(j)
                            if list22 == "car_dispatch_undistribute":
                                with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                                    pass
                            if list22 == "car_dispatch_completed":
                                fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                                assert fz_ccb == '操作成功'

        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤B7788",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            # assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{}".format(orderNumber)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'

        '''集装箱出口订单撤销派自有车B'''
        with allure.step("自有车撤销派单，订单号:{}".format(orderNumber)):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        '''取消订单'''
        with allure.step("计划管理，分单查询，订单号：{}".format(orderNumber)):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=orderNumber)
            assert fd_xx[0] == '操作成功'
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("撤销分单,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("集装箱运输》取消订单，订单号：{}".format(orderNumber)):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=order_id)
            assert qx_dd == '操作成功'
        with allure.step("订单管理》集装箱运输》查看订单状态，订单号：{}".format(orderNumber)):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id,customerDelegateCode="")
            assert jzx_ys[0] == '操作成功'
            assert jzx_ys[1][0]["orderStatus"] == 'status_undo_completed'

    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景十五 厢式车多装一卸（测试点：货主端下单，厢车运输）")
    def test_business_scenario002(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("获取货主联系人"):
            lxr_name1 = ict.Test_Added01().test_Added0014(hz_id=hz_id)
            assert lxr_name1[0] == '操作成功'
            lxr_id = lxr_name1[1]    #货主联系人id
            lxr_name = lxr_name1[3]  #货主联系人名称
            lxr_hm = lxr_name1[4]    #货主联系人号码
        with allure.step("获取卸货地省编码"):
            sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="湖南省")
            assert sf_bm1[0] == '操作成功'
            xsf_bm = sf_bm1[1]
            xsf_name = sf_bm1[2]
        with allure.step("获取卸货地市编码"):
            cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="长沙市")
            assert cs_bm1[0] == '操作成功'
            xcs_bm = cs_bm1[1]
            xcs_name = cs_bm1[2]
        with allure.step("获取卸货地区编码"):
            q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="雨花区")
            assert q_bm1[0] == '操作成功'
            xq_bm = q_bm1[1]
            xq_name = q_bm1[2]
        with allure.step("获取卸货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="洞井街道")
            assert jd_bm1[0] == '操作成功'
            xjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]

        with allure.step("获取装货地省编码"):
            sf_bm1 = ict.Test_Added01().test_Added0001(lx=3, name="广东省")
            assert sf_bm1[0] == '操作成功'
            zsf_bm = sf_bm1[1]
            zsf_name = sf_bm1[2]
        with allure.step("获取装货地市编码"):
            cs_bm1 = ict.Test_Added01().test_Added0001(lx=4, name="深圳市")
            assert cs_bm1[0] == '操作成功'
            zcs_bm = cs_bm1[1]
            zcs_name = cs_bm1[2]
        with allure.step("获取装货地区编码"):
            q_bm1 = ict.Test_Added01().test_Added0001(lx=5, name="盐田区")
            assert q_bm1[0] == '操作成功'
            zq_bm = q_bm1[1]
            zq_name = q_bm1[2]
        with allure.step("获取装货地街道编码"):
            jd_bm1 = ict.Test_Added01().test_Added0001(lx=6, name="海山街道")
            assert jd_bm1[0] == '操作成功'
            zjd_bm = jd_bm1[1]
            xjd_name = jd_bm1[2]


        with allure.step("获取装货单位1档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="厢式车装货地址1")
            assert sfh_dd[0] == '操作成功'
            zhdw1_id = sfh_dd[1]         #装货单位id
            zhdw1_name = sfh_dd[2]       #装货单位名称
            zhdw1_lxr =  sfh_dd[3]       #装货联系人
            zhdw1_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw1_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取装货单位2档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="厢式车装货地址2")
            assert sfh_dd[0] == '操作成功'
            zhdw2_id = sfh_dd[1]         #装货单位id
            zhdw2_name = sfh_dd[2]       #装货单位名称
            zhdw2_lxr =  sfh_dd[3]       #装货联系人
            zhdw2_xlrdh = sfh_dd[4]      #装货联系电话
            zhdw2_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取卸货单位档案"):
            sfh_dd = ict.Test_Added01().test_Added0029(hz_id=hz_id, zh_name="测试集装箱装货地址")
            assert sfh_dd[0] == '操作成功'
            xhdw_id = sfh_dd[1]         #装货单位id
            xhdw_name = sfh_dd[2]       #装货单位名称
            xhdw_lxr =  sfh_dd[3]       #装货联系人
            xhdw_xlrdh = sfh_dd[4]      #装货联系电话
            xhdw_xxdz = sfh_dd[5]       #装货详细地址
        with allure.step("获取时间"):
            time1 = bf.Common_page().get_today001()
            time2 = time1[1]  # +5天 年月日时分秒
            time3 = time1[2]  # +10天  年月日时分秒
            time4 =time1[3]  # +20天  年月日时分秒
            time5 = time1[4]  # 今天  年月日
            time6 =time1[5]  # +50天  年月日
            time7 =time1[6]  # +100天  年月日
            time8 =time1[7]  # +200天  年月日
            time9 =time1[8]  # 按时间年月日时分秒生成数组-客户委托号
            SSS = bf.Common_page().start()  #订舱号
        with allure.step("厢式车运输货主合同报价,查看报价id"):
            bjd_bm2 = ict.Test_Added01().test_Added0102(customerId=hz_id,provinces=xsf_bm,city=xcs_bm,area=xq_bm,street=xjd_bm,provinces1=zsf_bm,city1=zcs_bm,area1=zq_bm,street1=zjd_bm,consigneeConsignorId1=zhdw1_id,consigneeConsignorId2=zhdw2_id)
            assert bjd_bm2[0] == '操作成功'
            bjd_id = bjd_bm2[2]
            bjd_je = bjd_bm2[1]
        with allure.step("新增厢式车运输"):
            xz_xsc =  ict.Shipperapi().test_Added015(hz_host=hz_host,token=hz_token,customerId=hz_id,customerContact=lxr_name,customerContactPhone=lxr_hm,customerServiceId=kf_id,consigneeId=xhdw_id,consigneeName=xhdw_name,consigneeContact=xhdw_lxr,
                        consigneeContactPhone=xhdw_xlrdh,consigneeContactAddr=xhdw_xxdz,xh_sf=xsf_bm,xh_cs=xcs_bm,xh_q=xq_bm,xh_jd=xjd_bm,zh_sf=zsf_bm,zh_cs=zcs_bm,zh_q=zq_bm,zh_jd=zjd_bm,zh_dz1id=zhdw1_id,zh_dz1name=zhdw1_name,zh_dz1lxr=zhdw1_lxr,
                        zh_dz1lxrdh=zhdw1_xlrdh,zh_dz1=zhdw1_xxdz,zh_dz2id=zhdw2_id,zh_dz2name=zhdw2_name,zh_dz2lxr=zhdw2_lxr,zh_dz2lxrdh=zhdw2_xlrdh,zh_dz2=zhdw2_xxdz,zh_time=time2,jc_time=time3,bj_je=bjd_je,bj_id=bjd_id,kh_hao=time9)
            assert xz_xsc == '操作成功'
        with allure.step("后台查看新增厢式车运输信息"):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host,token=ht_token,order_number="",customerDelegateCode=time9)
            assert ht_order_info[0] == '操作成功'
            order_id = ht_order_info[1][0]["id"]    #订单id
            orderNumber = ht_order_info[1][0]["orderNumber"]
            status = ht_order_info[1][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_pending")  # 断言订单状态：待接单

        with allure.step("厢式车运输审核下发"):
            audit_issue = ict.Test_Added01().test_Added0196(ht_host=ht_host,token=ht_token,order_id=order_id)
            assert audit_issue == '操作成功'
        with allure.step("审核下发，查看订单状态"):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host,token=ht_token,order_number="",customerDelegateCode=time9)
            assert ht_order_info[0] == '操作成功'
            pytest.assume(ht_order_info[1][0]["orderStatus"] == "status_execution")  #订单状态= 执行中


        '''厢式车订单分单管理》分供应商'''
        with allure.step("计划管理，分单查询，订单号：{}".format(orderNumber)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=orderNumber)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 1
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("分单，分派供应商,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host,token=ht_token,zy_che="", gys=fd_id, hy_dt="")
                    assert qy_jdzx == '操作成功'

        '''厢式车订单派供应商A：手工报价'''
        with allure.step("计划管理，获取订单ID，订单号：{}".format(orderNumber)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=orderNumber)
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
        with allure.step("厢式车订单派供应商A》查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys2_name)
            assert gys_id[0] == '操作成功'
        with allure.step("厢式车订单派供应商A》查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr =  gys_xx[2]
            gys_lxrdh =  gys_xx[3]
        with allure.step("派供应商A"):
            gys_xx = ict.Test_Added01().test_Added0106(dd_id=dd_id,gys_lxr=gys_lxr,gys_lxrdh=gys_lxrdh,gys_id=gys_id[1],je=2500)
            assert gys_xx == '操作成功'

        '''厢式车订单改派供应商B：合同报价'''
        with allure.step("厢式车订单改派供应商B》查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("厢式车订单改派供应商B》查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr =  gys_xx[2]
            gys_lxrdh =  gys_xx[3]
        with allure.step("派供应商B"):
            gys_xx = ict.Test_Added01().test_Added0107(dd_id=dd_id,gys_lxr=gys_lxr,gys_lxrdh=gys_lxrdh,gys_id=gys_id[1])
            assert gys_xx == '操作成功'

        '''供应商B接单，并指派车辆'''
        with allure.step("供应商接单"):
            gys_id1 = ict.Test_transport_company01().test_transport0002(dd_id=dd_id)
            assert gys_id1== '操作成功'
        with allure.step("查看司机ID"):
            siji_da = ict.Test_transport_company01().test_transport0003(siji_name="测试运输公司司机1",gys_id=gys_id[1])
            assert siji_da[0] == '操作成功'
            siji_id =  siji_da[2][0]["id"]
            siji_name = siji_da[2][0]["driverName"]
            siji_dh = siji_da[2][0]["driverMobilePhone"]
        with allure.step("查看车辆档案"):
            cl_da = ict.Test_transport_company01().test_transport0007(c_pai="粤A6688",gys_id=gys_id[1])
            assert cl_da[0] == '操作成功'
            cl_id =  cl_da[2][0]["id"]
            c_pai = cl_da[2][0]["carNumber"]
        with allure.step("供应商指派车辆"):
            zp_cl = ict.Test_transport_company01().test_transport0009(dd_id=dd_id,shiji_dh=siji_dh,cl_id=cl_id,siji_id=siji_id,
                                                                      c_pai=c_pai,siji_name=siji_name)
            assert zp_cl == '操作成功'

        '''取消订单'''
        with allure.step("调度管理》撤销派单/车，订单号：{}".format(orderNumber)):
            cx_pc = ict.Test_Added01().test_Added0156(dd_id=dd_id)
            assert cx_pc == '操作成功'
        with allure.step("计划管理，分单查询，订单号：{}".format(orderNumber)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host,token=ht_token,dd_hao=orderNumber)
            assert fd_xx[0] == '操作成功'
            data1 = fd_xx[2]
            id = []
            for item in data1:
                for key in item:
                    # print(key)
                    if key == "id":
                        # print(item[key])
                        id.append(item[key])
            id0 = len(id)
            id1 = 0
            while id1 < id0:
                id2 = id1
                id1 += 1
                # print(id2)
                fd_id = id[id2]
                with allure.step("撤销分单,分单号：{}".format(fd_id)):
                    qy_jdzx = ict.Test_Added01().test_Added0157(dd_id=fd_id)
                    assert qy_jdzx == '操作成功'
        with allure.step("集装箱运输》取消订单，订单号：{}".format(orderNumber)):
            qx_dd = ict.Test_Added01().test_Added015701(dd_id=order_id)
            assert qx_dd == '操作成功'
        with allure.step("订单管理》集装箱运输》查看订单状态，订单号：{}".format(orderNumber)):
            jzx_ys = ict.Test_Added01().test_Added0168(orderNumber=orderNumber)
            assert jzx_ys[0] == '操作成功'
            assert jzx_ys[1][0]["orderStatus"] == 'status_undo_completed'







