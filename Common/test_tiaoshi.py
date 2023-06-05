#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: test_tiaoshi.py
# @Time:2023/4/18 13:34
# @Author:PH
import datetime

import allure
from Common import ict_api as ict
from Config import config as cf
from Common import common_funtion as bf
from Config import config as long
from  Common import  ict_api as api
import requests,json
class Test_query01():
    def __init__(self):
        self.host=long.ht_host
        self.headers=long.ht_headers
        self.ht_token=api.Test_login().Test_login001()
    def test_Added0093(self,dd_hao="MCSZ-MCO-20230504-0010",fw_lx="port_container_export_transport"):
        fy_lb = ict.Test_Added01().test_Added0094(dd_hao=dd_hao, fw_lx=fw_lx)

        list11 = []
        time1 = fy_lb[2]
        print(time1)
        for key in time1:
            print(key)
            if key == "supplierId":
                # print(time1[key])
                list11.append(time1[key])
        print(list11)

        # pytest.assume(list11 != ['租户测试自有车-集1'])  # 断言结算单位为空


if __name__ == '__main__':
    run=Test_query01()
    run.test_Added0093()