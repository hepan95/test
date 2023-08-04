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


ApiTms = Query()
