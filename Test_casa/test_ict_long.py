#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: test_ict_long.py
# @Time:2023/2/28 11:12
# @Author:PH
from Common import ict_api as ict
import allure
import pytest
import requests,json
myskip = pytest.mark.skipif()

@allure.parent_suite('ict登录接口测试包')  # 包的注释
@allure.suite('ict登录t接口测试模块')   #模块的注释
@allure.sub_suite('各端登录接口')      #大类的注释

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



