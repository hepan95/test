from utils.read import base_data
from testcases.conftest import get_data
from core.rest_client import Api
url = base_data.read_ini()['host']['api_sit_url']


class ApiTms:

    def login(self):
        """
        登录接口
        :param json_data:
        :return:
        """
        data = get_data()['login_fixture']
        account = data['account']
        password = data['password']
        json_data = {
            "account": account,
            "password": password
        }
        result = Api.post('/api/login', json=json_data)
        return result


login_outcome = ApiTms()
