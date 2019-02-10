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
class ShouYe(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #实例化
        self.fangfa=fangfa.FireFox()
        self.url=url.URL()
        pass
    def setUp(self):
        self.fangfa.fire_start(self.url.JD_MAIN)
        pass
    def tearDown(self):
        self.fangfa.firefox_close()
        pass
    # def test_shouye(self):
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.firefox_yidong()
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickID("new_person_channel")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.title=self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title,u"1号店新人专享大礼包")
    # def test_shouye1(self):
    #     self.fangfa.fifefox_bottom()
    #     self.current = self.fangfa.getCurrent_window()
    #     self.fangfa.ClickXpath("//*[@id='bottomHelpLinkId']/dl[1]/dd[1]/a")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.title = self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title, u"购物流程-1号店帮助中心")
    # def test_shouye2(self):
    #     self.fangfa.fifefox_bottom()
    #     self.current = self.fangfa.getCurrent_window()
    #     self.fangfa.ClickXpath("//*[@id='bottomHelpLinkId']/dl[1]/dd[2]/a")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.title = self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title, u"会员制度-1号店帮助中心")
    # def test_shouye3(self):
    #     ele=self.fangfa.ClickClass("icon-menu")
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickLink(u"全球进口")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.title=self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title,u"进口食品【价格、评价、图片】-1号店")
    def test_shouye4(self):
        ele = self.fangfa.ClickClass("hd_topbar_city")
        self.fangfa.ClickXpath("//*[@id='hd_city_select']/div[2]/div/a[2]")
        self.fangfa.TimeSleep(2)
        self.msg=self.fangfa.FingXpath("//*[@id='currProvince']/em")
        self.message=self.msg.text
        print self.message
        self.assertEqual(self.message, u"北京")
        pass
