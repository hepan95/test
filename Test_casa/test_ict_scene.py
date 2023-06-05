#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: test_ict_scene.py.py
# @Time:2023/4/12 15:17
# @Author:PH

import datetime
import allure
import pytest
myskip = pytest.mark.skipif()

from Common import ict_api as ict
from Config import config as cf
from Common import common_funtion as bf


@pytest.mark.skip(reason="无理由跳过")
@allure.parent_suite('ict业务场景测试用例')  # 包的注释
@allure.suite('ict业务场景测试用例模块')  # 模块的注释
@allure.sub_suite('前置条件')      #大类的注释
class Test_query01():
    '''大类'''
    def setup_class(self):
        '''大类前置'''
        pass
    def teardown_class(self):
        '''大类后置'''
        pass
    @allure.title("区域规则-集装箱出口运输,操作区域蛇口")   #类方法的注释
    @pytest.mark.skip(reason="无理由跳过")
    def test_query001(self):
        '''用例描述'''
        with allure.step("查看区域规则-集装箱出口运输,操作区域蛇口是否存在"):
            qy_gh = ict.Test_Added01().test_Added0031(taskUnitCode="port_container_export_transport",centerName="shekou_group")
            assert qy_gh[0] =='操作成功'
            if qy_gh[1] == [] :
                with allure.step("新增集装箱出口区域规划"):
                    xz_gh = ict.Test_Added01().test_Added0032(taskUnitCode="port_container_export_transport",centerName="shekou_group",isContainer=1)
                    assert xz_gh[0] == '操作成功'
                with allure.step("查看区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="port_container_export_transport",centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                with allure.step("启用区域规划状态"):
                    qyqy_gh = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                    assert qyqy_gh == '操作成功'
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query002(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query003(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query004(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query005(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query006(self):
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
    @allure.title("集装箱货主市场报价")
    @pytest.mark.skip(reason="无理由跳过")
    def test_query007(self):
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
                with allure.step("新增货主合同报价:港口：{},{}{}{}{}".format(gk_name,sf_name,cs_name,q_name,jd_name)):
                    xzsc_bj = ict.Test_Added01().test_Added0052(customerPriceId=bz_dd[2],taskUnitCode="port_container_export_transport",
                    taskUnitTypeName="集装箱出口运输",transportPort=gk_id,departure=jd_bm,departureProvinces=sf_bm,departureCity=cs_bm,
                    departureArea=q_bm)
                    assert xzsc_bj[0] == '操作成功'
                with allure.step("新增集装箱出口运输货主合同报价，查看报价单信息"):
                    bjd_bm = ict.Test_Added01().test_Added0053(bjd_id=bz_dd[2],transportPort=gk_id,departure=jd_bm)
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
                        bjd_bm1 = ict.Test_Added01().test_Added0051(bjd_id=bjd_bm[2],transportPort=gk_id,departure=jd_bm)
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
                                bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_bm[2], transportPort=gk_id,departure=jd_bm)
                                assert bjd_bm2[0] == '操作成功'
                            with allure.step("启用新增集装箱出口运输货主市场报价,报价单编码：{}".format(bjd_bm[3])):
                                jd_bm = ict.Test_Added01().test_Added0054(bj_id=bjd_bm2[1])
                                assert jd_bm == '操作成功'
                        if bjd_bm1[1] != []:
                            with allure.step("存在集装箱出口运输货主合同报价,查看报价id"):
                                bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_bm[2],transportPort=gk_id,departure=jd_bm)
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
    @allure.title("自有车集装箱报价")
    @pytest.mark.skip(reason="无理由跳过")
    def test_query008(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query009(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query010(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query011(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query012(self):
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
    @allure.title("厢式车货主市场报价")
    @pytest.mark.skip(reason="无理由跳过")
    def test_query013(self):
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
                    bjd_bm = ict.Test_Added01().test_Added0101(bjd_id=bz_dd[2],taskUnitCode="bulkcargo_transport",jd_bm=zjd_bm)
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
                    bjd_bm3 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=zjd_bm)
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
                            bjd_bm5 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=zjd_bm)
                            assert bjd_bm5[0] == '操作成功'
                            bj_id = bjd_bm5[2][0]["id"]
                        with allure.step("启用新增厢式车运输货主合同报价,报价单编码：{},{}".format(bjd_bm[3],bj_id)):
                            jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                            assert jd_bm == '操作成功'
                    if bjd_bm3[1] != 0:
                        with allure.step("存在厢式车运输货主合同报价，查看报价单信息"):
                                bjd_bm4 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=zjd_bm)
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query014(self):
        '''用例描述'''
        with allure.step("查看区域规则-厢式车运输,操作区域蛇口是否存在"):
            qy_gh = ict.Test_Added01().test_Added0031(taskUnitCode="bulkcargo_transport",centerName="shekou_group")
            assert qy_gh[0] =='操作成功'
            if qy_gh[1] == [] :
                with allure.step("新增厢式车运输区域规划"):
                    xz_gh = ict.Test_Added01().test_Added0032(taskUnitCode="bulkcargo_transport",centerName="shekou_group",isContainer=0)
                    assert xz_gh[0] == '操作成功'
                with allure.step("查看厢式车运输区域规划id+状态"):
                    qygh_id = ict.Test_Added01().test_Added0033(taskUnitCode="bulkcargo_transport",centerName="shekou_group")
                    assert qygh_id[0] == '操作成功'
                with allure.step("启用厢式车运输区域规划状态"):
                    qyqy_gh = ict.Test_Added01().test_Added0034(gh_id=qygh_id[2])
                    assert qyqy_gh == '操作成功'
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query015(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query016(self):
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
    @allure.title("运输公司合同报价，厢式车")
    @pytest.mark.skip(reason="无理由跳过")
    def test_query017(self):
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
                    bjd_bm = ict.Test_Added01().test_Added0101(bjd_id=bz_dd[2],taskUnitCode="bulkcargo_transport",jd_bm=zjd_bm)
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
                        bjd_bm3 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=zjd_bm)
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
                                bjd_bm1 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=zjd_bm)
                                assert bjd_bm1[0] == '操作成功'
                                bj_id = bjd_bm1[2][0]["id"]
                            with allure.step("启用新增厢式车运输公司合同报价,报价单编码：{}".format(bjd_bm[3])):
                                jd_bm = ict.Test_Added01().test_Added0054(bj_id=bj_id)
                                assert jd_bm == '操作成功'
                        if bjd_bm3[1] != 0:
                            with allure.step("存在厢式车运输运输公司合同报价，查看报价单信息"):
                                bjd_bm4 = ict.Test_Added01().test_Added0101(bjd_id=bjd_bm[2],taskUnitCode="bulkcargo_transport",jd_bm=zjd_bm)
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query018(self):
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
    @pytest.mark.skip(reason="无理由跳过")
    def test_query019(self):
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
    @allure.title("司机市场报价--集装箱")
    @pytest.mark.skip(reason="无理由跳过")
    def test_query020(self):
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
                    bjd_bm2 = ict.Test_Added01().test_Added0053(bjd_id=bjd_id, transportPort=gk_id,departure=jd_bm)
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

@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('集装箱出口,业务场景一（测试点应付费用生成五条明细')
@pytest.mark.skip(reason="无理由跳过")
class Test_business_scenario1():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("新增集装箱出口订单")
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
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("集装箱出口运输订单号：{}".format(dd_xx[3])):
            pass
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单分单管理》分自有车")
    def test_business_scenario002(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
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
                    qy_jdzx = ict.Test_Added01().test_Added0058(zy_che=fd_id,gys="",hy_dt="")
                    assert qy_jdzx == '操作成功'
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单派自有车A")
    def test_business_scenario003(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[5][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[5][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[4]    #订单号
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
                    if cc_dd[2] == "car_dispatch_undistribute":
                        with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                            pass
                    if cc_dd[2] == "car_dispatch_completed":
                        fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                        assert fz_ccb == '操作成功'
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            assert bz_dd1[1] != []
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
            g_hao = ict.Test_Added01().test_Added0089(x_hao=x_hao,kg_z=kg_z,dd_id=dd_id,ft_hao=ft_hao)
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单撤销派自有车A")
    def test_business_scenario004(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            pytest.assume(hz_id1[0] == '操作成功')
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            pytest.assume(dd_xx[0] == '操作成功')
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3], lx="port_container_export_transport")
            pytest.assume(dd_xx1[0] == '操作成功')
            dd_id = dd_xx1[1]  # 订单id
        with allure.step("自有车撤销派单，订单号:{}".format(dd_xx1[4])):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        with allure.step("跟踪管理查看柜号不清空，订单:{}".format(dd_xx1[4])):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_xx1[4],fw_lx="port_container_export_transport")
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
        with allure.step("跟踪管理查看提柜节点时间跟踪清空，订单:{}".format(dd_xx1[4])):
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
        with allure.step("断言应付费用列表清空，订单:{}".format(dd_xx1[4])):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_xx1[4],fw_lx="port_container_export_transport")
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单派自有车B")
    def test_business_scenario005(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[5][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[5][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[4]    #订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')   #装货时间  年月日
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
                    if cc_dd[2] == "car_dispatch_undistribute":
                        with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                            pass
                    if cc_dd[2] == "car_dispatch_completed":
                        fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                        assert fz_ccb == '操作成功'
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤B7788",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            assert bz_dd1[1] != []
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

        with allure.step("跟踪管理查看柜号，订单:{}".format(dd_hao)):
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
        with allure.step("跟踪管理查看提柜节点时间跟踪点亮，订单:{}".format(dd_hao)):
            dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
            pytest.assume(dl_time[0]  == '操作成功')
            taskTypeName = dl_time[1][2]["taskTypeName"]
            pytest.assume(taskTypeName == '离开提柜地')    #节点名称
            time1= dl_time[1][2]
            list22 = []
            for key in time1:
                # print(key)
                if key == "finishTime":
                    # print(time1[key])
                    list22.append(key)
            pytest.assume(list22 != [])      #断言节点时间key存在
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单撤销派自有车B")
    def test_business_scenario006(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            pytest.assume(hz_id1[0] == '操作成功')
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            pytest.assume(dd_xx[0] == '操作成功')
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3], lx="port_container_export_transport")
            pytest.assume(dd_xx1[0] == '操作成功')
            dd_id = dd_xx1[1]  # 订单id
        with allure.step("自有车撤销派单，订单号:{}".format(dd_xx1[4])):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        with allure.step("跟踪管理查看柜号不清空，订单:{}".format(dd_xx1[4])):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_xx1[4],fw_lx="port_container_export_transport")
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
        with allure.step("跟踪管理查看提柜节点时间跟踪清空，订单:{}".format(dd_xx1[4])):
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
        with allure.step("断言应付费用列表清空，订单:{}".format(dd_xx1[4])):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_xx1[4],fw_lx="port_container_export_transport")
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单派自有车c")
    def test_business_scenario007(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3], lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id = dd_xx1[1]  # 订单id
            zh_time = dd_xx1[5][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[5][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[4]  # 订单号
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
                    if cc_dd[2] == "car_dispatch_undistribute":
                        with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                            pass
                    if cc_dd[2] == "car_dispatch_completed":
                        fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                        assert fz_ccb == '操作成功'
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001", zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id = cc_xx[1]  # 出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2, fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            assert bz_dd1[1] != []
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
        with allure.step("跟踪管理查看柜号，订单:{}".format(dd_hao)):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao, fw_lx="port_container_export_transport")
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
        with allure.step("跟踪管理查看提柜节点时间跟踪点亮，订单:{}".format(dd_hao)):
            dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
            pytest.assume(dl_time[0] == '操作成功')
            taskTypeName = dl_time[1][2]["taskTypeName"]
            finishTime = dl_time[1][2]["finishTime"]
            pytest.assume(taskTypeName == '离开提柜地')  # 节点名称
            pytest.assume(finishTime != [])  # 节点时间
        with allure.step("应付费用费用明细审核，订单:{}".format(dd_hao)):
            mx_sh = ict.Test_Added01().test_Added0095(mx_id=zd_id1)
            pytest.assume(mx_sh == '操作成功')
        with allure.step("应付费用费用整审，订单:{}".format(dd_hao)):
            fy_zs = ict.Test_Added01().test_Added0096(dd_id=dd_id)
            pytest.assume(fy_zs == '操作成功')
        with allure.step("断言应付费用列表订单费用状态已完成，订单:{}".format(dd_xx1[4])):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_xx1[4], fw_lx="port_container_export_transport")
            pytest.assume(fy_lb[0] == '操作成功')
            allure.attach(body=fy_lb[0], name="接口响应", attachment_type=allure.attachment_type.TEXT)
            pytest.assume(fy_lb[2]["chargeStatus"] == "status_check_all_completed")  # 断言订单费用状态已整审
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单撤销派自有车c")
    def test_business_scenario008(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            pytest.assume(hz_id1[0] == '操作成功')
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            pytest.assume(dd_xx[0] == '操作成功')
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3], lx="port_container_export_transport")
            pytest.assume(dd_xx1[0] == '操作成功')
            dd_id = dd_xx1[1]  # 订单id
        with allure.step("自有车撤销派单，订单号:{}".format(dd_xx1[4])):
            cx_pd = ict.Test_Added01().test_Added0092(dd_id=dd_id)
            pytest.assume(cx_pd == '操作成功')
        with allure.step("跟踪管理查看柜号不清空，订单:{}".format(dd_xx1[4])):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_xx1[4], fw_lx="port_container_export_transport")
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
        with allure.step("跟踪管理查看提柜节点时间跟踪清空，订单:{}".format(dd_xx1[4])):
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
        with allure.step("断言应付费用列表清空，订单:{}".format(dd_xx1[4])):
            fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_xx1[4], fw_lx="port_container_export_transport")
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单派自有车D")
    def test_business_scenario009(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[5][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[5][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[4]    #订单号
            str_datetime = zh_time
            time1 = datetime.datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")
            time2 = time1.strftime('%Y-%m-%d')   #装货时间  年月日
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
                    if cc_dd[2] == "car_dispatch_undistribute":
                        with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                            pass
                    if cc_dd[2] == "car_dispatch_completed":
                        fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                        assert fz_ccb == '操作成功'
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤B7788",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'
        with allure.step("跟踪管理查看柜号，订单:{}".format(dd_hao)):
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_hao,fw_lx="port_container_export_transport")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
        with allure.step("跟踪管理查看提柜节点时间跟踪点亮，订单:{}".format(dd_hao)):
            dl_time = ict.Test_Added01().test_Added0093(dd_id=dd_id)
            pytest.assume(dl_time[0]  == '操作成功')
            taskTypeName = dl_time[1][2]["taskTypeName"]
            pytest.assume(taskTypeName == '离开提柜地')    #节点名称
            time1= dl_time[1][2]
            list22 = []
            for key in time1:
                # print(key)
                if key == "finishTime":
                    # print(time1[key])
                    list22.append(key)
            pytest.assume(list22 != [])      #断言节点时间key存在
        with allure.step("应付费用改单查询，订单:{}".format(dd_hao)):
            yf_gd = ict.Test_Added01().test_Added0097(dd_hao=dd_hao)
            pytest.assume(yf_gd[0]  == '操作成功')
            pytest.assume(yf_gd[1][0]["renewalReason"]  == '海格原因')  #断言改单原因
            pytest.assume(yf_gd[1][0]["statusType"]  == 'status_submit_awaiting')  #断言改单状态
        with allure.step("应付费用改单提交，订单:{}".format(dd_hao)):
            gd_tj = ict.Test_Added01().test_Added0098(gd_id=yf_gd[1][0]["id"])
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

@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('厢式车多装一卸,业务场景二（测试点应付费用生成五条明细）')
@pytest.mark.skip(reason="无理由跳过")
class Test_business_scenario2():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("新增厢式车多点装货订单")
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
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("集装箱出口运输订单号：{}".format(dd_xx[3])):
            pass
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("厢式车订单分单管理》分供应商")
    def test_business_scenario002(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，分单查询，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0103(dd_hao=dd_xx[3])
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
                    qy_jdzx = ict.Test_Added01().test_Added0058(zy_che="", gys=fd_id, hy_dt="")
                    assert qy_jdzx == '操作成功'
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("厢式车订单派供应商A：手工报价")
    def test_business_scenario003(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，获取订单ID，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0103(dd_hao=dd_xx[3])
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("厢式车订单派供应商A：应付费用断言")
    def test_business_scenario004(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，获取订单ID，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0103(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
        with allure.step("应付费用基本信息明细，订单:{}".format(dd_xx[3])):
            jb_xx = ict.Test_Added01().test_Added0087(dd_id=dd_id)
            pytest.assume(jb_xx[0] == '操作成功')
            zd_id =jb_xx[1]["chargeInfo"][0]["id"]  # 账单ID
        with allure.step("应付费用费用信息明细，订单:{}".format(dd_xx[3])):
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("厢式车订单改派供应商B：合同报价")
    def test_business_scenario005(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，获取订单ID，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0103(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
        with allure.step("查看供应商id"):
            gys_id = ict.Test_Added01().test_Added0062(gys_name=cf.gys1_name)
            assert gys_id[0] == '操作成功'
        with allure.step("查看供应商联系人信息"):
            gys_xx = ict.Test_Added01().test_Added0105(gys_id=gys_id[1])
            assert gys_xx[0] == '操作成功'
            gys_lxr =  gys_xx[2]
            gys_lxrdh =  gys_xx[3]
        with allure.step("派供应商A"):
            gys_xx = ict.Test_Added01().test_Added0107(dd_id=dd_id,gys_lxr=gys_lxr,gys_lxrdh=gys_lxrdh,gys_id=gys_id[1])
            assert gys_xx == '操作成功'
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("供应商B接单，并指派车辆")
    def test_business_scenario006(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，获取订单ID，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0103(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
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

        with allure.step("应付费用基本信息明细，订单:{}".format(dd_xx[3])):
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("厢式车订单改派供应商C：手工报价")
    def test_business_scenario007(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，获取订单ID，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0103(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
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


        with allure.step("应付费用费用信息明细，订单:{}".format(dd_xx[3])):
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("厢式车订单改派供应商D：合同报价")
    def test_business_scenario008(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，获取订单ID，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0103(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("供应商D接单，并指派车辆")
    def test_business_scenario009(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询厢式车运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("计划管理，获取订单ID，订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0103(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            dd_id = fd_xx[2][0]["id"]
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
        with allure.step("断言应付费用插入改单明细信息，订单:{}".format(dd_xx[3])):
            yf_gd = ict.Test_Added01().test_Added0097(dd_hao=dd_xx[3])
            pytest.assume(yf_gd[0] == '操作成功')
            pytest.assume(yf_gd[1][0]["renewalReason"] == '海格原因')  # 断言改单原因
            pytest.assume(yf_gd[1][0]["statusType"] == 'status_submit_awaiting')  # 断言改单状态
        with allure.step("应付费用改单提交，订单:{}".format(dd_xx[3])):
            gd_tj = ict.Test_Added01().test_Added0098(gd_id=yf_gd[1][0]["id"])
            pytest.assume(gd_tj == '操作成功')
        with allure.step("应付费用改单审核，订单:{}".format(dd_xx[3])):
            gd_sh = ict.Test_Added01().test_Added0099(gd_id=yf_gd[1][0]["id"])
            pytest.assume(gd_sh == '操作成功')
        with allure.step("断言改单明细插入应付账单，订单:{}".format(dd_xx[3])):  #断言的是改单明细是否插入应付账单
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


@allure.parent_suite('ict业务场景测试用例')
@allure.suite('ict业务场景测试用例模块')
@allure.sub_suite('集装箱出口,业务场景四（测试点：柜号多路径同步）')
# @pytest.mark.skip(reason="无理由跳过")
class Test_business_scenario3():
    @pytest.mark.skip(reason="无理由跳过")
    @allure.title("新增集装箱出口订单")
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
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("集装箱出口运输订单号：{}".format(dd_xx[3])):
            pass
    @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单分单管理》分自有车")
    def test_business_scenario002(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]     #货主id
            kf_id = hz_id1[2]     #客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
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
                    qy_jdzx = ict.Test_Added01().test_Added0058(zy_che=fd_id,gys="",hy_dt="")
                    assert qy_jdzx == '操作成功'
    @pytest.mark.skip(reason="无理由跳过")
    @allure.title("集装箱出口订单派自有车A，并审核应付明细")
    def test_business_scenario003(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[5][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[5][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[4]    #订单号
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
                    if cc_dd[2] == "car_dispatch_undistribute":
                        with allure.step("出车表存在,车牌号：{}，并未分配".format(cc_dd[4])):
                            pass
                    if cc_dd[2] == "car_dispatch_completed":
                        fz_ccb = ict.Test_Added01().test_Added0084(ccb_id=cc_dd[1])
                        assert fz_ccb == '操作成功'
        with allure.step("维护出车表信息"):
            cc_xx = ict.Test_Added01().test_Added0074(sj_id=sj_id, cp_hao="粤ZZ0001",zh_time=time2)
            assert cc_xx[0] == '操作成功'
            ccb_id =  cc_xx[1]   #出车表ID
        with allure.step("调度管理，获取车牌号:{}".format(cc_xx[4])):
            bz_dd1 = ict.Test_Added01().test_Added0085(zh_time=time2,fw_lx="port_container_export_transport")
            assert bz_dd1[0] == '操作成功'
            assert bz_dd1[1] != []
        with allure.step("调度管理，派自有车，订单号：{}".format(dd_hao)):
            pzyc = ict.Test_Added01().test_Added0075(id=dd_id,driverId=sj_id,supplierId=gys_id,mainlandLicensePlateNumber=cp_hao,
                                                      orderNumber=dd_hao,pickupTime=zh_time,transportType="transport_type_one_one",
                                                      mainlandLicensePlate=cl_id,driverName=sj_name,mainlandPhone=sj_haoma,supplierName=gyl_name,
                                                      carDispatchId=ccb_id)
            assert pzyc == '操作成功'
    @pytest.mark.skip(reason="无理由跳过")
    @allure.title("跟踪管理，柜号录入")
    def test_business_scenario004(self):
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("查询新增集装箱出口运输订单信息"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
        with allure.step("查询调度管理集装箱出口运输订单信息"):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3],lx="port_container_export_transport")
            assert dd_xx1[0] == '操作成功'
            dd_id =  dd_xx1[1]   #订单id
            zh_time = dd_xx1[5][0]["pickupTime"]    #装货时间  年月日时分秒
            cz_qy = dd_xx1[5][0]["operationGroup"]   # 操作区域
            dd_hao = dd_xx1[4]    #订单号
        with allure.step("手动录入柜号，订单:{}".format(dd_hao)):
            x_hao = "FSCU5130217"
            ft_hao = "CAAU5507656"
            kg_z = "2580"
            g_hao = ict.Test_Added01().test_Added0089(x_hao=x_hao,kg_z=kg_z,dd_id=dd_id,ft_hao=ft_hao)
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
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("查看同步柜号")
    def test_business_scenario005(self):
        x_hao = "FSCU5130217"
        ft_hao = "CAAU5507656"
        kg_z = 2580
        with allure.step("查看货主id，货主：{}".format(cf.hz_name)):
            hz_id1 = ict.Test_Added01().test_Added0012(hz_name=cf.hz_name)
            assert hz_id1[0] == '操作成功'
            hz_id = hz_id1[1]  # 货主id
            kf_id = hz_id1[2]  # 客服id
        with allure.step("订单管理》订单录入列表，查看同步柜号"):
            dd_xx = ict.Test_Added01().test_Added0056(hz_id=hz_id)
            assert dd_xx[0] == '操作成功'
            xianghao1 =  dd_xx[6]["containerNumber"]
            fengtiao1 =  dd_xx[6]["sealNumber"]
            konggui1 = dd_xx[6]["cabinetWeight"]
            pytest.assume(x_hao == xianghao1)
            pytest.assume(ft_hao == fengtiao1)
            pytest.assume(kg_z == konggui1)
        with allure.step("订单管理》集装箱运输列表，查看同步柜号,订单号：{}".format(dd_xx[3])):
            jzx_ys = ict.Test_Added01().test_Added0117(hz_id=hz_id)
            assert jzx_ys[0] == '操作成功'
            xianghao2 =  jzx_ys[1][0]["containerNumber"]
            fengtiao2 =  jzx_ys[1][0]["sealNumber"]
            konggui2 = jzx_ys[1][0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao2)
            pytest.assume(ft_hao == fengtiao2)
            pytest.assume(kg_z == konggui2)
        with allure.step("运单管理>计划管理>集装箱>订单号：{}".format(dd_xx[3])):
            fd_xx = ict.Test_Added01().test_Added0057(dd_hao=dd_xx[3])
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 4
            data2 = fd_xx[2]
            xianghao3 =  data2[0]["containerNumber"]
            fengtiao3 =  data2[0]["sealNumber"]
            konggui3 = data2[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao3)
            pytest.assume(ft_hao == fengtiao3)
            pytest.assume(kg_z == konggui3)
            xianghao4 =  data2[1]["containerNumber"]
            fengtiao4 =  data2[1]["sealNumber"]
            konggui4 = data2[1]["cabinetWeight"]
            pytest.assume(x_hao == xianghao4)
            pytest.assume(ft_hao == fengtiao4)
            pytest.assume(kg_z == konggui4)
            xianghao5 =  data2[2]["containerNumber"]
            fengtiao5 =  data2[2]["sealNumber"]
            konggui5 = data2[2]["cabinetWeight"]
            pytest.assume(x_hao == xianghao5)
            pytest.assume(ft_hao == fengtiao5)
            pytest.assume(kg_z == konggui5)
            xianghao6 =  data2[3]["containerNumber"]
            fengtiao6 =  data2[3]["sealNumber"]
            konggui6 = data2[3]["cabinetWeight"]
            pytest.assume(x_hao == xianghao6)
            pytest.assume(ft_hao == fengtiao6)
            pytest.assume(kg_z == konggui6)
        with allure.step("运单管理>调度管理>集装箱>订单号：{}").format(dd_xx[3]):
            dd_xx1 = ict.Test_Added01().test_Added0083(dd_hao=dd_xx[3], lx="")
            assert dd_xx1[0] == '操作成功'
            data3 = dd_xx1[5]
            xianghao7 = data3[0]["containerNumber"]
            fengtiao7 = data3[0]["sealNumber"]
            konggui7 = data3[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_z == konggui7)
            xianghao8 = data3[1]["containerNumber"]
            fengtiao8 = data3[1]["sealNumber"]
            konggui8 = data3[1]["cabinetWeight"]
            pytest.assume(x_hao == xianghao8)
            pytest.assume(ft_hao == fengtiao8)
            pytest.assume(kg_z == konggui8)
            xianghao9 = data3[2]["containerNumber"]
            fengtiao9 = data3[2]["sealNumber"]
            konggui9 = data3[2]["cabinetWeight"]
            pytest.assume(x_hao == xianghao9)
            pytest.assume(ft_hao == fengtiao9)
            pytest.assume(kg_z == konggui9)
            xianghao11 = data3[3]["containerNumber"]
            fengtiao11 = data3[3]["sealNumber"]
            konggui11 = data3[3]["cabinetWeight"]
            pytest.assume(x_hao == xianghao11)
            pytest.assume(ft_hao == fengtiao11)
            pytest.assume(kg_z == konggui11)
        with allure.step("运单管理>监理管理>订单号：{}").format(dd_xx[3]):
            jl_gl = ict.Test_Added01().test_Added0118(dd_hao=dd_xx[3])
            assert jl_gl[0] == '操作成功'
            data4 =  jl_gl[1]
            xianghao7 = data4[0]["containerNumber"]
            fengtiao7 = data4[0]["sealNumber"]
            konggui7 = data4[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_z == konggui7)
        with allure.step("运单管理>监理管理>订单号：{}").format(dd_xx[3]):
            bg_gl = ict.Test_Added01().test_Added0119(dd_hao=dd_xx[3])
            assert bg_gl[0] == '操作成功'
            data5 = bg_gl[1]
            xianghao7 = data5[0]["containerNumber"]
            fengtiao7 = data5[0]["sealNumber"]
            konggui7 = data5[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_z == konggui7)
        with allure.step("跟踪管理>集装箱>订单:{}".format(dd_xx[3])):
            ck_g_hao = ict.Test_Added01().test_Added0091(dd_hao=dd_xx[3],fw_lx="")
            pytest.assume(ck_g_hao[0] == '操作成功')
            pytest.assume(ck_g_hao[1][0]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][0]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][0]["cabinetWeight"] == kg_z)
            pytest.assume(ck_g_hao[1][1]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][1]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][1]["cabinetWeight"] == kg_z)
            pytest.assume(ck_g_hao[1][2]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][2]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][2]["cabinetWeight"] == kg_z)
            pytest.assume(ck_g_hao[1][3]["containerNumber"] == x_hao)
            pytest.assume(ck_g_hao[1][3]["sealNumber"] == ft_hao)
            pytest.assume(ck_g_hao[1][3]["cabinetWeight"] == kg_z)
        with allure.step("跟踪管理>监理管理>订单号：{}").format(dd_xx[3]):
            gz_jl = ict.Test_Added01().test_Added0120(dd_hao=dd_xx[3])
            assert gz_jl[0] == '操作成功'
            data7 = gz_jl[1]
            xianghao7 = data7[0]["containerNumber"]
            fengtiao7 = data7[0]["sealNumber"]
            konggui7 = data7[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_z == konggui7)
        with allure.step("跟踪管理>监理管理>订单号：{}").format(dd_xx[3]):
            gz_bg = ict.Test_Added01().test_Added0121(dd_hao=dd_xx[3])
            assert gz_bg[0] == '操作成功'
            data8 = gz_bg[1]
            xianghao7 = data8[0]["containerNumber"]
            fengtiao7 = data8[0]["sealNumber"]
            konggui7 = data8[0]["cabinetWeight"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
            pytest.assume(kg_z == konggui7)
        with allure.step("应收费用制作>订单号：{}").format(dd_xx[3]):
            ys_fy = ict.Test_Added01().test_Added0086(dd_hao=dd_xx[3])
            assert ys_fy[0] == '操作成功'
            data9 = ys_fy[1]
            xianghao7 = data9[0]["containerNumber"]
            fengtiao7 = data9[0]["sealNumber"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)
        with allure.step("应付费用制作>订单号：{}").format(dd_xx[3]):
            yf_fy = ict.Test_Added01().test_Added0094(dd_hao=dd_xx[3])
            assert yf_fy[0] == '操作成功'
            data11 = yf_fy[2]
            xianghao7 = data11[0]["containerNumber"]
            fengtiao7 = data11[0]["sealNumber"]
            pytest.assume(x_hao == xianghao7)
            pytest.assume(ft_hao == fengtiao7)


            #qqqqqq