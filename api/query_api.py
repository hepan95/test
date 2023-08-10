from utils.read import base_data
from core.rest_client import Api
from datetime import date, timedelta

url = base_data.read_ini()['host']['api_sit_url']
yesterday = date.today() + timedelta(days=-3)  # 前三天


class Query:

    def order_accept_list(self, login_fixture):
        """
        接入订单查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}", "cs_tag": -1,
                     "orderType": "status_waiting_receipt"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/accept/list', json=json_data, headers=headers)
        return result

    def order_pending_list(self, login_fixture):
        """
        待办任务查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "orderType": "status_waiting_perfect"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/pending/list', json=json_data, headers=headers)
        return result

    def order_complete_list(self, login_fixture):
        """
        执行中任务查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/complete/list', json=json_data, headers=headers)
        return result

    def track_order_list(self, login_fixture, statusType):
        """
        订单跟踪-各个页签列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "statusType": statusType}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/track_order/list', json=json_data, headers=headers)
        return result

    def order_total_list(self, login_fixture):
        """
        订单汇总列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/order/total/list', json=json_data, headers=headers)
        return result

    def lob_list(self, login_fixture):
        """
        配载优化-配载列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 2000, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/loading/load_optimized/beLoaded', json=json_data, headers=headers)
        return result

    def lop_list(self, login_fixture):
        """
        配载优化-预配载列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"orderPlanPickupTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/loading/load_optimized/preLoaded', json=json_data, headers=headers)
        return result

    def lol_list(self, login_fixture):
        """
        配载优化-已配载列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "filter": {"insertTimeFrom": f"{yesterday}"}}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/loading/load_optimized/loadedList', json=json_data, headers=headers)
        return result

    def dispatch_todo_list(self, login_fixture):
        """
        待办任务-待派单列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "orderType": "status_waiting_delivery", "intelligenceTag": 1}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/todo/list', json=json_data, headers=headers)
        return result

    def dispatch_todo2_list(self, login_fixture):
        """
        待办任务-待智能派单列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "orderType": "status_waiting_delivery", "intelligenceTag": 0}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/todo/list', json=json_data, headers=headers)
        return result

    def dispatch_todo3_list(self, login_fixture):
        """
        待办任务-待司机确认列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "orderType": "status_waiting_check", "ownerCarTag": 1}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/todo/list', json=json_data, headers=headers)
        return result

    def dispatch_todo4_list(self, login_fixture):
        """
        待办任务-待司机确认列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "orderType": "status_waiting_check", "ownerCarTag": 0}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/todo/list', json=json_data, headers=headers)
        return result

    def dispatch_todo5_list(self, login_fixture):
        """
        待办任务-已拒绝列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}",
                     "orderType": "status_reject_completed", "intelligenceTag": 1}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/todo/list', json=json_data, headers=headers)
        return result

    def dispatch_done_list(self, login_fixture):
        """
        执行中任务列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/done/list', json=json_data, headers=headers)
        return result

    def dispatch_finished_list(self, login_fixture):
        """
        已完成任务列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/finished/list', json=json_data, headers=headers)
        return result

    def tft_list(self, login_fixture, waybillStatus):
        """
        运单跟踪-各个页签列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}", "statusType": waybillStatus}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/follow_transport/list', json=json_data, headers=headers)
        return result

    def dst_list(self, login_fixture, tab):
        """
        监理任务-各个页签列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "dispatchTimeFrom": f"{yesterday}", "supervisorTag": tab}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/dispatch/supervisor_task/list', json=json_data, headers=headers)
        return result

    def ttt_list(self, login_fixture):
        """
        跟踪管控-在途跟踪列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/track_transport/list', json=json_data, headers=headers)
        return result

    def tfm_list(self, login_fixture, fileStatus):
        """
        跟踪管控-文件管理各个页签列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}", "fileStatus": fileStatus}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/file_manager/list', json=json_data, headers=headers)
        return result

    def ccm_list(self, login_fixture, carState):
        """
        跟踪管控-车辆管理各个页签列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "carState": carState}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/config/car_manager/list', json=json_data, headers=headers)
        return result

    def tee_list(self, login_fixture, abnormalStatus):
        """
        跟踪管控-事件异常各个页签列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"itemFrom": 0, "itemTo": 10, "accidentReportDateFrom": f"{yesterday}",
                     "statusType": abnormalStatus}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/event_exception/list', json=json_data, headers=headers)
        return result

    def ta_list(self, login_fixture, appointmentTag):
        """
        跟踪管控-预约管理各个页签列表查询接口
        :param json_data:
        :return:
        """
        json_data = {"appointmentTag": appointmentTag, "itemFrom": 0, "itemTo": 10, "insertTimeFrom": f"{yesterday}"}
        token = login_fixture
        headers = {
            "Cookie": 'token={}'.format(token)
        }
        result = Api.post('/api/track/appointment/list', json=json_data, headers=headers)
        return result


ApiTms = Query()
