#-*-coding:utf-8-*-
#导入单元测试
import unittest
#导入工具类
from fz import fangfa
from url import url
#引入ActionChains包
from selenium.webdriver.common.action_chains import ActionChains

import sys
from selenium import webdriver



reload(sys)
sys.setdefaultencoding( "utf-8" )
class SHOPPING(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #实例化
        self.fangfa=fangfa.FireFox()
        self.url=url.URL()
        pass
    def setUp(self):
        self.fangfa.fire_start(self.url.JD_MAIN2)
        pass
    def tearDown(self):
        self.fangfa.firefox_close()
        pass
    def test_SHOPPING(self):
        self.fangfa.ClickXpath("//*[@id='cart_main_body']/div[2]/div[2]/div[1]/span/a")
        self.fangfa.TimeSleep(2)
        self.msg=self.fangfa.FindID("//*[@id='963181']/div/div[1]/p")
        self.message=self.msg.text
        print self.message