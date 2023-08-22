#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: ict_api.py
# @Time:2023/2/28 10:28
# @Author:PH
# import urllib3

import urllib3

import Common.common_funtion as cc

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


from Config import config as long
import requests,json
ht_host_FBA = long.ht_host_FBA
hz_host_FBA = long.hz_host_FBA
tiem3 = cc.Common_page().get_today001()[11]  #今天时间 年月日
'''递归，获取value'''
def get_k(data_json):

    if isinstance(data_json,dict):
        # if 'value' in data_json.keys():
        for key in data_json.keys():
            if isinstance(data_json[key],dict):
                if 'value' in data_json[key].keys():
                    data_json[key] = data_json[key]['value']

                else:
                    get_k(data_json[key])

    return data_json



'''登录接口'''
class Test_login():
    def __init__(self):
        self.ht_host=long.ht_host
        self.hz_host=long.hz_host
        self.gys_host=long.gys_host
        self.headers=long.ht_headers
        self.mobile=long.ht_mobile
        self.password=long.ht_password
        self.hz_modile=long.hz_mobile
        self.hz_password=long.hz_password
        self.ys_modile=long.ys_mobile
        self.ys_password=long.ys_password
        # self.sj_modile=long.siji_mobile
        # self.sj_password=long.siji_password
        # self.sj_headers=long.siji_headers
        # self.sj_host=long.siji_host
        self.ht_mobile_FBA=long.ht_mobile_FBA
        self.ht_password_FBA=long.ht_password_FBA
        self.hz_modile_FBA=long.hz_mobile_FBA
        self.hz_password_FBA=long.hz_password_FBA
        self.hz_host_FBA = long.hz_host_FBA
        self.ht_host_FBA = long.ht_host_FBA


    '''后台登录接口'''
    def Test_login001(self):
        url =self.ht_host+"/api/login"
        headers=self.headers
        data={"account":self.mobile,"password":self.password}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        token=A.json()["result"]["token"]
        # print(token)
        return token
    '''货主端登录接口'''
    def Test_login002(self):
        url = self.hz_host + "/api/login"
        headers = self.headers
        data = {"account": self.hz_modile, "password": self.hz_password}
        r =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(r.json())
        token = r.json()["result"]["token"]
        # print(token)
        return token
    '''运输公司端登录接口'''
    def Test_login003(self):
        url = self.gys_host + "/api/login"
        headers = self.headers
        data = {"account": self.ys_modile, "password": self.ys_password }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        token = A.json()["result"]["token"]
        # print(token)
        return token
    '''司机小程序登录接口'''
    # '''登录司机后台'''
    # def Test_login004(self):
    #     url = self.sj_host + "/auth-center/authc/authenticate"
    #     headers = {'Content-type': 'application/json', }
    #     data = {"account": "testregister@default.com", "password": "v7zh@QhWlQ"}
    #     r = requests.post(url=url, headers=headers, data=json.dumps(data))
    #     # print(r.json())
    #     token = r.json()["result"]["token"]
    #     # print(token)
    #     return token
    # '''登录小程序'''
    # def Test_login005(self):
    #     url = self.sj_host + "/archiver-service/driver_register/registerAndLogin?token={}".format(self.Test_login004())
    #     headers = {'Content-Type': 'application/json'}
    #
    #     data = {"appId": "wx2b45a1766fa7d7e5", "captcha": "", "openId": "o0QmA5Xg_quqHlON0BanNU2vUeKA",
    #             "registerType": 0, "supplierContactMobile": "13088823813", "supplierContactName": ""}
    #     r = requests.post(url=url, headers=headers, data=json.dumps(data))
    #     # print(r.json())
    #     dl_token = r.json()["result"]["token"]
    #     returnMsg=r.json()["returnMsg"]
    #     # print(dl_token,returnMsg)
    #     return dl_token,returnMsg

    '''后台登录接口_FBA'''


    def Test_login004(self):

        url =self.ht_host_FBA+"/api/login"
        headers=self.headers
        data={"account":self.ht_mobile_FBA,"password":self.ht_password_FBA}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        token=A.json()["result"]["token"]
        # print(token)
        return token
    '''货主端登录接口_FBA'''
    def Test_login005(self):
        url = self.hz_host_FBA + "/api/login"
        headers = self.headers
        data = {"account": self.hz_modile_FBA, "password": self.hz_password_FBA}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        token = A.json()["result"]["token"]
        # print(token)
        return token







'''后台查询基础信息接口'''
class Test_login01():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''获取货主id》传的是货主名称'''
    def test_query0001(self,hz_nema="毛敏租户测试货主1"):
        url = self.host + "/api/platform/customersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerName":hz_nema}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        hz_id = A.json()["result"]["data"][0]["id"]
        # print("获取货主id:{}".format(hz_id))
        return hz_id
    '''获取行政区id》传的是地址'''
    def test_query0002(self,zxq_nema="万石植物园"):
        url = self.host + "/api/platform/area/districtList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"active":"active_activated","districtName":zxq_nema}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        xzq_id = A.json()["result"]["data"][0]["guid"]
        # print("获取行政区id:{}".format(xzq_id))
        return xzq_id
    '''获取港口id》传的是港口名称'''
    def test_query0003(self,gk_nema="澳门"):
        url = self.host + "/api/platform/area/siteList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"active":"active_activated","placeName":gk_nema}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        gk_id = A.json()["result"]["data"][0]["guid"]
        # print("获取行政区id:{}".format(gk_id))
        return gk_id
    '''获取运输公司id》传的是运输公司名称'''
    def test_query0004(self,gys_nema="毛敏租户测试供应商1"):
        url = self.host + "/api/platform/suppliersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"supplierName":gys_nema}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        gys_id = A.json()["result"]["data"][0]["id"]
        # print("获取运输公司id:{}".format(gys_id))
        return gys_id
'''后台业务场景前置接口接口'''
class Test_preposition():
    def __init__(self):
        self.host = long.ht_host
        self.headers = long.ht_headers
        self.ht_token = Test_login().Test_login001()
    '''后台查询货主合同id,传参是货主id'''
    def preposition001(self,hz_id="4d16a4af1ff64e9aa854e54db9e2d5f7"):
        url = self.host + "/api/platform/cargoOwnerContract/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id,"contractType":"cargo_owner_type"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        ht_id = A.json()["result"]["data"][0]["id"]
        # print("后台查询货主合同id:{}".format(ht_id))
        return ht_id
    '''启用后台货主合同启用,传参是货主合同id'''
    def preposition002(self, ht_id="7a026ae1fe3844ccafac5c810b401880"):
        url = self.host + "/api/platform/cargoOwnerContract/enable/{}".format(ht_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台货主合同启用:{}".format(returnMsg))
        return returnMsg
    '''查询后台货主报价合同禁用的明细,传参是货主合同id'''
    def preposition003(self, ht_id="7a026ae1fe3844ccafac5c810b401880"):
        url = self.host + "/api/platform/cargoOwnerContract/detailList/{}".format(ht_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"filter":{"enabledType":"enabled_type_disabled","departure":[],"destination":[]},"itemFrom":0,"itemTo":10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        data1 = A.json()["result"]["data"][0]
        id = []
        for key,value in data1.items():
            # print(key,':',value)
            if key == "id":
                print(key,':',value)
        # returnMsg = A.json()["returnMsg"]
        # print("后台货主合同启用:{}".format(data1))
        # return data1
'''后台业务操作查询接口'''
class Test_query01():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''后台工作看板》客户数据'''
    def test_query001(self):
        url = self.host + "/api/platform/home/client/total/2023-02-01"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台工作看板客户数据获取{}".format(returnMsg))
        return returnMsg,url,headers
    '''后台工作看板》供应商数据'''
    def test_query002(self):
        url = self.host + "/api/platform/home/supplier/total/2023-02-01"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台工作看板供应商数据获取{}".format(returnMsg))
        return returnMsg
    '''后台工作看板》个体司机数据'''
    def test_query003(self):
        url = self.host + "/api/platform/home/driver/total/2023-02-01"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台工作看板个体司机数据获取{}".format(returnMsg))
        return returnMsg
    '''后台工作看板》客户结算方式数据'''
    def test_query004(self):
        url = self.host + "/api/platform/home/bill/total/2023-02-01"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台工作看板客户结算方式数据获取{}".format(returnMsg))
        return returnMsg
    '''后台工作看板》平台管理数据'''
    def test_query005(self):
        url = self.host + "/api/platform/home/totals/2023-02-01"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台工作看板平台管理数据获取{}".format(returnMsg))
        return returnMsg
    '''后台工作台》坪山项目日报表'''
    def test_query006(self):
        url = self.host + "/api/platform/pinshanDayReport/data"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"pickupTimeFrom":"2023-02-01","pickupTimeTo":"2023-02-28"}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台工作看板坪山项目日报表数据获取{}".format(returnMsg))
        return returnMsg
    '''后台订单管理》订单录入查询》危险品出口'''
    def test_query007(self):
        url = self.host + "/api/platform/inputOrder/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagKey":"statusCompleting","orderStatus":["status_completing"],"taskUnitCode":"dangerous_cargo_export_transport"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台订单录入查询获取{}".format(returnMsg))
        return returnMsg
    '''后台订单管理》集装箱运输查询'''
    def test_query008(self):
        url = self.host + "/api/platform/receiveOrderPort/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagKey":"all","taskUnitCodeType":"container"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("集装箱运输查询{}".format(returnMsg))
        return returnMsg
    '''后台订单管理》厢式车运输查询'''
    def test_query009(self):
        url = self.host + "/api/platform/receiveOrder/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagKey":"all","taskUnitCodeType":"vanType"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("厢式车运输查询{}".format(returnMsg))
        return returnMsg
    '''后台配载计划》查询'''
    def test_query010(self):
        url = self.host + "/api/platform/plan/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagKey":"statusWaitingPlan","planStatusTypes":["status_waiting_plan"]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("后台配载计划查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》计划管理集装箱查询'''
    def test_query011(self):
        url = self.host + "/api/platform/planPortTransport/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"status_waiting_distribute"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("计划管理集装箱查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》计划管理厢式车查询'''
    def test_query012(self):
        url = self.host + "/api/platform/planBulkcargoTransport/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"status_waiting_distribute"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("计划管理厢式车查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》调度管理集装箱查询'''
    def test_query013(self):
        url = self.host + "/api/platform/dispatchPortTransport/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("调度管理集装箱查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》调度管理厢式车查询'''
    def test_query014(self):
        url = self.host + "/api/platform/dispatchBulkcargoTransport/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"status_waiting_dispatch"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("调度管理厢式车查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》出车表信息查询'''
    def test_query015(self):
        url = self.host + "/api/platform/carManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("出车表信息查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》监理管理信息查询'''
    def test_query016(self):
        url = self.host + "/api/platform/supervisorManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tagKey":"supervisionStatusWait","status":"supervision_status_wait"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("监理管理信息查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》报关管理信息查询'''
    def test_query017(self):
        url = self.host + "/api/platform/customsManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"status_waiting_dispatch"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("报关管理信息查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》路桥费借款表信息查询'''
    def test_query018(self):
        url = self.host + "/api/platform/roadAndBridgeFee/loanList"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"statusType":"maintained_type"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("路桥费借款表信息查询{}".format(returnMsg))
        return returnMsg
    '''后台运单管理》路桥费维护表信息查询'''
    def test_query019(self):
        url = self.host + "/api/platform/roadAndBridgeFee/maintainList"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("路桥费维护表信息查询{}".format(returnMsg))
        return returnMsg
    '''后台跟踪管理》集装箱运输查询'''
    def test_query020(self):
        url = self.host + "/api/platform/containerTransport/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"currentTag":"status_execution"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("集装箱运输查询{}".format(returnMsg))
        return returnMsg
    '''后台跟踪管理》厢式车运输查询'''
    def test_query021(self):
        url = self.host + "/api/platform/vanTransport/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"currentTag":"status_execution"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("厢式车运输查询{}".format(returnMsg))
        return returnMsg
    '''后台跟踪管理》监理管理查询'''
    def test_query022(self):
        url = self.host + "/api/platform/supervisionManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"status":"undone"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("监理管理查询{}".format(returnMsg))
        return returnMsg
    '''后台跟踪管理》报关管理查询'''
    def test_query023(self):
        url = self.host + "/api/platform/customsClearanceManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"undone"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("报关管理查询{}".format(returnMsg))
        return returnMsg
    '''后台异常管理》异常管理查询'''
    def test_query024(self):
        url = self.host + "/api/platform/exceptionManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"exceptionStatus":"exception_status_completing"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("异常管理查询{}".format(returnMsg))
        return returnMsg
    '''后台文件管理》文件管理查询'''
    def test_query025(self):
        url = self.host + "/api/platform/fileManagement/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"currentTag":"undone","insertTimeFrom":"2023-02-01"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("异常管理查询{}".format(returnMsg))
        return returnMsg
    '''后台货源大厅》货源大厅订单管理查询'''
    def test_query026(self):
        url = self.host + "/api/platform/orderManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tagKey":"all"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("异常管理查询{}".format(returnMsg))
        return returnMsg
'''后台费用与对账查询接口'''
class Test_query02():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''应收管理》应收费用制作'''
    def test_query027(self):
        url = self.host + "/api/platform/expensesReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"chargeStatusArray":["status_check_awaiting","status_check_all_completed_awaiting_upstream","status_check_detail_completed","status_check_completed"]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应收费用制作数据获取{}".format(returnMsg))
        return returnMsg
    '''应收管理》应收改单数据获取'''
    def test_query028(self):
        url = self.host + "/api/platform/changePay/list/0"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"status":["status_submit_awaiting","status_checked_awaiting","status_submit_completed","status_undo_completed"]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应收改单数据获取{}".format(returnMsg))
        return returnMsg
    '''应收管理》应收对账单》待生成对账单数据获取'''
    def test_query029(self):
        url = self.host + "/api/platform/accountStatementReceivable/listTab1"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"statusType":"status_check_all_completed"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("待生成对账单数据获取{}".format(returnMsg))
        return returnMsg
    '''应收管理》应收对账单》对账单合计数据获取'''
    def test_query030(self):
        url = self.host + "/api/platform/accountStatementReceivable/listTab2"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"statusType":"status_bill_awaiting"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("对账单合计数据获取{}".format(returnMsg))
        return returnMsg
    '''应收管理》应收票结账单》'''
    def test_query031(self):
        url = self.host + "/api/platform/accountsReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应收票结账单数据获取{}".format(returnMsg))
        return returnMsg
    '''应收管理》应收月结账单》'''
    def test_query032(self):
        url = self.host + "/api/platform/monthlyAccountsReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"statusType":["status_draft","status_fall_back_completed"]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应收月结账单数据获取{}".format(returnMsg))
        return returnMsg
    '''应收管理》应收发票管理》'''
    def test_query033(self):
        url = self.host + "/api/platform/invoiceReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应收发票管理数据获取{}".format(returnMsg))
        return returnMsg
    '''应付管理》应付费用制作查询》'''
    def test_query034(self):
        url = self.host + "/api/platform/expensesPay/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"chargeStatusArray":["status_check_awaiting","status_check_all_completed_awaiting_upstream","status_check_detail_completed","status_check_completed"]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应付费用制作查询{}".format(returnMsg))
        return returnMsg
    '''应付管理》应付改单查询》'''
    def test_query035(self):
        url = self.host + "/api/platform/changePay/list/1"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"status":["status_submit_awaiting","status_checked_awaiting","status_submit_completed","status_undo_completed"]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应付改单查询{}".format(returnMsg))
        return returnMsg
    '''应付管理》应付月结账单查询》'''
    def test_query036(self):
        url = self.host + "/api/platform/monthlyAccountsPay/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"statusType":["status_bill_awaiting"]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应付月结账单查询{}".format(returnMsg))
        return returnMsg
'''后台审核中心查询接口'''
class Test_query03():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''认证审核》货主认证审核获取'''
    def test_query037(self):
        url = self.host + "/api/platform/individual/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("货主认证审核获取{}".format(returnMsg))
        return returnMsg
    '''认证审核》运输公司认证获取'''
    def test_query038(self):
        url = self.host + "/api/platform/transport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"statusType":"status_register"}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("运输公司认证获取{}".format(returnMsg))
        return returnMsg
    '''认证审核》个人司机认证获取'''
    def test_query039(self):
        url = self.host + "/api/platform/driverCertification/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"isOwner":0}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("个人司机认证获取{}".format(returnMsg))
        return returnMsg
    '''认证审核》车老板审核获取'''
    def test_query040(self):
        url = self.host + "/api/platform/carBossCertification/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("车老板审核获取{}".format(returnMsg))
        return returnMsg
    '''认证审核》证件监控管理》司机证件变更管理获取'''
    def test_query041(self):
        url = self.host + "/api/platform/certificateManagement/manageList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"statusType":["status_check_awaiting"]}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("司机证件变更管理获取{}".format(returnMsg))
        return returnMsg
    '''认证审核》证件监控管理》司机证件监控列表获取'''
    def test_query042(self):
        url = self.host + "/api/platform/certificateManagement/monitoringList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("司机证件监控列表获取{}".format(returnMsg))
        return returnMsg
    '''认证审核》证件监控管理》货主提额管理获取'''
    def test_query043(self):
        url = self.host + "/api/platform/withdrawalManagement/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"statusType":["all"]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("货主提额管理获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》货主市场报价获取'''
    def test_query044(self):
        url = self.host + "/api/platform/cargoOwnerMarket/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("货主提额管理获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》司机市场报价获取'''
    def test_query045(self):
        url = self.host + "/api/platform/driverMarket/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("司机市场报价获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》货主合同报价获取'''
    def test_query046(self):
        url = self.host + "/api/platform/cargoOwnerContract/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"contractType":"cargo_owner_type"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("货主合同报价获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》报价说明》服务类型报价说明'''
    def test_query047(self):
        url = self.host + "/api/platform/offerExplain/list1"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("服务类型报价说明获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》报价说明》服务类型港口报价说明'''
    def test_query048(self):
        url = self.host + "/api/platform/offerExplain/list2"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("服务类型港口报价说明获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》监理报价》职业监理报价获取'''
    def test_query049(self):
        url = self.host + "/api/platform/supervisionQuotation/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supervisionType":"supervision_type_profession"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("职业监理报价获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》监理报价》司机监理报价获取'''
    def test_query050(self):
        url = self.host + "/api/platform/supervisionQuotation/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supervisionType":"supervision_type_driver"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("司机监理报价获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》监理报价》运输公司合同报价获取'''
    def test_query051(self):
        url = self.host + "/api/platform/cargoOwnerContract/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"contractType":"transportation_company_type"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("运输公司合同报价获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》监理报价》自有司机报价获取'''
    def test_query052(self):
        url = self.host + "/api/platform/ownDriverQuotation/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("自有司机报价获取{}".format(returnMsg))
        return returnMsg
    '''报价管理》监理报价》附加费获取'''
    def test_query053(self):
        url = self.host + "/api/platform/cargoOwnerContract/extra_charge/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("附加费获取{}".format(returnMsg))
        return returnMsg
'''后台智能分析查询接口'''
class Test_query04():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''智能分析》Excel获取'''
    def test_query054(self):
        url = self.host + "/api/platform/excelReport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("Excel获取{}".format(returnMsg))
        return returnMsg
    '''智能分析》订阅计划获取'''
    def test_query055(self):
        url = self.host + "/api/platform/excelReport/planList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("订阅计划获取{}".format(returnMsg))
        return returnMsg
'''后台营销中心查询接口'''
class Test_query05():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''市场活动》激励卷档案获取'''
    def test_query056(self):
        url = self.host + "/api/platform/incentiveCoupon/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("激励卷档案获取{}".format(returnMsg))
        return returnMsg
    '''市场活动》营销活动管理获取'''
    def test_query057(self):
        url = self.host + "/api/platform/MarketingActivityManagement/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("营销活动管理获取{}".format(returnMsg))
        return returnMsg
    '''市场活动》营销活动分析获取'''
    def test_query058(self):
        url = self.host + "/api/platform/analysis/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("营销活动分析获取{}".format(returnMsg))
        return returnMsg
    '''市场活动》提现管理》红包每日汇总提现列表获取'''
    def test_query059(self):
        url = self.host + "/api/platform/withdrawal/listRed"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("红包每日汇总提现列表获取{}".format(returnMsg))
        return returnMsg
    '''市场活动》提现管理》司机收入提现列表获取'''
    def test_query060(self):
        url = self.host + "/api/platform/withdrawal/listDer"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("司机收入提现列表获取{}".format(returnMsg))
        return returnMsg
    '''推广活动》推广活动档案获取'''
    def test_query061(self):
        url = self.host + "/api/platform/promotionActivity/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("推广活动档案获取{}".format(returnMsg))
        return returnMsg
    '''推广活动》推广活动分析》推广奖励明细列表获取'''
    def test_query062(self):
        url = self.host + "/api/platform/promotionActivityAnalysis/tab1List"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"isSend":-1}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("推广奖励明细列表获取{}".format(returnMsg))
        return returnMsg
    '''推广活动》推广活动分析》推广汇总列表获取'''
    def test_query063(self):
        url = self.host + "/api/platform/promotionActivityAnalysis/tab2List"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("推广汇总列表获取{}".format(returnMsg))
        return returnMsg
    '''推广活动》推广发放列表获取'''
    def test_query064(self):
        url = self.host + "/api/platform/promotionActivityAdministration/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("推广发放列表获取{}".format(returnMsg))
        return returnMsg
'''后台系统跟进查询接口'''
class Test_query06():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''接口日志》推送日志获取'''
    def test_query065(self):
        url = self.host + "/api/platform/interfaceLog/pushLogList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"insertTimeFrom":"2023-03-01 00:00:00"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("推送日志获取{}".format(returnMsg))
        return returnMsg
    '''接口日志》接收日志获取'''
    def test_query066(self):
        url = self.host + "/api/platform/interfaceLog/receivingLogList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"insertTimeFrom":"2023-03-01 00:00:00"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("接收日志获取{}".format(returnMsg))
        return returnMsg
    '''货主交易日志》充值日志获取'''
    def test_query067(self):
        url = self.host + "/api/platform/transactionLog/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"cashType":"1"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("充值日志获取{}".format(returnMsg))
        return returnMsg
    '''货主交易日志》提现日志获取'''
    def test_query068(self):
        url = self.host + "/api/platform/transactionLog/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"cashType":"0"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("提现日志获取{}".format(returnMsg))
        return returnMsg
    '''供应商运单》供应商运单获取'''
    def test_query069(self):
        url = self.host + "/api/platform/companyOrder/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":100,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("供应商运单获取{}".format(returnMsg))
        return returnMsg
    '''跟进管理》操作日志'''
    def test_query070(self):
        url = self.host + "/api/platform/operationLog/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("操作日志获取{}".format(returnMsg))
        return returnMsg
    '''咨询投诉列表'''
    def test_query071(self):
        url = self.host + "/api/platform/consult/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("咨询投诉列表获取{}".format(returnMsg))
        return returnMsg
'''后台设置查询接口'''
class Test_query07():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''标准档案》系统字典获取'''
    def test_query072(self):
        url = self.host + "/api/system/sysDictionary/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("系统字典获取{}".format(returnMsg))
        return returnMsg
    '''标准档案》车辆档案获取'''
    def test_query073(self):
        url = self.host + "/api/platform/carType/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("车辆档案获取{}".format(returnMsg))
        return returnMsg
    '''标准档案》内部档案获取'''
    def test_query074(self):
        url = self.host + "/api/platform/insideFactory/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("内部档案获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》系统配置获取'''
    def test_query075(self):
        url = self.host + "/api/platform/systemConfig/data"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("系统配置获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》邮箱配置获取'''
    def test_query076(self):
        url = self.host + "/api/platform/emailAccept/email_list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data= {"itemFrom":0,"itemTo":10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("邮箱配置获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》邮箱接收配置获取'''
    def test_query077(self):
        url = self.host + "/api/platform/emailAccept/accept_list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data= {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("邮箱接收配置获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》邮箱接收日志获取'''
    def test_query078(self):
        url = self.host + "/api/platform/emailAccept/log_list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data= {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("邮箱接收日志获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》表单号设置获取'''
    def test_query079(self):
        url = self.host + "/api/platform/fromOddDefine/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("表单号设置获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》服务类型节点设置获取'''
    def test_query080(self):
        url = self.host + "/api/platform/serviceNode/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("服务类型节点设置获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》币种设置获取'''
    def test_query081(self):
        url = self.host + "/api/platform/tenantCurrency/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("币种设置获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》Excel配置库获取'''
    def test_query082(self):
        url = self.host + "/api/platform/excelConfigLib/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("Excel配置库获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》报表模板设计获取'''
    def test_query083(self):
        url = self.host + "/api/platform/modeOutputDesign/getModeTree"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("报表模板设计获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》模板制作获取'''
    def test_query084(self):
        url = self.host + "/api/platform/mouldMake/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("模板制作获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》通知账号配置获取'''
    def test_query085(self):
        url = self.host + "/api/platform/SMSmail/smsList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("通知账号配置获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》接口接收设置获取'''
    def test_query086(self):
        url = self.host + "/api/platform/interfaceReception/autoList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("接口接收设置获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》接收消息分配获取'''
    def test_query087(self):
        url = self.host + "/api/platform/messageSetting/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("接收消息分配获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》内容管理获取'''
    def test_query088(self):
        url = self.host + "/api/platform/contentManager/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("内容管理获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》短信模板获取'''
    def test_query089(self):
        url = self.host + "/api/platform/smsTemplate/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("短信模板获取{}".format(returnMsg))
        return returnMsg
    '''系统规则》虚拟账号配置获取'''
    def test_query090(self):
        url = self.host + "/api/platform/virtualAccountConfig/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("虚拟账号配置获取{}".format(returnMsg))
        return returnMsg
    '''权限管理》角色权限分配获取'''
    def test_query091(self):
        url = self.host + "/api/platform/roleAuthorityDistribution/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("角色权限分配获取{}".format(returnMsg))
        return returnMsg
    '''权限管理》用户角色分配获取'''
    def test_query092(self):
        url = self.host + "/api/platform/accountManager/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("用户角色分配获取{}".format(returnMsg))
        return returnMsg
    '''权限管理》用户数据权限分配获取'''
    def test_query093(self):
        url = self.host + "/api/platform/roleDataAuthority/search"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("用户数据权限分配获取{}".format(returnMsg))
        return returnMsg
    '''用户设置》默认输出模板获取'''
    def test_query094(self):
        url = self.host + "/api/platform/defaultOutput/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("用户数据权限分配获取{}".format(returnMsg))
        return returnMsg
    '''用户设置》常用输出模板获取'''
    def test_query095(self):
        url = self.host + "/api/platform/commonOutput/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("常用输出模板获取{}".format(returnMsg))
        return returnMsg
    '''组织档案》组织机构获取'''
    def test_query096(self):
        url = self.host + "/api/platform/institution/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("组织机构获取{}".format(returnMsg))
        return returnMsg
    '''组织档案》用户档案获取'''
    def test_query097(self):
        url = self.host + "/api/platform/user/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("用户档案获取{}".format(returnMsg))
        return returnMsg
    '''基础档案》标准汇率获取'''
    def test_query098(self):
        url = self.host + "/api/platform/rate/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("标准汇率获取{}".format(returnMsg))
        return returnMsg
    '''基础档案》客户汇率获取'''
    def test_query099(self):
        url = self.host + "/api/platform/rate/currencyList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("客户汇率获取{}".format(returnMsg))
        return returnMsg
    '''基础档案》费用项档案获取'''
    def test_query100(self):
        url = self.host + "/api/platform/chargeItem/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("费用项档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》货主档案获取'''
    def test_query101(self):
        url = self.host + "/api/platform/customersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("费用项档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》二级客户获取'''
    def test_query102(self):
        url = self.host + "/api/platform/customersArchives/secondCustomer/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("二级客户获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》收发货人档案获取'''
    def test_query103(self):
        url = self.host + "/api/platform/customerFactory/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("收发货人档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》货主联系人档案获取'''
    def test_query104(self):
        url = self.host + "/api/platform/customerContact/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"type":"customer"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("货主联系人档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》对账单发票档案获取'''
    def test_query105(self):
        url = self.host + "/api/platform/customerInvoice/invoiceList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("对账单发票档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》开票档案获取'''
    def test_query106(self):
        url = self.host + "/api/platform/customerInvoice/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("开票档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》运输公司档案获取'''
    def test_query107(self):
        url = self.host + "/api/platform/suppliersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("运输公司档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》运输公司联系人档案获取'''
    def test_query108(self):
        url = self.host + "/api/platform/suppliersContact/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"type":"supplier"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("运输公司联系人档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》车辆档案获取'''
    def test_query109(self):
        url = self.host + "/api/platform/supplierCar/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("车辆档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》司机档案获取'''
    def test_query110(self):
        url = self.host + "/api/platform/supplierDriver/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("司机档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》监理档案获取'''
    def test_query111(self):
        url = self.host + "/api/platform/supervisor/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("监理档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》船公司档案获取'''
    def test_query112(self):
        url = self.host + "/api/platform/shipCompany/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("船公司档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》客服人员分配档案获取'''
    def test_query113(self):
        url = self.host + "/api/platform/customerService/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("客服人员分配档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》客户税率档案获取'''
    def test_query114(self):
        url = self.host + "/api/platform/taxRateFile/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagSign":0}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("客户税率档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》供应商税率档案获取'''
    def test_query115(self):
        url = self.host + "/api/platform/taxRateFile/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagSign":1}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("供应商税率档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》个体司机税率档案获取'''
    def test_query116(self):
        url = self.host + "/api/platform/taxRateFile/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagSign":2}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("个体司机税率档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》自有车税率档案获取'''
    def test_query117(self):
        url = self.host + "/api/platform/taxRateFile/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagSign":3}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("自有车税率档案获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》装载量策略获取'''
    def test_query118(self):
        url = self.host + "/api/platform/loadCarRule/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("装载量策略获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》通用设置获取'''
    def test_query119(self):
        url = self.host + "/api/platform/generalSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("通用设置获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》线路范围设置获取'''
    def test_query120(self):
        url = self.host + "/api/platform/lineRangeSetting/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("线路范围设置获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》项目管控获取'''
    def test_query121(self):
        url = self.host + "/api/platform/projectControl/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("项目管控获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》接单中心获取'''
    def test_query122(self):
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"centerType":"center_type_op"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("接单中心获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》计划中心获取'''
    def test_query123(self):
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"centerType":"center_type_plan"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("计划中心获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》调度中心获取'''
    def test_query124(self):
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"centerType":"center_type_dispatch"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("调度中心获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》区域规划获取'''
    def test_query125(self):
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"centerType":"operation_group"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("区域规划获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》应付额外费用审核配置获取'''
    def test_query126(self):
        url = self.host + "/api/platform/additionalCostReview/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应付额外费用审核配置获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》每日产表维护表获取'''
    def test_query127(self):
        url = self.host + "/api/platform/ownCarManagement/everyDay/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"pickupTime":"2023-03-01"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("每日产表维护表获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》虚拟产值基础表获取'''
    def test_query128(self):
        url = self.host + "/api/platform/ownCarManagement/virtual/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"outputValueType":0}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("虚拟产值基础表获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》实际产值优惠表获取'''
    def test_query129(self):
        url = self.host + "/api/platform/ownCarManagement/actual/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"outputValueType":1}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("实际产值优惠表获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》自动分单规则列表获取'''
    def test_query130(self):
        url = self.host + "/api/platform/automaticSortingRules/list/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("自动分单规则列表获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》分单渠道份额设置获取'''
    def test_query131(self):
        url = self.host + "/api/platform/automaticSortingRules/setting/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("分单渠道份额设置获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》客户文件配置管理获取'''
    def test_query132(self):
        url = self.host + "/api/platform/customerFileManagement/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("客户文件配置管理获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》待办预警阈值获取'''
    def test_query133(self):
        url = self.host + "/api/platform/pendingWarning/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("待办预警阈值获取{}".format(returnMsg))
        return returnMsg
    '''运营策略》拆子任务规则获取'''
    def test_query134(self):
        url = self.host + "/api/platform/splitSubtasksRules/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("拆子任务规则获取{}".format(returnMsg))
        return returnMsg
'''后台消息通知查询接口'''
class Test_query08():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''消息》系统消息》发信箱获取'''
    def test_query135(self):
        url = self.host + "/api/message/business/msg_list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"type":0,"insertTimeFrom":"","insertTimeTo":"","content":"","pageDto":{"pageNum":1,"pageSize":10},"senderInfo":""}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("发信箱获取{}".format(returnMsg))
        return returnMsg
    '''消息》系统消息》收信箱获取'''
    def test_query136(self):
        url = self.host + "/api/message/business/msg_send_list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"type":0,"insertTimeFrom":"","insertTimeTo":"","content":"","pageDto":{"pageNum":1,"pageSize":10},"recipientInfo":""}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("收信箱获取{}".format(returnMsg))
        return returnMsg
    '''消息》业务消息》收信箱获取'''
    def test_query137(self):
        url = self.host + "/api/message/business/msg_list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"type":3,"insertTimeFrom":"","insertTimeTo":"","content":"","pageDto":{"pageNum":1,"pageSize":10},"senderInfo":""}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("收信箱获取{}".format(returnMsg))
        return returnMsg
    '''消息》业务消息》发信箱获取'''
    def test_query138(self):
        url = self.host + "/api/message/business/msg_send_list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"type":3,"insertTimeFrom":"","insertTimeTo":"","content":"","pageDto":{"pageNum":1,"pageSize":10},"recipientInfo":""}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("发信箱获取{}".format(returnMsg))
        return returnMsg
    '''消息》进度消息获取'''
    def test_query139(self):
        url = self.host + "/api/message/process/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("进度消息获取{}".format(returnMsg))
        return returnMsg
    '''消息》WEB消息订阅获取'''
    def test_query140(self):
        url = self.host + "/api/message/msgReceiveSetting/subscribe_list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("WEB消息订阅获取{}".format(returnMsg))
        return returnMsg
    '''通知》短信日志获取'''
    def test_query141(self):
        url = self.host + "/api/system/sendMessageByShortMes/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("短信日志获取{}".format(returnMsg))
        return returnMsg
    '''通知》邮件日志获取'''
    def test_query142(self):
        url = self.host + "/api/system/sendMessageByEmail/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("邮件日志获取{}".format(returnMsg))
        return returnMsg
    '''通知》微信日志获取'''
    def test_query143(self):
        url = self.host + "/api/system/sendMessageByWX/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("微信日志获取{}".format(returnMsg))
        return returnMsg
'''货主端查询接口'''
class Test_query09():
    def __init__(self):
        self.host=long.hz_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login002()
    '''查询报价》集装箱出口运输报价获取'''
    def test_query144(self,hz_id="19b2ccc762484fda99aa28fe7fdea866",gk_id="0596b3b2-fcc0-46b0-9e7e-ea25b839e3fc",xzq_id="18228"):
        url = self.host + "/api/owner/searchPrice/price"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        '''customerId = 货主id  taskUnitCode= 服务类型   transportPort = 港口id  departure = 行政区id'''
        data = {"customerId":hz_id,"taskUnitCode":"port_container_export_transport","transportPort":gk_id,"departure":xzq_id}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("集装箱出口运输报价获取{}".format(returnMsg))
        return returnMsg
    '''查询报价》集装箱进口运输报价获取'''
    def test_query145(self,hz_id="19b2ccc762484fda99aa28fe7fdea866",gk_id="0596b3b2-fcc0-46b0-9e7e-ea25b839e3fc",xzq_id="18228"):
        url = self.host + "/api/owner/searchPrice/price"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        '''customerId = 货主id  taskUnitCode= 服务类型   transportPort = 港口id  departure = 行政区id'''
        data = {"customerId":hz_id,"taskUnitCode":"port_container_import_transport","transportPort":gk_id,"destination":xzq_id}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("集装箱进口运输报价获取{}".format(returnMsg))
        return returnMsg
    '''查询报价》厢式车运输报价获取'''
    def test_query146(self,hz_id="19b2ccc762484fda99aa28fe7fdea866",zh_id="18228",xh_id="18228"):
        url = self.host + "/api/owner/searchPrice/price"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        '''customerId = 货主id  taskUnitCode= 服务类型   transportPort = 港口id  departure = 行政区id'''
        data = {"customerId":hz_id,"taskUnitCode":"bulkcargo_transport","departure":zh_id,"destination":xh_id}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("厢式车运输报价获取{}".format(returnMsg))
        return returnMsg
    '''询价管理》询价管理查询获取'''
    def test_query147(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/searchPriceManager/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("询价管理查询获取{}".format(returnMsg))
        return returnMsg
    '''订单管理》订单管理查询获取'''
    def test_query148(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/order/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("订单管理查询获取{}".format(returnMsg))
        return returnMsg
    '''费用中心》费用查询获取'''
    def test_query149(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/costQuery/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("费用查询获取{}".format(returnMsg))
        return returnMsg
    '''费用中心》应付账单查询获取'''
    def test_query150(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/accountsReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应付账单查询获取{}".format(returnMsg))
        return returnMsg
    '''费用中心》应收发票查询获取'''
    def test_query151(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/invoiceReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("应收发票查询获取{}".format(returnMsg))
        return returnMsg
    '''费用中心》月账单查询获取'''
    def test_query152(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/monthlyBill/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("月账单查询获取{}".format(returnMsg))
        return returnMsg
    '''费用中心》对账单查询获取'''
    def test_query153(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/accountStatement/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("对账单查询获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》收发货人查询获取'''
    def test_query154(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/customerFactory/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("收发货人查询获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》联系人档案查询获取'''
    def test_query155(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/customerContact/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id,"type":"customer"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("联系人档案查询获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》结算信息档案查询获取'''
    def test_query156(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/billArchive/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"ownerCustomerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("结算信息档案查询获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》合同报价查询获取'''
    def test_query157(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/cargoOwnerContract/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("结算信息档案查询获取{}".format(returnMsg))
        return returnMsg
    '''智能分析》Excel报表查询获取'''
    def test_query158(self):
        url = self.host + "/api/platform/excelReport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("Excel报表查询获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》个人中心查询获取'''
    def test_query159(self):
        url = self.host + "/api/owner/personalCenter/info"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("个人中心查询获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》账号交易充值记录查询获取'''
    def test_query160(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/personalCenter/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"cashType":1,"customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("账号交易充值记录查询获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》账号交易提现记录查询获取'''
    def test_query161(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/owner/personalCenter/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"cashType":0,"customerId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("账号交易提现记录查询获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》咨询投诉查询获取'''
    def test_query162(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/consult/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"userRoleType":"user_role_type_customer","userRoleId":hz_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("咨询投诉查询获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》权限管理用户管理查询获取'''
    def test_query163(self):
        url = self.host + "/api/owner/privilege/userList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("权限管理用户管理查询获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》权限管理角色管理查询获取'''
    def test_query164(self):
        url = self.host + "/api/owner/privilege/dept_roles"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("权限管理角色管理查询获取{}".format(returnMsg))
        return returnMsg
'''运输公司查询接口'''
class Test_query10():
    def __init__(self):
        self.host=long.gys_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login003()
    '''运单管理》集装箱运输获取'''
    def test_query165(self,gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/company/portTransport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderTag":0,"tagKey":"all","supplierId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("集装箱运输获取{}".format(returnMsg))
        return returnMsg
    '''运单管理》厢式车运输获取'''
    def test_query166(self,gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/company/portTransport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderTag":0,"tagKey":"all","supplierId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("厢式车运输获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》车辆档案获取'''
    def test_query167(self,gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/platform/supplierCar/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supplierId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("车辆档案获取{}".format(returnMsg))
        return returnMsg
    '''档案管理》司机档案获取'''
    def test_query168(self,gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/platform/supplierDriver/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supplierId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("司机档案获取{}".format(returnMsg))
        return returnMsg
    '''excel报表》excel报表获取'''
    def test_query169(self):
        url = self.host + "/api/platform/excelReport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("excel报表获取{}".format(returnMsg))
        return returnMsg
    '''excel报表》订阅计划获取'''
    def test_query170(self):
        url = self.host + "/api/platform/excelReport/planList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("订阅计划获取{}".format(returnMsg))
        return returnMsg
    '''费用中心》月账单获取'''
    def test_query171(self,gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/company/supplierMonthBill/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supplierId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("月账单获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》基础信息获取'''
    def test_query172(self,gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/company/supplierMonthBill/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supplierId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("基础信息获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》咨询投诉获取'''
    def test_query173(self,gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/platform/consult/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"userRoleType":"user_role_type_supplier","userRoleId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("咨询投诉获取{}".format(returnMsg))
        return returnMsg
    '''权限管理》用户管理获取'''
    def test_query174(self):
        url = self.host + "/api/owner/privilege/userList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("用户管理获取{}".format(returnMsg))
        return returnMsg
    '''用户中心》角色管理获取'''
    def test_query175(self):
        url = self.host + "/api/owner/privilege/dept_roles"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print("角色管理获取{}".format(returnMsg))
        return returnMsg

'''后台接口'''
class Test_Added01():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login001()
    '''后台查询港口id'''
    def test_Added000(self,placeName="盐田港"): #传的是行政区名称
        url = self.host + "/api/platform/area/siteList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"active":"active_activated","placeName":placeName}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        gk_id =  A.json()["result"]["data"][0]["guid"]  #港口id
        gk_name =  A.json()["result"]["data"][0]["placeCode"]  #港口名称
        # print(gk_id)
        return  returnMsg,gk_id,gk_name
    '''后台查询行政区id'''
    def test_Added0001(self,lx=3,name="湖南省"): #传的是行政区名称
        url = self.host + "/api/platform/area/districtList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}  #lx 1是大洲 2是国家 3是省  4是市  5是区  6是街道
        data = {"itemFrom":0,"itemTo":10,"filter":{"districtType":lx,"districtName":name}}  # name是地区名称
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        xzq_id =  A.json()["result"]["data"][0]["guid"]  #行政区id
        xzq_name =  A.json()["result"]["data"][0]["districtName"]  #行政区id
        # print(xzq_id)
        return  returnMsg, xzq_id,xzq_name
    '''后台新增货主市场报价单-集装箱运输'''
    def test_Added0002(self):
        url = self.host + "/api/platform/cargoOwnerMarket/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"marketPriceType":"customer","taskUnitCode":"port_container_export_transport","level":3,"showLogo":"",
                "priceType":"price_type_allday","startTime":"2023-03-01","endTime":"2027-03-06","taskUnitTypeName":"集装箱出口运输"}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        bjd_id =  A.json()["result"]["id"]   #报价单id
        bjd_name =  A.json()["result"]["priceNumber"]   #报价单id

        # print(bjd_id)
        return  returnMsg,bjd_id,bjd_name
    '''后台查看货主市场报价单-是否存在'''
    def test_Added0003(self,taskUnitCode="port_container_export_transport"):
        url = self.host + "/api/platform/cargoOwnerMarket/list"
        headers = {'Content-Type': 'application/json',    #报关订单：custom_transport  海事报关：marine_transport
                   'Cookie': 'token={}'.format(self.ht_token)}    #危险品出口运输：dangerous_cargo_export_transport   厢式车：bulkcargo_transport
        data = {"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":taskUnitCode}}  # 服务类型 集装箱出口运输：port_container_export_transport   进口：port_container_import_transport
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems =  A.json()["result"]["returnTotalItems"]   #存在是1
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''后台查看货主市场报价单-状态'''
    def test_Added0004(self,taskUnitCode="port_container_export_transport"):
        url = self.host + "/api/platform/cargoOwnerMarket/list"
        headers = {'Content-Type': 'application/json',    #未启用：status_type_unenabled  已启用：status_type_enabled
                   'Cookie': 'token={}'.format(self.ht_token)}    #已禁用：status_disabled   已生效：status_effective_completed
        data = {"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":taskUnitCode}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        bjd_id =  A.json()["result"]["data"][0]["id"]   #报价单id
        statusType =  A.json()["result"]["data"][0]["statusType"]  #报价单状态
        bjd_bm =  A.json()["result"]["data"][0]["priceNumber"]   #报价单编码
        # print(statusType)
        return returnMsg,statusType,bjd_id,bjd_bm
    '''后台启用货主市场报价单'''
    def test_Added0005(self,bjd_id="a03b736d0e9b43568c45f639fba55087"):
        url = self.host + "/api/platform/cargoOwnerMarket/enable/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''后台禁用货主市场报价单'''
    def test_Added0006(self,bjd_id="a03b736d0e9b43568c45f639fba55087"):
        url = self.host + "/api/platform/cargoOwnerMarket/disable/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''后台删除货主市场报价单'''
    def test_Added0007(self,bjd_id="a9604987beae4fd393c099f6ef53f86e"):
        url = self.host + "/api/platform/cargoOwnerMarket/delete/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''后台新增货主市场报价》集装箱出口'''
    def test_Added0008(self,marketPriceId="",transportPort="",departure="",departureProvinces="",
                       departureCity="",departureArea="",taskUnitCode="", ):
        url = self.host + "/api/platform/cargoOwnerMarket/addDetail"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [{   "marketPriceId": marketPriceId, #报价单id  bjd_id
                    "transportPort": transportPort,        #港口id
                    "departure": departure,           #街道
                    "departureProvinces":departureProvinces,  #省
                    "departureCity": departureCity,       #市
                    "departureArea": departureArea,       #区
                    "taskUnitCode": taskUnitCode,  #服务类型
                    "20GP": "3500",                #报价
                    "currencyType": "CNY",
                    "detailList": [
                        {"20GP": "3500"}           #报价
                    ]}]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # bj_id = A.json()["result"]["data"][0]["id"]   #报价id
        # bjd_bm =  A.json()["result"]["data"][0]["priceNumber"]   #报价单编码
        return returnMsg
    '''后台货主市场集装箱市场报价是否存在'''
    def test_Added0009(self,bzd_id="d196797ffc6d48249988e8fad86c2d03",transportPort="2077",departure="27532"):
        url = self.host + "/api/platform/cargoOwnerMarket/detailList/{}".format(bzd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}  #transportPort 港口id   departure：收货地址id》取街道
        data ={"itemFrom":0,"itemTo":10,"filter":{"transportPort":transportPort,"departure":[departure]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''后台查看货主市场集装箱市场报价id+状态+报价'''
    def test_Added0010(self,bzd_id="d196797ffc6d48249988e8fad86c2d03",transportPort="2077",departure="27532"):
        url = self.host + "/api/platform/cargoOwnerMarket/detailList/{}".format(bzd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}  #transportPort 港口id   departure：收货地址id》取街道
        data ={"itemFrom":0,"itemTo":10,"filter":{"transportPort":transportPort,"departure":[departure]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        enabledType = A.json()["result"]["data"][0]["enabledType"]  # 报价状态 未启用 enabled_type_unenabled 启用 enabled_type_enabled 禁用 enabled_type_disabled
        bj_id = A.json()["result"]["data"][0]["id"]   #报价id
        bj_je = A.json()["result"]["data"][0]["20GP"]   #报价金额

        # print(bj_id)
        return returnMsg,enabledType,bj_id,bj_je
    '''后台启用货主市场集装箱市场报价'''
    def test_Added0011(self,bz_id="642fcfb1e4b0cad4ce795b5e"):
        url = self.host + "/api/platform/cargoOwnerMarket/enableDetail"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[bz_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''后台获取货主id'''
    def test_Added0012(self,hz_name="毛敏租户测试货主1"):
        url = self.host + "/api/platform/customersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerName":hz_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        hz_id = A.json()["result"]["data"][0]["id"]   #货主id
        kf_id = A.json()["result"]["data"][0]["customerServiceId"]["value"] #客服id
        # print(hz_id)
        return returnMsg,hz_id,kf_id
    '''后台查看货主联系人是否存在'''
    def test_Added0013(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/customerContact/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id,"type":"customer"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]   #1表示存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''后台获取货主联系人信息id'''
    def test_Added0014(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/customerContact/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id,"contactName":"测试货主1-联系人1","type":"customer"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        lxr_name = A.json()["result"]["data"][0]["contactName"]   #联系人名称
        lxr_hm = A.json()["result"]["data"][0]["contactMobile"]   #联系方式
        lxr_zt = A.json()["result"]["data"][0]["enabledType"]   #联系人状态 未启用：enabled_type_unenabled 启用：enabled_type_enabled  禁用：enabled_type_disabled
        lxr_id =  A.json()["result"]["data"][0]["id"]  #联系人id
        # print(lxr_name)
        # print(lxr_hm)
        # print(lxr_zt)
        return returnMsg,lxr_id,lxr_zt,lxr_name,lxr_hm
    '''后台新增货主联系人信息'''
    def test_Added0015(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/customerContact/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"customerId":hz_id,"type":"customer","contactName":"货主联系人","contactTelephone":"联系人手机号123456","isDefault":"1"}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''后台启用货主联系人信息'''
    def test_Added0016(self,lxr_id="23c862df9cb040fbb8a90950061d51d9"):
        url = self.host + "/api/platform/customerContact/enable/enabled_type_enabled"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[lxr_id]
        
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''后台查询监理客服是否存在'''
    def test_Added0017(self,jl_name="毛敏监理01"):
        url = self.host + "/api/platform/user/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"username":jl_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"] #存在是1
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''后台查询监理客服id+状态'''
    def test_Added0018(self,jl_name="毛敏监理01"):
        url = self.host + "/api/platform/user/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"username":jl_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        jl_id = A.json()["result"]["data"][0]["guid"]   #监理id
        jl_zt = A.json()["result"]["data"][0]["active"]   #监理状态  激活：active_activated 失效： active_invalid 未激活：active_unactivated
        # print(jl_id)
        # print(jl_zt)
        return returnMsg,jl_id,jl_zt
    '''后台查询组织机构是否存在'''
    def test_Added0019(self,jg_name="测试人员测试租户"):#传的是机构名称
        url = self.host + "/api/platform/institution/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"institutionName":jg_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItem = A.json()["result"]["returnTotalItem"] #存在是1
        # print(returnTotalItem)
        return returnMsg,returnTotalItem
    '''后台查询组织机构信息'''
    def test_Added0020(self,jg_name="测试人员测试租户"):#传的是机构名称
        url = self.host + "/api/platform/institution/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"institutionName":jg_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        jg_id = A.json()["result"]["data"][0]["guid"]   #组织机构id
        jg_zt = A.json()["result"]["data"][0]["active"]   #组织机构状态  激活：active_activated 失效： active_invalid 未激活：active_unactivated
        # print(jg_id)
        # print(jg_zt)
        return returnMsg,jg_zt,jg_id
    '''后台新增组织机构信息'''
    def test_Added0021(self,bm="hp20230412001",jg_name="测试人员测试租户"):#传的是机构编码+机构名称
        url = self.host + "/api/platform/institution"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"institutionCode":bm,"institutionName":jg_name,"customerName":"","supplierName":""}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # jg_id = A.json()["result"]["data"][0]["guid"]   #监理id
        # jg_zt = A.json()["result"]["data"][0]["active"]   #监理状态  激活：active_activated 失效： active_invalid 未激活：active_unactivated
        # print(jg_id)
        # print(jg_zt)
        return returnMsg
    '''后台激活组织机构'''
    def test_Added0022(self,jg_id="49f596d8-b126-4046-a23a-cc76277f4fa2"):#传的是机构id
        url = self.host + "/api/platform/institution/active"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [jg_id]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''后台组织机构是否有部门'''
    def test_Added0023(self,jg_id="8178689e-d3d1-44af-baf9-303ec3579867"): #传的是机构id
        url = self.host + "/api/platform/user/department"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"filter":{"departmentName":"","institutionGuid":jg_id},"itemFrom":0,"itemTo":10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["result"]
        data=  A.json()["result"]["data"]   #有值就是有部门
        # print(data)
        return returnMsg,data
    '''后台组织机构新增部门'''
    def test_Added0024(self,jg_id="8178689e-d3d1-44af-baf9-303ec3579867",bm_name="部门名称"): #传的是机构id
        url = self.host + "/api/platform/department"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"institutionGuid":jg_id,"departmentName":bm_name}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["result"]
        return returnMsg
    '''货主id档案获取'''
    def test_Added0025(self,hz_name="毛敏租户测试货主1"): #传的是货主名称
        url = self.host + "/api/platform/customersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"customerName":hz_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        hz_id = A.json()["result"]["data"][0]["id"] #货主id
        kf_id = A.json()["result"]["data"][0]["customerServiceId"]["value"] #客服id
        # print(hz_id)
        # print(kf_id)
        return returnMsg,hz_id,kf_id
    '''装货单位是否存在'''
    def test_Added0026(self,hz_id="19b2ccc762484fda99aa28fe7fdea866",zh_name="测试集装箱装货地址"): #传的是货主id+装货地址
        url = self.host + "/api/platform/customerFactory/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id,"name":zh_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''装货单位新增/收发货人档案''' #gj_bm 国家编码 sf_id省份编码  cs_bm城市编码 xzq_bm 行政区编码 jd_bm 街道编码  chargingPlaceId：计费地点
    def test_Added0028(self, hz_id="19b2ccc762484fda99aa28fe7fdea866",gj_bm="2",sf_bm="3",cs_bm="4",xzq_bm="5",jd_bm="399",name="测试集装箱装货地址",address="洞井大道1111号"):
        url = self.host + "/api/platform/customerFactory/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"fenceRadius":"","customerId":hz_id,
                "factoryType":0,"name":name,"shortName":name,"country":gj_bm,"province":sf_bm,"city":cs_bm,
                "district":xzq_bm,"street":jd_bm,"chargingPlaceId":cs_bm,
                "address":address,"longitude":"","latitude":"","fenceShape":"none",
                "customerFactoryRemark":"装卸货注意事项","supervisionRemark":"装卸货注意事项",
                "remark":"装卸货注意事项","customerFactoryContactList":[{"isDefault":"1",
                "contactName":"测试","contactTelephone":"152524523524"}]}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        zhdw_id = A.json()["result"]["id"]  # 装货单位id
        zhdw_name = A.json()["result"]["name"]  # 装货单位名称
        zhdw_lxr = A.json()["result"]["customerFactoryContactList"][0]["contactName"] # 装货联系人
        zhdw_xlrdh = A.json()["result"]["customerFactoryContactList"][0]["contactTelephone"] # 装货联系人电话
        zhdw_xxdz = A.json()["result"]["address"] # 装货详细地址
        zhdw_zt = A.json()["result"]["enabledType"] # 装货单位状态
        zh_sx = A.json()["result"]["customerFactoryRemark"] # 装货注意事项
        jl_sx = A.json()["result"]["supervisionRemark"] # 监理注意事项
        # print(zhdw_id)
        # print(zhdw_name)
        # print(zhdw_lxr)
        # print(zhdw_xlrdh)
        # print(zhdw_xxdz)
        # print(zhdw_zt)
        return returnMsg,zhdw_id,zhdw_name,zhdw_lxr,zhdw_xlrdh,zhdw_xxdz,zhdw_zt,zh_sx,jl_sx
    '''装货单位档案'''
    def test_Added0029(self,hz_id="19b2ccc762484fda99aa28fe7fdea866",zh_name="测试集装箱装货地址"): #传的是货主id+装货地址
        url = self.host + "/api/platform/customerFactory/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id,"name":zh_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        zhdw_id = A.json()["result"]["data"][0]["id"]  # 装货单位id
        zhdw_name = A.json()["result"]["data"][0]["name"]  # 装货单位名称
        zhdw_lxr = A.json()["result"]["data"][0]["customerFactoryContactList"][0]["contactName"] # 装货联系人
        zhdw_xlrdh = A.json()["result"]["data"][0]["customerFactoryContactList"][0]["contactTelephone"] # 装货联系人电话
        zhdw_xxdz = A.json()["result"]["data"][0]["address"] # 装货详细地址
        zhdw_zt = A.json()["result"]["data"][0]["enabledType"] # 装货单位状态
        # print(zhdw_id)
        # print(zhdw_name)
        # print(zhdw_lxr)
        # print(zhdw_xlrdh)
        # print(zhdw_xxdz)
        # print(zhdw_zt)
        return returnMsg,zhdw_id,zhdw_name,zhdw_lxr,zhdw_xlrdh,zhdw_xxdz,zhdw_zt
    '''启用装货单位档案'''
    def test_Added0030(self,zhdw_id="e5ebf71d3f0046b4aa373c0b1318d226"): #传装货单位id
        url = self.host + "/api/platform/customerFactory/enable/enabled_type_enabled"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[zhdw_id]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看区域规划是否存在'''
    def test_Added0031(self,taskUnitCode="port_container_export_transport",centerName="shekou_group"): #传的是服务类型 port_container_export_transport 集装箱出口 ,操作区域centerName
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":taskUnitCode,"centerName":centerName,"centerType":"operation_group"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data = A.json()["result"]["data"]   #不存在是[]
        # print(data)
        return returnMsg,data
    '''新增区域规划'''
    def test_Added0032(self,taskUnitCode="port_container_export_transport",centerName="shekou_group",isContainer=1): #传的是服务类型,操作区域centerName
        url = self.host + "/api/platform/centralRuleSettings/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"centerType":"operation_group","isContainer":isContainer,"centerName":centerName,
               "taskUnitCode":[taskUnitCode],"transportPortValue":None,"departureValue":None,"destinationValue":None}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看区域规划id+状态'''
    def test_Added0033(self,taskUnitCode="port_container_export_transport",centerName="shekou_group"): #传的是服务类型 port_container_export_transport 集装箱出口 ,操作区域centerName
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":taskUnitCode,"centerName":centerName,"centerType":"operation_group"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        gh_zt = A.json()["result"]["data"][0]["statusType"]  #启用：enabled_type_enabled 未启用：enabled_type_unenabled   禁用：enabled_type_disabled
        gh_id = A.json()["result"]["data"][0]["id"]  #区域规划id
        # print(gh_zt)
        return returnMsg,gh_zt,gh_id
    '''启用区域规划状态'''
    def test_Added0034(self,gh_id="1646323619694297088"): #传的是区域规划id
        url = self.host + "/api/platform/centralRuleSettings/enable"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[gh_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]    #==启用成功
        return returnMsg
    '''查看接单中心是否存在'''
    def test_Added0035(self,taskUnitCode="port_container_export_transport"): #传的是服务类型
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":taskUnitCode,"centerType":"center_type_op"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''新增接单中心'''
    def test_Added0036(self,taskUnitCode="dangerous_cargo_import_transport",isContainer=1): #传的是服务类型
        url = self.host + "/api/platform/centralRuleSettings/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"centerType":"center_type_op","isContainer":isContainer,"centerName":"center_type_op_sz","taskUnitCode":[taskUnitCode],"transportPortValue":None,"departureValue":None,"destinationValue":None}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看接单中心id+状态'''
    def test_Added0037(self,taskUnitCode="dangerous_cargo_import_transport"): #传的是服务类型
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":taskUnitCode,"centerType":"center_type_op"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示存在
        enabledType = A.json()["result"]["data"][0]["statusType"]  # 接单中心状态 未启用:enabled_type_unenabled 启用：enabled_type_enabled 禁用 enabled_type_disabled
        jdzx_id = A.json()["result"]["data"][0]["id"]
        # print(returnTotalItems)
        # print(enabledType)
        # print(jdzx_id)
        return returnMsg,jdzx_id,enabledType
    '''启用接单中心'''
    def test_Added0038(self, jdzx_id="1646406042251735040"):  # 传的是接单中心id
        url = self.host + "/api/platform/centralRuleSettings/enable"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [jdzx_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看计划中心是否存在'''
    def test_Added0039(self,taskUnitCode="port_container_export_transport"): #传的是服务类型
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":taskUnitCode,"centerType":"center_type_plan"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''新增计划中心'''
    def test_Added0040(self,taskUnitCode="dangerous_cargo_import_transport",isContainer=1): #传的是服务类型
        url = self.host + "/api/platform/centralRuleSettings/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"centerType":"center_type_plan","centerName":"center_type_plan_sz","isContainer":isContainer,"taskUnitCode":[taskUnitCode],"transportPortValue":None,"departureValue":None,"destinationValue":None}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看计划中心'''
    def test_Added0041(self,taskUnitCode="dangerous_cargo_import_transport"): #传的是服务类型
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":taskUnitCode,"centerType":"center_type_plan"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示存在
        enabledType = A.json()["result"]["data"][0]["statusType"]  # 接单中心状态 未启用:enabled_type_unenabled 启用enabled_type_enabled 禁用 enabled_type_disabled
        jdzx_id = A.json()["result"]["data"][0]["id"]
        # print(returnTotalItems)
        # print(enabledType)
        # print(jdzx_id)
        return returnMsg,jdzx_id,enabledType
    '''启用计划中心'''
    def test_Added0042(self, jdzx_id="1646414879750926336"):  # 传的是接单中心id
        url = self.host + "/api/platform/centralRuleSettings/enable"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [jdzx_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看调度中心是否存在'''
    def test_Added0043(self,centerName="center_type_dispatch_mm02",taskUnitCode=""): #传的是调度中心+服务类型
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom": 0, "itemTo": 10,"filter": {"taskUnitCode": taskUnitCode, "centerName": centerName,"centerType": "center_type_dispatch"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]  #1表示存在
        # print(data1)
        return returnMsg,data1
    '''新增集装箱调度中心'''
    def test_Added0044(self,centerName="center_type_dispatch_mm02",distributionChannel=0,isContainer=1): #传的是分单渠道 0是货源大厅，1是自有车 2是供应商
        url = self.host + "/api/platform/centralRuleSettings/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}     #传的是centerName  调度中心
        data ={"centerType":"center_type_dispatch","isContainer":isContainer,"distributionChannel":distributionChannel,"centerName":centerName,"transportPortValue":None,"departureValue":None,"destinationValue":None}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看调度划中心'''
    def test_Added0045(self,centerName="center_type_dispatch_mm02"): #传的是调度中心
        url = self.host + "/api/platform/centralRuleSettings/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"centerName":centerName,"centerType":"center_type_dispatch"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data = A.json()["result"]["data"]
        enabledType = A.json()["result"]["data"][0]["statusType"]  # 接单中心状态 未启用:enabled_type_unenabled 启用enabled_type_enabled 禁用 enabled_type_disabled
        jdzx_id = A.json()["result"]["data"][0]["id"]
        # print(data)
        # print(enabledType)
        # print(jdzx_id)
        return returnMsg,jdzx_id,enabledType,data
    '''启用调度中心'''
    def test_Added0046(self, jdzx_id="1648516911673061376"):  #
        url = self.host + "/api/platform/centralRuleSettings/enable"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [jdzx_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查询货主合同报价单是否存在'''
    def test_Added0047(self, hz_id="2849745179154bee9d483bfcbd6e362b",contractType="transportation_company_type"):  # 传的是货主id
        url = self.host + "/api/platform/cargoOwnerContract/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom": 0, "itemTo": 10,"filter": {"customerId": hz_id, "contractType": contractType}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"] #0
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''查询货主合同报价单id+状态'''
    def test_Added0048(self,hz_id="2849745179154bee9d483bfcbd6e362b",contractType= "transportation_company_type"):  # 传的是货主id
        url = self.host + "/api/platform/cargoOwnerContract/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom": 0, "itemTo": 10,"filter": {"customerId": hz_id,"contractType": contractType}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]                          #已禁用：status_disabled   已生效：status_effective_completed
        statusType = A.json()["result"]["data"][0]["statusType"]    #状态  未启用：status_type_unenabled  已启用：status_type_enabled
        bj_id = A.json()["result"]["data"][0]["id"]      #报价id
        bj_name = A.json()["result"]["data"][0]["customerPriceCode"] #报价名称
        return returnMsg,statusType,bj_id,bj_name
    '''新增货主合同报价单'''
    def test_Added0049(self, hz_id="2849745179154bee9d483bfcbd6e362b",contractType="transportation_company_type"):  # 传的是货主id
        url = self.host + "/api/platform/cargoOwnerContract/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"customerId":hz_id,"startTime":"2023-04-14","endTime":"2030-04-15","fileList":[],"contractType":contractType,"balanceCompanyList":[]}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        bj_id = A.json()["result"]["id"]   #报价id
        bj_name = A.json()["result"]["customerPriceCode"]  #报价名称
        return returnMsg,bj_id,bj_name
    '''启用货主合同报价单'''
    def test_Added0050(self,bjd_id="f8d1ed71e0924dc49cabc8f07d14200f"):  # 传的是报价单id
        url = self.host + "/api/platform/cargoOwnerContract/enable/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查询货主合同报价是否存在''' #transportPort 港口id   departure 街道id
    def test_Added0051(self,bjd_id="41f1c9fd3a3f43ad976fac45eb07688c",transportPort="d017a1b4-7056-4734-9b95-86476e40ffc3",departure=["430111008000"],taskUnitCode="port_container_export_transport"):  # 传的是报价单id
        url = self.host + "/api/platform/cargoOwnerContract/detailList/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"filter": {"transportPort": transportPort, "departure": departure, "taskUnitCode":taskUnitCode, "destination": []}, "itemFrom": 0, "itemTo": 10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data = A.json()["result"]["data"]   #[] 表示不存在
        returnTotalItems = A.json()["result"]["returnTotalItems"]
        # di_id = A.json()["result"]["data"][0]["id"]
        # print(data)
        # print(returnTotalItems)
        return returnMsg,data,returnTotalItems
    '''后台新增货主市场合同报价-集装箱出口运输'''
    def test_Added0052(self, customerPriceId="c344642fec0242a293fa9f186945bb71", taskUnitCode="port_container_export_transport",
                       taskUnitTypeName="集装箱出口运输", transportPort="d017a1b4-7056-4734-9b95-86476e40ffc3",
                       departure="430111008000", departureProvinces="27514", departureCity="27515",
                       departureArea="27569",):
        url = self.host + "/api/platform/cargoOwnerContract/addDetail"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
                {
                    "customerPriceId":customerPriceId, #报价单id
                    "taskUnitCode":taskUnitCode,  #运输类型
                    "taskUnitTypeName":taskUnitTypeName,   #运输类型
                    "transportPort":transportPort,#港口id
                    "departure":departure,  #街道id
                    "departureProvinces":departureProvinces,  #省份
                    "departureCity":departureCity, #装货城市
                    "departureArea":departureArea,  #装货行政区
                    "20GP":"5500",    #车辆类型+价格
                    "currencyType":"CNY",  #币种
                    "detailList":[
                        {
                            "20GP":"5500"   #价格
                        }
                    ]
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查询货主合同报价id+状态''' #transportPort 港口id   departure 街道id
    def test_Added0053(self,bjd_id="7a026ae1fe3844ccafac5c810b401880",transportPort="ed91380f-0a98-4deb-8292-735f52354699",departure=[],taskUnitCode="port_container_import_transport"):  # 传的是报价单id
        url = self.host + "/api/platform/cargoOwnerContract/detailList/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"filter": {"transportPort": transportPort, "departure": departure, "taskUnitCode":taskUnitCode, "destination": []}, "itemFrom": 0, "itemTo": 10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        di_id = A.json()["result"]["data"][0]["id"]   #未启用：enabled_type_unenabled  已启用：enabled_type_enabled
        bj_zt = A.json()["result"]["data"][0]["enabledType"]# 已禁用：enabled_type_disabled
        bj_je = A.json()["result"]["data"][0]["20GP"]
        # print(bj_zt,di_id)
        return returnMsg,di_id,bj_zt,bj_je
    '''启用货主合同报价''' #transportPort 港口id   departure 街道id
    def test_Added0054(self,bj_id="643df6c5e4b06f1c7c74ea4b"):  # 传的是报价id
        url = self.host + "/api/platform/cargoOwnerContract/enableDetail"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [bj_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''获取集装箱出口报价'''
    def test_Added0055(self,taskUnitCode="port_container_export_transport",customerId="19b2ccc762484fda99aa28fe7fdea866",
                       transportPort="d017a1b4-7056-4734-9b95-86476e40ffc3",provinces="27514",city="27515",area="27569",
                       street="430111008000",consigneeConsignorId="e5ebf71d3f0046b4aa373c0b1318d226",pickupTime="2023-04-18 14:02:14",
                       carModeId="20GP"):
        url = self.host + "/api/platform/inputOrder/getPrice"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "taskUnitCode":taskUnitCode, #服务类型
                "customerId":customerId,  #货主id
                "transportPort":transportPort,#港口id
                "departure":[
                    {
                        "provinces":provinces, #省id
                        "city":city,      #市id
                        "area":area,      #区id
                        "street":street,  #街道id
                        "consigneeConsignorId":consigneeConsignorId  #装货单位id
                    }
                ],
                "listDetail":[
                    {
                        "pickupTime":pickupTime,  #装货时间
                        "carModeId":carModeId,                  #柜型
                        "sequence":0
                    }
                ],
                # "institutionId":"49f596d8-b126-4046-a23a-cc76277f4fa2", #机构id
                "isMultipoint":0,
                # "combinationStreet":combinationStreet  #街道名称
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        bj_je = A.json()["result"][0]["price"]
        bj_id = A.json()["result"][0]["customerPricePropertyId"]
        # print(bj_je,bj_id)
        return returnMsg,bj_je,bj_id
    '''后台订单录入查询（全部）''' #transportPort 港口id   departure 街道id
    def test_Added0056(self,hz_id="19b2ccc762484fda99aa28fe7fdea866",customerDelegateCode=""):  # 传的是货主id
        url = self.host + "/api/platform/inputOrder/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "itemFrom": 0,
                "itemTo": 10,
                "filter": {
                    "tagKey": "all",
                    "orderStatus": [
                        "status_completing",
                        "status_fall_back_completed",
                        "status_undo_completed",
                        "status_execution",
                        "status_pending",
                        "status_execution_completed",
                        "status_completed"
                    ],
                    "customerId": hz_id,
                    "customerDelegateCode":customerDelegateCode
                }
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        taskUnitCode = A.json()["result"]["data"][0]["taskUnitCode"] #服务类型
        hz_name = A.json()["result"]["data"][0]["customerId"]["title"] #货主名称
        dd_hao = A.json()["result"]["data"][0]["orderNumber"] #订单号
        weituo_hao = A.json()["result"]["data"][0]["customerDelegateCode"] #客户委托号
        # cz_qy = A.json()["result"]["data"][0]["operationGroup"] #操作区域
        zh_time = A.json()["result"]["data"][0]["pickupTime"] #装货时间
        data1 = A.json()["result"]["data"][0]
        # print(taskUnitCode,hz_name,dd_hao,weituo_hao)
        # print(data1)
        return returnMsg,taskUnitCode,hz_name,dd_hao,weituo_hao,zh_time,data1
    '''计划管理-集装箱出口拆单 查询''' #
    def test_Added0057(self,dd_hao="MCSZ-MCO-20230705-0008"):
        url = self.host + "/api/platform/planPortTransport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"","orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #分单数量
        data1 = A.json()["result"]["data"]
        # data2 = A.json()["result"]["data"][0]["tags"]
        # print(data2)
        # print(returnTotalItems,data1)
        return returnMsg,returnTotalItems,data1
    '''计划管理-集装箱》分单'''
    def test_Added0058(self,zy_che="",gys="",hy_dt=""):  #传的是派自有车，拍供应商，派货源大厅
        url = self.host + "/api/platform/planPortTransport/dispatch"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"isSubmit":1,"ownerCarList":[zy_che],"supplierList":[gys],"supplyHallList":[hy_dt]}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看运输公司是否存在'''
    def test_Added0059(self,gys_name="租户测试自有车-集1"):  #传的是供应商类型
        url = self.host + "/api/platform/suppliersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supplierName":gys_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #=0表示不存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''查看归属法人'''
    def test_Added0060(self):
        url = self.host + "/api/platform/customersArchives/corporations"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"maxNumber":20,"filter":""}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]   #Success
        fr_id = A.json()["result"][0]["value"]  #归属法人id
        # print(fr_id)
        return returnMsg,fr_id
    '''新增运输公司'''
    def test_Added0061(self,fr_id="49f596d8-b126-4046-a23a-cc76277f4fa2",gys_name="租户测试自有车-集1",gyslx="supplier_type_car_owner"):  #传的是供应商类型
        url = self.host + "/api/platform/suppliersArchives/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)} #自有车 supplier_type_car_owner 运输公司：supplier_type_trailer 个体司机：supplier_type_car_other
        data = {"institutionId":fr_id,"innerInstitutionId":fr_id,"supplierName":gys_name,
                "supplierType":gyslx,"companyLevel":"company_level_three","balanceCurrency":"CNY","isContract":"","supplierManager":[]}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        gys_id = A.json()["result"]["id"]  #新增供应商id
        gys_bm = A.json()["result"]["supplierCode"]  #新增供应商编码
        gys_zt = A.json()["result"]["enabledType"]  #新增供应商状态
        gys_name = A.json()["result"]["supplierName"]  #新增供应商名称
        # print(gys_id,gys_bm,gys_zt)
        return returnMsg,gys_id,gys_bm,gys_zt,gys_name
    '''查看运输公司是档案'''
    def test_Added0062(self,gys_name="毛敏租户测试供应商1"):  #传的是供应商类型
        url = self.host + "/api/platform/suppliersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supplierName":gys_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        gys_id = A.json()["result"]["data"][0]["id"]  #新增供应商id
        gys_bm = A.json()["result"]["data"][0]["supplierCode"]  #供应商编码
        gys_zt = A.json()["result"]["data"][0]["enabledType"]  #供应商状态
        gys_name = A.json()["result"]["data"][0]["supplierName"]  #新增供应商名称
        # print(gys_zt,gys_id)
        return returnMsg,gys_id,gys_bm,gys_zt,gys_name
    '''启用运输公司是档案'''
    def test_Added0063(self,gys_id="4f32d9f6fabb4f5199b09f93284902f9",lx="enabled_type_enabled"):  #传的是供应商id
        url = self.host + "/api/platform/suppliersArchives/able" #启用 ：enabled_type_enabled   禁用：enabled_type_disabled
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"ids":[gys_id],"type":lx}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看司机档案是否存在'''
    def test_Added0064(self,sj_name="测试自有车-集1"):  #传的是司机名称
        url = self.host + "/api/platform/supplierDriver/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"driverName":sj_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #=0表示不存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''新增司机档案'''
    def test_Added0065(self,gys_id="4f32d9f6fabb4f5199b09f93284902f9",sj_name="测试自有车-集2",fulx="container_type"):  #传的是供应商id +司机名称+服务类型
        url = self.host + "/api/platform/supplierDriver/save"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}    #服务类型：集装箱：container_type 厢式车：van_type
        data = {"supplierId":gys_id,"driverName":sj_name,"idCardNumber":"","driverMobilePhone":"151252352482",
                "isCanRegister":"1","isRoadBridge":"1","serviceType":fulx,"isJobSupervision":"1","isOwner":0}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        lb_id = A.json()["result"]["id"]  #司机档案ID        新增供应商id  未启用：enabled_type_unenabled  启用：enabled_type_enabled   禁用：enabled_type_disabled
        sj_zt = A.json()["result"]["enabledType"]  #司机状态
        sj_name = A.json()["result"]["driverName"]#司机名称
        sj_id = A.json()["result"]["idCardNumber"]#司机id
        si_dh = A.json()["result"][0]["driverMobilePhone"]#司机号码
        # print(lb_id,sj_id,sj_zt,sj_name,si_dh)
        return returnMsg,lb_id,sj_id,sj_zt,sj_name,si_dh
    '''查看司机档案'''
    def test_Added0066(self,sj_name="测试自有车-集1"):  #传的是司机名称
        url = self.host + "/api/platform/supplierDriver/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"driverName":sj_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        lb_id = A.json()["result"]["data"][0]["id"]  #司机档案ID        新增供应商id  未启用：enabled_type_unenabled  启用：enabled_type_enabled   禁用：enabled_type_disabled
        sj_zt = A.json()["result"]["data"][0]["enabledType"]  #司机状态
        sj_name = A.json()["result"]["data"][0]["driverName"]#司机名称
        sj_id = A.json()["result"]["data"][0]["id"]#司机id
        si_dh = A.json()["result"]["data"][0]["driverMobilePhone"]#司机号码
        dada1 = A.json()["result"]["data"]
        # print(lb_id,sj_id,sj_zt,sj_name,si_dh,dada1)
        return returnMsg,lb_id,sj_id,sj_zt,sj_name,si_dh,dada1
    '''启用司机档案'''
    def test_Added0067(self,lb_id="dc7bafe095e24c0ca5e9c5a8f95e3f99",lx="enabled_type_enabled"):  #传的是司机档案列表id,启用：enabled_type_enabled 禁用：enabled_type_disabled
        url = self.host + "/api/platform/supplierDriver/active_or_inactive/{}".format(lx)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [lb_id]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看车辆档案是否存在'''
    def test_Added0068(self,gys_id="4f32d9f6fabb4f5199b09f93284902f9",cp_hao="粤B7788"):  #传的是供应商id
        url = self.host + "/api/platform/supplierCar/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supplierId":gys_id,"carNumber":cp_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #=0表示不存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    '''新增车辆档案'''
    def test_Added0069(self,gys_id="4f32d9f6fabb4f5199b09f93284902f9",sjda_id="dc7bafe095e24c0ca5e9c5a8f95e3f99",
                       cz_qy="shekou_group",fw_lx="container_type",cp_hao="粤B7788"):  #传的是供应商id+司机档案id
        url = self.host + "/api/platform/supplierCar/updateList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)} #operationGroup = 操作区域   服务类型= serviceType  集装箱：container_type 厢式车：van_type
        data = {"supplierId":gys_id,"driverId":sjda_id,"isOwner":1,"operationGroup":cz_qy,
                "serviceType":fw_lx,"carModeId":"","carNumber":cp_hao,"vehicleIdentificationCode":"test1234567","companyHeaderAddress":""}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        lb_id = A.json()["result"]["id"]  #车辆档案ID        新增供应商id  未启用：enabled_type_unenabled  启用：enabled_type_enabled   禁用：enabled_type_disabled
        sj_zt = A.json()["result"]["enabledType"]  #司机状态
        sj_name = A.json()["result"]["driverName"]#司机名称
        sj_id = A.json()["result"]["id"]#司机id
        si_dh = A.json()["result"][0]["driverMobilePhone"]#司机号码
        # print(lb_id,sj_id,sj_zt,sj_name,si_dh)
        return returnMsg,lb_id,sj_id,sj_zt,sj_name,si_dh
    '''查看车辆档案'''
    def test_Added0070(self,gys_id="4f32d9f6fabb4f5199b09f93284902f9",cp_hao="粤B7788"):  #传的是供应商id
        url = self.host + "/api/platform/supplierCar/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supplierId":gys_id,"carNumber":cp_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        lb_id = A.json()["result"]["data"][0]["id"]  #车辆档案ID         未启用：enabled_type_unenabled  启用：enabled_type_enabled   禁用：enabled_type_disabled
        cp_hao = A.json()["result"]["data"][0]["carNumber"]  #车牌号
        cl_id = A.json()["result"]["data"][0]["driverId"]["value"]#车辆id
        cl_name = A.json()["result"]["data"][0]["driverId"]["title"]#车辆名称
        cl_zt = A.json()["result"]["data"][0]["enabledType"]  # 车辆状态
        cz_qy = A.json()["result"]["data"][0]["operationGroup"]  # 操作区域
        dada1 = A.json()["result"]["data"]
        # print(lb_id,cp_hao,cl_id,cl_name,cl_zt,cz_qy,dada1)
        return returnMsg,lb_id,cp_hao,cl_id,cl_name,cl_zt,cz_qy,dada1
    ''' 启用车辆档案'''
    def test_Added0071(self,lb_id="b944bf1313ac4899a4eb33c5b7f0f3d5",lx="enabled_type_enabled"):  #传的是车辆档案id  启用：enabled_type_enabled 禁用：enabled_type_disabled
        url = self.host + "/api/platform/supplierCar/state/{}".format(lx)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [lb_id]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 查看出车表信息是否存在'''
    def test_Added0072(self,sj_id="dc7bafe095e24c0ca5e9c5a8f95e3f99",cp_hao="粤ZZ0001",zh_time="2023-04-25"):
        url = self.host + "/api/platform/carManager/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom": 0, "itemTo": 10,"filter": {"driverId": sj_id, "mainlandLicensePlateNumber": cp_hao,"pickupTimeFrom":zh_time}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #=0表示不存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    ''' 生成出车表'''
    def test_Added0073(self,fw_lx="container_type",cz_qy="yuenan_group",tims="2023-04-25"):
        url = self.host + "/api/platform/carManager"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"serviceType":fw_lx,"operationGroup":cz_qy,"pickupTime":tims}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 查看出车表信息档案'''
    def test_Added0074(self,sj_id="dc7bafe095e24c0ca5e9c5a8f95e3f99",cp_hao="粤ZZ0001",zh_time="2023-04-25 15:18:43"):
        url = self.host + "/api/platform/carManager/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom": 0, "itemTo": 10,"filter": {"driverId": sj_id, "mainlandLicensePlateNumber": cp_hao,"pickupTimeFrom":zh_time}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        ccb_id = A.json()["result"]["data"][0]["id"]  #出车表档案id
        cc_zt = A.json()["result"]["data"][0]["status"]  #出车状态     未分配：car_dispatch_undistribute , 已分配：car_dispatch_completed
        isDispatch = A.json()["result"]["data"][0]["isDispatch"]  #是否出车    是1  否 0
        cc_pz = A.json()["result"]["data"][0]["mainlandLicensePlateNumber"]  #车牌号
        # print(ccb_id,cc_zt,isDispatch,cc_pz)
        print("这个是出车状态：{}".format(cc_zt))
        return returnMsg,ccb_id,cc_zt,isDispatch,cc_pz
    ''' 计划管理》派自有车'''
    def test_Added0075(self,id="f01261b41a854d3eb4ca99837a8cfe9e",driverId="dc7bafe095e24c0ca5e9c5a8f95e3f99",supplierId="4f32d9f6fabb4f5199b09f93284902f9",
                       mainlandLicensePlateNumber="粤ZZ0001",orderNumber="MCSZ-MCO-20230724-0001",pickupTime="2023-07-29 08:55:13",bookingNumber="1283074956",
                       transportType="transport_type_one_one",mainlandLicensePlate="7e637a1126b14f759dbdb2b77ab893f8",driverName="测试自有车-集1",mainlandPhone="13022222521",
                       supplierName="租户测试自有车-集1",carDispatchId="85b527a861ad4284b6279e81bc59e67c"):
        url = self.host + "/api/platform/dispatchPortTransport/delivery/submit"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
                {
                    "id":id,           #订单id
                    "driverId":driverId,     #司机档案列表id（司机id）
                    "supplierId":supplierId,   #供应商id
                    "driverUserId":"",
                    "mainlandLicensePlateNumber":mainlandLicensePlateNumber,      #车牌号
                    "dispatchGroup":"",
                    "orderNumber":orderNumber,     #订单号
                    "pickupTime":pickupTime,         #装货时间
                    # "bookingNumber":bookingNumber,   #订舱号
                    "isSanitaryTreatment":"0",
                    "transportType":transportType,   #运输方式 多点装货	：transport_type_many_one  多点卸货：transport_type_one_many 单点运输：transport_type_one_one
                    "mainlandLicensePlate":mainlandLicensePlate,  #车辆档案id
                    "driverName":driverName,                                 #司机名称
                    "mainlandPhone":mainlandPhone,                              #司机号码
                    "supplierName":supplierName,                           #供应商名称  不必填
                    "isContainer":1,
                    "carDispatchId":carDispatchId         #出车表档案id
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 查看自有车司机报价单是否存在'''
    def test_Added0076(self,fw_lx="port_container_export_transport"):  #传的是服务类型
        url = self.host + "/api/platform/ownDriverQuotation/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":fw_lx}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #=0表示不存在
        # print(returnTotalItems)
        return returnMsg,returnTotalItems
    ''' 新增自有车司机报价单'''
    def test_Added0078(self,fw_lx="port_container_export_transport",fw_name="集装箱出口运输"): #传的是服务类型 + 时间 + 服务类型名称
        url = self.host + "/api/platform/ownDriverQuotation/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"marketPriceType":"owner_driver","taskUnitCode":fw_lx,"startTime":"2023-04-23","endTime":"2027-04-30","taskUnitTypeName":fw_name}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        bjd_id = A.json()["result"]["id"]   #报价单id
        bjd_name = A.json()["result"]["priceNumber"]   #报价单名称
        # print(returnMsg)
        return returnMsg,bjd_id,bjd_name
    ''' 查看自有车司机报价单信息'''
    def test_Added0079(self,fw_lx="port_container_export_transport"):  #传的是服务类型
        url = self.host + "/api/platform/ownDriverQuotation/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":fw_lx}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        bjd_id = A.json()["result"]["data"][0]["id"]  #报价单id
        bjd_nama = A.json()["result"]["data"][0]["priceNumber"]  #报价单名称
        bjd_zt = A.json()["result"]["data"][0]["statusType"]  #报价单状态  未启用：status_type_unenabled  已启用：status_type_enabled 禁用：status_disabled
        bjd_lx = A.json()["result"]["data"][0]["taskUnitTypeName"]  #报价单类型

        # print(bjd_id,bjd_nama,bjd_zt,bjd_lx)
        return returnMsg,bjd_id,bjd_nama,bjd_zt,bjd_lx
    ''' 启用自有车司机报价单'''
    def test_Added0080(self,bjd_id="756a5cea58864b5799fc0aa8e5b3ea63"): #传的是报价单id
        url = self.host + "/api/platform/cargoOwnerMarket/enable/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 查看自有车司机报价档案》进口'''
    def test_Added0081(self,bjd_id="3050e8ba351a4de28bab7047ffe61a69",transportPort="d017a1b4-7056-4734-9b95-86476e40ffc3",departure="430111008000"): #传的是报价单id+港口id+街道id
        url = self.host + "/api/platform/cargoOwnerMarket/detailList/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"transportPort":transportPort,"departure":[departure]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        di_id = A.json()["result"]["data"][0]["id"]  # 未启用：enabled_type_unenabled  已启用：enabled_type_enabled
        bj_zt = A.json()["result"]["data"][0]["enabledType"]  # 已禁用：enabled_type_disabled
        bj_je = A.json()["result"]["data"][0]["20GP"]
        # print(bj_zt, di_id)
        return returnMsg,di_id,bj_zt,bj_je
    ''' 查看自有车司机报价是否存在'''
    def test_Added0082(self,bjd_id="756a5cea58864b5799fc0aa8e5b3ea63",transportPort="d017a1b4-7056-4734-9b95-86476e40ffc3",departure="430111008000"): #传的是报价单id+港口id+街道id
        url = self.host + "/api/platform/cargoOwnerMarket/detailList/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"transportPort":transportPort,"departure":[departure]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  # =0表示不存在

        return returnMsg,returnTotalItems
    '''调度管理集装箱查询'''
    def test_Added0083(self,dd_hao="MCSZ-MCO-20230726-0008",lx="port_container_export_transport"):
        url = self.host + "/api/platform/dispatchPortTransport/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderNumber":dd_hao,"taskUnitCode":lx}}

        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        dd_id = A.json()["result"]["data"][0]["id"]   #订单id
        # zh_tine = A.json()["result"]["data"][0]["pickupTime"]  #装货时间
        # cz_qy = A.json()["result"]["data"][0]["operationGroup"]  # 操作区域
        dd_hao = A.json()["result"]["data"][0]["orderNumber"]  # 订单号
        data1 = A.json()["result"]["data"]
        # print(dd_id,dd_hao)
        return returnMsg,dd_id,dd_hao,data1

    ''' 复制出车表'''
    def test_Added0084(self,ccb_id="c21779f726f84721954e74151a91b2e3"):
        url = self.host + "/api/platform/carManager/copy"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [ccb_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 调度管理》获取车牌号'''
    def test_Added0085(self,zh_time="2023-06-19",fw_lx="port_container_export_transport"):
        url = self.host + "/api/standard/search/car_dispatch?filter=&pickupTime={}&serviceType={}&dispatchGroup=".format(zh_time,fw_lx)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        result = A.json()["result"]
        # print(result)
        return returnMsg,result
    ''' 应收费用制作查询费用信息>待完成页签'''
    def test_Added0086(self,dd_hao="MCSZ-MCO-20230615-0001"):
        url = self.host + "/api/platform/expensesReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"chargeStatusArray":["status_check_awaiting","status_check_all_completed_awaiting_upstream",
                                            "status_check_detail_completed","status_check_completed"],"orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id = A.json()["result"]["data"][0]["id"]   #账单ID
        # dd_hao = A.json()["result"]["data"][0]["orderNumber"]    #订单号    明细已审核：status_check_completed
        # zd_zt = A.json()["result"]["data"][0]["chargeStatus"]    #账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
        # cp_hao = A.json()["result"]["data"][0]["mainlandLicensePlateNumber"]  #车牌号
        # js_dw = A.json()["result"]["data"][0]["supplierName"]  #结算单位
        # js_je = A.json()["result"]["data"][0]["inComeAmountTotal"]  #结算金额
        # sj_name = A.json()["result"]["data"][0]["driverName"]  #司机姓名
        data1 = A.json()["result"]["data"]
        # print(zd_id)
        return returnMsg,data1

    ''' 应付费用制作查询运单基本信息(费用明细)'''
    def test_Added0087(self,dd_id="0280f8173f364950a6123d6094d995d4"):
        url = self.host + "/api/company/portTransport/executionInfo/{}".format(dd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id = A.json()["result"]["chargeInfo"][0]["id"]   #账单ID
        # cp_hao = A.json()["result"]["supplierTransportOrderVo"]["mainlandLicensePlateNumber"]  #车牌号
        # sj_name = A.json()["result"]["supplierTransportOrderVo"]["driverName"]  #司机姓名
        data1 =  A.json()["result"]
        # print(data1)
        return returnMsg,data1
    ''' 应付费用制作查询运单费用明细信息(费用明细)'''
    def test_Added0088(self,dd_id="0280f8173f364950a6123d6094d995d4"):
        url = self.host + "/api/platform/expensesPay/details/{}".format(dd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id = A.json()["result"]["costList"][0]["id"]   #账单ID
        # dd_hao = A.json()["result"]["costList"][0]["orderNumber"]    #订单号    明细已审核：status_check_completed
        # zd_zt = A.json()["result"]["costList"][0]["statusType"]    #明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
        # js_dw = A.json()["result"]["costList"][0]["balanceId"]["title"] #结算单位
        data1 = A.json()["result"]["costList"]
        # print(zd_id)
        return returnMsg,data1
    ''' 跟踪管理》录入柜号'''
    def test_Added0089(self,x_hao="FSCU5130217",kg_z="2580",dd_id="4b70de7b20c84f3abe72908c1a4cb70f",ft_hao="CAAU5507656"):
        url = self.host + "/api/company/portTransport/inputBoxNumber"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
                  {
                    "cabinetWeight": kg_z,  #空柜重
                    "carWeight": 0,
                    "containerNumber": x_hao,  #箱号
                    "fileList": [
                      {
                        "fileFormat": "",
                        "fileName": "",
                        "fileUrl": ""
                      }
                    ],
                    "fileType": "",
                    "id": dd_id,#订单ID
                    "interfaceId": "",
                    "sealNumber": ft_hao,  #封条号
                    "trailerWeight": 0
                  }
                ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 查看服务节点是否存在'''
    def test_Added0090(self,fw_lx="port_container_export_transport"):
        url = self.host + "/api/platform/serviceNode/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"taskUnitCode":fw_lx}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        result = A.json()["result"]["returnTotalItems"]  # 0表示不存在
        # print(result)
        return returnMsg,result
    ''' 跟踪管理》集装箱运输》主列表'''
    def test_Added0091(self,dd_hao="MCSZ-MCO-20230504-0010",fw_lx="port_container_export_transport"):
        url = self.host + "/api/platform/containerTransport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"currentTag":"status_execution","orderNumber":dd_hao,"taskUnitCode":fw_lx}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # g_hao = A.json()["result"]["data"][0]["containerNumber"]  #柜号
        # ft_hao = A.json()["result"]["data"][0]["sealNumber"]    #封条号
        # k_gz = A.json()["result"]["data"][0]["cabinetWeight"]   #空柜重
        data1 = A.json()["result"]["data"]
        # print(data1 )
        return returnMsg,data1
    ''' 自有车撤销派单'''
    def test_Added0092(self,dd_id="22dca9ef20204b1dbdf5ec33f0dda3ae"):
        url = self.host + "/api/platform/dispatchPortTransport/revoke"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"cancelDispatchType":"cancel_dispatch_type_01","cancelDispatchReason":"测试撤销派自有车","ids":[dd_id]}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # print(result)
        return returnMsg
    ''' 跟踪管理》节点跟踪'''
    def test_Added0093(self,dd_id="8b79ca87635843d8bf5c368ee96c4286"):
        url = self.host + "/api/company/portTransport/trackNodeList/{}".format(dd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]
        # a=data1[2]["taskTypeName"]
        # b=data1[2]["finishTime"]
        # print(data1[2])
        # print(data1[2]["taskTypeName"])

        return returnMsg,data1
    ''' 应付管理》应付制作费用列表（主列表）'''
    def test_Added0094(self,dd_hao="MCSZ-MCO-20230627-0007",fw_lx="port_container_export_transport"):
        url = self.host + "/api/platform/expensesPay/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"chargeStatusArray":[],"orderNumber":dd_hao,"taskUnitCode":fw_lx}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # sj_name = A.json()["result"]["data"][0]["driverName"]  #司机名称
        # dd_id = A.json()["result"]["data"][0]["id"]
        # cp_hao = A.json()["result"]["data"][0]["mainlandLicensePlateNumber"]  #车牌号
        # js_dw = A.json()["result"]["data"][0]["supplierId"]["title"] #结算单位  未派单的时候没有结算单位key
        dd_hao = A.json()["result"]["data"][0]["orderNumber"]  #订单号      已整审：status_check_all_completed
        # dd_zt = A.json()["result"]["data"][0]["chargeStatus"]  # 订单号状态  #待审核：status_check_awaiting，明细已审核：status_check_completed
        data1 = A.json()["result"]["data"][0]
        # print(data1)
        return returnMsg,dd_hao,data1

    ''' 应付费用制作明细审核'''
    def test_Added0095(self,mx_id="814279557554364416"):
        url = self.host + "/api/platform/expensesPay/examine"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [mx_id]  #账单明细id
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]

        return returnMsg
    ''' 应付费用制作审核'''
    def test_Added0096(self,dd_id="b6633add8f9245d49c6e0458044716c5"):
        url = self.host + "/api/platform/expensesPay/check"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [dd_id]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]

        return returnMsg
    ''' 应付费用改单列表查询'''
    def test_Added0097(self,dd_hao="MCSZ-MCO-20230505-0001"):
        url = self.host + "/api/platform/changePay/list/1"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"status":[],"orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        # print(data1)
        return returnMsg,data1
    ''' 应付费用改单提交'''
    def test_Added0098(self,title,detail):
        url = self.host + "/api/platform/changePay/submit/1"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        # data = {
        #     "title":{
        #         "id":"1572ceeb757e416c9d5e3bbde29aa1c8",
        #         "statusType":"status_submit_awaiting",
        #         "renewalMode":"renewal_type_average",
        #         "renewalNumber":"MCSZ-MPC-230802-0001",
        #         "orderId":"c29a892b691b46158087ff9fb7fc795c",
        #         "orderNumber":"MCSZ-MCO-20230802-0012",
        #         "responsibleParty":"responsible_party_haige",
        #         "renewalReason":"responsible_party_haige_01",
        #         "beforeAmount":0,
        #         "afterAmount":3500,
        #         "diffAmount":3500,
        #         "currency":"CNY",
        #         "chargeFrom":"change_dispatch_owner_car",
        #         "customerId":"19b2ccc762484fda99aa28fe7fdea866",
        #         "insertTime":"2023-08-02 17:10:35",
        #         "updateTime":"2023-08-02 17:10:35",
        #         "remark":"费用改单",
        #         "taskUnitTypeName":"集装箱出口运输",
        #         "isSalesPrice":0,
        #         "chargeDirection":1
        #     },
        #     "detail":[
        #         {
        #             "id":"846644694972321792",
        #             "renewalId":"1572ceeb757e416c9d5e3bbde29aa1c8",
        #             "balanceId":"f93e3a57bc3346d88537c657ace2cf5d",
        #             "statusType":"status_submit_awaiting",
        #             "chargeItemId":"3b557931010249bd844f607e1dc2ab1f",
        #             "chargeUnit":"charge_unit_767",
        #             "price":3500,
        #             "number":1,
        #             "amount":3500,
        #             "currency":"CNY",
        #             "exchangeRate":1,
        #             "tax":3,
        #             "taxType":"tax_rate_way_include",
        #             "taxAmount":101.94,
        #             "netAmount":3398.06,
        #             "amountIncludingTax":3500,
        #             "insertTime":"2023-08-02 17:10:35",
        #             "insertUser":"c038a360537011edac69fa163e78c411",
        #             "chargeType":"charge_type_base",
        #             "reimburseType":"reimburse_type_03",
        #             "mainlandLicensePlateNumber":"粤B7788",
        #             "supplierType":"supplier_type_car_owner",
        #             "chargeOrigin":"change_dispatch_owner_car",
        #             "salesPrice":3500,
        #             "salesAmount":3500,
        #             "salesNumber":1
        #         }
        #     ]
        # }
        data = {"title":title,"detail":[detail]}


        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 应付费用改单审核'''
    def test_Added0099(self,gd_id="fe0b32496b574fff85ebba7999cf7984"):
        url = self.host + "/api/platform/changePay/check/1/{}".format(gd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 新增货主厢式车多点运输报价'''
    def test_Added0100(self,customerPriceId,taskUnitCode,taskUnitTypeName,departure,departureProvinces
                       ,departureCity,departureArea,destination,destinationProvinces,destinationCity,destinationArea):
        url = self.host + "/api/platform/cargoOwnerContract/addDetail"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
                {
                    "customerPriceId":customerPriceId, #报价单id
                    "taskUnitCode":taskUnitCode,  #运输类型 厢式车运输 bulkcargo_transport
                    "taskUnitTypeName":taskUnitTypeName, #运输类型名称
                    "departure":departure,   #装货街道
                    "departureProvinces":departureProvinces, #装货省
                    "departureCity":departureCity,   #装货市
                    "departureArea":departureArea,   #装货区
                    "destination":destination, #卸货街道
                    "destinationProvinces":destinationProvinces, #卸货省
                    "destinationCity":destinationCity,        #卸货市
                    "destinationArea":destinationArea, #卸货区
                    "3T":"1000",
                    "5T":"2000",
                    "8T":"2500",
                    "10T":"3000",
                    "12T":"3500",
                    "14T":"4000",
                    "15T":"5000",
                    "18T":"6000",
                    "currencyType":"CNY",
                    "detailList":[
                        {
                            "3T":"1000",
                            "5T":"2000",
                            "8T":"2500",
                            "10T":"3000",
                            "12T":"3500",
                            "14T":"4000",
                            "15T":"5000",
                            "18T":"6000"
                        }
                    ]
                }
            ]


        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 查询货主合同报价厢式车报价'''
    def test_Added0101(self,bjd_id="41f1c9fd3a3f43ad976fac45eb07688c",taskUnitCode="dangerous_cargo_export_transport",jd_bm=[]):
        url = self.host + "/api/platform/cargoOwnerContract/detailList/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"filter":{"taskUnitCode":taskUnitCode,"departure":jd_bm,"destination":[]},"itemFrom":0,"itemTo":10}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  # 1表示存在
        # bj_id = A.json()["result"]["data"][0]["id"]   #未启用：enabled_type_unenabled  已启用：enabled_type_enabled
        # bj_zt = A.json()["result"]["data"][0]["enabledType"]# 已禁用：enabled_type_disabled
        data1 =  A.json()["result"]["data"]
        # print(data1)
        return returnMsg,returnTotalItems,data1
    ''' 获取厢式车报价》集装箱'''
    def test_Added0102(self,customerId,provinces,city,area,street,provinces1,city1,area1,street1,consigneeConsignorId1,consigneeConsignorId2):
        url = self.host + "/api/platform/inputOrder/getPrice"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "taskUnitCode":"bulkcargo_transport", #服务类型
                "customerId":customerId, #货主id
                "transportPort":"",  #港口id
                "destination":[
                    {
                        "provinces":provinces, #卸货省id
                        "city":city, #卸货市id
                        "area":area, #卸货区id
                        "street":street, #卸货街道id
                        "consigneeConsignorId":""
                    }
                ],
                "departure":[
                    {
                        "provinces":provinces1, #装货省id
                        "city":city1,      #装货市id
                        "area":area1,      #装货区id
                        "street":street1,  #装货街道id
                        "consigneeConsignorId":consigneeConsignorId1  #装货单位id
                    },
                    {
                        "provinces":provinces1, #装货省id
                        "city":city1,       #装货市id
                        "area":area1,      #装货区id
                        "street":street1,   #装货街道id
                        "consigneeConsignorId":consigneeConsignorId2 #装货单位id
                    }
                ],
                "listDetail":[
                    {
                        "pickupTime":"2023-05-10 00:00:00",   #装货时间
                        "carModeId":"15T",
                        "sequence":0
                    }
                ],
                "institutionId":"",
                "isMultipoint":1,
                "combinationStreet":"海山街道+海山街道"   #装货街道
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        bj_je = A.json()["result"][0]["price"]
        bj_id = A.json()["result"][0]["customerPricePropertyId"]
        # print(bj_je,bj_id)
        return returnMsg,bj_je,bj_id
    '''计划管理-厢式车拆单 查询''' #
    def test_Added0103(self,dd_hao="MCSZ-MCO-20230724-0008"):  # 传的是报价id
        url = self.host + "/api/platform/planBulkcargoTransport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"","orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #分单数量
        data1 = A.json()["result"]["data"]
        # print(data1)
        return returnMsg,returnTotalItems,data1
    '''计划管理厢式车-派供应商 合同报价''' #
    def test_Added0104(self,dd_id="1ac675a6abe2458ca72706e821320607",gys_lxr="",gys_lxrdh="",gys_id=""):  # 传的是报价id
        url = self.host + "/api/platform/dispatchPortTransport/supplier/submit"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "ids":[
                    dd_id    #订单ID
                ],
                "supplierContact":gys_lxr,  #供应商联系人
                "supplierContactPhone":gys_lxrdh,#供应商联系人电话
                "supplierId":gys_id  #供应商ID
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''供应商信息查询''' #
    def test_Added0105(self,gys_id="0c2d642860a84e798d78ed81aaa2a0ec"):  # 传的是供应商id
        url = self.host + "/api/platform/suppliersContact/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "itemFrom":0,
                "itemTo":10,
                "filter":{
                    "customerId":gys_id,
                    "type":"supplier"
                }
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        gys_id = A.json()["result"]["data"][0]["customerId"]["value"]
        gys_lxr = A.json()["result"]["data"][0]["contactName"]
        gys_lxrdh = A.json()["result"]["data"][0]["contactTelephone"]
        # print(gys_id,gys_lxr,gys_lxrdh)
        return returnMsg,gys_id,gys_lxr,gys_lxrdh
    '''计划管理厢式车-派供应商 手工报价'''  #
    def test_Added0106(self, dd_id="1ac675a6abe2458ca72706e821320607", gys_lxr="", gys_lxrdh="", gys_id="",je=""):  # 传的是报价id
        url = self.host + "/api/platform/dispatchPortTransport/supplier/charge"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
                {
                    "supplierId":gys_id, #供应商ID
                    "supplierContact":gys_lxr,                  #供应商联系人
                    "supplierContactPhone":gys_lxrdh,              #供应商联系电话
                    "_chargeName":"运费",
                    "price":je,                                  #金额
                    "currency":"CNY",
                    "supplierTransportOrderId":dd_id  #订单ID
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''计划管理厢式车-改派供应商合同报价 '''  #
    def test_Added0107(self, dd_id="1ac675a6abe2458ca72706e821320607", gys_lxr="", gys_lxrdh="", gys_id=""):  # 传的是报价id
        url = self.host + "/api/platform/dispatchPortTransport/changeSupplier"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
                {
                    "id":dd_id,
                    "supplierId":gys_id, #供应商ID
                    "supplierContact":gys_lxr,            #供应商联系人
                    "supplierContactPhone":gys_lxrdh,   #供应商联系电话
                    "changeReason":"测试改派"
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg


    '''计划管理厢式车-改派供应商 手工报价'''  #
    def test_Added0108(self, dd_id="37acc58a8b634cc995ba1dbed24b46ce",gys_lxr="测试联系人",gys_lxrdh="123456789",gys_id="92e1c29609f34002bdea0ee52959fe56"):  # 传的是报价id
        url = self.host + "/api/platform/dispatchPortTransport/changeSupplier"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
                {
                    "id":dd_id,
                    "supplierId":gys_id,
                    "supplierContact":gys_lxr,
                    "supplierContactPhone":gys_lxrdh,
                    "changeReason":"测试改派"
                }
            ]


        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1= A.json()["result"]
        # print(data1)
        return returnMsg,data1

    '''计划管理厢式车-改派供应商 手工报价'''  #
    def test_Added0109(self, dd_id="6df89883d446448ebb31067ba957c517",gys_lxr="测试联系人",gys_lxrdh="123456789",gys_id="92e1c29609f34002bdea0ee52959fe56"):  # 传的是报价id
        url = self.host + "/api/platform/dispatchPortTransport/supplier/charge"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
                {
                    "supplierId":gys_id,
                    "supplierContact":gys_lxr,
                    "supplierContactPhone":gys_lxrdh,
                    "_chargeName":"运费",
                    "price":4500,
                    "currency":"CNY",
                    "supplierTransportOrderId":dd_id
                }
            ]


        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''应付费用制作》新增费用明细'''  #
    def test_Added0110(self,dd_id="6df89883d446448ebb31067ba957c517", cp_hao="测试联系人",jj_dw="123456789",
                       gys_id="92e1c29609f34002bdea0ee52959fe56",fyx_id="",fy_lx=""):  # 传的是报价id
        url = self.host + "/api/platform/expensesPay/preservation"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}

        data =[
                {
                    "number":1,
                    "currency":"CNY",
                    "supplierTransportId":dd_id, #订单id
                    "balanceId":gys_id,   #结算单位id（运输公司id）
                    # "supplierType":"supplier_type_car_owner",    #供应商类型
                    "customerId":gys_id,  #结算单位id（运输公司id）
                    "secondCustomer":"",
                    "mainlandLicensePlateNumber":cp_hao,    #车牌号
                    "price":666,                        #单价
                    "chargeUnit":jj_dw,     #计量单位
                    "chargeItemId":fyx_id,  #费用项id
                    "chargeType":fy_lx     #费用类型
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    ''' 查询费用项id'''
    def test_Added0111(self,fyx_name="报关费"):
        url = self.host + "/api/platform/chargeItem/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"chargeName":fyx_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #存在是1
        data1 = A.json()["result"]["data"]
        # id = A.json()["result"]["data"][0]["id"]
        # fy_lx = A.json()["result"]["data"][0]["chargeType"]  #费用类型
        # jl_dw = A.json()["result"]["data"][0]["chargeUnit"]  #计量单位
        # fy_zt = A.json()["result"]["data"][0]["active"]  #计费用状态    失效：active_invalid 激活：active_activated
        # print(id,fy_lx,jl_dw)
        return returnMsg,returnTotalItems,data1

    ''' 新增费用项'''
    def test_Added0112(self,fyx_name="报关费"):
        url = self.host + "/api/platform/chargeItem/save"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"chargeName":fyx_name}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 激活费用项'''
    def test_Added0113(self,fyx_id="7458ec3b3cef47138ba0057fcdec3035"):
        url = self.host + "/api/platform/chargeItem/active/{}".format(fyx_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 变更分单>供应商'''
    def test_Added0114(self,dd_id="f01261b41a854d3eb4ca99837a8cfe9e",isSubmit=1):
        url = self.host + "/api/platform/planPortTransport/change"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"isSubmit":isSubmit,"supplierList":[dd_id]}  #supplierList 表示供应商
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 查询司机市场报价'''
    def test_Added0115(self,fy_lx="port_container_export_transport"):
        url = self.host + "/api/platform/driverMarket/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"taskUnitCode":fy_lx}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]
        data1 = A.json()["result"]["data"]
        # id = A.json()["result"]["data"][0]["id"]
        # zt = A.json()["result"]["data"][0]["statusType"]
        # print(returnTotalItems,id,zt)
        return returnMsg,returnTotalItems,data1
    ''' 新增司机市场报价'''
    def test_Added0116(self,fy_lx="port_container_export_transport",fy_name="集装箱出口运输"):
        url = self.host + "/api/platform/driverMarket/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={
                "marketPriceType":"driver",
                "taskUnitCode":fy_lx,  #费用类型
                "level":3,                         #优先级
                "showLogo":"",
                "priceType":"price_type_allday",   #价格类型
                "startTime":"2023-05-01",          #有效开始时间
                "endTime":"2026-05-31",            #有效结束时间
                "taskUnitTypeName":fy_name  #费用类型
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''后台订单管理》集装箱运输列表'''
    def test_Added0117(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/receiveOrderPort/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id,"tagKey":"all","taskUnitCodeType":"container"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        # print(data1)

        return returnMsg,data1
    '''后台运单管理》监理管理信息查询'''
    def test_Added0118(self,dd_hao="MCSZ-MCO-20230615-0001-02"):
        url = self.host + "/api/platform/supervisorManager/list"
        headers = {'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagKey":"","status":"","orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        # jldd_id = A.json()["result"]["data"][0]["id"]   #监理订单ID
        # dd_id = A.json()["result"]["data"][0]["orderId"]  # ID
        # dd_zt = A.json()["result"]["data"][0]["orderStatus"]  # 状态
        # print(jldd_id,dd_zt)
        return returnMsg,data1
    '''后台运单管理》报关管理信息查询'''
    def test_Added0119(self,dd_hao="MCSZ-MCO-20230615-0001"):
        url = self.host + "/api/platform/customsManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"","orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        return returnMsg,data1
    '''后台跟踪管理》监理管理查询'''
    def test_Added0120(self,dd_hao="MCSZ-MCO-20230625-0001"):
        url = self.host + "/api/platform/supervisionManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"status":"","orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        return returnMsg,data1

    '''后台跟踪管理》报关管理查询'''
    def test_Added0121(self,dd_hao="MCSZ-MCO-20230625-0001"):
        url = self.host + "/api/platform/customsClearanceManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"orderStatus":"all","orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        return returnMsg,data1
    '''后台跟踪管理》集装箱运输》清除柜号'''
    def test_Added0122(self,dd_id="MCSZ-MCO-20230605-0001"):
        url = self.host + "/api/platform/containerTransport/containerNumber"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data =[dd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''运单管理》集装箱运输》节点录入'''
    def test_Added0123(self,dd_id="",g_hao="",ft_hao="",k_gz="",time1="",jd_id=""):
        url = self.host + "/api/company/portTransport/editNode"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={
                "taskType":"task_type_leave_pickup_container",
                "taskTypeName":"离开提柜地",
                "containerNumber":g_hao,  #柜号
                "sealNumber":ft_hao,  #封条号
                "cabinetWeight":k_gz, #空柜重
                "finishTime":time1,        #提柜时间
                "supplierTransportOrderId":dd_id, #订单ID
                "id":jd_id   #节点ID
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''运单管理》集装箱运输》节点录入》获取节点ID'''
    def test_Added0124(self,dd_id="8c8abd9d071b43188b1eafcdacaf316d"):
        url = self.host + "/api/company/portTransport/trackNodeList/{}".format(dd_id)
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}

        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        jd_id = A.json()["result"][2]["id"]   #节点ID
        returnMsg = A.json()["returnMsg"]
        # print(jd_id)
        return returnMsg,jd_id
    '''查看监理档案'''
    def test_Added0125(self,jl_name="毛敏监理01"):
        url = self.host + "/api/platform/supervisor/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"supervisionName":jl_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # # print(A.json())
        # jl_id = A.json()["result"]["data"][0]["id"]   #监理ID   未激活：active_unactivated
        # jl_zt = A.json()["result"]["data"][0]["active"]   #监理状态 激活：active_activated 失效：active_invalid
        # ji_dh =  A.json()["result"]["data"][0]["supervisionPhone"]  #监理电话
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示存在
        # print(data1)
        return returnMsg,data1,returnTotalItems
    '''激活监理档案'''
    def test_Added0126(self,jl_id="5af64802aa6d4681ab6d697e4e6103ef"):
        url = self.host + "/api/platform/supervisor/enable"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = [jl_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''新增监理档案'''
    def test_Added0127(self, gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/platform/supervisor"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={
                "supplierId":gys_id,
                "supervisionLevel":"professional_supervision_junior",
                "supervisionName":"毛敏监理01",
                "supervisionPhone":"13999991111",
                "identityCard":"123545685478523252",
                "creditDays":3,
                "entryTime":"2023-06-01",
                "route":"transport_line_gd"
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''派监理'''
    def test_Added0128(self,ji_id="5af64802aa6d4681ab6d697e4e6103ef",ji_dh="13099999991",jldd_id="d69ac91d10c240a995cb425bd2cddc7f",
                       orderId="eabb8f38569b4ab29e322145f34f3080",gys_id="7d313a8828574614a5fe19df22145581",jl_name="毛敏监理01"):
        url = self.host + "/api/platform/supervisorManager/dispatch"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[
                {
                    # "orderNumber":"MCSZ-MCO-20230615-0001-02",
                    "status":"supervision_status_assigned",
                    "supervisionId":ji_id, #监理ID
                    "supervisionPhone":ji_dh, #监理电话
                    # "taskUnitTypeName":"监理运单",
                    # "pickupTime":"2023-06-20 10:54:23",
                    # "mainlandLicensePlateNumber":"粤ZZ0001",
                    # "driverName":"测试自有车-集1",
                    # "supplierName":"租户测试自有车-集1",
                    # "consignorConsigneeDistrict":"",
                    # "consignorConsignor":"",
                    # "consignorContactAddr":"硅白路大道101号",
                    # "consigneeName":"",
                    # "consigneeContactAddr":"",
                    "id":jldd_id,  #监理订单id
                    "orderId":orderId,#orderId
                    "supervisionName":jl_name,  #监理名称
                    # "options":"",
                    "supplierId":gys_id,  #供应商ID
                    "supervisionType":"supervision_type_profession"   #监理类型
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg


    '''上传附件>获取图片ID'''
    def test_Added0129(self,tp_lj):
        url = self.host + "/api/proxy/zuul/ict-service/file/upload/document"
        headers = {'Cookie': 'token={}'.format(self.ht_token)}
        file = {"file": open("{}".format(tp_lj), "rb")}
        # A = requests.post(url=url, headers=headers,files=file)
        A =requests.request("POST",url,headers=headers,files=file,verify=False)
        # print(A.json())
        tp_id = A.json()["result"]
        returnMsg = A.json()["returnMsg"]
        # print(tp_id)
        return tp_id,returnMsg, url

    '''监理管理》上传附件'''
    def test_Added0130(self,jldd_id,tp_name,tp_id):
        url = self.host + "/api/platform/supervisorManager/upload"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "id":jldd_id,
                "parentList":[
                    {
                        "taskType":"测试集装箱装货地址结束监装",
                        "fileList":[
                            {
                                "fileFormat":"id",
                                "fileName":tp_name,
                                "fileUrl":tp_id,
                                "fileType":"supervisor"
                            }
                        ]
                    }
                ]
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''监理管理》审核文件'''
    def test_Added0131(self,jlyd_id="d69ac91d10c240a995cb425bd2cddc7f"):
        url = self.host + "/api/platform/supervisorManager/auditPass/{}".format(jlyd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("POST",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看报关公司是档案'''
    def test_Added0132(self):
        url = self.host + "/api/platform/suppliersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":500,"filter":{"supplierType":"supplier_type_customs"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        gys_id = A.json()["result"]["data"][0]["id"]  #新增供应商id
        gys_bm = A.json()["result"]["data"][0]["supplierCode"]  #供应商编码
        gys_zt = A.json()["result"]["data"][0]["enabledType"]  #供应商状态
        gys_name = A.json()["result"]["data"][0]["supplierName"]  #新增供应商名称
        # print(gys_zt,gys_id)
        return returnMsg,gys_id,gys_bm,gys_zt,gys_name
    '''报关订单派单'''
    def test_Added0133(self,bbd_id="25e4719a8d054b67babd75554cda6906",gys_id="5215f390fbe64416902e1875e1cbc400",gys_lxr="报关公司联系人",lx_dh="13111111118"):
        url = self.host + "/api/platform/customsManager/supplier"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"ids":[bbd_id],"supplierId":gys_id,"supplierContact":gys_lxr,"supplierContactPhone":lx_dh}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''跟踪管理》推送日志'''
    def test_Added0134(self,dd_id="MCSZ-MCO-20230615-0001-01"):
        url = self.host + "/api/platform/interfaceLog/pushLogList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"showContent":dd_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  # 1 表示存在推送日志
        data1 =  A.json()["result"]["data"]

        return returnMsg,returnTotalItems,data1
    '''跟踪管理》新增异常'''
    def test_Added0135(self,dd_id="",dd_hao="",yc_time="",):
        url = self.host + "/api/platform/exceptionManager/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "isEscalation":"0",
                "relationOrderType":"1",
                "exceptionFrom":"source_channel_handle",
                "relationOrderNumber":dd_hao, #订单号
                "exceptionDesc":"异常描述异常描述",
                "taskType":"task_type_leave_pickup_container",
                "exceptionType":"exception_type_car",
                "exceptionRank":"exception_rank_ordinary",
                "exceptionReason":"exception_reason_04",
                "exceptionTime":yc_time,  #异常发生时间
                "exceptionLocation":"4",  #异常发生地编码
                "isLatentLoss":"1",       #是否潜在损失
                "lossAmount":120,         #潜在损失金额
                "exceptionLocationName":"深圳市",   #异常发生地
                "relationId":dd_id  #订单id
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''异常管理'''
    def test_Added0136(self,dd_hao="MCSZ-MCO-20230625-0001"):
        url = self.host + "/api/platform/exceptionManager/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "itemFrom":0,
                "itemTo":10,
                "filter":{
                    "exceptionStatus":"",
                    "relationOrderNumber":dd_hao
                }
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        zt = A.json()["result"]["data"][0]["exceptionLogList"][0]["status"]  #异常状态
        yc_dhao = A.json()["result"]["data"][0]["exceptionCode"]   #异常单号
        yc_id =  A.json()["result"]["data"][0]["id"]    #异常id
        returnMsg = A.json()["returnMsg"]
        # print(zt)
        data1 = A.json()["result"]["data"]
        return returnMsg,data1

    '''异常处理'''
    def test_Added0137(self,cy_id="",dd_id="",cy_dhao="",dd_hao="",yc_time="",gjr=""):
        url = self.host + "/api/platform/exceptionManager/edit"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "id":cy_id,  #异常id
                # "insertUser":"c038a360537011edac69fa163e78c411",
                # "insertTime":"2023-06-25 14:02:56",
                "exceptionCode":cy_dhao,  #异常单号
                "relationOrderType":1,                    #关联类型{0 订单 1 运单}
                "relationId":dd_id, #运单id
                "relationOrderNumber":dd_hao, #运单号
                "taskType":"task_type_leave_pickup_container",  #节点状态
                "exceptionType":"exception_type_car",      #异常类型
                "exceptionReason":"exception_reason_04",  #异常原因
                "exceptionTime":yc_time,  #异常发生时间
                "exceptionLocation":"4",       #异常发生地点(城市下拉)
                "exceptionDesc":"异常描述异常描述",  #异常描述
                "isLatentLoss":1,  #是否潜在损失
                "lossAmount":120,   #潜在损失金额
                "exceptionFrom":"source_channel_handle",  #异常来源渠道
                "exceptionRank":"exception_rank_ordinary",  #异常等级
                "handleDesc":"异常描述异常描述",  #处理描述
                # "tableTotal":"MCSZ-MEXP-230625-001待处理",
                "exceptionLogList":[
                    {
                        # "id":"fbbb8ed5be164d7b89213306d2ae12f1",
                        # "insertTime":"2023-06-25 14:02:56",
                        # "tenantId":"cd2ab17e-52ce-4f59-bdcc-f60c34ec348a",
                        # "exceptionId":"00c967d96e0a4e68bd0e5ab4d3f74c13",
                        # "handleDesc":"异常描述异常描述",
                        # "status":"待处理",
                        # "type":0
                    }
                ],
                "exceptionTabTotal":[
                    {
                        # "value":"00c967d96e0a4e68bd0e5ab4d3f74c13",
                        # "title":"MCSZ-MEXP-230625-001",
                        # "remark":"exception_status_awaiting"
                    }
                ],
                "followUserId":gjr, #跟进人-供应商联系人（监理档案联系人）
                "exceptionOwner":"responsible_party_accident",  #异常责任方
                "lossNum":10,      #货损数量
                "lossUnit":"packaging_unit_074", #数量单位
                "actualLossAmount":120,   #实际损失金额
                "exceptionStatus":"exception_status_handle", #状态
                "fileList":[

                ]
            }
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''跟踪管理》推送日志'''
    def test_Added0138(self,cy_id=""):
        url = self.host + "/api/platform/exceptionManager/complete"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [cy_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 应收费用制作查询运单基本信息(费用明细)'''
    def test_Added0139(self,fy_id="110bfd0cf0ed4514b8f9aef03b72e9bf"):
        url = self.host + "/api/platform/expensesReceivable/platform/{}".format(fy_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id = A.json()["result"]["incomeList"][0]["id"]   #账单ID
        # cp_hao = A.json()["result"]["supplierTransportOrderVo"]["mainlandLicensePlateNumber"]  #车牌号
        # sj_name = A.json()["result"]["supplierTransportOrderVo"]["driverName"]  #司机姓名
        data1 = A.json()["result"]["incomeList"]
        # print(zd_id)
        return returnMsg, data1
    ''' 应收费用制作查询运单费用明细信息(费用明细)'''
    def test_Added0140(self,fy_id="110bfd0cf0ed4514b8f9aef03b72e9bf"):  #账单id
        url = self.host + "/api/platform/inputOrder/info/{}".format(fy_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id = A.json()["result"]["costList"][0]["id"]   #账单ID
        # dd_hao = A.json()["result"]["costList"][0]["orderNumber"]    #订单号    明细已审核：status_check_completed
        # zd_zt = A.json()["result"]["costList"][0]["statusType"]    #明细账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
        # js_dw = A.json()["result"]["costList"][0]["balanceId"]["title"] #结算单位
        data1 = A.json()["result"]["costList"]
        # print(zd_id)
        return returnMsg, data1
    ''' 应收费用明细审核'''
    def test_Added0141(self,zd_id="833240255241338880"):  #明细id
        url = self.host + "/api/platform/expensesReceivable/examine"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [zd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 应收费用整审'''
    def test_Added0142(self,zd_id="5e3265d03970424188e46440b3a88211"):  #账单id
        url = self.host + "/api/platform/expensesReceivable/check"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [zd_id]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    ''' 费用项档案'''
    def test_Added0143(self):
        url = self.host + "/api/platform/chargeItem/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        fy_dw = A.json()["result"]["data"][0]["chargeUnit"] #计量单位
        fy_id = A.json()["result"]["data"][0]["id"]  #费用id
        fy_lx = A.json()["result"]["data"][0]["chargeType"]  #费用类型
        # print(fy_lx)
        return returnMsg,fy_dw,fy_id,fy_lx

    ''' 新增应收改单明细费用'''
    def test_Added0144(self,dd_hao,hz_id,dd_id,fy_id,fy_lx,fy_dw,gdlx):
        url = self.host + "/api/platform/changePay/submit/{}".format(gdlx)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                    "title":{
                        "renewalMode":"renewal_type_average", #改单类别
                        "orderNumber":dd_hao,  #订单号
                        "customerId":hz_id, #货主id
                        "secondCustomer":"",
                        "statusType":"status_check_all_completed",  #状态
                        "orderId":dd_id, #订单id
                        # "transportPort":"d017a1b4-7056-4734-9b95-86476e40ffc3",
                        # "taskUnitCode":"port_container_export_transport",
                        # "transportType":"transport_type_one_one",
                        "defaultBalanceCompany":[

                        ],
                        "responsibleParty":"responsible_party_haige",#改单责任方
                        "renewalReason":"responsible_party_haige_01",#改单原因
                        "chargeDirection":gdlx  #费用方向（0:应收/1;应付）
                    },
                    "detail":[
                        {
                            "currency":"CNY",
                            "balanceId":hz_id,  #结算单位货主id
                            "chargeItemId":fy_id, #费用名称费用类型id
                            "chargeType":fy_lx,#费用类型
                            "number":1,
                            "price":1000,
                            "chargeUnit":fy_dw,  #计量单位
                            "mainlandLicensePlateNumber":None
                        }
                    ]
                }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    ''' 应收费用制作查询费用信息>待完成页签'''
    def test_Added0145(self,dd_hao="MCSZ-MCO-20230625-0001"):
        url = self.host + "/api/platform/expensesReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"chargeStatusArray":["status_check_all_completed"],"orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id = A.json()["result"]["data"][0]["id"]   #账单ID
        # dd_hao = A.json()["result"]["data"][0]["orderNumber"]    #订单号    明细已审核：status_check_completed
        # zd_zt = A.json()["result"]["data"][0]["chargeStatus"]    #账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
        # cp_hao = A.json()["result"]["data"][0]["mainlandLicensePlateNumber"]  #车牌号
        # js_dw = A.json()["result"]["data"][0]["supplierName"]  #结算单位
        # js_je = A.json()["result"]["data"][0]["inComeAmountTotal"]  #结算金额
        # sj_name = A.json()["result"]["data"][0]["driverName"]  #司机姓名
        data1 = A.json()["result"]["data"]
        return returnMsg,data1

    '''应收管理》应收改单类表查询'''
    def test_Added0146(self,dd_hao="MCSZX-MCO-20230721-0006"):
        url = self.host + "/api/platform/changePay/list/0"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"status":[],"orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # gd_id =  A.json()["result"]["data"][0]["id"]
        # gd_zt = A.json()["result"]["data"][0]["statusType"]
        data1 =  A.json()["result"]["data"]
        # print(data1)
        return returnMsg,data1

    '''应收管理》应收改单审核'''
    def test_Added0147(self,gd_id="1bb373f74b814493836a9e617cd1b535"): #账单id
        url = self.host + "/api/platform/changePay/check/0/{}".format(gd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''应收管理》对账单提交'''
    def test_Added0148(self,zd_id="1bb373f74b814493836a9e617cd1b535"): #账单id
        url = self.host + "/api/platform/accountStatementReceivable/order"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [zd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''应收对账单》待生成对账单数据获取'''
    def test_Added0149(self,dd_hao="MCSZ-MCO-20230625-0001"):
        url = self.host + "/api/platform/accountStatementReceivable/listTab1"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderNumber":dd_hao,"statusType":"status_check_all_completed"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id =  A.json()["result"]["data"][0]["id"]
        # sf_gd = A.json()["result"]["data"][0]["isRenewal"]  # 1表示改单
        data1 =  A.json()["result"]["data"]
        # print(sf_gd)
        return returnMsg,data1

    '''确认对账'''
    def test_Added0150(self,zd_id="675cc364dfe94a9d890eabb590d78e89"): #账单id
        url = self.host + "/api/platform/accountStatementReceivable/confirm"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [zd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''对账单合计列表查询'''
    def test_Added0151(self,dd_hao="MCSZ-MCO-20230627-0004"):
        url = self.host + "/api/platform/accountStatementReceivable/listTab2"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"statusType":"","orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id =  A.json()["result"]["data"][0]["id"]         #已对账：   status_bill_complete
        # sf_gd = A.json()["result"]["data"][0]["statusType"]  # 状态 待对账：status_bill_awaiting
        # dzd_hao = A.json()["result"]["data"][0]["billOrderNumber"]  #对账单号
        data1 =  A.json()["result"]["data"]
        # print(sf_gd)
        return returnMsg,data1

    '''对账单生成结算单并确认'''
    def test_Added0152(self,zd_id="675cc364dfe94a9d890eabb590d78e89"):
        url = self.host + "/api/platform/accountStatementReceivable/bill/2"   #1生成 2生成并确认
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [zd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''应收月结账单》确认收款'''
    def test_Added0153(self,zd_id="MCSZ-MDN-20230626-0003",tp_name="",tp_id=""):
        url = self.host + "/api/platform/monthlyAccountsReceivable/receivable"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={
                "id":zd_id,
                "payAmountMode":"pay_amount_mode_offline",
                "payOrderNumber":"流水号123",
                "orderFileList":[
                    {
                        "fileFormat":"id",
                        "fileName":tp_name,
                        "fileUrl":tp_id
                    }
                ]
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''应收月结账单列表查询'''
    def test_Added0154(self,zd_hao="MCSZ-MDN-20230627-0002"):
        url = self.host + "/api/platform/monthlyAccountsReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"billNumber":zd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        # print(data1)
        return returnMsg,data1
    '''手工应付费用改单'''
    def test_Added0155(self,dd_hao,hz_id,dd_id,fy_id,fy_lx,fy_dw,gdlx,gys_id,cp_hao):
        url = self.host + "/api/platform/changePay/submit/1"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "title":{
                    "renewalMode":"renewal_type_average",
                    "orderNumber":dd_hao,
                    "customerId":hz_id,
                    "supplierId":gys_id, #供应商id
                    # "transportPort":"d017a1b4-7056-4734-9b95-86476e40ffc3",
                    "secondCustomer":"",
                    "statusType":"status_check_all_completed",
                    "orderId":dd_id, #订单id
                    # "taskUnitCode":"port_container_export_transport",
                    # "transportType":"transport_type_one_one",
                    "responsibleParty":"responsible_party_haige", #改单责任方
                    "renewalReason":"responsible_party_haige_01", #改单原因
                    "chargeDirection":gdlx  #费用方向（0:应收/1;应付）
                },
                "detail":[
                    {
                        "currency":"CNY",
                        "balanceId":gys_id, #结算单位货主id
                        "salesNumber":1,
                        "mainlandLicensePlateNumber":cp_hao,   #结算单位车牌
                        "isReadonly":[

                        ],
                        "chargeItemId":fy_id, #费用名称费用类型id
                        "chargeType":fy_lx, #费用类型
                        "number":1,
                        "price":222,
                        "chargeUnit":fy_dw, #计量单位
                        "salesPrice":222,
                        "salesAmount":222
                    }
                ]
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]

        # print(data1)
        return returnMsg
    '''撤销派车'''
    def test_Added0156(self,dd_id="c882163fbd4b44ca92403137e9ddb49d"):
        url = self.host + "/api/platform/dispatchPortTransport/revoke"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"cancelDispatchType":"cancel_dispatch_type_01","cancelDispatchReason":"测试撤销派车","ids":[dd_id]}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''撤销分单'''
    def test_Added0157(self,dd_id="c882163fbd4b44ca92403137e9ddb49d"):
        url = self.host + "/api/platform/planPortTransport/revoke"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"idList":[dd_id]}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''取消订单'''
    def test_Added015701(self,dd_id="c882163fbd4b44ca92403137e9ddb49d"):
        url = self.host + "/api/owner/order/cancel"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"idList":[dd_id],"cancelType":"cancel_order_reason_001","cancelRemark":"测试取消订单"}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''后台新增货主市场合同报价-集装箱进口运输'''
    def test_Added0158(self, customerPriceId="c344642fec0242a293fa9f186945bb71",
                       taskUnitCode="port_container_export_transport",
                       taskUnitTypeName="集装箱出口运输", transportPort="d017a1b4-7056-4734-9b95-86476e40ffc3",
                       departure="430111008000", departureProvinces="27514", departureCity="27515",
                       departureArea="27569", ):
        url = self.host + "/api/platform/cargoOwnerContract/addDetail"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [
            {
                "customerPriceId": customerPriceId,  # 报价单id
                "taskUnitCode": taskUnitCode,  # 运输类型
                "taskUnitTypeName": taskUnitTypeName,  # 运输类型
                "transportPort": transportPort,  # 港口id
                "destination": departure,  # 街道id
                "destinationProvinces": departureProvinces,  # 省份
                "destinationCity": departureCity,  # 装货城市
                "destinationArea": departureArea,  # 装货行政区
                "20GP":"5000",
                "20RF":"6000",
                "20OT":"6100",
                "20HQ":"6200",
                "20HT":"6300",
                "20TK":"6400",
                "20FR":"6500",
                "20RH":"6600",
                "40GP":"6700",
                "40HQ":"6800",
                "40OT":"6900",
                "40RH":"7000",
                "40RF":"7100",
                "40HT":"7200",
                "40FR":"7300",
                "40TK":"7400",
                "45HQ":"7500",
                "53HQ":"7600",
                "20GP DG":"7700",
                "40GP DG ":"7800",
                "40HQ DG":"7900",
                "currencyType":"CNY",
                "detailList": [
                    {
                "20GP":"5000",
                "20RF":"6000",
                "20OT":"6100",
                "20HQ":"6200",
                "20HT":"6300",
                "20TK":"6400",
                "20FR":"6500",
                "20RH":"6600",
                "40GP":"6700",
                "40HQ":"6800",
                "40OT":"6900",
                "40RH":"7000",
                "40RF":"7100",
                "40HT":"7200",
                "40FR":"7300",
                "40TK":"7400",
                "45HQ":"7500",
                "53HQ":"7600",
                "20GP DG":"7700",
                "40GP DG ":"7800",
                "40HQ DG":"7900",
                    }
                ]
            }
        ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''获取集装箱进口报价'''
    def test_Added0159(self, taskUnitCode="port_container_export_transport",
                       customerId="19b2ccc762484fda99aa28fe7fdea866",
                       transportPort="d017a1b4-7056-4734-9b95-86476e40ffc3", provinces="27514", city="27515",
                       area="27569",
                       street="430111008000", consigneeConsignorId="e5ebf71d3f0046b4aa373c0b1318d226",
                       pickupTime="2023-04-18 14:02:14",
                       carModeId="20GP"):
        url = self.host + "/api/platform/inputOrder/getPrice"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
            "taskUnitCode": taskUnitCode,  # 服务类型
            "customerId": customerId,  # 货主id
            "transportPort": transportPort,  # 港口id
            "destination": [
                {
                    "provinces": provinces,  # 省id
                    "city": city,  # 市id
                    "area": area,  # 区id
                    "street": street,  # 街道id
                    "consigneeConsignorId": consigneeConsignorId  # 装货单位id
                }
            ],
            "listDetail": [
                {
                    "pickupTime": pickupTime,  # 装货时间
                    "carModeId": carModeId,  # 柜型
                    "sequence": 0
                }
            ],
            # "institutionId":"49f596d8-b126-4046-a23a-cc76277f4fa2", #机构id
            "isMultipoint": 0,
            # "combinationStreet":combinationStreet  #街道名称
        }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        bj_je = A.json()["result"][0]["price"]
        bj_id = A.json()["result"][0]["customerPricePropertyId"]
        # print(bj_je,bj_id)
        return returnMsg, bj_je, bj_id
    '''修改申请'''
    def test_Added0160(self,data1,id):
        url = self.host + "/api/platform/inputOrder/submitModify"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        content = str(data1)
        data = {
            "id":id,
            "editType":"change_order_reason_003",
            "editRemark":"修改说明修改说明",
            "content":content
        }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''获取个人信息'''
    def test_Added0161(self):
        url = self.host + "/api/login/person"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        institutionGuid = A.json()["result"]["institutionGuid"]["value"]  #所属租户id
        name = A.json()["result"]["institutionGuid"]["title"]  #所属租户
        # print(institutionGuid)
        return returnMsg,institutionGuid,name
    '''集装箱运输订单详情页'''
    def test_Added0162(self,dd_id="3706d566f0fb436583cc6110edc73e77"):
        url = self.host + "/api/platform/inputOrder/info/{}".format(dd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]
        # print(data1)
        # baseInfo = data1["baseInfo"]
        # addrList = data1["addrList"]
        # costList = data1["costList"]
        # goodsList = data1["goodsList"]
        # priceList = data1["priceList"]
        # baseInfo.update([('orderStatus','status_execution'),("customerDelegateCode","11111")])  # 修改状态
        # data = {"baseInfo": baseInfo, "addrList": addrList, "costList": costList, "goodsList": goodsList,
        #         "priceList": priceList}
        # print(str(data))
        return returnMsg,data1

    '''改单审核'''
    def test_Added0163(self,data,dd_id,dd_hao,editType,editRemark):
        url = self.host + "/api/platform/receiveOrder/changeAudit"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        content = data
        data = {
                "id":dd_id,
                "editType":editType,
                "editRemark":editRemark,
                "content":content

                ,
                "changeList":[],
                "orderNumber":dd_hao,  #订单号
                "resultType":1
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''获取改单详情页信息'''
    def test_Added0164(self,dd_id="0d5aa5a8fe5547b9a16cac243a22c0c6"):
        url = self.host + "/api/platform/receiveOrder/changeAuditInfo/{}".format(dd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg1 = A.json()["returnMsg"]
        result = A.json()["result"]
        # print(result)
        returnMsg = A.json()["result"]["content"]
        data1 = json.loads(returnMsg)  #json.load(f)之后，返回的对象是python的字典对象。
        # addrList = json.loads(returnMsg)['addrList'][0]
        # baseInfo = json.loads(returnMsg)['baseInfo']
        # costList = json.loads(returnMsg)['costList'][0]
        # print(addrList)
        # # print(baseInfo)
        # # print(costList)
        # aa = get_k(addrList)
        # bb = get_k(baseInfo)
        # cc = get_k(costList)
        # # print(aa)
        # # print(bb)
        # # print(cc)
        # data2 = {"baseInfo": bb, "addrList": [aa], "costList": [cc]}
        # print(data2)
        return returnMsg,data1,result,returnMsg1

    '''计划管理》通改、执改确认'''
    def test_Added0165(self,customerOrderId="14bbcc978a0a476aba870097d5f8f22a"):
        url = self.host + "/api/platform/planPortTransport/modifyInfoConfirm/{}".format(customerOrderId)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''后台新增报价》集装箱进口'''
    def test_Added0166(self, marketPriceId="", transportPort="", departure="", departureProvinces="",
                       departureCity="", departureArea="", taskUnitCode="", ):
        url = self.host + "/api/platform/cargoOwnerMarket/addDetail"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [{"marketPriceId": marketPriceId,  # 报价单id  bjd_id
                 "transportPort": transportPort,  # 港口id
                 "destination": departure,  # 街道
                 "destinationProvinces": departureProvinces,  # 省
                 "destinationCity": departureCity,  # 市
                 "destinationArea": departureArea,  # 区
                 "taskUnitCode": taskUnitCode,  # 服务类型
                 "20GP": "3500",  # 报价
                 "20RF": "100",
                 "20OT": "100",
                 "20HQ": "100",
                 "20HT": "100",
                 "20TK": "100",
                 "20FR": "100",
                 "20RH": "100",
                 "40GP": "100",
                 "40HQ": "100",
                 "40OT": "100",
                 "currencyType": "CNY",
                 "detailList": [
                {"20GP": "3500",
                 "20RF": "100",
                 "20OT": "100",
                 "20HQ": "100",
                 "20HT": "100",
                 "20TK": "100",
                 "20FR": "100",
                 "20RH": "100",
                 "40GP": "100",
                 "40HQ": "100",
                 "40OT": "100",}  # 报价
                 ]}]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # bj_id = A.json()["result"]["data"][0]["id"]   #报价id
        # bjd_bm =  A.json()["result"]["data"][0]["priceNumber"]   #报价单编码
        return returnMsg
    ''' 查看自有车司机报价档案》进口'''
    def test_Added0167(self,bjd_id="5ce640e2b52743009c26ac0b3702acff",
                       transportPort="",departure="399"):  # 传的是报价单id+港口id+街道id
        url = self.host + "/api/platform/cargoOwnerMarket/detailList/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom": 0,"itemTo": 10,"filter": {"transportPort": transportPort, "destination": [departure]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # di_id = A.json()["result"]["data"][0]["id"]  # 未启用：enabled_type_unenabled  已启用：enabled_type_enabled
        # bj_zt = A.json()["result"]["data"][0]["enabledType"]  # 已禁用：enabled_type_disabled
        # bj_je = A.json()["result"]["data"][0]["20GP"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  # =0表示不存在
        data1 =  A.json()["result"]["data"]
        # print(bj_zt, di_id)
        return returnMsg,returnTotalItems,data1

    '''后台订单管理》厢式车运输列表'''
    def test_Added0168(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/receiveOrder/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id,"tagKey":"all","taskUnitCodeType":"vanType"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        # print(data1)
        return returnMsg,data1

    ''' 查看厢式车市场报价报价单档案》'''
    def test_Added0169(self,bjd_id="5ce640e2b52743009c26ac0b3702acff",departure="399"):  # 传的是报价单id+港口id+街道id
        url = self.host + "/api/platform/cargoOwnerMarket/detailList/{}".format(bjd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"departure":[departure]}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # di_id = A.json()["result"]["data"][0]["id"]  # 未启用：enabled_type_unenabled  已启用：enabled_type_enabled
        # bj_zt = A.json()["result"]["data"][0]["enabledType"]  # 已禁用：enabled_type_disabled
        # bj_je = A.json()["result"]["data"][0]["20GP"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  # =0表示不存在
        data1 =  A.json()["result"]["data"]
        # print(bj_zt, di_id)
        return returnMsg,returnTotalItems,data1

    '''新增厢式车运输报价'''
    def test_Added0170(self,bjd_id="",zh_jd="", zh_s="",zh_cs="", zh_q="", xh_jd="",xh_s="",xh_cs="",xh_q="",fu_lx="" ):
        url = self.host + "/api/platform/cargoOwnerMarket/addDetail"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[
                {
                    "marketPriceId":bjd_id,  #报价单id
                    "departure": zh_jd,    #装货街道
                    "departureProvinces":zh_s,  #装货省份
                    "departureCity":zh_cs,#装货市
                    "departureArea":zh_q,#装货区
                    "destination": xh_jd, #卸货街道
                    "destinationProvinces": xh_s,#卸货省份
                    "destinationCity": xh_cs,#卸货市
                    "destinationArea": xh_q,#卸货区
                    "taskUnitCode": fu_lx, #服务类型
                    "3T": "1000",
                    "5T": "2000",
                    "8T": "3000",
                    "10T": "4000",
                    "15T": "5000",
                    "currencyType": "CNY",
                    "detailList": [
                        {
                            "3T": "1000",
                            "5T": "2000",
                            "8T": "3000",
                            "10T": "4000",
                            "15T": "5000"
                        }
                    ]
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # bj_id = A.json()["result"]["data"][0]["id"]   #报价id
        # bjd_bm =  A.json()["result"]["data"][0]["priceNumber"]   #报价单编码
        return returnMsg

    '''货源大厅列表订单管理查询'''
    def test_Added0171(self,dd_hao="MCSZ-MCO-20230724-0009"):
        url = self.host + "/api/platform/orderManager/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"tagKey":"all","orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems =  A.json()["result"]["returnTotalItems"]  #表示存在
        data1 =  A.json()["result"]["data"]
        # orderStatus 待派单  status_waiting_dispatch
        # cargoShowStatus  待发布  status_send_awaiting
        # print(data1[0]["cargoShowStatus"])
        return returnMsg,returnTotalItems,data1

    '''货源大厅抢单发布'''
    def test_Added0172(self,dd_id="ec50ac999bb6417a8e9dfdfda6e7ff2f",sendStartTime="2023-06-01 13:53:23"):
        url = self.host + "/api/platform/orderManager/orderSetting/commit"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data =[
                {
                    "id": dd_id,  #运单ID
                    "sendMode": 1,
                    "sendPrice": 3500,    #金额
                    "balanceMode": "balance_way_month_60", #结算方式
                    "companyLevel": "",
                    "autoAmount": "",
                    "intervals": "",
                    "maxAmount": "",
                    "sendStartTime": sendStartTime,  #派车时间》当前时间
                    "sendEndTime": ""
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''货源大厅撤销发布'''
    def test_Added0173(self,dd_id="2e9173bc33f3483b8caba7b65d242f09"):
        url = self.host + "/api/platform/orderManager/revoke"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data =[dd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''货源大厅回退业务系统'''
    def test_Added0174(self,dd_id="2e9173bc33f3483b8caba7b65d242f09"):
        url = self.host + "/api/platform/orderManager/fallback"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data =[dd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''调度管理厢式车查询'''
    def test_Added0175(self,dd_hao="MCSZ-MCO-20230724-0009"):
        url = self.host + "/api/platform/dispatchBulkcargoTransport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderNumber":dd_hao}}

        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        dd_id = A.json()["result"]["data"][0]["id"]  # 订单id
        # zh_tine = A.json()["result"]["data"][0]["pickupTime"]  #装货时间
        # cz_qy = A.json()["result"]["data"][0]["operationGroup"]  # 操作区域
        dd_hao = A.json()["result"]["data"][0]["orderNumber"]  # 订单号
        data1 = A.json()["result"]["data"]
        # print(data1)
        return returnMsg,dd_id,dd_hao,data1


    '''客户文件配置新增厢式车类型，并启用'''
    def test_Added0176(self,hz_id="19b2ccc762484fda99aa28fe7fdea866"):
        url = self.host + "/api/platform/customerFileManagement/add"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {
                "configFileList": [
                    {
                        "fileCode": "customer_proxy",
                        "fileName": "客户委托书",
                        "isReadonly": [],
                        "isNeedPaper":"1"

                    },
                    {
                        "fileCode": "customer_standard_ collage",
                        "fileName": "拼载计划",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_ loop",
                        "fileName": "循环收货封条检测表",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_ supervision",
                        "fileName": "监装理货表",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_additional",
                        "fileName": "额外代垫票据",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_car",
                        "fileName": "车辆作业单（工厂签名盖章）",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_declaration",
                        "fileName": "报关单",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_declare",
                        "fileName": "报关单/ASN",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_entrust",
                        "fileName": "客户委托书",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_factory",
                        "fileName": "工厂收货通知单",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_file",
                        "fileName": "厢式车标准文件",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_nucleus",
                        "fileName": "核注清单",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_prove",
                        "fileName": "暂收证明/落货纸",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_receipt",
                        "fileName": "入仓单（仓库盖章）",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_release",
                        "fileName": "放行通知书",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_unloading",
                        "fileName": "入仓单/落货纸",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    },
                    {
                        "fileCode": "customer_standard_vehicle",
                        "fileName": "车辆作业单",
                        "isReadonly": [],
                        "isNeedPaper":"1"
                    }
                ],
                "serviceType": "van_type",
                "customerId": [
                    hz_id
                ],
                "isEnable": "1"
            }

        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg


    '''客户文件配置查看档案'''
    def test_Added0177(self,hz_id="19b2ccc762484fda99aa28fe7fdea866",fw_lx="container_type"):
        url = self.host + "/api/platform/customerFileManagement/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerId":hz_id,"serviceType":fw_lx}}

        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示存在
        data1 = A.json()["result"]["data"]
        # print(data1)
        return returnMsg,returnTotalItems,data1

    '''启用客户文件配置'''
    def test_Added0178(self,da_id="1683738568102305792"):
        url = self.host + "/api/platform/customerFileManagement/enable/{}".format(da_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg


    '''客户文件上传'''
    def test_Added0179(self,dd_id="2e9173bc33f3483b8caba7b65d242f09",tp_id="85dc18d685d640ce840418d9ec115330",tp_name="25.6 KB .jpeg"):
        url = self.host + "/api/platform/fileManagement/orderFile"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data ={
                "orderId": dd_id,
                "fileDto": [
                    {
                        "fileFormat": "id",
                        "fileName": tp_name,
                        "fileUrl": tp_id
                    }
                ]
            }

        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''后台文件管理》文件管理查询'''
    def test_Added0180(self,dd_hao="MCSZ-MCO-20230818-0006"):
        url = self.host + "/api/platform/fileManagement/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"orderNumber":dd_hao,"currentTag":"","insertTimeFrom":tiem3}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        # print(data1)
        return returnMsg,data1

    '''后台文件管理》确认回收'''
    def test_Added0181(self,dd_id="24febdaf63194d31865f855863e32fa5"):
        url = self.host + "/api/platform/fileManagement/recycleWaybill"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data =[dd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''后台文件管理》审核'''
    def test_Added0182(self,dd_id="2e9173bc33f3483b8caba7b65d242f09"):
        url = self.host + "/api/platform/fileManagement/checkWaybill"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        data =[dd_id]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''应付改单详情页》'''
    def test_Added0183(self,zd_id="ce12d2e82f0e4728ade6c173e8353838"):
        url = self.host + "/api/platform/changePay/renewal/1/{}".format(zd_id)
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(self.ht_token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg =  A.json()["returnMsg"]
        # print(returnMsg)
        data1 = A.json()["result"]
        # print(data1)
        # title = data1["title"]
        # print(title)
        # details = data1["details"][5]
        # print(details)
        # a = get_k(details)
        # print(a)
        # a.update([("salesPrice",3500),("salesAmount",3500),("salesNumber",1)])
        # print(a)
        # b= get_k(title)
        # b.update([("chargeDirection","1")])
        # print(b)

        return returnMsg,data1

    '''EXCEL配置库》模板ID'''
    def test_Added0184(self,ht_host="",modelName="询价管理导入-盐田",token="16a5b57b-7883-4453-8fe3-f9963a3c1742:226c6a46-83c7-461d-9ad8-1a85054c25a0"):
        url = ht_host + "/api/platform/excelConfigLib/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(token)}
        data ={"itemFrom":0,"itemTo":10,"modelName":modelName}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        mb_id =  A.json()["result"]["data"][0]["id"]
        # print(mb_id)
        return returnMsg,mb_id

    '''后台获取货主id'''
    def test_Added0185(self,ht_host,hz_name="毛敏租户测试货主1",token=""):
        url = ht_host + "/api/platform/customersArchives/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(token)}
        data ={"itemFrom":0,"itemTo":10,"filter":{"customerName":hz_name}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        hz_id = A.json()["result"]["data"][0]["id"]   #货主id
        # kf_id = A.json()["result"]["data"][0]["customerServiceId"]["value"] #客服id
        # print(hz_id)
        return returnMsg,hz_id
    '''后台订单录入查询（全部）''' #transportPort 港口id   departure 街道id
    def test_Added0186(self,ht_host="",token="",hz_id="19b2ccc762484fda99aa28fe7fdea866"):  # 传的是货主id
        url = ht_host + "/api/platform/inputOrder/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(token)}
        data = {
                "itemFrom": 0,
                "itemTo": 10,
                "filter": {
                    "tagKey": "all",
                    "orderStatus": [
                        "status_completing",
                        "status_fall_back_completed",
                        "status_undo_completed",
                        "status_execution",
                        "status_pending",
                        "status_execution_completed",
                        "status_completed"
                    ],
                    "customerId": hz_id
                }
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        taskUnitCode = A.json()["result"]["data"][0]["taskUnitCode"] #服务类型
        hz_name = A.json()["result"]["data"][0]["customerId"]["title"] #货主名称
        dd_hao = A.json()["result"]["data"][0]["orderNumber"] #订单号
        weituo_hao = A.json()["result"]["data"][0]["customerDelegateCode"] #客户委托号
        # cz_qy = A.json()["result"]["data"][0]["operationGroup"] #操作区域
        zh_time = A.json()["result"]["data"][0]["pickupTime"] #装货时间
        data1 = A.json()["result"]["data"][0]
        # print(taskUnitCode,hz_name,dd_hao,weituo_hao)
        # print(data1)
        return returnMsg,taskUnitCode,hz_name,dd_hao,weituo_hao,zh_time,data1




    '''后台订单管理》厢式车运输列表'''
    def test_Added0187(self,ht_host="",token="",order_number="HC-CO-20230814-0004"):
        url = ht_host + "/api/platform/receiveOrder/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderNumber":order_number,"tagKey":"all","taskUnitCodeType":"vanType"}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        # print(data1)
        return returnMsg,data1

    '''后台订单管理》厢式车运输列表，回退订单'''
    def test_Added0188(self,ht_host="",token="",order_number="HC-CO-20230814-0004",order_id=""):
        url = ht_host + "/api/platform/receiveOrderPort/batchRejectFallback"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(token)}
        data = [
                {
                    "id":order_id,
                    "orderNumber":order_number,
                    "rejectOrderType":"reject_order_type_06",
                    "rejectOrderRemark":"测试回退",
                    "orderStatus":"status_fall_back_completed"
                }
            ]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        returnMsg = A.json()["returnMsg"]
        # print(data1)
        return returnMsg

    '''后台订单管理》厢式车运输列表，取消订单'''
    def test_Added0189(self,ht_host="",token="",order_id=""):
        url = ht_host + "/api/owner/order/revokeSubmit"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(token)}
        data = [order_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        returnMsg = A.json()["returnMsg"]
        # print(data1)
        return returnMsg
    '''后台订单管理》通知》邮件日志查询'''
    def test_Added0190(self,ht_host="http://ict-test.epldcloud.com",token="3e28a307-43ec-47e9-9914-48a87d13514e:bc5d4e89-f82b-4713-8d85-131ff2fde70d",subject="【HC-CO-20230816-0021,AL0-230816141914】已下单"):
        url = ht_host + "/api/system/sendMessageByEmail/list"
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"subject":subject}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        # print(A.json())
        returnTotalItems = A.json()["result"]["returnTotalItems"]  #1表示有
        return returnMsg,returnTotalItems,data1

    '''后台订单管理》获取附件ID'''
    def test_Added0191(self,ht_host="http://ict-test.epldcloud.com",token="3e28a307-43ec-47e9-9914-48a87d13514e:bc5d4e89-f82b-4713-8d85-131ff2fde70d",Attachment_neme="55e29a3b87ef45dbbe745c4e621b2331"):
        url = ht_host + "/api/standard/download/{}".format(Attachment_neme)
        headers = { 'Content-Type': 'application/json',
                     'Cookie':'token={}'.format(token)}

        A =requests.request("GET",url,headers=headers,verify=False)
        returnMsg = A.json()["returnMsg"]
        # print(A.json())
        data1 =  A.json()["result"]
        C= data1[Attachment_neme]
        Attachment_id = C[14:46]
        # print(fj_id)

        return returnMsg,Attachment_id

    '''后台订单管理》附件下载'''
    def test_Added0192(self,ht_host,token,Attachment_id,save_path):
        url = ht_host + "/api/proxy/zuul/file-center-service/file/download/{}".format(Attachment_id)
        headers = {'Cookie':'token={}'.format(token)}

        A =requests.request("GET",url,headers=headers,verify=False)
        # returnMsg = A.json()["returnMsg"]
        # print(A)  # <Response [200]>
        # 保存路径+名称  D:\work\xiangmu\test_ICT_api\Test_data\inquiry_document\报价单111
        with open("{}".format(save_path), "wb") as code:
            code.write(A.content)
        return A


    ''' 应收费用制作查询费用信息>待完成页签'''
    def test_Added0193(self,ht_host,token,order_number="MCSZ-MCO-20230615-0001"):
        url = ht_host + "/api/platform/expensesReceivable/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"chargeStatusArray":["status_check_awaiting","status_check_all_completed_awaiting_upstream",
                                            "status_check_detail_completed","status_check_completed"],"orderNumber":order_number}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        # zd_id = A.json()["result"]["data"][0]["id"]   #账单ID
        # dd_hao = A.json()["result"]["data"][0]["orderNumber"]    #订单号    明细已审核：status_check_completed
        # zd_zt = A.json()["result"]["data"][0]["chargeStatus"]    #账单状态  待审核：status_check_awaiting  一整审：status_check_all_completed
        # cp_hao = A.json()["result"]["data"][0]["mainlandLicensePlateNumber"]  #车牌号
        # js_dw = A.json()["result"]["data"][0]["supplierName"]  #结算单位
        # js_je = A.json()["result"]["data"][0]["inComeAmountTotal"]  #结算金额  应收合计
        # sj_name = A.json()["result"]["data"][0]["driverName"]  #司机姓名
        data1 = A.json()["result"]["data"]
        # print(zd_id)
        return returnMsg,data1


    ''' 订单管理>厢式车》批量跟新货物信息'''
    def test_Added0194(self,ht_host,token,order_number="MCSZ-MCO-20230615-0001",planWeight="",planVolume="",
                       planGoodsNumber="", planPiecesNumber="",weight="",volume="",goodsNumber="",piecesNumber="",order_id=""):
        url = ht_host + "/api/platform/receiveOrder/goodsInfoBatch"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(token)}
        data = [
                {
                    "orderNumber":order_number,  #订单号
                    "planWeight":planWeight,  #计划重量
                    "planVolume":planVolume,   #计划体积
                    "planGoodsNumber":planGoodsNumber,  #计划箱数
                    "planPiecesNumber":planPiecesNumber, #计划件数
                    "weight":weight,    #实际重量
                    "volume":volume,     #实际体积
                    "goodsNumber":goodsNumber,   #实际箱数
                    "piecesNumber":piecesNumber,   #实际件数
                    "id":order_id  #订单id
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        print(A.json())
        returnMsg = A.json()["returnMsg"]

        return  returnMsg
































    '''后台新增集装箱出口订单'''
    def test_Added02100(self,customerId,customerContact,customerContactPhone,customerServiceId,transportPort,departureProvinces,
                       departureCity,departureArea,departure,cyCutOffTime,consignorId,consignorName,consignorContact,consignorContactPhone,
                       consignorContactAddr,provinces,city,district,street,pickupTime,bookingNumber,customerDelegateCode,baseAmount,price,
                       customerPricePropertyId,matchKey):
        url = self.host + "/api/platform/inputOrder/submit"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[{
                "isAgentOperate": 1,  #是否代操作
                "baseInfo": {
                    "isSanitaryTreatment": 1, #是否存重还柜
                    "customerId": customerId,  #委托客户id（货主id）
                    "customerContact": customerContact,  #货主联系人名称
                    "customerContactPhone": customerContactPhone,   #货主联系电话
                    "customerContactMail": "",  #客户邮箱
                    "customerServiceId": customerServiceId, #货主客服id 用户档案，监理客服
                    "customerServiceEmail": "",   #po
                    "balanceId": "",
                    "balancePhone": "",
                    "balanceMail": "",
                    "payerId": "",
                    "payerPhone": "",
                    "payerMail": "",
                    "consignorId": "",
                    "consigneeId": "",
                    "balanceWay": "balance_way_bill",    #结算方式
                    "isMultiLoad": True,
                    "discount": "0.85",  #折扣系数
                    "transportPort": transportPort,  #港口id
                    "departureProvinces": departureProvinces,  #装货省份
                    "departureCity": departureCity,  #装货城市
                    "departureArea": departureArea,  #装货行政区
                    "departure": departure,  #装货街道
                    "isTwinDrag": 0,
                    "cyCutOffTime": cyCutOffTime, #截重/空柜时间
                    "isCustoms": "1",   #是否委托报关
                    "customsType": "Customs_Type_002",  #报关方式
                    "otherFile": None,
                    # "isSanitaryTreatment":"1",  #是否监理
                    "bookingNumberFile": None,
                    "hblNumberFile": None,
                    "taskUnitCode": "port_container_export_transport",  #服务类型
                    "taskUnitTypeName": "集装箱出口运输",   #服务类型
                    "id": ""
                },
                "priceList": [],
                "addrList": [
                    {
                        # "lineNo": "15c1c7f586510e4f1555f2233d256ab35350",
                        "pickupDeliveryType": 0,
                        "options": "",
                        "consignorId": consignorId,  #装货单位id（收发货人档案）
                        "consignorName": consignorName,  #装货单位名称
                        "consignorContact": consignorContact,             #装货联系人
                        "consignorContactPhone": consignorContactPhone,   #装货联系电话
                        "consignorContactAddr": consignorContactAddr,   #装货详细地址
                        "provinces": provinces,    #装货始发省份
                        "city": city,         #装货始发城市
                        "district": district,     #装货始发行政区
                        "street": street,#装货街道
                        "departureProvinces": "",
                        "departureCity": "",
                        "departureArea": "",
                        "departure": "",
                        "driverRemark": "装卸货注意事项",
                        "supervisionRemark": "监理注意事项",
                        "sequence": 1
                    }
                ],
                "planList": [
                    {
                        "goodsCurrency": "USD",
                        "isReserveCabinet": "1",   #是否预提柜
                        "weighingMethod": "weighing_method_needless",  #过磅方式
                        "goodsValueType": "goods_value_type_001",  #货物价值
                        "pickupTime": pickupTime,  #装货时间
                        "bookingNumber": bookingNumber,   #订舱号
                        "customerDelegateCode":customerDelegateCode,  #客户委托号
                        "carModeId": "20GP",   #柜型
                        "isWeightStorage": "1",
                        "saveContainerTime": "",
                        "isReturnWeightStorage": "1",
                        "containerLocation": "container_location_003",  #集装箱摆放要求
                        "weight": 1,    #毛重
                        # "lineNo": "47802372c1638f975380b70ec79d51f3a042",
                        "isReadonly": [
                            "cabinetPickupTime",
                            "saveContainerTime",
                            "returnContainerTime"
                        ],
                        "isRequired": [
                            "containerLocation"
                        ],
                        "baseAmount": baseAmount,        #报价
                        "priceType": "",
                        "chargeInfo": {
                            "currencyType": "CNY",
                            "exchangeRate": 1,
                            "price": price,                #报价
                            "pickupTime": pickupTime,  #装货时间
                            "sequence": 0,
                            "carModeId": "20GP",    #柜型
                            "customerPricePropertyId": customerPricePropertyId, #报价单id（明细）
                            "departure": departure, #装货街道
                            "departureArea": departureArea,  #装货始发行政区
                            "departureCity": departureCity,   #装货始发城市
                            "departureProvinces": departureProvinces,  #始装货发省份
                            "balanceCompany": "",
                            "matchKey": "null:null:{}".format(matchKey) #装货街道
                        }
                    }
                ]
            }
        ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return  returnMsg

    ''' 新增厢式车多点运输'''
    def test_Added02101(self,customerId,customerContact,customerContactPhone,customerServiceId,consigneeId,consigneeName,consigneeContact,
                        consigneeContactPhone,consigneeContactAddr,xh_sf,xh_cs,xh_q,xh_jd,zh_sf,zh_cs,zh_q,zh_jd,zh_dz1id,zh_dz1name,zh_dz1lxr,
                        zh_dz1lxrdh,zh_dz1,zh_dz2id,zh_dz2name,zh_dz2lxr,zh_dz2lxrdh,zh_dz2,zh_time,jc_time,bj_je,bj_id,kh_hao):
        url = self.host + "/api/platform/inputOrder/submit"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[
                {
                    "isAgentOperate":1,    #是否代操作
                    "baseInfo":{
                        "customerId":customerId,  #委托客户id（货主id）
                        "customerContact":customerContact,                      #货主联系人名称
                        "customerContactPhone":customerContactPhone,               #货主联系电话
                        "customerContactMail":"",
                        "customerServiceId":customerServiceId, #货主客服id 用户档案，监理客服
                        "customerServiceEmail":"",
                        "balanceId":"",
                        "balancePhone":"",
                        "balanceMail":"",
                        "payerId":"",
                        "payerPhone":"",
                        "payerMail":"",
                        "consignorId":"",
                        "consigneeId":consigneeId,  #卸货单位id
                        "balanceWay":"balance_way_bill",                   #结算方式
                        "isMultiLoad":True,
                        "discount":"0.85",
                        "consigneeName":consigneeName,   #卸货单位名称
                        "consigneeContact":consigneeContact,   #卸货单位联系人
                        "consigneeContactPhone":consigneeContactPhone,   #卸货单位联系人手机号
                        "consigneeContactAddr":consigneeContactAddr,  #卸货单位详细地址
                        "provinces":"",
                        "city":"",
                        "district":"",
                        "street":"",
                        "destinationProvinces":xh_sf,  #卸货省份
                        "destinationCity":xh_cs,  #卸货城市
                        "destinationArea":xh_q,  #卸货行政区
                        "destination":xh_jd, #卸货街道
                        "driverRemark":"装卸货注意事项",
                        "supervisionRemark":"监理注意事项",
                        "departureProvinces":zh_sf, #装货省份
                        "departureCity":zh_cs, #装货市
                        "departureArea":zh_q,#装货区
                        "departure":zh_jd, #装货街道
                        "otherFile":None,
                        "bookingNumberFile":None,
                        "hblNumberFile":None,
                        "taskUnitCode":"bulkcargo_transport", #服务类型
                        "transportType":"transport_type_many_one",
                        "taskUnitTypeName":"厢式车运输",  #服务类型
                        "id":""
                    },
                    "priceList":[

                    ],
                    "addrList":[
                        {
                            # "lineNo":"3da0e30cfd2abfb98c0609275dd13378fbb2",
                            "pickupDeliveryType":0,
                            "options":"",
                            "consignorId":zh_dz1id, #装货地址1 id
                            "consignorName":zh_dz1name,  #装货地址1 名称
                            "consignorContact":zh_dz1lxr,       #装货地址1 联系人
                            "consignorContactPhone":zh_dz1lxrdh,  #装货地址1 联系的话
                            "consignorContactAddr":zh_dz1,   #装货地址1 详细地址
                            "provinces":zh_sf,  #装货省份
                            "city":zh_cs,  #装货市
                            "district":zh_q, #装货区
                            "street":zh_jd, #装货街道
                            "departureProvinces":"",
                            "departureCity":"",
                            "departureArea":"",
                            "departure":"",
                            "driverRemark":"装卸货注意事项",
                            "supervisionRemark":"装卸货注意事项",
                            "sequence":1
                        },
                        {
                            # "lineNo":"ed4a99a02262ea295a096277ba6b2dc02a12",
                            "pickupDeliveryType":0,
                            "options":"",
                            "consignorId":zh_dz2id,  #装货地址2 id
                            "consignorName":zh_dz2name,   #装货地址2 名称
                            "consignorContact":zh_dz2lxr,  #装货地址2 联系人
                            "consignorContactPhone":zh_dz2lxrdh,  #装货地址2 联系的话
                            "consignorContactAddr":zh_dz2,  #装货地址2 详细地址
                            "provinces":zh_sf,   #装货省份
                            "city":zh_cs,         #装货市
                            "district":zh_q,    #装货区
                            "street":zh_jd,    #装货街道
                            "departureProvinces":"",
                            "departureCity":"",
                            "departureArea":"",
                            "departure":"",
                            "driverRemark":"装卸货注意事项",
                            "supervisionRemark":"装卸货注意事项",
                            "sequence":2
                        }
                    ],
                    "planList":[
                        {
                            "goodsCurrency":"CNY",
                            "isReserveCabinet":0,
                            "weighingMethod":"weighing_method_needless",
                            "goodsValueType":"goods_value_type_001",
                            "pickupTime":zh_time,   #装货时间
                            "carModeId":"15T",
                            "containerLocation":"",
                            "isTwinDrag":"",
                            "weight":4,  #毛重
                            "volume":6,   #体积
                            "goodsNumber":8,  #件数
                            "packageUnit":"packaging_unit_074",
                            "cyCloseTime":jc_time,  #截仓时间
                            # "lineNo":"6d35297fd19ec467f1e9ccc6066a02e9a78d",
                            "isReadonly":[
                                "cabinetPickupTime",
                                "saveContainerTime",
                                "returnContainerTime",
                                "savePile",
                                "containerLocation",
                                "isTwinDrag",
                                "containerLocation",
                                "isTwinDrag"
                            ],
                            "isRequired":[

                            ],
                            "baseAmount":bj_je,  #报价金额
                            "priceType":"",
                            "chargeInfo":{
                                "currencyType":"CNY",
                                "exchangeRate":1,
                                "price":bj_je,   #报价金额
                                "pickupTime":zh_time,  #装货时间
                                "sequence":0,
                                "carModeId":"15T",
                                "customerPricePropertyId":bj_id, #报价单id（明细）
                                "departure":zh_jd, #装货街道
                                "destination":xh_jd,  #卸货街道
                                "departureArea":zh_q, #装货区
                                "departureCity":zh_cs,#装货市
                                "departureProvinces":zh_sf,#装货省份
                                "destinationArea":xh_q,#卸货行政区
                                "destinationCity":xh_cs,#卸货城市
                                "destinationProvinces":xh_sf, #卸货省份
                                "matchKey":"null:null:{}:{}".format(zh_jd,xh_jd) #卸货街道
                            },
                            "customerDelegateCode":kh_hao  #客户委托号
                        }
                    ]
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg


    '''后台新增集装箱进口订单'''
    def test_Added02102(self,customerId,customerContact,customerContactPhone,customerServiceId,transportPort,departureProvinces,
                       departureCity,departureArea,departure,cyCutOffTime,consignorId,consignorName,consignorContact,consignorContactPhone,
                       consignorContactAddr,provinces,city,district,street,pickupTime,bookingNumber,customerDelegateCode,baseAmount,price,
                       customerPricePropertyId,matchKey):
        url = self.host + "/api/platform/inputOrder/submit"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[{
                "isAgentOperate": 1,  #是否代操作
                "baseInfo": {
                    "isSanitaryTreatment": "", #是否存重还柜
                    "customerId": customerId,  #委托客户id（货主id）
                    "customerContact": customerContact,  #货主联系人名称
                    "customerContactPhone": customerContactPhone,   #货主联系电话
                    "customerContactMail": "",  #客户邮箱
                    "customerServiceId": customerServiceId, #货主客服id 用户档案，监理客服
                    "customerServiceEmail": "",   #po
                    "balanceId": "",
                    "balancePhone": "",
                    "balanceMail": "",
                    "payerId": "",
                    "payerPhone": "",
                    "payerMail": "",
                    "consignorId": "",
                    "consigneeId": "",
                    "balanceWay": "balance_way_bill",    #结算方式
                    "isMultiLoad": True,
                    "discount": "0.85",  #折扣系数
                    "transportPort": transportPort,  #港口id

                    "destinationProvinces": departureProvinces,  #卸货省份
                    "destinationCity": departureCity,  #卸货城市
                    "destinationArea": departureArea,  #卸货行政区
                    "destination": departure,  #卸货街道
                    "isTwinDrag": 0,
                    "cyCutOffTime": cyCutOffTime, #截重/空柜时间

                    "isCustoms": "0",   #是否委托报关
                    "customsType": "",  #报关方式
                    "otherFile": None,
                    # "isSanitaryTreatment":"1",  #是否监理
                    "bookingNumberFile": None,
                    "hblNumberFile": None,
                    "taskUnitCode": "port_container_import_transport",  #服务类型
                    "taskUnitTypeName": "集装箱进口运输",   #服务类型
                    "id": ""
                },
                "priceList": [],
                "addrList": [
                    {
                        # "lineNo": "15c1c7f586510e4f1555f2233d256ab35350",
                        "pickupDeliveryType": 1,
                        "options": "",
                        "consignorId": consignorId,  #装货单位id（收发货人档案）
                        "consignorName": consignorName,  #装货单位名称
                        "consignorContact": consignorContact,             #装货联系人
                        "consignorContactPhone": consignorContactPhone,   #装货联系电话
                        "consignorContactAddr": consignorContactAddr,   #装货详细地址
                        "provinces": provinces,    #装货始发省份
                        "city": city,         #装货始发城市
                        "district": district,     #装货始发行政区
                        "street": street,#装货街道
                        "departureProvinces": "",
                        "departureCity": "",
                        "departureArea": "",
                        "departure": "",
                        "driverRemark": "装卸货注意事项",
                        "supervisionRemark": "监理注意事项",
                        "sequence": 1
                    }
                ],
                "planList": [
                    {
                        "goodsCurrency": "USD",
                        "isReserveCabinet": "0",   #是否预提柜
                        "weighingMethod": "weighing_method_needless",  #过磅方式
                        "goodsValueType": "goods_value_type_001",  #货物价值

                        "pickupTime": pickupTime,  #装货时间
                        "bookingNumber": bookingNumber,   #提单号
                        "customerDelegateCode":customerDelegateCode,  #客户委托号
                        "carModeId": "20GP",   #柜型
                        "containerNumber": "FSCU5130217",
                        "isWeightStorage": "",
                        "saveContainerTime": "",
                        "isReturnWeightStorage": "",
                        "containerLocation": "container_location_003",  #集装箱摆放要求
                        "weight": 2,    #毛重
                        # "lineNo": "47802372c1638f975380b70ec79d51f3a042",
                        "isReadonly": [
                            "cabinetPickupTime",
                            "saveContainerTime",
                            "returnContainerTime"
                        ],
                        "isRequired": [
                            "containerLocation"
                        ],
                        "baseAmount": baseAmount,        #报价
                        "priceType": "",
                        "chargeInfo": {
                            "currencyType": "CNY",
                            "exchangeRate": 1,
                            "price": price,                #报价
                            "pickupTime": pickupTime,  #装货时间
                            "sequence": 0,
                            "carModeId": "20GP",    #柜型
                            "customerPricePropertyId": customerPricePropertyId, #报价单id（明细）
                            "destination": departure, #装货街道
                            "destinationArea": departureArea,  #装货始发行政区
                            "destinationCity": departureCity,   #装货始发城市
                            "destinationProvinces": departureProvinces,  #始装货发省份
                            "balanceCompany": "",
                            "matchKey": "null:null:{}".format(matchKey) #装货街道
                        }
                    }
                ]
            }
        ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return  returnMsg

    '''后台新增危险品出口订单'''
    def test_Added02103(self,customerId,customerContact,customerContactPhone,customerServiceId,transportPort,cyCutOffTime,
                        isCustoms,customsType,marineApplyType,consignorId,consignorName,consignorContact,consignorContactPhone,
                        consignorContactAddr,provinces,city,district,street,pickupTime,bookingNumber,customerDelegateCode,pickupContainer,price,customerPricePropertyId):
        url = self.host + "/api/platform/inputOrder/submit"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[
                {
                    "isAgentOperate":1,  #是否代操作
                    "baseInfo":{
                        "customerId":customerId, #委托客户id（货主id）
                        "customerContact":customerContact, #货主联系人名称
                        "customerContactPhone":customerContactPhone,  #货主联系电话
                        "customerContactMail":"",
                        "customerServiceId":customerServiceId,#货主客服id 用户档案，监理客服
                        "customerServiceEmail":"",
                        "balanceId":"",
                        "balancePhone":"",
                        "balanceMail":"",
                        "payerId":"",
                        "payerPhone":"",
                        "payerMail":"",
                        "consignorId":"",
                        "consigneeId":"",
                        "balanceWay":"balance_way_bill",  #结算方式
                        "isMultiLoad":True,
                        "discount":"0.85",  #折扣系数
                        "transportPort":transportPort, #港口id
                        "cyCutOffTime":cyCutOffTime,   #截重/空柜时间
                        "isCustoms":isCustoms,    #是否委托报关 1
                        "customsType":customsType,   #报关方式  Customs_Type_002
                        "marineApplyType":marineApplyType, #申报方式 marine_type_haige
                        "otherFile":None,
                        "bookingNumberFile":None,
                        "hblNumberFile":None,
                        "taskUnitCode":"dangerous_cargo_export_transport",  #服务类型
                        "taskUnitTypeName":"危险品出口运输",  #服务类型
                        "id":""
                    },

                    "priceList":[

                    ],
                    "addrList":[
                        {
                            # "lineNo":"bcadc3845afcc883abb3914e55f35ae1caa4",
                            "pickupDeliveryType":1,
                            "options":"",
                            "consignorId":consignorId,  #装货单位id（收发货人档案）
                            "consignorName":consignorName,   #装货单位名称
                            "consignorContact":consignorContact,     #装货联系人
                            "consignorContactPhone":consignorContactPhone,   #装货联系电话
                            "consignorContactAddr":consignorContactAddr,   #装货详细地址
                            "provinces":provinces,   #装货始发省份
                            "city":city,    #装货始发城市
                            "district":district,  #装货始发行政区
                            "street":street, #装货街道
                            "departureProvinces":"",
                            "departureCity":"",
                            "departureArea":"",
                            "departure":"",
                            "driverRemark":"装卸货注意事项",
                            "supervisionRemark":"监理注意事项",
                            "sequence":1
                        }
                    ],
                    "planList":[
                        {
                            "goodsCurrency":"USD",
                            "isReserveCabinet":0,    #是否预提柜
                            "weighingMethod":"weighing_method_needless",  #过磅方式
                            "goodsValueType":"goods_value_type_001",   #货物价值
                            "pickupTime":pickupTime,   #装货时间
                            "bookingNumber":bookingNumber,   #订舱号
                            "customerDelegateCode":customerDelegateCode,  #客户委托号
                            "carModeId":"20GP",   #柜型
                            "containerLocation":"",
                            "isTwinDrag":"",
                            "pickupContainer":pickupContainer,  # 提柜地
                            "returnContainer":pickupContainer,   # 还柜地
                            "weight":5,  #毛重
                            # "lineNo":"3e24ff2bce0eb8e183b75cd9ad992197f8dd",
                            "isReadonly":[
                                "cabinetPickupTime",
                                "saveContainerTime",
                                "returnContainerTime",
                                "savePile",
                                "containerLocation",
                                "isTwinDrag"
                            ],
                            "isRequired":[

                            ],
                            "baseAmount": price,  # 报价
                            "chargeInfo":{
                                "currencyType": "CNY",
                                "exchangeRate": 1,
                                "price": price,  # 报价
                                "pickupTime": pickupTime,  # 装货时间
                                "sequence": 0,
                                "carModeId": "20GP",  # 柜型
                                "customerPricePropertyId": customerPricePropertyId,  # 报价单id（明细）
                                "departure": street,  # 装货街道
                                "departureArea": district,  # 装货始发行政区
                                "departureCity": city,  # 装货始发城市
                                "departureProvinces": provinces,  # 始装货发省份
                                "balanceCompany": "",
                                "matchKey": "null:null:{}".format(street)  # 装货街道
                            }
                        }
                    ],
                    "orderFromTag":1
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return  returnMsg




'''货主端接口'''
class Shipperapi():
    def __init__(self):
        self.host = long.hz_host
        self.headers = long.ht_headers
        self.hz_token = Test_login().Test_login002()
        self.hz_token_FBA = Test_login().Test_login005()

    '''询价导入》'''
    def test_Added001(self,hz_host="",mb_id="aadaba98a5684432b0dbed74d19ee439",wj_name="AL0.xlsm",wj_dz="D:\work\AL0.xlsm",token="3e28a307-43ec-47e9-9914-48a87d13514e:067f7dbf-ee44-4d29-9d60-d25acb2ac61b"):
        url = hz_host + "/api/proxy/zuul/integration-service/excelModel/importExcelContent?id={}".format(mb_id)  #模板ID aadaba98a5684432b0dbed74d19ee439
        headers = {  'Cookie':'token={}'.format(token)}
        # 上传文件的参数
        filename = wj_name    #模板名称
        file_path = r"{}".format(wj_dz) #模板地址
        files = {'file': (filename, open("{}".format(file_path),'rb'))}  # 重点：上传文件请求数据。
        # print(files)
        # A = requests.post(url = url,files=files ,headers= headers)
        A =requests.request("POST",url,headers=headers,files=files ,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return  returnMsg
    '''个人信息》'''
    def test_Added002(self,hz_host="",token="3e28a307-43ec-47e9-9914-48a87d13514e:067f7dbf-ee44-4d29-9d60-d25acb2ac61b"):
        url = hz_host + "/api/login/person"
        headers = {  'Cookie':'token={}'.format(token)}

        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        receiveEmail = A.json()["result"]["receiveEmail"]  #获取配置发送邮箱

        receiveEmail = receiveEmail.split(",")  #讲邮箱字符串拆为字典
        return  returnMsg
    '''询价管理列表查询》'''
    def test_Added003(self,hz_host="",hz_id="e0fe8ce1d0c6430cbeec69533a8c7760",xj_dh="AL0-T202308111455",token="3e28a307-43ec-47e9-9914-48a87d13514e:451a984c-c4f4-4dfd-85b2-e20cd3ed84cc"):
        url = hz_host + "/api/owner/searchPriceManager/list"
        headers = { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tabKey":"all","customerId":hz_id,"customerDelegateCode":xj_dh}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems =  A.json()["result"]["returnTotalItems"]  #数量
        data1 = A.json()["result"]["data"]
        return  returnMsg,returnTotalItems,data1

    '''上传附件>获取图片ID'''
    def test_Added004(self,hz_host="",tp_lj="",token="",):
        url = hz_host + "/api/proxy/zuul/ict-service/file/upload/document"
        headers = {'Cookie': 'token={}'.format(token)}
        file = {"file": open("{}".format(tp_lj), "rb")}
        # A = requests.post(url=url, headers=headers,files=file)
        A =requests.request("POST",url,headers=headers,files=file,verify=False)
        # print(A.json())
        tp_id = A.json()["result"]
        returnMsg = A.json()["returnMsg"]
        # print(tp_id)
        return tp_id,returnMsg,url

    '''询价管理，确认上传附件'''
    def test_Added005(self,hz_host="http://ict-test.epldcloud.com",token="3e28a307-43ec-47e9-9914-48a87d13514e:697ee057-de8d-480a-a4a5-85466c2bcbf3",id="1690966185697406976",tp_name="2.02 MB.JPG",tp_id="84d59f9826054832a6cf818013246e87"):  #询价单id
        url = hz_host + "/api/owner/searchPriceManager/upload"
        headers =  { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        data = {
                "id":id,  #订单id
                "otherFile":[
                    {
                        "fileFormat":"id",
                        "fileName":tp_name, #图片名称
                        "fileUrl":tp_id #图片id
                    }
                ]
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''询价管理，按推荐报价生成'''
    def test_Added006(self,hz_host="",token="",id=""): #询价单id
        url = hz_host + "/api/owner/searchPriceManager/recommend"
        headers =  { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        data =[id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''询价管理，订单详情页'''
    def test_Added007(self,hz_host=hz_host_FBA,token="3e28a307-43ec-47e9-9914-48a87d13514e:86c85b49-d3f3-4ec3-aa63-2741c3d38374",id="1691253123336155136"): #询价单id
        url = hz_host + "/api/owner/searchPriceManager/info/{}".format(id)
        headers = { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        A =requests.request("GET",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]
        # print(data1)
        # get_k(data1)
        # print(get_k(data1))
        # print(data1["customerDelegateCode"])
        # alo = data1["customerDelegateCode"]+data1["customerDelegateCode"]
        # print(str(alo))
        # print(alo[0:17],alo[18:34])
        # print("{},{}".format(data1["customerDelegateCode"],data1["customerDelegateCode"]))
        # print(data1)
        # data1.update([('ltlFtlType', '111')])
        # print(data1)

        return returnMsg,data1
    '''询价管理，编辑》立即下单'''
    def test_Added008(self,hz_host="",token="",data1=""): #
        url = hz_host + "/api/owner/searchPriceManager/submit"
        headers =  { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        data =data1
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]
        return returnMsg,data1
    '''询价管理，合并及生成订单'''
    def test_Added009(self,hz_host="http://ict-test.epldcloud.com",token="3e28a307-43ec-47e9-9914-48a87d13514e:64592645-a11c-4514-972a-4d2d00f3441a",data1=""):
        url = hz_host + "/api/owner/searchPriceManager/mergeSubmit"
        headers =  { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        # data ={
        #     "customerId":"e0fe8ce1d0c6430cbeec69533a8c7760",
        #     "taskUnitTypeName":"厢式车运输",
        #     "taskUnitCode":"bulkcargo_transport",
        #     "pickupTime":"2023-08-16 14:00:00",
        #     "goodsName":"eva case",  #商品名称
        #     "isTailboard":0,
        #     "isStack":0,
        #     "customerDelegateCode":"AL0-230815104540,AL0-230815104530",  #对应的客户委托号
        #     "goodsNumber":8,   #箱数
        #     "piecesNumber":160,  #件数
        #     "volume":10,  #体积
        #     "weight":28,  #毛重
        #     "netWeight":20,  #货物总净重
        #     "goodsTotalAmount":960, #货物总价(
        #     "palletsSize":"",
        #     "priceInfoList":{    #报价信息
        #         "ltl":[
        #             {
        #                 "isMain":1,
        #                 "price":30,
        #                 "number":10,
        #                 "amount":300,
        #                 "chargeItemId":"charge_item_003",
        #                 "chargeItemName":"运费",
        #                 "currency":"CNY",
        #                 "chargeUnit":"charge_unit_198",
        #                 "customerPricePropertyId":"647d482be4b04995f497e0c2",
        #                 "minCost":3,
        #                 "minChargeUnit":"charge_unit_2908",
        #                 "weightPrice":30,
        #                 "volumePrice":30,
        #                 "transitTime":12
        #             }
        #         ],
        #         "ftl":[
        #             {
        #                 "isMain":1,
        #                 "price":310,
        #                 "number":1,
        #                 "amount":310,
        #                 "chargeItemId":"charge_item_003",
        #                 "chargeItemName":"运费",
        #                 "currency":"CNY",
        #                 "chargeUnit":"charge_unit_410",
        #                 "customerPricePropertyId":"647d482be4b04995f497e0c2",
        #                 "minCost":3,
        #                 "minChargeUnit":"charge_unit_2908",
        #                 "weightPrice":30,
        #                 "volumePrice":30,
        #                 "isContainer":0,
        #                 "transitTime":12
        #             }
        #         ]
        #     },
        #     "carModeId":"3T",
        #     "ftlAmount":310,
        #     "ltlAmount":300,
        #     "currency":"CNY",
        #     "ltlFtlType":"LTL",
        #     "otherFile":[
        #         {
        #             "fileUrl":"55771afc2fb8463fa16b0a1243f35b4d",
        #             "fileName":"2.02 MB.jpg",
        #             "fileFormat":"id"
        #         },
        #         {
        #             "fileUrl":"de0da97ef0d3456386c2a6a8576ad94a",
        #             "fileName":"2.02 MB.jpg",
        #             "fileFormat":"id"
        #         }
        #     ],
        #     "contractId":"379e7aaa7bec42cfa9240644726dbf41",
        #     "priceRemark":"FTL报价(FTL Quotation): 运费(freight)310CNY LTL报价(LTL Quotation): 运费(freight)300CNY 单价(Unit Price): 30CNY 体积(Volume): 10CBM 重泡货比例 1000KGS=3.5CBM，二者取最大值计算运费",
        #     "balanceCompany":"23d80071fcb543fbab0c687024b14bc2",
        #     "minPerShipment":3,
        #     "transitTime":12,
        #     "ftlTransitTime":12,
        #     "ltlPrice":30,
        #     "minCost":3,
        #     "minChargeUnit":"charge_unit_2908",
        #     "weightPrice":30,
        #     "volumePrice":30,
        #     "sequence":1,
        #     "departureCity":"4",
        #     "departureArea":"6",
        #     "departure":"389",
        #     "destinationCity":"4",
        #     "destinationArea":"5",
        #     "destination":"397",
        #     "mergeList":[
        #         {
        #             "sequence":0,
        #             "id":"1691279964520361984"
        #         },
        #         {
        #             "sequence":1,
        #             "id":"1691279925504946176"
        #         }
        #     ]
        # }
        data = data1
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]
        return returnMsg,data1

    '''询价管理，合并保存订单'''
    def test_Added010(self,hz_host="http://ict-test.epldcloud.com",token="3e28a307-43ec-47e9-9914-48a87d13514e:64592645-a11c-4514-972a-4d2d00f3441a",data1=""):
        url = hz_host + "/api/owner/searchPriceManager/mergeSave"
        headers =  { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        # data ={
        #     "customerId":"e0fe8ce1d0c6430cbeec69533a8c7760",
        #     "taskUnitTypeName":"厢式车运输",
        #     "taskUnitCode":"bulkcargo_transport",
        #     "pickupTime":"2023-08-16 14:00:00",
        #     "goodsName":"eva case",  #商品名称
        #     "isTailboard":0,
        #     "isStack":0,
        #     "customerDelegateCode":"AL0-230815104540,AL0-230815104530",  #对应的客户委托号
        #     "goodsNumber":8,   #箱数
        #     "piecesNumber":160,  #件数
        #     "volume":10,  #体积
        #     "weight":28,  #毛重
        #     "netWeight":20,  #货物总净重
        #     "goodsTotalAmount":960, #货物总价(
        #     "palletsSize":"",
        #     "priceInfoList":{    #报价信息
        #         "ltl":[
        #             {
        #                 "isMain":1,
        #                 "price":30,
        #                 "number":10,
        #                 "amount":300,
        #                 "chargeItemId":"charge_item_003",
        #                 "chargeItemName":"运费",
        #                 "currency":"CNY",
        #                 "chargeUnit":"charge_unit_198",
        #                 "customerPricePropertyId":"647d482be4b04995f497e0c2",
        #                 "minCost":3,
        #                 "minChargeUnit":"charge_unit_2908",
        #                 "weightPrice":30,
        #                 "volumePrice":30,
        #                 "transitTime":12
        #             }
        #         ],
        #         "ftl":[
        #             {
        #                 "isMain":1,
        #                 "price":310,
        #                 "number":1,
        #                 "amount":310,
        #                 "chargeItemId":"charge_item_003",
        #                 "chargeItemName":"运费",
        #                 "currency":"CNY",
        #                 "chargeUnit":"charge_unit_410",
        #                 "customerPricePropertyId":"647d482be4b04995f497e0c2",
        #                 "minCost":3,
        #                 "minChargeUnit":"charge_unit_2908",
        #                 "weightPrice":30,
        #                 "volumePrice":30,
        #                 "isContainer":0,
        #                 "transitTime":12
        #             }
        #         ]
        #     },
        #     "carModeId":"3T",
        #     "ftlAmount":310,
        #     "ltlAmount":300,
        #     "currency":"CNY",
        #     "ltlFtlType":"LTL",
        #     "otherFile":[
        #         {
        #             "fileUrl":"55771afc2fb8463fa16b0a1243f35b4d",
        #             "fileName":"2.02 MB.jpg",
        #             "fileFormat":"id"
        #         },
        #         {
        #             "fileUrl":"de0da97ef0d3456386c2a6a8576ad94a",
        #             "fileName":"2.02 MB.jpg",
        #             "fileFormat":"id"
        #         }
        #     ],
        #     "contractId":"379e7aaa7bec42cfa9240644726dbf41",
        #     "priceRemark":"FTL报价(FTL Quotation): 运费(freight)310CNY LTL报价(LTL Quotation): 运费(freight)300CNY 单价(Unit Price): 30CNY 体积(Volume): 10CBM 重泡货比例 1000KGS=3.5CBM，二者取最大值计算运费",
        #     "balanceCompany":"23d80071fcb543fbab0c687024b14bc2",
        #     "minPerShipment":3,
        #     "transitTime":12,
        #     "ftlTransitTime":12,
        #     "ltlPrice":30,
        #     "minCost":3,
        #     "minChargeUnit":"charge_unit_2908",
        #     "weightPrice":30,
        #     "volumePrice":30,
        #     "sequence":1,
        #     "departureCity":"4",
        #     "departureArea":"6",
        #     "departure":"389",
        #     "destinationCity":"4",
        #     "destinationArea":"5",
        #     "destination":"397",
        #     "mergeList":[
        #         {
        #             "sequence":0,
        #             "id":"1691279964520361984"
        #         },
        #         {
        #             "sequence":1,
        #             "id":"1691279925504946176"
        #         }
        #     ]
        # }
        data = data1
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]
        return returnMsg,data1



    '''询价管理，合并询价单》报价'''
    def test_Added011(self,hz_host,token,customerId,pickupTime,departureList,departureAreaList,destinationList,
                      destinationAreaList,departureCityList,consigneeCityList,balanceCompany,departureAddressList,weight,volume,isTailboard):
        url = hz_host + "/api/owner/searchPriceManager/priceMultiple"
        headers =  { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        data ={
                "customerId":customerId, #货主id
                "pickupTime":pickupTime, #装货时间
                "departureList":[
                    departureList
                ],  #装货街道id
                "departureAreaList":[
                    departureAreaList
                ],  #装货区id
                "destinationList":[
                    destinationList
                ],#卸货街道id
                "destinationAreaList":[
                    destinationAreaList
                ],#卸货区
                "departureCityList":[
                    departureCityList
                ],
                "consigneeCityList":[
                    consigneeCityList
                ],#卸货市
                "weight":weight, #毛重
                "volume":volume, #体积
                "isTailboard":isTailboard, #是否需要尾板 ,
                "balanceCompany":balanceCompany, #结算单位订单详情页取  balanceCompany
                "departureAddressList":[
                    departureAddressList
                ]#装货详细地址
            }
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]
        return returnMsg,data1


    '''询价管理》取消合并'''
    def test_Added012(self,hz_host="",token="",order_id=""): #
        url = hz_host + "/api/owner/searchPriceManager/cancel/{}".format(order_id)
        headers =  { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        A =requests.request("POST",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''订单管理》列表查询'''
    def test_Added013(self,hz_host="",token="",customerId="e0fe8ce1d0c6430cbeec69533a8c7760",orderNumber="HC-CO-20230815-0056"): #
        url = hz_host + "/api/owner/order/list"
        headers =  { 'Content-Type': 'application/json',
                    'Cookie':'token={}'.format(token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"tagKey":"all","customerId":customerId,"orderNumber":orderNumber}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        data1 = A.json()["result"]["data"]
        return returnMsg,data1



























'''运输公司订单接口'''
class Test_transport_company01():
    def __init__(self):
        self.host=long.gys_host
        self.headers=long.ht_headers
        self.ht_token=Test_login().Test_login003()

    '''供应商运单管理》厢式车运输获取'''
    def test_transport0001(self,gys_id="2849745179154bee9d483bfcbd6e362b",dd_hao=""):
        url = self.host + "/api/company/portTransport/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"orderTag":1,"tagKey":"all","supplierId":gys_id,"orderNumber":dd_hao}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        dd_hao = A.json()["result"]["data"][0]["orderNumber"]
        dd_id = A.json()["result"]["data"][0]["id"]
        return returnMsg,dd_hao,dd_id
    '''供应商运单管理》接单'''
    def test_transport0002(self,dd_id="1ac675a6abe2458ca72706e821320607"):
        url = self.host + "/api/company/portTransport/receiveConfirm"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [dd_id]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看司机档案'''
    def test_transport0003(self,siji_name="测试运输公司司机1",gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/platform/supplierDriver/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"driverName":siji_name,"supplierId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]   #0表示不存在
        data1 =  A.json()["result"]["data"]
        # siji_id = A.json()["result"]["data"][0]["id"]   #司机id
        # siji_name = A.json()["result"]["data"][0]["driverName"]  #司机名称
        # siji_dh = A.json()["result"]["data"][0]["driverMobilePhone"] #司机电话
        # siji_zt = A.json()["result"]["data"][0]["enabledType"]  #司机状态 启用：enabled_type_enabled 禁用：enabled_type_disabled 未启用：enabled_type_unenabled
        # print(siji_id)
        return returnMsg,returnTotalItems,data1
    '''新增司机档案'''
    def test_transport0004(self,gys_id="2849745179154bee9d483bfcbd6e362b",shiji_name="测试运输公司司机1",siji_dh="15252545555"):
        url = self.host + "/api/platform/supplierDriver/save"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"supplierId":gys_id,"driverName":shiji_name,"idCardNumber":"123456789",
                "driverMobilePhone":siji_dh,"isCanRegister":1,"otherRemark":shiji_name,"isOwner":0}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''启用司机档案'''
    def test_transport0005(self,siji_id="4c603f4473f54d0e82744f900931860d"):
        url = self.host + "/api/platform/supplierDriver/active_or_inactive/enabled_type_enabled"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [siji_id]
        A =requests.request("PUT",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''新增车辆档案'''
    def test_transport0006(self,gys_id="2849745179154bee9d483bfcbd6e362b",c_pai="粤A6688",siji_id="4c603f4473f54d0e82744f900931860d"):
        url = self.host + "/api/platform/supplierCar/updateList"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"supplierId":gys_id,"isOwner":0,"carModeId":"10T","carNumber":c_pai,
                "driverId":siji_id,"remark":"测试车辆"}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''查看车辆档案'''
    def test_transport0007(self,c_pai="粤A6688",gys_id="2849745179154bee9d483bfcbd6e362b"):
        url = self.host + "/api/platform/supplierCar/list"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = {"itemFrom":0,"itemTo":10,"filter":{"carNumber":c_pai,"supplierId":gys_id}}
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        returnTotalItems = A.json()["result"]["returnTotalItems"]   #0表示不存在
        data1 =  A.json()["result"]["data"]
        # cl_id = A.json()["result"]["data"][0]["id"]   #车辆id
        # c_pai = A.json()["result"]["data"][0]["carNumber"]  #车牌号
        # siji_zt = A.json()["result"]["data"][0]["enabledType"]  #车辆状态 启用：enabled_type_enabled 禁用：enabled_type_disabled未启用：enabled_type_unenabled
        # print(c_pai,siji_zt)
        return returnMsg,returnTotalItems,data1
    '''启用车辆档案'''
    def test_transport0008(self,cl_id="df3d057a88e34e8982eac5c53f0fa406"):
        url = self.host + "/api/platform/supplierCar/state/enabled_type_enabled"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data = [cl_id]
        A =requests.request("PUT",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg
    '''厢式车派车'''
    def test_transport0009(self,dd_id,shiji_dh,cl_id,siji_id,c_pai,siji_name):
        url = self.host + "/api/company/portTransport/delivery/0"
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        data =[
                {
                    "id":dd_id,  #订单id
                    "mainlandPhone":shiji_dh, #司机电话
                    "mainlandLicensePlate":cl_id,  #车辆id
                    "driverId":siji_id,  #司机id
                    "isCanRegister":"1",
                    "mainlandLicensePlateNumber":c_pai, #车牌
                    "driverName":siji_name,    #司机名称
                    "containerNumber":""
                }
            ]
        A =requests.request("POST",url,headers=headers,data=json.dumps(data),verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg

    '''撤销派车'''
    def test_transport0010(self,dd_id="1ac675a6abe2458ca72706e821320607"):
        url = self.host + "/api/company/portTransport/revokeCar/{}".format(dd_id)
        headers = {'Content-Type': 'application/json',
                   'Cookie': 'token={}'.format(self.ht_token)}
        A =requests.request("POST",url,headers=headers,verify=False)
        # print(A.json())
        returnMsg = A.json()["returnMsg"]
        return returnMsg







if __name__ == '__main__':
    run=Test_Added01()  # 后台
    # run.test_Added0056()

    # run2 = Test_login()
    # run2.Test_login005()

    run1=Shipperapi()  #货主
    run1.test_Added007()
