#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: Run.py.py
# @Time:2022/10/18 17:07
# @Author:PH
import os

import pytest
# import unittest
# from HTMLTestRunner import HTMLTestRunner
from Common import common_funtion as lj

# if __name__ == '__main__':
#     '''调用方法：  ./文件名/.py/类/类方法'''
#     #           "./Test_casa/test_test.py::Test_login_01::test_002"
#     test="./Test_casa/test_test.py"
#     pytest.main(['-vs',test])

'''配合jenkins生成测试报告的使用方法'''
if __name__ == '__main__':
    from Config  import config
    test01 = config.test01
    if test01 == 0 :   # 0 是测试环境
        test="./Test_casa/test_ict_long.py"
    # 执行测试用例生成测试数据，如果已经存在报告，那就先清空，然后再生成新的测试报告，使用命令： --clean-alluredir
        pytest.main(['-vs', test, '--clean-alluredir', '--alluredir', './allure-results'])
    if test01 == 1 :   # 1 是生产环境
        test="./Test_casa/test_ict_long.py"
        # test = ".//Test_casa"
    # 执行测试用例生成测试数据，如果已经存在报告，那就先清空，然后再生成新的测试报告，使用命令： --clean-alluredir
        pytest.main(['-vs', test, '--clean-alluredir', '--alluredir', './allure-results'])


'''生成allure测试报告，存放本地'''
# if __name__ == '__main__':
#     import os
#     reprot_name="Reprot{}.html".format(lj.Common_page().get_today())      #测试报告的名字（当天时间命名）
#     # file_path 是自动化脚本文件
#     # file_path = "./Test_casa/test_ict_long.py"
#     file_path = "./Test_casa"
#     # xmlpth是生成的xml数据文件，用来生成最终报告
#     xmlpath = "./xml"
#     xmlStr = "pytest -vs -q {file_path} --alluredir {xmlpath}".format(file_path=file_path, xmlpath=xmlpath)
#     # print("xmlStr", xmlStr)
#     # 执行命令，生成xml文件
#     a = os.system(xmlStr)
#     # 生成报告，--clean会清除旧文件
#     htmlStr = "allure generate {xmlpath} -o ./apache-tomcat-10.0.20/webapps/ROOT/Report/{reprot_name}/ --clean".format(xmlpath=xmlpath,reprot_name=reprot_name)
#     r=os.system(htmlStr)
#
