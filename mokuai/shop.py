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
class Shop(unittest.TestCase):
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


    # def test_gouwu1(self):
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.SendKeysClass("hd_search_ipt",u"足球鞋")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.ClickClass("hd_search_btn")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.title=self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title,u"足球鞋-1号店yhd.com")
    #     self.fangfa.ClickID("itemSearchResultCon_38968272401")
    #     self.fangfa.TimeSleep(3)
    #     self.msg=self.fangfa.FingXpath("//*[@id='promotion_title']/div/div/span[2]")
    #     self.fangfa.TimeSleep(10)
    #     self.messag=self.msg.text
    #     print self.messag
    #     self.assertEqual(self.messag,u"满599元减100元，满699元减150元")
    #     pass
    # def test_gouwu2(self):
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.SendKeysClass("hd_search_ipt", u"足球鞋")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.ClickClass("hd_search_btn")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.ClickID("buyButton_38968272401")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.msg=self.fangfa.FindClass("mh")
    #     self.fangfa.TimeSleep(2)
    #     self.message=self.msg.text
    #     print self.message
    #     self.assertEqual(self.message,u"新品足球鞋男女刺客碎钉内马尔人造草地学生长钉C罗梅西款训练鞋成人TF/AG刺客儿童青少年比赛球鞋 2051-2黄色-碎钉款 41")
    #     pass
    def test_gouwu3(self):
        self.fangfa.SendKeysClass("hd_search_ipt", "iphone")
        self.fangfa.TimeSleep(2)
        self.fangfa.ClickClass("hd_search_btn")
        self.fangfa.TimeSleep(2)
        self.fangfa.ClickID("pdlink1_100000177760")
        self.fangfa.FindClass("buy_btn6").click()
        self.fangfa.TimeSleep(2)
        #self.msg1 = self.fangfa.FindClass("hd_pop_tips")
        #self.message1 = self.msg1.text
        #print self.message1
        #self.assertEqual(self.message1, u"已成功加入购物车")
        self.fangfa.AssertEquilTitle(self, u"商品已成功加入购物车")
        pass







