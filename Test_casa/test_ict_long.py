#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: test_ict_long.py
# @Time:2023/2/28 11:12
# @Author:PH
from Common import ict_api as ict
import allure
import pytest
import requests,json
# myskip = pytest.mark.skipif()

@allure.parent_suite('ict登录接口测试包')  # 包的注释
@allure.suite('ict登录t接口测试模块')   #模块的注释
@allure.sub_suite('各端登录接口')      #大类的注释
@myskip
# @pytest.mark.skip(reason="无理由跳过")
class Test_login_01():
    '''大类'''
    def setup_class(self):
        '''大类前置'''
        pass
    def teardown_class(self):
        '''大类后置'''
        pass
    @allure.title("后台端登录接口")   #类方法的注释
    def test_long001(self):
        '''用例描述'''
        with allure.step("调取后台端登录接口返回token不为空"):
            cf=ict.Test_login().Test_login001()
            # 接口自动化
            allure.attach(body=cf[1], name="请求地址", attachment_type=allure.attachment_type.TEXT)
            assert cf[0] !=None
    @allure.title("货主端登录接口")   #类方法的注释
    def test_long002(self):
        '''用例描述'''
        with allure.step("调取货主端登录接口返回token不为空"):
            cf=ict.Test_login().Test_login002()
            # 接口自动化
            allure.attach(body=cf[1], name="请求地址", attachment_type=allure.attachment_type.TEXT)
            assert cf[0] !=None
    @allure.title("运输公司端登录接口")   #类方法的注释
    def test_long003(self):
        '''用例描述'''
        with allure.step("调取运输公司端登录接口返回token不为空"):
            cf=ict.Test_login().Test_login003()
            # 接口自动化
            allure.attach(body=cf[1], name="请求地址", attachment_type=allure.attachment_type.TEXT)
            assert cf[0] !=None
    # @allure.title("司机小程序端登录接口")   #类方法的注释
    # def test_long004(self):
    #     '''用例描述'''
    #     with allure.step("调取司机小程序端登录接口返回操作成功"):
    #         cf=ict.Test_login().Test_login005()
    #         assert cf != None
    # @allure.title("司机小程序端获取界面接口")   #类方法的注释
    # def test_long005(self):
    #     '''用例描述'''
    #     with allure.step("调取司机小程序端登录接口返回操作成功"):
    #         cf=ict.Test_login().Test_login005()[1]
    #         assert cf == '操作成功'
'''后台查询接口'''
@allure.parent_suite('ict后台查询接口测试包')  # 包的注释
@allure.suite('ict后台查询接口测试模块')  # 模块的注释
@allure.sub_suite('后台端查询接口')      #大类的注释
@myskip
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
@allure.parent_suite('ict货主查询接口测试包')  # 包的注释
@allure.suite('ict货主查询接口测试模块')  # 模块的注释
@allure.sub_suite('货主端查询接口')      #大类的注释
@myskip
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
@allure.parent_suite('ict运输公司查询接口测试包')  # 包的注释
@allure.suite('ict运输公司查询接口测试模块')  # 模块的注释
@allure.sub_suite('运输公司端查询接口')      #大类的注释
@myskip
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
