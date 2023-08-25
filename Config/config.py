#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: config.py.py
# @Time:2022/8/29 8:30
# @Author:PH
'''ict测试环境，测试租户'''
'''后台端'''
test01 = 0                                    #代表测试环境
ht_host="http://ict-test.epldcloud.com"      #测试环境api
ht_headers={
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
	    'Accept': '*/*',
	    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	    'Accept-Encoding': 'gzip, deflate',
	    'Content-Type': 'application/json',
	    'Content-Length': '68',
	    'Connection': 'keep-alive',
		'Cookie' : ''}                             #请求头
ht_mobile="maomin@hercules-logistics.com"              #后台端测试环境登录账号
ht_password="meMFPugSk6"                      #后台测试环境登录的密码

ht_mobile_FBA="tcp@cloudlinkscm.com"     #翠萍账号 正常租户
ht_password_FBA="tcp123"                      #
ht_host_FBA="http://ict-test.epldcloud.com"

'''货主端'''
hz_host="http://ict-test.epldcloud.com"
hz_mobile="13022222821"                     #货主端测试环境登录账号
hz_password="hg123456"                       #货主测试环境登录的密码
hz_name="毛敏租户测试货主1"                     #货主名称

hz_mobile_FBA= "17875465665@default.com"   #翠萍账号  正常租户
hz_password_FBA="HG123456"
hz_name_FBA="Amazon Global Logistics - FBA"                     #货主名称
hz_host_FBA="http://ict-test.epldcloud.com"


'''运输公司'''
gys_host="http://ict-test.epldcloud.com"
ys_mobile="13022222921"                      #运输公司测试环境登录账号
ys_password="hg123456"                       #运输公司测试环境登录密码
gys1_name="毛敏租户测试供应商1"                     #供应商1名称
gys2_name="测试人员测试租户" 						 #供应商1名称

'''司机小程序'''
siji_host="https://icttxdev.epldcloud.com"
siji_headers={
			'Connection': 'keep-alive',
			'Content-Length': '246',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 '
			'MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
			'content-type': 'application/json',
			'token': '142eb686-0216-4c12-99ef-8c4b9beb19a9:03722dc2-05a4-497c-bf21-c1fe4c0edc39',
			'Accept-Encoding': 'gzip, deflate, br'}
siji_mobile="18875914340"
siji_password="123456"





'''ict生产环境--测试租户'''
'''后台端'''
# test01 = 1                                                  #代表生产环境
# ht_host="http://www.hercules-transportation.net"       					#生产环境api
# ht_headers={
# 	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
# 	    'Accept': '*/*',
# 	    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
# 	    'Accept-Encoding': 'gzip, deflate',
# 	    'Content-Type': 'application/json',
# 	    'Content-Length': '68',
# 	    'Connection': 'keep-alive',
# 		'Cookie' : ''}                           				 #请求头
#
# ht_mobile="hepan@hercules-logistics.com" 						#后台生产环境登录账号
# ht_password="DLgIkV2Kl"                       					#后台生产环境登录密码
# '''货主端'''
# hz_host="http://ict-cs.hercules-transportation.net"
# hz_mobile="13022222821@default.com"    							#货主端生产环境登录账号
# hz_password="hg123456"                    						#生产环境#登录的密码
# hz_name="毛敏租户测试货主1"                     #货主名称
# '''运输公司'''
# gys_host="http://ict-sp.hercules-transportation.net"
# ys_mobile="13022222921@default.com"         					#运输公司生产环境登录账号要带后缀！！！
# ys_password="hg123456"                      					#运输公司生产环境登录密码
# gys1_name="毛敏租户测试供应商1"                     #供应商1名称
# gys2_name="测试人员测试租户" 						 #供应商1名称
#
#
# #
# '''ictUAT环境，测试租户'''
# '''后台端'''
# #请求头
# ht_mobile_FBA="hjs2@cloudlinkscm.com"     # 正常租户
# ht_password_FBA="HG32774"                      #
# ht_host_FBA="https://ict-uat.cloudlinkscm.com"
# ht_headers_FBA = {
# 	'Content-Type': 'application/json'
# }
#
# '''货主端'''
# hz_mobile_FBA= "17875465665@default.com"   #正常租户
# hz_password_FBA="hg12345"
# hz_name_FBA="Amazon Global Logistics - FBA"              #货主名称
# hz_host_FBA="https://ict-uat.cloudlinkscm.com"
