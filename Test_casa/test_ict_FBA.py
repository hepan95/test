#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: test_ict_scene.py.py
# @Time:2023/8/11 08:35
# @Author:PH

import datetime
import time
import allure
import pytest
# from pytest_assume.plugin import assume
myskip = pytest.mark.skipif()
from Common import common_funtion as pz #获取项目地址
from Common import ict_api as ict
from Config import config as cf
from Common import common_funtion as bf
hz_token = ict.Test_login().Test_login005()  #货主
ht_token = ict.Test_login().Test_login004()  #后台
ht_host_FBA = cf.ht_host_FBA  #后台
hz_host_FBA = cf.hz_host_FBA  #货主


@allure.parent_suite('FBA业务场景测试用例')
@allure.suite('FBA业务场景测试用例模块')
@allure.sub_suite('业务场景十 FBA')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso1():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景十（测试点：<盐田模板>订单1按推荐报价生产-回退-编辑立即下单-回退-订单1,2合并询价单--订单3 加入合并-查看可合并询价单-合并询价单 ")
    def test_business_scenario001(self):
        with allure.step("获取货主ID"):
            hz_name = ict.Test_Added01().test_Added0185(ht_host=ht_host_FBA,hz_name=cf.hz_name_FBA,token=ht_token)
            assert hz_name[0] == '操作成功'
            hz_id = hz_name[1]

        with allure.step("后台获取导入询价模板ID"):
            modelName = ict.Test_Added01().test_Added0184(ht_host=ht_host_FBA,modelName="询价管理导入-盐田",token=ht_token)
            assert modelName[0] == '操作成功'
            modelid = modelName[1]

        with allure.step("获取导入询价模板,第一个订单"):
            time1 = bf.Common_page().get_today001()[12]  #获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[11]  #获取当前时间年月日
            ALO1 = 'AL0-T'+time1   #询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls" #模板IP路径
            bf.Common_page().read_excel(file_path=Template_path,ALO=ALO1,time1=time2,pygidium="No")

        with allure.step("货主导入询价模板,第一个订单,ALO号：{}".format(ALO1)):
            to_channel = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA,mb_id=modelid,wj_name="FBA_inquiry_list.xls",wj_dz=Template_path,token=hz_token)
            assert to_channel == '导入成功,操作成功'

        with allure.step("货主导入询价模板,第一个订单信息,第一个订单ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            orderNumber1 = order_info[2][0]["orderNumber"]  #询价单号
            enquiry_id1 = order_info[2][0]["id"]                #询价单id
            status = order_info[2][0]["orderStatus"]  #询价单状态
            pytest.assume(status == "status_draft")  # 断言订单状态：草稿
            time.sleep(1)
        with allure.step("后台查看邮件日志，询价单导入触发邮件通知，,第一个询价单号：{}".format(ALO1)):
            subject = ALO1 + "询价结果"
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA,token=ht_token,subject=subject)
            assert enquiry_log[0] == '操作成功'
            pytest.assume(enquiry_log[1] == 1)  # 断言订单状态：存在询价日志

        with allure.step("获取图片地址上传附件,,第一个订单询价单号：{}".format(orderNumber1)):
            tu_dz = pz.Common_page().projects_path() + r"\Common\picture\2.02 MB.JPG"  # 图片地址

        with allure.step("货主上传图片，,第一个订单获取图片id"):
            tp_id = ict.Shipperapi().test_Added004(tp_lj=tu_dz,hz_host=hz_host_FBA,token=hz_token)  # 获取图片id
            assert tp_id[1] == "success"

        with allure.step("货主询价导入》上传附件，,第一个订单询价单号{}".format(orderNumber1)):
            sc_tp = ict.Shipperapi().test_Added005(hz_host=hz_host_FBA,token=hz_token,id=enquiry_id1,tp_name="2.02 MB.JPG",tp_id=tp_id[0])
            assert sc_tp == "操作成功"

        with allure.step("货主询价导入》按推荐报价生成，,第一个订单询价单号{}".format(orderNumber1)):
            Recommend_puotation = ict.Shipperapi().test_Added006(hz_host=hz_host_FBA,id=enquiry_id1,token=hz_token)
            assert Recommend_puotation == "操作成功"

        with allure.step("货主导入询价模板,第一个订单状态,第一个订单ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            customerOrderNumber1 = order_info[2][0]["customerOrderNumber"]  #订单号
            status = order_info[2][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_generated")  # 断言订单状态：已生成

        time.sleep(5)
        with allure.step("后台查看邮件日志，按推荐报价下单入触发邮件通知,第一个订单订单号：{}".format(customerOrderNumber1)):
            subject = "【{},{}】已下单".format(customerOrderNumber1,ALO1)
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA,token=ht_token,subject=subject)
            assert enquiry_log[0] == '操作成功'
            pytest.assume(enquiry_log[1] != 0)  # 断言订单状态：存在下单日志

        with allure.step("后台查看订单状态，,第一个订单订单号：{}".format(customerOrderNumber1)):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1)
            assert ht_order_info[0] == '操作成功'
            customerOrderId1 = ht_order_info[1][0]["id"]    #订单id
            status = ht_order_info[1][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_pending")  # 断言订单状态：待接单

        with allure.step("后台第一次回退订单，,第一个订单订单号：{}".format(customerOrderNumber1)):
            Backspace = ict.Test_Added01().test_Added0188(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1,order_id=customerOrderId1)
            assert Backspace == '操作成功'

        with allure.step("货主查看回退后状态,,第一个订单ALO号：{}".format(ALO1)):
            order_state = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_state[0] == '操作成功'
            status = order_state[2][0]["orderStatus"]  #询价单状态
            pytest.assume(status == "status_draft")  # 断言订单状态：草稿

        with allure.step("货主查看订单详情页,,第一个订单ALO号：{}".format(ALO1)):
            Detail_Pages1 = ict.Shipperapi().test_Added007(hz_host=hz_host_FBA,token=hz_token,id=enquiry_id1)
            assert Detail_Pages1[0] == '操作成功'
            data1 = ict.get_k(Detail_Pages1[1])
            otherFile1 =  Detail_Pages1[1]["otherFile"]  #附件信息

        with allure.step("货主编辑》立即下单,,第一个订单ALO号：{}".format(ALO1)):
            immediately_place = ict.Shipperapi().test_Added008(hz_host=hz_host_FBA,token=hz_token,data1=data1)
            assert immediately_place[0] == '操作成功'

        with allure.step("编辑立即下单,查看订单号,第一个订单ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            customerOrderNumber2 = order_info[2][0]["customerOrderNumber"]  #订单号
            time.sleep(1)
        with allure.step("后台查看邮件日志，编辑立即下单入触发邮件通知,第一个订单订单号：{}".format(customerOrderNumber2)):
            subject = "【{},{}】已下单".format(customerOrderNumber2,ALO1)
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA,token=ht_token,subject=subject)
            assert enquiry_log[0] == '操作成功'
            pytest.assume(enquiry_log[1] != 0)  # 断言订单状态：存在下单日志

        with allure.step("编辑立即下单，后台查看订单状态，,第一个订单ALO号：{}".format(ALO1)):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber2)
            assert ht_order_info[0] == '操作成功'
            customerOrderId2 = ht_order_info[1][0]["id"]    #订单id

        with allure.step("后台第二次回退订单，,第一个订单ALO号：{}".format(ALO1)):
            Backspace = ict.Test_Added01().test_Added0188(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber2,order_id=customerOrderId2)
            assert Backspace == '操作成功'

        with allure.step("获取导入询价模板,第二个订单"):
            time1 = bf.Common_page().get_today001()[12]  #获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[11]  #获取当前时间年月日
            ALO2 = 'AL0-T'+time1   #询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls" #模板IP路径
            bf.Common_page().read_excel(file_path=Template_path,ALO=ALO2,time1=time2,pygidium="No")

        with allure.step("货主导入询价模板,第二个订单,ALO号：{}".format(ALO2)):
            to_channel2 = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA,mb_id=modelid,wj_name="FBA_inquiry_list.xls",wj_dz=Template_path,token=hz_token)
            assert to_channel2 == '导入成功,操作成功'

        with allure.step("货主导入询价模板,第二个订单,第二个订单ALO号：{}".format(ALO2)):
            order_info2 = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO2,token=hz_token)
            assert order_info2[0] == '操作成功'
            assert order_info2[1] != 0
            orderNumber2 = order_info2[2][0]["orderNumber"]  #询价单号
            enquiry_id2 = order_info2[2][0]["id"]                #询价单id
            status = order_info2[2][0]["orderStatus"]  #询价单状态
            pytest.assume(status == "status_draft")  # 断言订单状态：草稿

        with allure.step("货主查看订单详情页,,第二个订单ALO号：{}".format(ALO2)):
            Detail_Pages2 = ict.Shipperapi().test_Added007(hz_host=hz_host_FBA,token=hz_token,id=enquiry_id2)
            assert Detail_Pages2[0] == '操作成功'
            time_loading =  Detail_Pages2[1]["pickupTime"]   #装货时间
            departure =  Detail_Pages2[1]["departure"]["value"]  #装货街道
            departureArea =  Detail_Pages2[1]["departureArea"]["value"]  #装货区
            destination =  Detail_Pages2[1]["destination"]["value"]  #卸货街道
            destinationArea =  Detail_Pages2[1]["destinationArea"]["value"]  #卸货区
            departureCity =  Detail_Pages2[1]["departureCity"]["value"]  #卸货市
            destinationCity =  Detail_Pages2[1]["destinationCity"]["value"]  #卸货市
            consignorContactAddr = Detail_Pages2[1]["consignorContactAddr"]  #详细装货地址
            balanceCompany = Detail_Pages2[1]["balanceCompany"]  #结算单位
            enquiry_id2 = Detail_Pages2[1]["id"]             #询价单id
            goodsName = Detail_Pages2[1]["goodsName"]        #商品名称
            goodsNumber = Detail_Pages2[1]["goodsNumber"]*2        #箱数
            piecesNumber =  Detail_Pages2[1]["piecesNumber"]*2        #件数
            volume  =  Detail_Pages2[1]["volume"]*2        #体积
            weight =  Detail_Pages2[1]["weight"]*2        #毛重
            netWeight  =  Detail_Pages2[1]["netWeight"]*2        #货物总净重
            goodsTotalAmount =  Detail_Pages2[1]["goodsTotalAmount"]*2        #货物总价
            time.sleep(1)
        with allure.step("后台查看邮件日志，询价单导入触发邮件通知，,第二个询价单号：{}".format(ALO2)):
            subject = ALO2 + "询价结果"
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA,token=ht_token,subject=subject)
            assert enquiry_log[0] == '操作成功'
            pytest.assume(enquiry_log[1] == 1)  # 断言订单状态：存在询价日志

        with allure.step("第一个订单ALO号：{}，第二个订单ALO号：{},查看合并报价，".format(ALO1,ALO2)):
            merge_offer = ict.Shipperapi().test_Added011(hz_host=hz_host_FBA,token=hz_token,customerId=hz_id,pickupTime=time_loading,departureList=departure,
                                                         departureAreaList=departureArea,destinationList=destination,destinationAreaList=destinationArea,
                                                         departureCityList=departureCity,consigneeCityList=destinationCity,balanceCompany=balanceCompany,
                                                         departureAddressList=consignorContactAddr,weight=weight,volume=volume,isTailboard=0)
            assert merge_offer[0] == '操作成功'
            data3 = merge_offer[1]
            mergeList = [
                {
                    "sequence":0,
                    "id":enquiry_id1
                },
                {
                    "sequence":1,
                    "id":enquiry_id2
                }
            ]
            customerDelegateCode = "{},{}".format(ALO1,ALO2)
            data3.update(
                [("mergeList", mergeList), ("otherFile", otherFile1), ("customerId", hz_id), ("taskUnitTypeName", "厢式车运输"),
                 ("taskUnitCode","bulkcargo_transport"), ("pickupTime",time_loading), ("goodsName",goodsName), ("isTailboard", 0),
                 ("isStack", 0), ("customerDelegateCode",customerDelegateCode), ("goodsNumber",goodsNumber), ("piecesNumber",piecesNumber),
                 ("volume",volume), ("weight",weight), ("netWeight",netWeight), ("goodsTotalAmount",goodsTotalAmount), ("palletsSize", "")])

        with allure.step("合并报价提交"):
            create_order = ict.Shipperapi().test_Added009(hz_host=hz_host_FBA,token=hz_token,data1=data3)
            assert create_order[0] == '操作成功'
            orderNumber = create_order[1]["orderNumber"]   #询价单号
            order_id =  create_order[1]["id"]               #询价单id

        with allure.step("查看货主合并询价单信息,合并询价单号：{}".format(orderNumber)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            customerOrderNumber1 = order_info[2][0]["customerOrderNumber"]  #订单号
            status = order_info[2][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_generated")  # 断言订单状态：已生成
            time.sleep(1)
        with allure.step("后台查看邮件日志，第一第二询价单合并下单入触发邮件通知，询价单号：{}，{}".format(ALO1,ALO2)):
            subject = "【{},{},{}】已下单".format(customerOrderNumber1,ALO1,ALO2)
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA,token=ht_token,subject=subject)
            assert enquiry_log[0] == '操作成功'
            pytest.assume(enquiry_log[1] != 0)  # 断言订单状态：存在下单日志

        with allure.step("后台查看订单状态，,合并询价单号：{}".format(orderNumber)):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1)
            assert ht_order_info[0] == '操作成功'
            customerOrderId1 = ht_order_info[1][0]["id"]    #订单id
            status = ht_order_info[1][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_pending")  # 断言订单状态：待接单

        with allure.step("后台第一次回退订单，,合并询价单号：{}".format(orderNumber)):
            Backspace = ict.Test_Added01().test_Added0188(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1,order_id=customerOrderId1)
            assert Backspace == '操作成功'

        with allure.step("货主查看回退后状态,,合并询价单：{}".format(orderNumber)):
            order_state = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_state[0] == '操作成功'
            status = order_state[2][0]["orderStatus"]  #询价单状态
            pytest.assume(status == "status_merge")  # 断言订单状态：已合并

        with allure.step("获取导入询价模板,第三个订单"):
            time1 = bf.Common_page().get_today001()[12]  #获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[11]  #获取当前时间年月日
            ALO3 = 'AL0-T'+time1   #询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls" #模板IP路径
            bf.Common_page().read_excel(file_path=Template_path,ALO=ALO3,time1=time2,pygidium="No")

        with allure.step("货主导入询价模板,第三个订单,ALO号：{}".format(ALO3)):
            to_channel3 = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA,mb_id=modelid,wj_name="FBA_inquiry_list.xls",wj_dz=Template_path,token=hz_token)
            assert to_channel3 == '导入成功,操作成功'

        with allure.step("货主导入询价模板,第三个订单,第三个订单ALO号：{}".format(ALO3)):
            order_info3 = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO3,token=hz_token)
            assert order_info3[0] == '操作成功'
            assert order_info3[1] != 0
            orderNumber3 = order_info3[2][0]["orderNumber"]  #询价单号
            enquiry_id3 = order_info3[2][0]["id"]                #询价单id
            status3 = order_info3[2][0]["orderStatus"]  #询价单状态
            pytest.assume(status3 == "status_draft")  # 断言订单状态：草稿
            time.sleep(1)
        with allure.step("后台查看邮件日志，询价单导入触发邮件通知，,第三个询价单号：{}".format(ALO3)):
            subject = ALO3 + "询价结果"
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA,token=ht_token,subject=subject)
            assert enquiry_log[0] == '操作成功'
            pytest.assume(enquiry_log[1] == 1)  # 断言订单状态：存在询价日志

        with allure.step("货主查看订单详情页,,第三个订单ALO号：{}".format(ALO3)):
            Detail_Pages3 = ict.Shipperapi().test_Added007(hz_host=hz_host_FBA,token=hz_token,id=enquiry_id2)
            assert Detail_Pages3[0] == '操作成功'
            time_loading =  Detail_Pages3[1]["pickupTime"]   #装货时间
            departure =  Detail_Pages3[1]["departure"]["value"]  #装货街道
            departureArea =  Detail_Pages3[1]["departureArea"]["value"]  #装货区
            destination =  Detail_Pages3[1]["destination"]["value"]  #卸货街道
            destinationArea =  Detail_Pages3[1]["destinationArea"]["value"]  #卸货区
            departureCity =  Detail_Pages3[1]["departureCity"]["value"]  #卸货市
            destinationCity =  Detail_Pages3[1]["destinationCity"]["value"]  #卸货市
            consignorContactAddr = Detail_Pages3[1]["consignorContactAddr"]  #详细装货地址
            balanceCompany = Detail_Pages3[1]["balanceCompany"]  #结算单位
            enquiry_id3 = Detail_Pages3[1]["id"]             #询价单id
            goodsName = Detail_Pages3[1]["goodsName"]        #商品名称
            goodsNumber = Detail_Pages3[1]["goodsNumber"]*3        #箱数
            piecesNumber =  Detail_Pages3[1]["piecesNumber"]*3        #件数
            volume  =  Detail_Pages3[1]["volume"]*3        #体积
            weight =  Detail_Pages3[1]["weight"]*3        #毛重
            netWeight  =  Detail_Pages3[1]["netWeight"]*3        #货物总净重
            goodsTotalAmount =  Detail_Pages3[1]["goodsTotalAmount"]*3        #货物总价

        with allure.step("第一个订单ALO号：{}，第二个订单ALO号：{},第三个订单ALO号：{}，查看合并报价，".format(ALO1,ALO2,ALO3)):
            merge_offer2 = ict.Shipperapi().test_Added011(hz_host=hz_host_FBA,token=hz_token,customerId=hz_id,pickupTime=time_loading,departureList=departure,
                                                         departureAreaList=departureArea,destinationList=destination,destinationAreaList=destinationArea,
                                                         departureCityList=departureCity,consigneeCityList=destinationCity,balanceCompany=balanceCompany,
                                                         departureAddressList=consignorContactAddr,weight=weight,volume=volume,isTailboard=0)
            assert merge_offer2[0] == '操作成功'
            data4 = merge_offer2[1]
            mergeList = [
                {
                    "sequence":0,
                    "id":enquiry_id1
                },
                {
                    "sequence":1,
                    "id":enquiry_id2
                },
                {
                    "sequence": 3,
                    "id": enquiry_id3
                }
            ]
            customerDelegateCode = "{},{},{}".format(ALO1,ALO2,ALO3)
            data4.update(
                [("mergeList", mergeList), ("otherFile", otherFile1), ("customerId", hz_id), ("taskUnitTypeName", "厢式车运输"),
                 ("taskUnitCode","bulkcargo_transport"), ("pickupTime",time_loading), ("goodsName",goodsName), ("isTailboard", 0),
                 ("isStack", 0), ("customerDelegateCode",customerDelegateCode), ("goodsNumber",goodsNumber), ("piecesNumber",piecesNumber),
                 ("volume",volume), ("weight",weight), ("netWeight",netWeight), ("goodsTotalAmount",goodsTotalAmount), ("palletsSize", "")])
            # print("这个是报文{}".format(data4))

        with allure.step("合并报价保存"):
            create_order2 = ict.Shipperapi().test_Added010(hz_host=hz_host_FBA,token=hz_token,data1=data4)
            assert create_order2[0] == '操作成功'
            orderNumber = create_order2[1]["orderNumber"]   #询价单号
            order_id =  create_order2[1]["id"]               #询价单id
            # print("合并三个询价单的订单号：{}".format(orderNumber))

        with allure.step("取消合并询价单"):
            create_order2 = ict.Shipperapi().test_Added012(hz_host=hz_host_FBA,token=hz_token,order_id=order_id)
            assert create_order2 == '操作成功'

        with allure.step("取消合并后询价单状态,第一个订单ALO号：{}".format(ALO1)):
            order_state = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_state[0] == '操作成功'
            status = order_state[2][0]["orderStatus"]  #询价单状态
            pytest.assume(status == "status_merge")  # 断言订单状态：已合并

        with allure.step("草稿合并报价提交"):
            create_order = ict.Shipperapi().test_Added009(hz_host=hz_host_FBA,token=hz_token,data1=data4)
            assert create_order[0] == '操作成功'
            orderNumber = create_order[1]["orderNumber"]   #询价单号
            order_id =  create_order[1]["id"]               #询价单id

        with allure.step("查看货主合并询价单信息,合并询价单号：{}".format(orderNumber)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA, hz_id=hz_id, xj_dh=ALO1, token=hz_token)
            assert order_info[0] == '操作成功'
            customerOrderNumber1 = order_info[2][0]["customerOrderNumber"]  # 订单号
            status = order_info[2][0]["orderStatus"]  # 订单状态
            pytest.assume(status == "status_generated")  # 断言订单状态：已生成
            time.sleep(1)
        with allure.step("后台查看邮件日志，三个询价单合并下单入触发邮件通知,询价单号：{},{},{}".format(ALO1,ALO2,ALO3)):
            subject = "【{},{},{},{}】已下单".format(customerOrderNumber1,ALO1,ALO2,ALO3)
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA,token=ht_token,subject=subject)
            assert enquiry_log[0] == '操作成功'
            pytest.assume(enquiry_log[1] != 0)  # 断言订单状态：存在下单日志

        with allure.step("草稿合并报价提交，后台查看订单状态，,合并询价单号：{}".format(orderNumber)):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1)
            assert ht_order_info[0] == '操作成功'
            customerOrderId1 = ht_order_info[1][0]["id"]    #订单id
            status = ht_order_info[1][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_pending")  # 断言订单状态：待接单

        with allure.step("后台，取消订单,合并询价单号：{}".format(orderNumber)):
            cancellation_order = ict.Test_Added01().test_Added0189(ht_host=ht_host_FBA,token=ht_token,order_id=customerOrderId1)
            assert cancellation_order == '操作成功'

        with allure.step("取消订单，后台查看订单状态，,合并询价单号：{}".format(orderNumber)):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1)
            assert ht_order_info[0] == '操作成功'
            customerOrderId1 = ht_order_info[1][0]["id"]    #订单id
            status = ht_order_info[1][0]["orderStatus"]  #订单状态
            customerOrderNumber = ht_order_info[1][0]["orderNumber"]   #订单号
            pytest.assume(status == "status_undo_completed")  # 断言订单状态：已撤销

        with allure.step("货主查看回退后状态,,合并询价单：{}".format(orderNumber)):
            list_inquire = ict.Shipperapi().test_Added013(hz_host=hz_host_FBA,customerId=hz_id,orderNumber=customerOrderNumber,token=hz_token)
            assert list_inquire[0] == '操作成功'
            orderStatus = list_inquire[1][0]["orderStatus"]
            pytest.assume(orderStatus == "status_undo_completed")  # 断言订单状态：已撤销


@allure.parent_suite('FBA业务场景测试用例')
@allure.suite('FBA业务场景测试用例模块')
@allure.sub_suite('业务场景十一 ')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso2():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("期望提货时间，表格时间小于邮件接收时间，取邮件接收时间+2,周末顺延 ")
    def test_business_scenario001(self):
        with allure.step("获取货主ID"):
            hz_name = ict.Test_Added01().test_Added0185(ht_host=ht_host_FBA,hz_name=cf.hz_name_FBA,token=ht_token)
            assert hz_name[0] == '操作成功'
            hz_id = hz_name[1]
        with allure.step("获取导入询价模板ID"):
            modelName = ict.Test_Added01().test_Added0184(ht_host=ht_host_FBA,modelName="询价管理导入-盐田",token=ht_token)
            assert modelName[0] == '操作成功'
            modelid = modelName[1]
        with allure.step("获取导入询价模板,第一个订单"):
            time1 = bf.Common_page().get_today001()[12]  #获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[11]  #获取当前时间年月日
            ALO1 = 'AL0-T'+time1   #询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls" #模板IP路径
            bf.Common_page().read_excel(file_path=Template_path,ALO=ALO1,time1=time2,pygidium="No")
        with allure.step("导入询价模板,第一个订单,ALO号：{}".format(ALO1)):
            to_channel = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA,mb_id=modelid,wj_name="FBA_inquiry_list.xls",wj_dz=Template_path,token=hz_token)
            assert to_channel == '导入成功,操作成功'
        with allure.step("导入询价模板,第一个订单信息,ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            orderNumber = order_info[2][0]["orderNumber"]
            time.sleep(1)
        with allure.step("后台查看邮件日志，询价单导入触发邮件通知，,第一个询价单号：{}".format(ALO1)):
            subject = ALO1 + "询价结果"
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA, token=ht_token, subject=subject)
            assert enquiry_log[0] == '操作成功'
            Attachment_neme = enquiry_log[2][0]["mailFile"]  #附件名称
            enquiry_name = enquiry_log[2][0]["subject"]  #询价单名称  "AL0-T230816154531询价结果"
            pytest.assume(enquiry_log[1] == 1)  # 断言订单状态：存在询价日
        with allure.step("后台获取附件ID,询价单名称：{}".format(enquiry_name)):
            Attachment_id1 = ict.Test_Added01().test_Added0191(ht_host=ht_host_FBA, token=ht_token, Attachment_neme=Attachment_neme)
            assert Attachment_id1[0] == '操作成功'
            Attachment_id = Attachment_id1[1]    #附件ID

        with allure.step("后台获取附件ID,询价单名称：{}".format(enquiry_name)):
            save_path = bf.Common_page().projects_path() + "\Test_data\inquiry_document\{}.xlsx".format(enquiry_name) #附件保存地址
            save_download = ict.Test_Added01().test_Added0192(ht_host=ht_host_FBA, token=ht_token,
                                                               Attachment_id=Attachment_id,save_path=save_path)
            # assert save_download == '<Response [200]>'
        time.sleep(10)
        with allure.step("导入询价模板,第一个订单,读取邮箱附件"):
            accessory = bf.Common_page().read_excel001(save_dir=save_path)
            Expected_pickup_date = accessory[0]["期望提货日期(Expected Pickup Date)"]
            Expected_pickup_time = accessory[0]["期望提货时间(Expected Pickup Time)"]
            print("这个是附件期望提货时间：{}".format(Expected_pickup_date))
            pytest.assume(Expected_pickup_time == "14:00")
        with allure.step("导入询价模板,第一个订单,断言提货时间,ALO号：{}".format(ALO1)):
            Week = bf.Common_page().Week(time=time2)  #获取是周几>年月日时分秒
            if Week == 1 :
                time2 = time2
                print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 2)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            if Week == 2 :
                print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 2)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            if Week == 3 :
                print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 2)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            if Week == 4 :
                print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 4)  # 断言邮箱提货时间，是邮箱时间的 + 4天中间两天非工作日
            if Week == 5 :
                print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 4)  # 断言邮箱提货时间，是邮箱时间的 + 4天中间两天非工作日
            if Week == 6 :
                print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 3)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            if Week == 7 :
                print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 2)  # 断言邮箱提货时间，是邮箱时间的 + 2天

    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("期望提货时间，表格时间大于邮件接收时间，取表格时间 ,周末顺延 ")
    def test_business_scenario002(self):
        with allure.step("获取货主ID"):
            hz_name = ict.Test_Added01().test_Added0185(ht_host=ht_host_FBA, hz_name=cf.hz_name_FBA, token=ht_token)
            assert hz_name[0] == '操作成功'
            hz_id = hz_name[1]
        with allure.step("获取导入询价模板ID"):
            modelName = ict.Test_Added01().test_Added0184(ht_host=ht_host_FBA, modelName="询价管理导入-盐田", token=ht_token)
            assert modelName[0] == '操作成功'
            modelid = modelName[1]
        with allure.step("获取导入询价模板,第一个订单"):
            time1 = bf.Common_page().get_today001()[12]  # 获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[13]  # 获取当前时间年月日  + 3天
            ALO1 = 'AL0-T' + time1  # 询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls"  # 模板IP路径
            bf.Common_page().read_excel(file_path=Template_path, ALO=ALO1, time1=time2,pygidium="No")
        with allure.step("导入询价模板,第一个订单,ALO号：{}".format(ALO1)):
            to_channel = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA, mb_id=modelid, wj_name="FBA_inquiry_list.xls",
                                                        wj_dz=Template_path, token=hz_token)
            assert to_channel == '导入成功,操作成功'
        with allure.step("导入询价模板,第一个订单信息,ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA, hz_id=hz_id, xj_dh=ALO1, token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            orderNumber = order_info[2][0]["orderNumber"]
            time.sleep(1)
        with allure.step("后台查看邮件日志，询价单导入触发邮件通知，,第一个询价单号：{}".format(ALO1)):
            subject = ALO1 + "询价结果"
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA, token=ht_token, subject=subject)
            assert enquiry_log[0] == '操作成功'
            Attachment_neme = enquiry_log[2][0]["mailFile"]  # 附件名称
            enquiry_name = enquiry_log[2][0]["subject"]  # 询价单名称  "AL0-T230816154531询价结果"
            pytest.assume(enquiry_log[1] == 1)  # 断言订单状态：存在询价日
        with allure.step("后台获取附件ID,询价单名称：{}".format(enquiry_name)):
            Attachment_id1 = ict.Test_Added01().test_Added0191(ht_host=ht_host_FBA, token=ht_token,
                                                               Attachment_neme=Attachment_neme)
            assert Attachment_id1[0] == '操作成功'
            Attachment_id = Attachment_id1[1]  # 附件ID

        with allure.step("后台获取附件ID,询价单名称：{}".format(enquiry_name)):
            save_path = bf.Common_page().projects_path() + "\Test_data\inquiry_document\{}.xlsx".format(
                enquiry_name)  # 附件保存地址
            save_download = ict.Test_Added01().test_Added0192(ht_host=ht_host_FBA, token=ht_token,
                                                              Attachment_id=Attachment_id, save_path=save_path)
            # assert save_download == '<Response [200]>'
        time.sleep(10)
        with allure.step("导入询价模板,第一个订单,读取邮箱附件"):
            accessory = bf.Common_page().read_excel001(save_dir=save_path)
            Expected_pickup_date = accessory[0]["期望提货日期(Expected Pickup Date)"]
            Expected_pickup_time = accessory[0]["期望提货时间(Expected Pickup Time)"]
            # print("这个是附件期望提货时间：{}".format(Expected_pickup_date))
            pytest.assume(Expected_pickup_time == "14:00") #
        with allure.step("导入询价模板,第一个订单,断言提货时间,ALO号：{}".format(ALO1)):
            time3 = bf.Common_page().get_today001()[13]  # 获取当前时间年月日
            Week = bf.Common_page().Week(time=time3)  #获取是周几>年月日时分秒
            if Week == 1 :
                time2 = time2
                # print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 0)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            if Week == 2 :
                # print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 0)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            if Week == 3 :
                # print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 0)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            if Week == 4 :
                # print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 0)  # 断言邮箱提货时间，是邮箱时间的 + 4天中间两天非工作日
            if Week == 5 :
                # print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 3)  # 断言邮箱提货时间，是邮箱时间的 + 4天中间两天非工作日
            if Week == 6 :
                # print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 2)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            if Week == 7 :
                # print("今天是周：{}".format(Week))
                end_date = Expected_pickup_date
                start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
                end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
                days = int((end_sec - start_sec) / 86400)
                # print(days)
                pytest.assume(days == 1)  # 断言邮箱提货时间，是邮箱时间的 + 2天


@allure.parent_suite('FBA业务场景测试用例')
@allure.suite('FBA业务场景测试用例模块')
@allure.sub_suite('业务场景十二')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso3():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("期望提货时间，表格时间小于邮件接收时间，取邮件接收时间+1,")
    def test_business_scenario001(self):
        with allure.step("获取货主ID"):
            hz_name = ict.Test_Added01().test_Added0185(ht_host=ht_host_FBA,hz_name=cf.hz_name_FBA,token=ht_token)
            assert hz_name[0] == '操作成功'
            hz_id = hz_name[1]
        with allure.step("获取导入询价模板ID"):
            modelName = ict.Test_Added01().test_Added0184(ht_host=ht_host_FBA,modelName="询价管理导入-平湖",token=ht_token)
            assert modelName[0] == '操作成功'
            modelid = modelName[1]
        with allure.step("获取导入询价模板,第一个订单"):
            time1 = bf.Common_page().get_today001()[12]  #获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[11]  #获取当前时间年月日
            ALO1 = 'AL0-T'+time1   #询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls" #模板IP路径
            bf.Common_page().read_excel(file_path=Template_path,ALO=ALO1,time1=time2,pygidium="No")
        with allure.step("导入询价模板,第一个订单,ALO号：{}".format(ALO1)):
            to_channel = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA,mb_id=modelid,wj_name="FBA_inquiry_list.xls",wj_dz=Template_path,token=hz_token)
            assert to_channel == '导入成功,操作成功'
        with allure.step("导入询价模板,第一个订单信息,ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            orderNumber = order_info[2][0]["orderNumber"]
            time.sleep(1)
        with allure.step("后台查看邮件日志，询价单导入触发邮件通知，,第一个询价单号：{}".format(ALO1)):
            subject = ALO1 + "询价结果"
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA, token=ht_token, subject=subject)
            assert enquiry_log[0] == '操作成功'
            Attachment_neme = enquiry_log[2][0]["mailFile"]  #附件名称
            enquiry_name = enquiry_log[2][0]["subject"]  #询价单名称  "AL0-T230816154531询价结果"
            pytest.assume(enquiry_log[1] == 1)  # 断言订单状态：存在询价日
        with allure.step("后台获取附件ID,询价单名称：{}".format(enquiry_name)):
            Attachment_id1 = ict.Test_Added01().test_Added0191(ht_host=ht_host_FBA, token=ht_token, Attachment_neme=Attachment_neme)
            assert Attachment_id1[0] == '操作成功'
            Attachment_id = Attachment_id1[1]    #附件ID

        with allure.step("后台获取附件ID,询价单名称：{}".format(enquiry_name)):
            save_path = bf.Common_page().projects_path() + "\Test_data\inquiry_document\{}.xlsx".format(enquiry_name) #附件保存地址
            save_download = ict.Test_Added01().test_Added0192(ht_host=ht_host_FBA, token=ht_token,
                                                               Attachment_id=Attachment_id,save_path=save_path)
            # assert save_download == '<Response [200]>'
        time.sleep(10)
        with allure.step("导入询价模板,第一个订单,读取邮箱附件"):
            accessory = bf.Common_page().read_excel001(save_dir=save_path)
            Expected_pickup_date = accessory[0]["期望提货日期(Expected Pickup Date)"]
            Expected_pickup_time = accessory[0]["期望提货时间(Expected Pickup Time)"]
            print("这个是附件期望提货时间（今天+1）：{}".format(Expected_pickup_date))
            pytest.assume(Expected_pickup_time == "14:00")
        with allure.step("导入询价模板,第一个订单,断言提货时间,ALO号：{}".format(ALO1)):
            time2 = time2
            end_date = Expected_pickup_date
            start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
            end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
            days = int((end_sec - start_sec) / 86400)   #邮箱期望提货时间-收到邮箱时间
            # print(days)
            present_time = int(bf.Common_page().get_today001()[14])  #获取当前时间  时分
            if present_time < 1400 :
                pytest.assume(days == 1)  # 断言邮箱提货时间，是邮箱时间的 + 1天
            if present_time > 1400 :
                pytest.assume(days == 2)  # 断言邮箱提货时间，是邮箱时间的 + 2天
            print("取邮箱日期+1：{}".format(days))

    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("期望提货时间，表格时间大于邮件接收时间，取表格时间  ")
    def test_business_scenario002(self):
        with allure.step("获取货主ID"):
            hz_name = ict.Test_Added01().test_Added0185(ht_host=ht_host_FBA, hz_name=cf.hz_name_FBA, token=ht_token)
            assert hz_name[0] == '操作成功'
            hz_id = hz_name[1]
        with allure.step("获取导入询价模板ID"):
            modelName = ict.Test_Added01().test_Added0184(ht_host=ht_host_FBA, modelName="询价管理导入-平湖", token=ht_token)
            assert modelName[0] == '操作成功'
            modelid = modelName[1]
        with allure.step("获取导入询价模板,第一个订单"):
            time1 = bf.Common_page().get_today001()[12]  # 获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[13]  # 获取当前时间年月日  + 3天
            ALO1 = 'AL0-T' + time1  # 询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls"  # 模板IP路径
            bf.Common_page().read_excel(file_path=Template_path, ALO=ALO1, time1=time2,pygidium="No")
        with allure.step("导入询价模板,第一个订单,ALO号：{}".format(ALO1)):
            to_channel = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA, mb_id=modelid, wj_name="FBA_inquiry_list.xls",
                                                        wj_dz=Template_path, token=hz_token)
            assert to_channel == '导入成功,操作成功'
        with allure.step("导入询价模板,第一个订单信息,ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA, hz_id=hz_id, xj_dh=ALO1, token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            orderNumber = order_info[2][0]["orderNumber"]
            time.sleep(1)
        with allure.step("后台查看邮件日志，询价单导入触发邮件通知，,第一个询价单号：{}".format(ALO1)):
            subject = ALO1 + "询价结果"
            enquiry_log = ict.Test_Added01().test_Added0190(ht_host=ht_host_FBA, token=ht_token, subject=subject)
            assert enquiry_log[0] == '操作成功'
            Attachment_neme = enquiry_log[2][0]["mailFile"]  # 附件名称
            enquiry_name = enquiry_log[2][0]["subject"]  # 询价单名称  "AL0-T230816154531询价结果"
            pytest.assume(enquiry_log[1] == 1)  # 断言订单状态：存在询价日
        with allure.step("后台获取附件ID,询价单名称：{}".format(enquiry_name)):
            Attachment_id1 = ict.Test_Added01().test_Added0191(ht_host=ht_host_FBA, token=ht_token,
                                                               Attachment_neme=Attachment_neme)
            assert Attachment_id1[0] == '操作成功'
            Attachment_id = Attachment_id1[1]  # 附件ID

        with allure.step("后台获取附件ID,询价单名称：{}".format(enquiry_name)):
            save_path = bf.Common_page().projects_path() + "\Test_data\inquiry_document\{}.xlsx".format(
                enquiry_name)  # 附件保存地址
            save_download = ict.Test_Added01().test_Added0192(ht_host=ht_host_FBA, token=ht_token,
                                                              Attachment_id=Attachment_id, save_path=save_path)
            # assert save_download == '<Response [200]>'
        time.sleep(10)
        with allure.step("导入询价模板,第一个订单,读取邮箱附件"):
            accessory = bf.Common_page().read_excel001(save_dir=save_path)
            Expected_pickup_date = accessory[0]["期望提货日期(Expected Pickup Date)"]
            Expected_pickup_time = accessory[0]["期望提货时间(Expected Pickup Time)"]
            print("这个是附件期望提货时间(今天+3)：{}".format(Expected_pickup_date))
            pytest.assume(Expected_pickup_time == "14:00")
        with allure.step("导入询价模板,第一个订单,断言提货时间,ALO号：{}".format(ALO1)):
            time2 = time2
            end_date = Expected_pickup_date
            start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
            end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
            days = int((end_sec - start_sec) / 86400)   #邮箱期望提货时间-收到邮箱时间
            # print(days)
            pytest.assume(days == 0)  # 断言邮箱提货时间，是邮箱时间的 + 3天
            print("取表格日期：{}".format(days))


@allure.parent_suite('FBA业务场景测试用例')
@allure.suite('FBA业务场景测试用例模块')
@allure.sub_suite('业务场景十三')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso4():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景十三（测试点：<盐田模板>（零担更新货量信息）更新应收费用 ")
    def test_business_scenario001(self):
        with allure.step("获取货主ID"):
            hz_name = ict.Test_Added01().test_Added0185(ht_host=ht_host_FBA,hz_name=cf.hz_name_FBA,token=ht_token)
            assert hz_name[0] == '操作成功'
            hz_id = hz_name[1]

        with allure.step("后台获取导入询价模板ID"):
            modelName = ict.Test_Added01().test_Added0184(ht_host=ht_host_FBA,modelName="询价管理导入-盐田",token=ht_token)
            assert modelName[0] == '操作成功'
            modelid = modelName[1]

        with allure.step("获取导入询价模板,第一个订单"):
            time1 = bf.Common_page().get_today001()[12]  #获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[11]  #获取当前时间年月日
            ALO1 = 'AL0-T'+time1   #询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls" #模板IP路径
            bf.Common_page().read_excel(file_path=Template_path,ALO=ALO1,time1=time2,pygidium="No")

        with allure.step("货主导入询价模板,第一个订单,ALO号：{}".format(ALO1)):
            to_channel = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA,mb_id=modelid,wj_name="FBA_inquiry_list.xls",wj_dz=Template_path,token=hz_token)
            assert to_channel == '导入成功,操作成功'

        with allure.step("货主导入询价模板,第一个订单信息,第一个订单ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            orderNumber1 = order_info[2][0]["orderNumber"]  #询价单号
            enquiry_id1 = order_info[2][0]["id"]                #询价单id
            status = order_info[2][0]["orderStatus"]  #询价单状态
            pytest.assume(status == "status_draft")  # 断言订单状态：草稿

        with allure.step("获取图片地址上传附件,,第一个订单询价单号：{}".format(orderNumber1)):
            tu_dz = pz.Common_page().projects_path() + r"\Common\picture\2.02 MB.JPG"  # 图片地址

        with allure.step("货主上传图片，,第一个订单获取图片id"):
            tp_id = ict.Shipperapi().test_Added004(tp_lj=tu_dz,hz_host=hz_host_FBA,token=hz_token)  # 获取图片id
            assert tp_id[1] == "success"

        with allure.step("货主询价导入》上传附件，,第一个订单询价单号{}".format(orderNumber1)):
            sc_tp = ict.Shipperapi().test_Added005(hz_host=hz_host_FBA,token=hz_token,id=enquiry_id1,tp_name="2.02 MB.JPG",tp_id=tp_id[0])
            assert sc_tp == "操作成功"


        with allure.step("货主查看订单详情页,,第一个订单ALO号：{}".format(ALO1)):
            Detail_Pages1 = ict.Shipperapi().test_Added007(hz_host=hz_host_FBA,token=hz_token,id=enquiry_id1)
            assert Detail_Pages1[0] == '操作成功'
            data1 = ict.get_k(Detail_Pages1[1])
            data1.update([('ltlFtlType', 'LTL')])  #零担

        with allure.step("货主编辑》立即下单,,第一个订单ALO号：{}".format(ALO1)):
            immediately_place = ict.Shipperapi().test_Added008(hz_host=hz_host_FBA,token=hz_token,data1=data1)
            assert immediately_place[0] == '操作成功'




        with allure.step("货主导入询价模板,第一个订单状态,第一个订单ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            customerOrderNumber1 = order_info[2][0]["customerOrderNumber"]  #订单号
            status = order_info[2][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_generated")  # 断言订单状态：已生成
            amount =  order_info[2][0]["priceInfoList"]["ltl"][0]["amount"] #推荐报价

        with allure.step("后台查看订单状态，,订单号：{}".format(customerOrderNumber1)):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1)
            assert ht_order_info[0] == '操作成功'
            customerOrderId1 = ht_order_info[1][0]["id"]    #订单id
            status = ht_order_info[1][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_pending")  # 断言订单状态：待接单
            planWeight = ht_order_info[1][0]["planWeight"]    #计划重量
            planVolume = ht_order_info[1][0]["planVolume"]  #计划体积
            planGoodsNumber = ht_order_info[1][0]["planGoodsNumber"]    #计划箱数
            planPiecesNumber = ht_order_info[1][0]["planPiecesNumber"]    #计划件数
            volume = planVolume *  10
        with allure.step("后台查看应收费用金额，,订单号：{}".format(customerOrderNumber1)):
            cost_info = ict.Test_Added01().test_Added0193(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1)
            assert cost_info[0] == '操作成功'
            pytest.assume(cost_info[1][0]["inComeAmountTotal"] == amount)  # 断言应收金额是推荐报价金额
        with allure.step("后台订单管理》厢式车运输，更新货量,订单订单号：{}".format(customerOrderNumber1)):
            update_cargo = ict.Test_Added01().test_Added0194(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1,
                                                          planWeight=planWeight,planVolume=planVolume,planGoodsNumber=planGoodsNumber,
                                                        planPiecesNumber=planPiecesNumber,weight=planWeight,volume=volume,
                                                             goodsNumber=planGoodsNumber,piecesNumber=planPiecesNumber,order_id=customerOrderId1)
            assert update_cargo == '操作成功'
        time.sleep(1)
        with allure.step("后台查看更新货量后应收费用金额，,订单号：{}".format(customerOrderNumber1)):
            cost_info = ict.Test_Added01().test_Added0193(ht_host=ht_host_FBA,token=ht_token,order_number=customerOrderNumber1)
            assert cost_info[0] == '操作成功'
            amount1 = amount * 10
            pytest.assume(cost_info[1][0]["inComeAmountTotal"] == amount1)  # 断言应收金额是推荐报价金额*10



@allure.parent_suite('FBA业务场景测试用例')
@allure.suite('FBA业务场景测试用例模块')
@allure.sub_suite('业务场景十五')
# @pytest.mark.skip(reason="无理由跳过")
class Test_businesso5():
    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景十五 FBA配置计划（测试点：零担》配载直接下发）")
    def test_business_scenario001(self):
        with allure.step("获取货主ID"):
            hz_name = ict.Test_Added01().test_Added0185(ht_host=ht_host_FBA,hz_name=cf.hz_name_FBA,token=ht_token)
            assert hz_name[0] == '操作成功'
            hz_id = hz_name[1]

        with allure.step("后台获取导入询价模板ID"):
            modelName = ict.Test_Added01().test_Added0184(ht_host=ht_host_FBA,modelName="询价管理导入-盐田",token=ht_token)
            assert modelName[0] == '操作成功'
            modelid = modelName[1]

        with allure.step("获取导入询价模板,第一个订单"):
            time1 = bf.Common_page().get_today001()[12]  #获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[11]  #获取当前时间年月日
            ALO1 = 'AL0-T'+time1   #询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls" #模板IP路径
            bf.Common_page().read_excel(file_path=Template_path,ALO=ALO1,time1=time2,pygidium="Yes")

        with allure.step("货主导入询价模板,第一个订单,ALO号：{}".format(ALO1)):
            to_channel = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA,mb_id=modelid,wj_name="FBA_inquiry_list.xls",wj_dz=Template_path,token=hz_token)
            assert to_channel == '导入成功,操作成功'

        with allure.step("货主导入询价模板,第一个订单信息,第一个订单ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA,hz_id=hz_id,xj_dh=ALO1,token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            orderNumber1 = order_info[2][0]["orderNumber"]  #询价单号
            enquiry_id1 = order_info[2][0]["id"]                #询价单id
            status = order_info[2][0]["orderStatus"]  #询价单状态
            pytest.assume(status == "status_draft")  # 断言订单状态：草稿

        with allure.step("获取图片地址上传附件,,第一个订单询价单号：{}".format(orderNumber1)):
            tu_dz = pz.Common_page().projects_path() + r"\Common\picture\2.02 MB.JPG"  # 图片地址

        with allure.step("货主上传图片，,第一个订单获取图片id"):
            tp_id = ict.Shipperapi().test_Added004(tp_lj=tu_dz,hz_host=hz_host_FBA,token=hz_token)  # 获取图片id
            assert tp_id[1] == "success"

        with allure.step("货主询价导入》上传附件，,第一个订单询价单号{}".format(orderNumber1)):
            sc_tp = ict.Shipperapi().test_Added005(hz_host=hz_host_FBA,token=hz_token,id=enquiry_id1,tp_name="2.02 MB.JPG",tp_id=tp_id[0])
            assert sc_tp == "操作成功"

        with allure.step("货主查看订单详情页,,第一个订单ALO号：{}".format(ALO1)):
            Detail_Pages1 = ict.Shipperapi().test_Added007(hz_host=hz_host_FBA,token=hz_token,id=enquiry_id1)
            assert Detail_Pages1[0] == '操作成功'
            data1 = ict.get_k(Detail_Pages1[1])
            data1.update([('ltlFtlType', 'LTL')])  #零担

        with allure.step("货主编辑》立即下单,,第一个订单ALO号：{}".format(ALO1)):
            immediately_place = ict.Shipperapi().test_Added008(hz_host=hz_host_FBA,token=hz_token,data1=data1)
            assert immediately_place[0] == '操作成功'

        with allure.step("后台查看新增厢式车运输信息"):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA,token=ht_token,order_number="",customerDelegateCode=ALO1)
            assert ht_order_info[0] == '操作成功'
            order_id = ht_order_info[1][0]["id"]    #订单id
            orderNumber = ht_order_info[1][0]["orderNumber"]
            status = ht_order_info[1][0]["orderStatus"]  #订单状态
            pytest.assume(status == "status_pending")  # 断言订单状态：待接单

        with allure.step("厢式车运输审核下发"):
            audit_issue = ict.Test_Added01().test_Added0196(ht_host=ht_host_FBA,token=ht_token,order_id=order_id)
            assert audit_issue == '操作成功'
        with allure.step("审核下发，查看订单状态"):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA,token=ht_token,order_number="",customerDelegateCode=ALO1)
            assert ht_order_info[0] == '操作成功'
            pytest.assume(ht_order_info[1][0]["orderStatus"] == "status_execution")  #订单状态= 执行中
        with allure.step("待配载查看订单状态，订单号：{}".format(orderNumber)):
            order_info = ict.Test_Added01().test_Added0197(ht_host=ht_host_FBA, token=ht_token,
                                                           orderNumber=orderNumber)
            assert order_info[0] == '操作成功'
            state1 = order_info[1][0]["planStatusType"]
            pytest.assume( state1 == "status_waiting_plan")  # 断言订单状态：待配载
        with allure.step("直接下发"):
            direct_issue = ict.Test_Added01().test_Added0200(ht_host=ht_host_FBA, token=ht_token,
                                                             order_id=[order_id])
            assert direct_issue == '操作成功'

        with allure.step("直接下发查看订单状态，订单号：{}".format(orderNumber)):
            order_info = ict.Test_Added01().test_Added0197(ht_host=ht_host_FBA, token=ht_token,
                                                           orderNumber=orderNumber)
            assert order_info[0] == '操作成功'
            state2 = order_info[1][0]["planStatusType"]
            pytest.assume( state2 == "status_plan_completed")  # 断言订单状态：已配载

        '''厢式车订单分单管理》分自有车'''
        with allure.step("计划管理，分单查询，订单号：{}".format(orderNumber)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host_FBA,token=ht_token,dd_hao=orderNumber)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 1
            fd_id = fd_xx[2][0]["id"]

        with allure.step("分单，分派供应商,分单号：{}".format(fd_id)):
            qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host_FBA,token=ht_token,zy_che=fd_id, gys="", hy_dt="")
            assert qy_jdzx == '操作成功'
        time.sleep(2)
        with allure.step("派自有车A，派供应商>断言分单渠道"):
            fd_qd = ict.Test_Added01().test_Added0175(dd_hao=orderNumber,ht_host=ht_host_FBA,token=ht_token)
            assert fd_qd[0] == '操作成功'
            pytest.assume("自有运力" == fd_qd[3][0]["distributeChannel"])  #分单渠道= 自有车
            pytest.assume("status_waiting_dispatch" == fd_qd[3][0]["orderStatus"])  #状态= 待派单

    # @pytest.mark.skip(reason="无理由跳过")
    @allure.title("业务场景十五 FBA配置计划（测试点：整车》配载直接下发）")
    def test_business_scenario002(self):
        with allure.step("获取货主ID"):
            hz_name = ict.Test_Added01().test_Added0185(ht_host=ht_host_FBA, hz_name=cf.hz_name_FBA, token=ht_token)
            assert hz_name[0] == '操作成功'
            hz_id = hz_name[1]

        with allure.step("后台获取导入询价模板ID"):
            modelName = ict.Test_Added01().test_Added0184(ht_host=ht_host_FBA, modelName="询价管理导入-盐田", token=ht_token)
            assert modelName[0] == '操作成功'
            modelid = modelName[1]

        with allure.step("获取导入询价模板,第一个订单"):
            time1 = bf.Common_page().get_today001()[12]  # 获取当前时间年月日时分秒
            time2 = bf.Common_page().get_today001()[11]  # 获取当前时间年月日
            ALO1 = 'AL0-T' + time1  # 询价单号
            Template_path = bf.Common_page().projects_path() + "\Test_data\FBA_inquiry_list.xls"  # 模板IP路径
            bf.Common_page().read_excel(file_path=Template_path, ALO=ALO1, time1=time2, pygidium="Yes")

        with allure.step("货主导入询价模板,第一个订单,ALO号：{}".format(ALO1)):
            to_channel = ict.Shipperapi().test_Added001(hz_host=hz_host_FBA, mb_id=modelid,
                                                        wj_name="FBA_inquiry_list.xls", wj_dz=Template_path,
                                                        token=hz_token)
            assert to_channel == '导入成功,操作成功'

        with allure.step("货主导入询价模板,第一个订单信息,第一个订单ALO号：{}".format(ALO1)):
            order_info = ict.Shipperapi().test_Added003(hz_host=hz_host_FBA, hz_id=hz_id, xj_dh=ALO1, token=hz_token)
            assert order_info[0] == '操作成功'
            assert order_info[1] != 0
            orderNumber1 = order_info[2][0]["orderNumber"]  # 询价单号
            enquiry_id1 = order_info[2][0]["id"]  # 询价单id
            status = order_info[2][0]["orderStatus"]  # 询价单状态
            pytest.assume(status == "status_draft")  # 断言订单状态：草稿

        with allure.step("获取图片地址上传附件,,第一个订单询价单号：{}".format(orderNumber1)):
            tu_dz = pz.Common_page().projects_path() + r"\Common\picture\2.02 MB.JPG"  # 图片地址

        with allure.step("货主上传图片，,第一个订单获取图片id"):
            tp_id = ict.Shipperapi().test_Added004(tp_lj=tu_dz, hz_host=hz_host_FBA, token=hz_token)  # 获取图片id
            assert tp_id[1] == "success"

        with allure.step("货主询价导入》上传附件，,第一个订单询价单号{}".format(orderNumber1)):
            sc_tp = ict.Shipperapi().test_Added005(hz_host=hz_host_FBA, token=hz_token, id=enquiry_id1,
                                                   tp_name="2.02 MB.JPG", tp_id=tp_id[0])
            assert sc_tp == "操作成功"

        with allure.step("货主查看订单详情页,,第一个订单ALO号：{}".format(ALO1)):
            Detail_Pages1 = ict.Shipperapi().test_Added007(hz_host=hz_host_FBA, token=hz_token, id=enquiry_id1)
            assert Detail_Pages1[0] == '操作成功'
            data1 = ict.get_k(Detail_Pages1[1])
            data1.update([('ltlFtlType', 'FTL')])  # 整车

        with allure.step("货主编辑》立即下单,,第一个订单ALO号：{}".format(ALO1)):
            immediately_place = ict.Shipperapi().test_Added008(hz_host=hz_host_FBA, token=hz_token, data1=data1)
            assert immediately_place[0] == '操作成功'

        with allure.step("后台查看新增厢式车运输信息"):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA, token=ht_token, order_number="",
                                                              customerDelegateCode=ALO1)
            assert ht_order_info[0] == '操作成功'
            order_id = ht_order_info[1][0]["id"]  # 订单id
            orderNumber = ht_order_info[1][0]["orderNumber"]
            status = ht_order_info[1][0]["orderStatus"]  # 订单状态
            pytest.assume(status == "status_pending")  # 断言订单状态：待接单

        with allure.step("厢式车运输审核下发"):
            audit_issue = ict.Test_Added01().test_Added0196(ht_host=ht_host_FBA, token=ht_token, order_id=order_id)
            assert audit_issue == '操作成功'
        with allure.step("审核下发，查看订单状态"):
            ht_order_info = ict.Test_Added01().test_Added0187(ht_host=ht_host_FBA, token=ht_token, order_number="",
                                                              customerDelegateCode=ALO1)
            assert ht_order_info[0] == '操作成功'
            pytest.assume(ht_order_info[1][0]["orderStatus"] == "status_execution")  # 订单状态= 执行中

        with allure.step("整车无需配载，查看订单状态，订单号：{}".format(orderNumber)):
            order_info = ict.Test_Added01().test_Added0197(ht_host=ht_host_FBA, token=ht_token,
                                                           orderNumber=orderNumber)
            assert order_info[0] == '操作成功'
            state2 = order_info[1][0]["planStatusType"]
            pytest.assume(state2 == "status_plan_completed")  # 断言订单状态：已配载

        '''厢式车订单分单管理》分自有车'''
        with allure.step("计划管理，分单查询，订单号：{}".format(orderNumber)):
            fd_xx = ict.Test_Added01().test_Added0103(ht_host=ht_host_FBA,token=ht_token,dd_hao=orderNumber)
            assert fd_xx[0] == '操作成功'
            assert fd_xx[1] == 1
            fd_id = fd_xx[2][0]["id"]

        with allure.step("分单，分自有车,分单号：{}".format(fd_id)):
            qy_jdzx = ict.Test_Added01().test_Added0058(ht_host=ht_host_FBA,token=ht_token,zy_che=fd_id, gys="", hy_dt="")
            assert qy_jdzx == '操作成功'
        time.sleep(2)
        with allure.step("派自有车A，派自有车>断言分单渠道"):
            fd_qd = ict.Test_Added01().test_Added0175(dd_hao=orderNumber,ht_host=ht_host_FBA,token=ht_token)
            assert fd_qd[0] == '操作成功'
            pytest.assume("自有运力" == fd_qd[3][0]["distributeChannel"])  # 分单渠道= 自有车
            pytest.assume("status_waiting_dispatch" == fd_qd[3][0]["orderStatus"])  # 状态= 待派单