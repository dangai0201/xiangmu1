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
class ShOP(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #实例化
        self.fangfa=fangfa.FireFox()
        self.url=url.URL()
        pass
    def setUp(self):
        self.fangfa.fire_start(self.url.JD_MAIN1)
        pass
    def tearDown(self):
        self.fangfa.firefox_close()
        pass
    # def test_danpin1(self):
    #     self.fangfa.FindClass("buy_btn6").click()
    #     self.fangfa.TimeSleep(3)
    #     self.msg=self.fangfa.FindClass("hd_pop_tips")
    #     self.message=self.msg.text
    #     print self.message
    #     self.assertEqual(self.message,u"已成功加入购物车")
    #     pass
    # def test_danpin2(self):
    #     self.fangfa.FindClass("buy_btn6").click()
    #     self.fangfa.TimeSleep(3)
    #     self.fangfa.ClickClass("hd_btn_l")
    #     self.title = self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title, u"Apple iPhone X (A1865) 64GB 深空灰色 移动联通电信4G手机【价格、品牌、报价】-1号店")
    #     pass
    def test_danpin3(self):
        self.fangfa.FindClass("buy_btn6").click()
        self.fangfa.TimeSleep(3)
        self.current=self.fangfa.getCurrent_window()
        self.fangfa.ClickClass("hd_btn_r")
        self.fangfa.TimeSleep(2)
        self.fangfa.switch_to_window(self.current)
        self.fangfa.TimeSleep(3)
        self.title=self.fangfa.getTitle()
        print self.title
        self.assertEqual(self.title,u"我的购物车-1号店,只为更好的生活")
        pass


