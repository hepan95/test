# ！/usr/bin/env python
# -- coding:utf-8 --
# @FileName : log_page.py.py
# @Time: 2022/7/4 9:52
# @Author: ph
import  os,time,logging
from Common import common_funtion as  cf
log_path=cf.Common_page().projects_path()+"\Log"
# print(log_path)
class Log():
    def __init__(self):  #创建log日志,以日期命名
        self.logname=os.path.join(log_path,"{}.log".format(time.strftime("%Y_%m_%d_%H%M%S")))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter=logging.Formatter('[%(asctime)s]-%(filename)s]-%(levelname)s:%(message)s')  #日志输出格式

    def console(self,level,message):  #控制台方法
        fh=logging.FileHandler(self.logname,"a",encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()
    def debug(self,message):    #调试调用的方法
        self.console("debug",message)
    def info(self,message):    #开始，结束 调用的方法
        self.console("info",message)
    def warning(self,message):   #操作动作的时候调用的方法
        self.console("warning",message)
    def error(self,message):
        self.console("error",message)   #报错的时候调用的方法

if __name__ == '__main__':
    run=Log()
    run.info("开始测试了！！！！哈哈哈！！！")
    run.info("现在输入密码了")
    run.warning("测试完了")
    run.error("牛逼啊！全部奔溃了！！！")