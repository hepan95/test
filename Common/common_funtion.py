#!/usr/bin/env/python
# --coding:utf-8--
# @fileName: common_funtion.py.py
# @Time:2022/10/18 11:07
# @Author:PH
import  socket  #获取本地主机IP地址
import datetime  #获取时间模块
import os        #获取主机IP地址模块
import string  #自动生成含税模块
import random
class Common_page():
    def __init__(slif):
        pass
    def projects_path(self):    #查看模块路径！！！！！！！兼容性强
        current_path=os.path.abspath(__file__)
        father_path=os.path.abspath(os.path.dirname(current_path)+os.path.sep)
        new_path=os.path.abspath(os.path.dirname(father_path)+os.path.sep)
        # print(new_path)
        return new_path
    '''获取内网IP地址'''
    def get_id01(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        # print(ip)
        return ip
    def get_today(self):     #获取今天的年月日的类方法
        now_time=datetime.datetime.now().strftime("%Y-%m-%d")
        # print(now_time)
        return  now_time
    def get_today001(self):
        # 获取今天（现在时间）
        today = datetime.datetime.today()
        yesterday = today - datetime.timedelta(days=1) # 昨天
        tomorrow = today + datetime.timedelta(days=1)  # 明天
        date = datetime.date.today()  # 获取当前日期
        y = today + datetime.timedelta(days=5) # 获取的时间---=1代表1天-
        z = today + datetime.timedelta(days=10) #
        q = today + datetime.timedelta(days=20)  #
        c = today + datetime.timedelta(days=50)  #
        t  = today + datetime.timedelta(days=100)  #
        w = today + datetime.timedelta(days=200)  #
        n = today + datetime.timedelta(days=0)  #
        h = y.strftime('%Y-%m-%d')   #今天
        y = y.strftime('%Y-%m-%d %H:%M:%S')  # +5天
        z = z.strftime('%Y-%m-%d %H:%M:%S')  # +10天
        q = q.strftime('%Y-%m-%d %H:%M:%S')  #+ 20天
        c = c.strftime('%Y-%m-%d ')  #+50天
        t = t.strftime('%Y-%m-%d ')  #+100天
        w = w.strftime('%Y-%m-%d ')  # + 200天
        n = n.strftime('%Y%m%d%H%M%S')  #+ 20天
        # print(today)
        # print(z)
        # print(q)
        # print(h)
        # print(c)
        # print(t)
        # print(w)
        # print(n)
        return today,y,z,q,h,c,t,w,n,h

    def start(self):

        x =  ''.join(random.sample(string.digits,10))

        # print(x)
        return x





if __name__ == '__main__':
    run=Common_page()
    run.projects_path()
    # run.get_today()
    # run.read_excel001()
    run.get_today001()
    # run.start()
