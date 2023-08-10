from utils.read import base_data
from core.rest_client import Api
from datetime import date, timedelta

url = base_data.read_ini()['host']['api_sit_url']
yesterday = date.today() + timedelta(days=-3)  # 前三天


class Query:

    def customerOrder_list(self, login_fixture):
        """
        客户订单列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeStart": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/customerOrder/list', json=json_data, headers=headers)
        return result

    def inbound_po_list(self, login_fixture):
        """
        INBOUND_PO列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeStart": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/inbound_po/list', json=json_data, headers=headers)
        return result

    def appointWarehouse_list(self, login_fixture):
        """
        预约资源设置---预约仓库列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/appointWarehouse/list', json=json_data, headers=headers)
        return result

    def appointPlatform_list(self, login_fixture):
        """
        预约资源设置---预约月台---月台设置列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/appointPlatform/list', json=json_data, headers=headers)
        return result

    def appointPlatform_allotList(self, login_fixture):
        """
        预约资源设置---预约月台---分配客户设置列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/appointPlatform/allotList', json=json_data, headers=headers)
        return result

    def logisticsAppointment_list(self, login_fixture):
        """
        平台预约---平台预约订单列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/logisticsAppointment/list', json=json_data, headers=headers)
        return result

    def logisticsAppointmentBooking_list(self, login_fixture):
        """
        平台预约---平台预约单管理列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/logisticsAppointmentBooking/list', json=json_data, headers=headers)
        return result

    def appointmentOrder_list(self, login_fixture):
        """
        外部预约---预约订单列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/appointmentOrder/list', json=json_data, headers=headers)
        return result

    def reservationManagement_list(self, login_fixture):
        """
        外部预约---预约订单列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/reservationManagement/list', json=json_data, headers=headers)
        return result

    def warehouse_id(self, login_fixture):
        """
        仓库名称下拉查询获取仓库ID接口
        :param json_data:
        :return:
        """
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.get('/api/standard/search/orderWarehouse?filter=', params='', headers=headers)
        warehouseGuid = result.body['result'][1]['value']
        return warehouseGuid

    def warehouse_name(self, login_fixture):
        """
        根据仓库ID获取仓库名称接口(列表查询接口)
        :param json_data:
        :return:
        """
        warehouseGuid = self.warehouse_id(login_fixture)
        json_data = {"filter": {"id": warehouseGuid}, "itemFrom": 0, "itemTo": 10}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/appointPlatform/warehouse', json=json_data, headers=headers)
        warehouseName = result.body['result']['data'][0]['warehouseGuid']['value']
        return warehouseName
        # return result

    def acceptAppointment_list(self, login_fixture):
        """
        仓库预约岗---预约单受理接口(查看月台使用情况)
        :param json_data:
        :return:
        """
        warehouseName = self.warehouse_name(login_fixture)
        json_data = {"appointmentDate": f"{yesterday}", "warehouseGuid": warehouseName}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/acceptAppointment/list', json=json_data, headers=headers)
        return result

    def storageTotal_list(self, login_fixture):
        """
        库存管理---总库存列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/storageTotal/list', json=json_data, headers=headers)
        return result

    def storageDetail_list(self, login_fixture):
        """
        库存管理---库存流水列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/storageDetail/list', json=json_data, headers=headers)
        return result

    def storageTurnover_list(self, login_fixture):
        """
        库存管理---库存流水列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/storageTurnover/list', json=json_data, headers=headers)
        return result

    def storageCompare_list(self, login_fixture):
        """
        库存管理---库存流水列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/warehouse/storageCompare/list', json=json_data, headers=headers)
        return result

    def delegation_list(self, login_fixture):
        """
        物流订单---委托订单列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/delegation/list', json=json_data, headers=headers)
        return result

    def po_list(self, login_fixture):
        """
        物流订单---PO Management---PO Management列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/po/list', json=json_data, headers=headers)
        return result

    def booking_list(self, login_fixture):
        """
        物流订单---PO Management---Booking Management列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"roleType": "4PL"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/booking/list', json=json_data, headers=headers)
        return result

    def receive_list(self, login_fixture):
        """
        物流订单---待接订单列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/receive/list', json=json_data, headers=headers)
        return result

    def logisticsExecutionOrder_list(self, login_fixture):
        """
        物流订单---物流执行订单列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/logisticsExecutionOrder/list', json=json_data, headers=headers)
        return result

    def input_list(self, login_fixture):
        """
        物流订单---订单录入列表接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "customerServiceDeptnameList": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/input/list', json=json_data, headers=headers)
        return result

    def job_list(self, login_fixture):
        """
        物流订单---订单完善列表
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/job/list', json=json_data, headers=headers)
        return result

    def all_list(self, login_fixture):
        """
        物流订单---订单汇总列表
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/all/list', json=json_data, headers=headers)
        return result

    def agent_list(self, login_fixture):
        """
        物流订单---预约管理---代理预约
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/agent/list', json=json_data, headers=headers)
        return result

    def logisticsBooking_list(self, login_fixture):
        """
        物流订单---预约管理---物流订单预约
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"appointmentQueryStatus": "appointment_query_status_001",
                                                             "insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/logisticsBooking/list', json=json_data, headers=headers)
        return result

    def volume_split_list(self, login_fixture):
        """
        物流订单---货量拆分
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"statusType": "status_quantity_split_waitting"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/volume_split/list', json=json_data, headers=headers)
        return result

    def nikeKpi_list(self, login_fixture):
        """
        物流订单---Nike报表---NIKEPI
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/nikeKpi/list', json=json_data, headers=headers)
        return result

    def nikeGoodsException_list(self, login_fixture):
        """
        物流订单---Nike报表---货物异常情况
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/nikeGoodsException/list', json=json_data, headers=headers)
        return result

    def orderProcess_list(self, login_fixture):
        """
        物流订单---数据处理中心---物流执行订单处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"pickupTimeStart": f"{yesterday}", "status": "status_exception_pending"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/orderProcess/list', json=json_data, headers=headers)
        return result

    def processRules_list(self, login_fixture):
        """
        物流订单---数据处理中心---处理规则配置
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/processRules/list', json=json_data, headers=headers)
        return result

    def processReport_list(self, login_fixture):
        """
        物流订单---数据处理中心---处理记录报表
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/processReport/list', json=json_data, headers=headers)
        return result

    def supplierRuleConfig_list(self, login_fixture):
        """
        物流订单---数据处理中心---供应商规则配置
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/supplierRuleConfig/list', json=json_data, headers=headers)
        return result

    def plan_list(self, login_fixture, serviceTypeCode):
        """
        物流计划---(所有类型)---待计划、配载
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": serviceTypeCode,
                                "isOptimizing": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/plan/list', json=json_data, headers=headers)
        return result

    def plan_list_planned(self, login_fixture, serviceTypeCode):
        """
        物流计划---(所有类型)---已计划
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": serviceTypeCode,
                                "isOptimizing": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/plan/list_planned', json=json_data, headers=headers)
        return result

    def air_transport_pending(self, login_fixture):
        """
        派单中心---空运---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "air_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/air_transport/pending', json=json_data, headers=headers)
        return result

    def air_transport_done(self, login_fixture):
        """
        派单中心---空运---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "air_transport", "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/air_transport/done', json=json_data, headers=headers)
        return result

    def air_transport_complete(self, login_fixture):
        """
        派单中心---空运---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "air_transport", "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/air_transport/complete', json=json_data, headers=headers)
        return result

    def air_transport_revoke(self, login_fixture):
        """
        派单中心---空运---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "air_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/air_transport/revoke', json=json_data, headers=headers)
        return result

    def air_transport_cancel(self, login_fixture):
        """
        派单中心---空运---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "air_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/air_transport/cancel', json=json_data, headers=headers)
        return result

    def mnt_pending(self, login_fixture):
        """
        派单中心---陆运---国内运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_native_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_native_transport/pending', json=json_data, headers=headers)
        return result

    def mnt_done(self, login_fixture):
        """
        派单中心---陆运---国内运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_native_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_native_transport/done', json=json_data, headers=headers)
        return result

    def mnt_complete(self, login_fixture):
        """
        派单中心---陆运---国内运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_native_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_native_transport/complete', json=json_data, headers=headers)
        return result

    def mnt_revoke(self, login_fixture):
        """
        派单中心---陆运---国内运输---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_native_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_native_transport/revoke', json=json_data, headers=headers)
        return result

    def mnt_cancel(self, login_fixture):
        """
        派单中心---陆运---国内运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_native_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_native_transport/cancel', json=json_data, headers=headers)
        return result

    def bt_pending(self, login_fixture):
        """
        派单中心---陆运---保税运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "bonded_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/bonded_transport/pending', json=json_data, headers=headers)
        return result

    def bt_done(self, login_fixture):
        """
        派单中心---陆运---保税运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "bonded_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/bonded_transport/done', json=json_data, headers=headers)
        return result

    def bt_complete(self, login_fixture):
        """
        派单中心---陆运---保税运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "bonded_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/bonded_transport/complete', json=json_data, headers=headers)
        return result

    def bt_revoke(self, login_fixture):
        """
        派单中心---陆运---保税运输---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "bonded_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/bonded_transport/revoke', json=json_data, headers=headers)
        return result

    def bt_cancel(self, login_fixture):
        """
        派单中心---陆运---保税运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "bonded_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/bonded_transport/cancel', json=json_data, headers=headers)
        return result

    def nit_pending(self, login_fixture):
        """
        派单中心---陆运---内贸运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_trade",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_trade/pending', json=json_data, headers=headers)
        return result

    def nit_done(self, login_fixture):
        """
        派单中心---陆运---内贸运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_trade",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_trade/done', json=json_data, headers=headers)
        return result

    def nit_complete(self, login_fixture):
        """
        派单中心---陆运---内贸运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_trade",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_trade/complete', json=json_data, headers=headers)
        return result

    def nit_revoke(self, login_fixture):
        """
        派单中心---陆运---内贸运输---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_trade",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_trade/revoke', json=json_data, headers=headers)
        return result

    def nit_cancel(self, login_fixture):
        """
        派单中心---陆运---内贸运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_trade",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_trade/cancel', json=json_data, headers=headers)
        return result

    def mht_pending(self, login_fixture):
        """
        派单中心---陆运---中港运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_hk_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_hk_transport/pending', json=json_data, headers=headers)
        return result

    def mht_done(self, login_fixture):
        """
        派单中心---陆运---中港运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_hk_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_hk_transport/done', json=json_data, headers=headers)
        return result

    def mht_complete(self, login_fixture):
        """
        派单中心---陆运---中港运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_hk_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_hk_transport/complete', json=json_data, headers=headers)
        return result

    def mht_revoke(self, login_fixture):
        """
        派单中心---陆运---中港运输---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_hk_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_hk_transport/revoke', json=json_data, headers=headers)
        return result

    def mht_cancel(self, login_fixture):
        """
        派单中心---陆运---中港运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_hk_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_hk_transport/cancel', json=json_data, headers=headers)
        return result

    def mcbt_pending(self, login_fixture):
        """
        派单中心---陆运---跨境运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_cross_border_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_cross_border_transport/pending', json=json_data, headers=headers)
        return result

    def mcbt_done(self, login_fixture):
        """
        派单中心---陆运---跨境运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_cross_border_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_cross_border_transport/done', json=json_data, headers=headers)
        return result

    def mcbt_complete(self, login_fixture):
        """
        派单中心---陆运---跨境运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_cross_border_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_cross_border_transport/complete', json=json_data,
                          headers=headers)
        return result

    def mcbt_cancel(self, login_fixture):
        """
        派单中心---陆运---跨境运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "mainland_cross_border_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/mainland_cross_border_transport/cancel', json=json_data, headers=headers)
        return result

    def pt_pending(self, login_fixture):
        """
        派单中心---陆运---港口运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "port_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/port_transport/pending', json=json_data, headers=headers)
        return result

    def pt_done(self, login_fixture):
        """
        派单中心---陆运---港口运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "port_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/port_transport/done', json=json_data, headers=headers)
        return result

    def pt_complete(self, login_fixture):
        """
        派单中心---陆运---港口运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "port_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/port_transport/complete', json=json_data, headers=headers)
        return result

    def pt_revoke(self, login_fixture):
        """
        派单中心---陆运---港口运输---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "port_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/port_transport/revoke', json=json_data, headers=headers)
        return result

    def pt_cancel(self, login_fixture):
        """
        派单中心---陆运---港口运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "port_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/port_transport/cancel', json=json_data, headers=headers)
        return result

    def hnt_pending(self, login_fixture):
        """
        派单中心---陆运---香港本地运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "hk_native_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/hk_native_transport/pending', json=json_data, headers=headers)
        return result

    def hnt_done(self, login_fixture):
        """
        派单中心---陆运---香港本地运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "hk_native_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/hk_native_transport/done', json=json_data, headers=headers)
        return result

    def hnt_complete(self, login_fixture):
        """
        派单中心---陆运---香港本地运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "hk_native_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/hk_native_transport/complete', json=json_data, headers=headers)
        return result

    def hnt_revoke(self, login_fixture):
        """
        派单中心---陆运---香港本地运输---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "hk_native_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/hk_native_transport/revoke', json=json_data, headers=headers)
        return result

    def hnt_cancel(self, login_fixture):
        """
        派单中心---陆运---香港本地运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "hk_native_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/hk_native_transport/cancel', json=json_data, headers=headers)
        return result

    def lu_pending(self, login_fixture):
        """
        派单中心---陆运---装卸服务---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "load_unload",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/load_unload/pending', json=json_data, headers=headers)
        return result

    def lu_done(self, login_fixture):
        """
        派单中心---陆运---装卸服务---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "load_unload",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/load_unload/done', json=json_data, headers=headers)
        return result

    def lu_complete(self, login_fixture):
        """
        派单中心---陆运---装卸服务---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "load_unload",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/load_unload/complete', json=json_data, headers=headers)
        return result

    def lu_revoke(self, login_fixture):
        """
        派单中心---陆运---装卸服务---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "load_unload",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/load_unload/revoke', json=json_data, headers=headers)
        return result

    def wp_pending(self, login_fixture):
        """
        派单中心---陆运---港内作业---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "within_port",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/within_port/pending', json=json_data, headers=headers)
        return result

    def wp_done(self, login_fixture):
        """
        派单中心---陆运---港内作业---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "within_port",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/within_port/done', json=json_data, headers=headers)
        return result

    def wp_complete(self, login_fixture):
        """
        派单中心---陆运---港内作业---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "within_port",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/within_port/complete', json=json_data, headers=headers)
        return result

    def wp_revoke(self, login_fixture):
        """
        派单中心---陆运---港内作业---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "within_port",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/within_port/revoke', json=json_data, headers=headers)
        return result

    def wp_cancel(self, login_fixture):
        """
        派单中心---陆运---港内作业---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "within_port",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/within_port/cancel', json=json_data, headers=headers)
        return result

    def st_pending(self, login_fixture):
        """
        派单中心---海运---海运---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "sea_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/sea_transport/pending', json=json_data, headers=headers)
        return result

    def st_done(self, login_fixture):
        """
        派单中心---海运---海运---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "sea_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/sea_transport/done', json=json_data, headers=headers)
        return result

    def st_complete(self, login_fixture):
        """
        派单中心---海运---海运---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "sea_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/sea_transport/complete', json=json_data, headers=headers)
        return result

    def st_revoke(self, login_fixture):
        """
        派单中心---海运---海运---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "sea_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/sea_transport/revoke', json=json_data, headers=headers)
        return result

    def st_cancel(self, login_fixture):
        """
        派单中心---海运---海运---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "sea_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/sea_transport/cancel', json=json_data, headers=headers)
        return result

    def abs_pending(self, login_fixture):
        """
        派单中心---海运---代订舱---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_booking_ship",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_booking_ship/pending', json=json_data, headers=headers)
        return result

    def abs_done(self, login_fixture):
        """
        派单中心---海运---代订舱---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_booking_ship",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_booking_ship/done', json=json_data, headers=headers)
        return result

    def abs_complete(self, login_fixture):
        """
        派单中心---海运---代订舱---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_booking_ship",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_booking_ship/complete', json=json_data, headers=headers)
        return result

    def abs_revoke(self, login_fixture):
        """
        派单中心---海运---代订舱---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_booking_ship",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_booking_ship/revoke', json=json_data, headers=headers)
        return result

    def abs_cancel(self, login_fixture):
        """
        派单中心---海运---代订舱---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_booking_ship",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_booking_ship/cancel', json=json_data, headers=headers)
        return result

    def niss_pending(self, login_fixture):
        """
        派单中心---海运---内贸海运---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_sea_shipping",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_sea_shipping/pending', json=json_data, headers=headers)
        return result

    def niss_done(self, login_fixture):
        """
        派单中心---海运---内贸海运---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_sea_shipping",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_sea_shipping/done', json=json_data, headers=headers)
        return result

    def niss_complete(self, login_fixture):
        """
        派单中心---海运---内贸海运---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_sea_shipping",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_sea_shipping/complete', json=json_data, headers=headers)
        return result

    def niss_cancel(self, login_fixture):
        """
        派单中心---海运---内贸海运---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "native_inshore_sea_shipping",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/native_inshore_sea_shipping/cancel', json=json_data, headers=headers)
        return result

    def ed_pending(self, login_fixture):
        """
        派单中心---快递---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "express_delivery",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/express_delivery/pending', json=json_data, headers=headers)
        return result

    def ed_done(self, login_fixture):
        """
        派单中心---快递---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "express_delivery",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/express_delivery/done', json=json_data, headers=headers)
        return result

    def ed_complete(self, login_fixture):
        """
        派单中心---快递---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "express_delivery",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/express_delivery/complete', json=json_data, headers=headers)
        return result

    def ed_revoke(self, login_fixture):
        """
        派单中心---快递---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "express_delivery",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/express_delivery/revoke', json=json_data, headers=headers)
        return result

    def ed_cancel(self, login_fixture):
        """
        派单中心---快递---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "express_delivery",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/express_delivery/cancel', json=json_data, headers=headers)
        return result

    def wo_pending(self, login_fixture):
        """
        派单中心---仓储---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "warehouse_operation",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/warehouse_operation/pending', json=json_data, headers=headers)
        return result

    def wo_done(self, login_fixture):
        """
        派单中心---仓储---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "warehouse_operation",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/warehouse_operation/done', json=json_data, headers=headers)
        return result

    def wo_complete(self, login_fixture):
        """
        派单中心---仓储---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "warehouse_operation",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/warehouse_operation/complete', json=json_data, headers=headers)
        return result

    def wo_revoke(self, login_fixture):
        """
        派单中心---仓储---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "warehouse_operation",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/warehouse_operation/revoke', json=json_data, headers=headers)
        return result

    def wo_cancel(self, login_fixture):
        """
        派单中心---仓储---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "warehouse_operation",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/warehouse_operation/cancel', json=json_data, headers=headers)
        return result

    def cs_pending(self, login_fixture):
        """
        派单中心---报关---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "customs_service",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/customs_service/pending', json=json_data, headers=headers)
        return result

    def cs_done(self, login_fixture):
        """
        派单中心---报关---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "customs_service",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/customs_service/done', json=json_data, headers=headers)
        return result

    def cs_complete(self, login_fixture):
        """
        派单中心---报关---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "customs_service",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/customs_service/complete', json=json_data, headers=headers)
        return result

    def cs_revoke(self, login_fixture):
        """
        派单中心---报关---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "customs_service",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/customs_service/revoke', json=json_data, headers=headers)
        return result

    def cs_cancel(self, login_fixture):
        """
        派单中心---报关---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "customs_service",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/customs_service/cancel', json=json_data, headers=headers)
        return result

    def td_pending(self, login_fixture):
        """
        派单中心---转DO---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "transform_do",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/transform_do/pending', json=json_data, headers=headers)
        return result

    def td_done(self, login_fixture):
        """
        派单中心---转DO---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "transform_do",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/transform_do/done', json=json_data, headers=headers)
        return result

    def td_complete(self, login_fixture):
        """
        派单中心---转DO---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "transform_do",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/transform_do/complete', json=json_data, headers=headers)
        return result

    def td_revoke(self, login_fixture):
        """
        派单中心---转DO---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "transform_do",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/transform_do/revoke', json=json_data, headers=headers)
        return result

    def td_cancel(self, login_fixture):
        """
        派单中心---转DO---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "transform_do",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/transform_do/cancel', json=json_data, headers=headers)
        return result

    def rt_pending(self, login_fixture):
        """
        派单中心---铁路运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "railroad_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/railroad_transport/pending', json=json_data, headers=headers)
        return result

    def rt_done(self, login_fixture):
        """
        派单中心---铁路运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "railroad_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/railroad_transport/done', json=json_data, headers=headers)
        return result

    def rt_complete(self, login_fixture):
        """
        派单中心---铁路运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "railroad_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/railroad_transport/complete', json=json_data, headers=headers)
        return result

    def rt_revoke(self, login_fixture):
        """
        派单中心---铁路运输---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "railroad_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/railroad_transport/revoke', json=json_data, headers=headers)
        return result

    def rt_cancel(self, login_fixture):
        """
        派单中心---铁路运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "railroad_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/railroad_transport/cancel', json=json_data, headers=headers)
        return result

    def railway_pending(self, login_fixture):
        """
        派单中心---驳船运输---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "barge_transport",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/barge_transport/pending', json=json_data, headers=headers)
        return result

    def railway_done(self, login_fixture):
        """
        派单中心---驳船运输---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "barge_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/barge_transport/done', json=json_data, headers=headers)
        return result

    def railway_complete(self, login_fixture):
        """
        派单中心---驳船运输---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "barge_transport",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/barge_transport/complete', json=json_data, headers=headers)
        return result

    def railway_revoke(self, login_fixture):
        """
        派单中心---驳船运输---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "barge_transport",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/barge_transport/revoke', json=json_data, headers=headers)
        return result

    def railway_cancel(self, login_fixture):
        """
        派单中心---驳船运输---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "barge_transport",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/barge_transport/cancel', json=json_data, headers=headers)
        return result

    def ao_pending(self, login_fixture):
        """
        派单中心---代办及单证服务---待派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_operation",
                                "deliveryType": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_operation/pending', json=json_data, headers=headers)
        return result

    def ao_done(self, login_fixture):
        """
        派单中心---代办及单证服务---已派单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_operation",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_waiting_check",
                                                   "delivery_order_status_checked"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_operation/done', json=json_data, headers=headers)
        return result

    def ao_complete(self, login_fixture):
        """
        派单中心---代办及单证服务---已完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_operation",
                                "deliveryType": 1,
                                "deliveryStatus": ["delivery_order_status_op_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_operation/complete', json=json_data, headers=headers)
        return result

    def ao_revoke(self, login_fixture):
        """
        派单中心---代办及单证服务---已撤销
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_operation",
                                "deliveryType": 2}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_operation/revoke', json=json_data, headers=headers)
        return result

    def ao_cancel(self, login_fixture):
        """
        派单中心---代办及单证服务---已取消
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertTimeFrom": f"{yesterday}", "serviceTypeCode": "agent_operation",
                                "deliveryType": 3}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list/agent_operation/cancel', json=json_data, headers=headers)
        return result

    def bill_receive_list(self, login_fixture):
        """
        计费与对账---应收结算---未完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}",
                                                             "statusType": ["status_check_awaiting",
                                                                            "status_check_detail_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/receive/list', json=json_data, headers=headers)
        return result

    def bill_receive_list_complete(self, login_fixture):
        """
        计费与对账---应收结算---已完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertDateFrom": f"{yesterday}", "statusType": ["status_check_all_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/receive/list', json=json_data, headers=headers)
        return result

    def change_receive_list(self, login_fixture):
        """
        计费与对账---应收改单---未完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}",
                                                             "statusType": "status_submit_awaiting status_submit_completed status_pay_check_awaiting status_fall_back_completed status_receive_oa_auditing"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/change_receive/list', json=json_data, headers=headers)
        return result

    def change_receive_list_complete(self, login_fixture):
        """
        计费与对账---应收改单---已完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}",
                                                             "statusType": "status_check_not_passed status_check_completed"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/change_receive/list', json=json_data, headers=headers)
        return result

    def receivable_pay_list(self, login_fixture):
        """
        计费与对账---应收账单---未完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "statusType": "status_draft status_check_awaiting status_fall_back_completed"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/receivable_pay/list', json=json_data, headers=headers)
        return result

    def receivable_pay_list_Audited(self, login_fixture):
        """
        计费与对账---应收账单---已审核页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "statusType": "status_check_completed"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/receivable_pay/list', json=json_data, headers=headers)
        return result

    def receivable_pay_list_Invoiced(self, login_fixture):
        """
        计费与对账---应收账单---已开票页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "statusType": "status_invoice_completed"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/receivable_pay/list', json=json_data, headers=headers)
        return result

    def invoice_apply_list(self, login_fixture):
        """
        计费与对账---应收发票
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/invoice_apply/list', json=json_data, headers=headers)
        return result

    def synergy_receive_list(self, login_fixture):
        """
        计费与对账---应收协同账单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "customerId": []}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/synergy_receive/list', json=json_data, headers=headers)
        return result

    def merge_list(self, login_fixture):
        """
        计费与对账---合并结算---未完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}",
                                                             "statusType": "status_check_awaiting status_check_detail_completed"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/merge/list', json=json_data, headers=headers)
        return result

    def merge_list_Completed(self, login_fixture):
        """
        计费与对账---合并结算---已完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertDateFrom": f"{yesterday}", "statusType": "status_check_all_completed"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/merge/list', json=json_data, headers=headers)
        return result

    def pay_list(self, login_fixture):
        """
        计费与对账---应付结算---未完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}",
                                                             "statusType": ["status_check_awaiting",
                                                                            "status_check_detail_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/pay/list', json=json_data, headers=headers)
        return result

    def pay_list_Completed(self, login_fixture):
        """
        计费与对账---应付结算---已完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10,
                     "filter": {"insertDateFrom": f"{yesterday}", "statusType": ["status_check_all_completed"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/pay/list', json=json_data, headers=headers)
        return result

    def change_pay_list(self, login_fixture):
        """
        计费与对账---应付改单---未完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}",
                                                             "statusType": "status_submit_awaiting status_submit_completed status_receive_oa_auditing"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/change_pay/list', json=json_data, headers=headers)
        return result

    def change_pay_list_Completed(self, login_fixture):
        """
        计费与对账---应付改单---已完成页签
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}",
                                                             "statusType": "status_check_not_passed status_check_completed"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/change_pay/list', json=json_data, headers=headers)
        return result

    def due_pay_list(self, login_fixture):
        """
        计费与对账---应付账单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}", "customerId": []}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/due_pay/list', json=json_data, headers=headers)
        return result

    def reimbursement_list(self, login_fixture):
        """
        计费与对账---报销结算
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/reimbursement/list', json=json_data, headers=headers)
        return result

    def receiveMonthBill_list(self, login_fixture):
        """
        计费与对账---应收月账单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/receiveMonthBill/list', json=json_data, headers=headers)
        return result

    def payMonthBill_list(self, login_fixture):
        """
        计费与对账---应付月账单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/payMonthBill/list', json=json_data, headers=headers)
        return result

    def payPrepaid_list(self, login_fixture):
        """
        计费与对账---应付代垫费
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/payPrepaid/list', json=json_data, headers=headers)
        return result

    def receivePrepaid_list(self, login_fixture):
        """
        计费与对账---应收代垫费
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/receivePrepaid/list', json=json_data, headers=headers)
        return result

    def payExtra_list(self, login_fixture):
        """
        计费与对账---应付额外费用
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/payExtra/list', json=json_data, headers=headers)
        return result

    def receiveExtra_list(self, login_fixture):
        """
        计费与对账---应收额外费用
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/receiveExtra/list', json=json_data, headers=headers)
        return result

    def other_list(self, login_fixture):
        """
        计费与对账---其他费用
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertDateFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/bill/other/list', json=json_data, headers=headers)
        return result

    def dispatch_list(self, login_fixture, serviceTypeCode):
        """
        物流执行---所有类型---执行中
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}",
                                                             "deliveryStatus": ["delivery_order_status_waiting_check",
                                                                                "delivery_order_status_checked"],
                                                             "serviceTypeCode": serviceTypeCode, "deliveryType": 1}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list', json=json_data, headers=headers)
        return result

    def dispatch_list_complete(self, login_fixture, serviceTypeCode):
        """
        物流执行---所有类型---执行完成
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}",
                                                             "deliveryStatus": ["delivery_order_status_op_completed"],
                                                             "serviceTypeCode": serviceTypeCode, "deliveryType": 1}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/list', json=json_data, headers=headers)
        return result

    def seaBill_list(self, login_fixture):
        """
        物流执行---提单制作---国际海运---待处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "acceptanceStatus": 2,
                     "filter": {"minInsertTime": f"{yesterday}", "customerId": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/seaBill/list', json=json_data, headers=headers)
        return result

    def seaBill_list_processed(self, login_fixture):
        """
        物流执行---提单制作---国际海运---已处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "acceptanceStatus": 1,
                     "filter": {"minInsertTime": f"{yesterday}", "customerId": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/seaBill/list', json=json_data, headers=headers)
        return result

    def airlift_list(self, login_fixture):
        """
        物流执行---提单制作---空运---待处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "acceptanceStatus": 2,
                     "filter": {"minInsertTime": f"{yesterday}", "customerId": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/airlift/list', json=json_data, headers=headers)
        return result

    def airlift_list_processed(self, login_fixture):
        """
        物流执行---提单制作---空运---已处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "acceptanceStatus": 1,
                     "filter": {"minInsertTime": f"{yesterday}", "customerId": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/airlift/list', json=json_data, headers=headers)
        return result

    def railway_list(self, login_fixture):
        """
        物流执行---提单制作---铁路---待处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "acceptanceStatus": 2,
                     "filter": {"minInsertTime": f"{yesterday}", "customerId": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/railway/list', json=json_data, headers=headers)
        return result

    def railway_list_processed(self, login_fixture):
        """
        物流执行---提单制作---铁路---已处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "acceptanceStatus": 1,
                     "filter": {"minInsertTime": f"{yesterday}", "customerId": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/railway/list', json=json_data, headers=headers)
        return result

    def barge_list(self, login_fixture):
        """
        物流执行---提单制作---驳船---待处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "acceptanceStatus": 2,
                     "filter": {"minInsertTime": f"{yesterday}", "customerId": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/barge/list', json=json_data, headers=headers)
        return result

    def barge_list_processed(self, login_fixture):
        """
        物流执行---提单制作---驳船---已处理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "acceptanceStatus": 1,
                     "filter": {"minInsertTime": f"{yesterday}", "customerId": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/barge/list', json=json_data, headers=headers)
        return result

    def taskList_list(self, login_fixture):
        """
        物流执行---文档管理---任务单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/taskList/list', json=json_data, headers=headers)
        return result

    def taskList_logisticslist(self, login_fixture):
        """
        物流执行---文档管理---物流订单
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}", "customerGuid": []}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/taskList/logisticslist', json=json_data, headers=headers)
        return result

    def base_list(self, login_fixture):
        """
        档案管理---客户---基本信息
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/client2/base/list', json=json_data, headers=headers)
        return result

    def contact_list(self, login_fixture):
        """
        档案管理---客户---联系人
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/client2/contact/list', json=json_data, headers=headers)
        return result

    def client2_agent_list(self, login_fixture):
        """
        档案管理---客户---代理跟进分配
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/client2/agent/list', json=json_data, headers=headers)
        return result

    def client2_cs_list(self, login_fixture):
        """
        档案管理---客户---客服分配
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/client2/cs/list', json=json_data, headers=headers)
        return result

    def client2_sn_list(self, login_fixture):
        """
        档案管理---客户---协同通知
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/client2/sn/list', json=json_data, headers=headers)
        return result

    def factory_list(self, login_fixture):
        """
        档案管理---客户---收发货人档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/factory/list', json=json_data, headers=headers)
        return result

    def tax_list(self, login_fixture):
        """
        档案管理---客户---税率档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/client2/tax/list', json=json_data, headers=headers)
        return result

    def customerInvoice_list(self, login_fixture):
        """
        档案管理---客户---开票档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/customerInvoice/list', json=json_data, headers=headers)
        return result

    def client_rate_list(self, login_fixture):
        """
        档案管理---客户---汇率档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/client_rate/list', json=json_data, headers=headers)
        return result

    def material_list(self, login_fixture):
        """
        档案管理---客户---物料档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/material/list', json=json_data, headers=headers)
        return result

    def customerClearingUnit_list(self, login_fixture):
        """
        档案管理---客户---结算单位
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/customerClearingUnit/list', json=json_data, headers=headers)
        return result

    def clientShare_list(self, login_fixture):
        """
        档案管理---客户---客户共享
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/clientShare/list', json=json_data, headers=headers)
        return result

    def customerCustomaryCost_list(self, login_fixture):
        """
        档案管理---客户---习惯费用项
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/customerCustomaryCost/list', json=json_data, headers=headers)
        return result

    def customerTerminal_list(self, login_fixture):
        """
        档案管理---客户---客户端管理
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/customerTerminal/list', json=json_data, headers=headers)
        return result

    def blm_list(self, login_fixture):
        """
        档案管理---客户---委托模板库
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"actives": ["active_activated", "active_unactivated"]}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/bussiness_library_modal/list', json=json_data, headers=headers)
        return result

    def customerDistrict_list(self, login_fixture):
        """
        档案管理---客户---客户地点档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/customerDistrict/list', json=json_data, headers=headers)
        return result

    def supplier_base_list(self, login_fixture):
        """
        档案管理---供应商---基本信息
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/supplier/base/list', json=json_data, headers=headers)
        return result

    def supplier_contact_list(self, login_fixture):
        """
        档案管理---供应商---联系人
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/supplier/contact/list', json=json_data, headers=headers)
        return result

    def car_list(self, login_fixture):
        """
        档案管理---供应商---车辆档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/car/list', json=json_data, headers=headers)
        return result

    def driver_list(self, login_fixture):
        """
        档案管理---供应商---司机档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/supplier/driver/list', json=json_data, headers=headers)
        return result

    def supplier_rate_list(self, login_fixture):
        """
        档案管理---供应商---汇率档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/supplier_rate/list', json=json_data, headers=headers)
        return result

    def suptaxrate_list(self, login_fixture):
        """
        档案管理---供应商---税率档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/supplier/suptaxrate/list', json=json_data, headers=headers)
        return result

    def tenantWarehouse_list(self, login_fixture):
        """
        档案管理---供应商---仓库档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/tenantWarehouse/list', json=json_data, headers=headers)
        return result

    def archiverService_list(self, login_fixture):
        """
        档案管理---供应商---地点档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/archiverService/list', json=json_data, headers=headers)
        return result

    def supplierClearingUnit_list(self, login_fixture):
        """
        档案管理---供应商---结算单位
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/supplierClearingUnit/list', json=json_data, headers=headers)
        return result

    def supplierCustomaryCost_list(self, login_fixture):
        """
        档案管理---供应商---习惯费用项
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/supplierCustomaryCost/list', json=json_data, headers=headers)
        return result

    def institution_list(self, login_fixture):
        """
        档案管理---组织档案---组织机构
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/institution/list', json=json_data, headers=headers)
        return result

    def insideStatement_list(self, login_fixture):
        """
        档案管理---组织档案---内部结算
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/insideStatement/list', json=json_data, headers=headers)
        return result

    def it_list(self, login_fixture):
        """
        档案管理---组织档案---利润转移设置
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/insideStatement/transferList', json=json_data, headers=headers)
        return result

    def department_list(self, login_fixture):
        """
        档案管理---组织档案---部门档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/department/list', json=json_data, headers=headers)
        return result

    def user_list(self, login_fixture):
        """
        档案管理---组织档案---用户档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/user/list', json=json_data, headers=headers)
        return result

    def tenantCorporateInfo_list(self, login_fixture):
        """
        档案管理---组织档案---法人档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/tenantCorporateInfo/list', json=json_data, headers=headers)
        return result

    def charge_item_list(self, login_fixture):
        """
        档案管理---费用项档案
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/charge_item/list', json=json_data, headers=headers)
        return result

    def excelReport_searchList(self, login_fixture):
        """
        智能分析---物流订单整审时效报表
        :param json_data:
        :return:
        """
        json_data = {"api": "trace-service/logistics_order_report/order/monitoring/report",
                     "filter": {"filter": {"insertTimeFrom": f"{yesterday}"}, "itemTo": 200, "itemFrom": 0}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/basic/excelReport/searchList', json=json_data, headers=headers)
        return result


ApiEpld = Query()
