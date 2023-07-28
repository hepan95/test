import os

import pytest


from core.rest_client import Api
from utils.log_util import logger
from utils.read import base_data


@pytest.fixture(scope="function", autouse=True)
def func():
    logger.info("开始执行测试用例")
    yield
    logger.info("测试用例执行完成")


def get_data():
    return base_data.read_data()


@pytest.fixture()
def login_fixture():
    if 'token' not in os.environ:
        data = get_data()['login_fixture']
        account = data['account']
        password = data['password']
        json_data = {
            "account": account,
            "password": password
        }
        result = Api.post('/api/login', json=json_data)
        os.environ['token'] = result.body['result']['token']
        return result.body['result']['token']
    else:
        return os.environ['token']

