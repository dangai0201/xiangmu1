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
#声明类继承单元测试
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #实例化
        self.fangfa=fangfa.FireFox()
        self.url=url.URL()
        pass
    def setUp(self):
        self.fangfa.fire_start(self.url.JD_LOGIN)
        pass
    def tearDown(self):
        self.fangfa.firefox_close()
        pass
    def test_login1(self):
        self.fangfa.SendKeysClass("ipt_username","")
        self.fangfa.SendKeysClass("ipt_password", "")
        self.fangfa.ClickClass("login_btn")
        self.fangfa.TimeSleep(2)
        self.msg=self.fangfa.FindClass("error_tips")
        self.message=self.msg.text
        self.assertEqual(self.message,u"请输入账号和密码")
        pass

    # def test_login2(self):
    #     self.fangfa.SendKeysClass("ipt_username", "1")
    #     self.fangfa.SendKeysClass("ipt_password", "")
    #     self.fangfa.ClickClass("login_btn")
    #     self.fangfa.TimeSleep(2)
    #     self.msg = self.fangfa.FindClass("error_tips")
    #     self.message = self.msg.text
    #     self.assertEqual(self.message, u"请输入密码")
    #     pass
    # def test_login3(self):
    #     self.fangfa.SendKeysClass("ipt_username", "1")
    #     self.fangfa.SendKeysClass("ipt_password", "1")
    #     self.fangfa.ClickClass("login_btn")
    #     self.fangfa.TimeSleep(2)
    #     self.msg = self.fangfa.FindClass("error_tips")
    #     self.message = self.msg.text
    #     self.assertEqual(self.message, u"账号和密码不匹配，请重新输入")
    #     pass
    # def test_login4(self):
    #     self.fangfa.SendKeysClass("ipt_username", "15712959187")
    #     self.fangfa.SendKeysClass("ipt_password", "ylg09051915")
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("login_btn")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.msg=self.fangfa.FindClass("hd_login_name")
    #     self.message=self.msg.text
    #     self.fangfa.TimeSleep(2)
    #     self.assertEqual(self.message,"dalian66666")
    #     pass

    # def test_login5(self):
    #     self.fangfa.ClickID("check_agreement")
    #     self.msg=self.fangfa.FindClass("auto_tips")
    #     self.message=self.msg.text
    #     self.assertEqual(self.message,u"请勿在公用电脑上启用")
    #     pass


    # def test_login6(self):
    #     self.fangfa.ClickClass("unfold")
    #     self.fangfa.TimeSleep(1)
    #     self.msg=self.fangfa.FingXpath("/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[1]/a")
    #     self.message=self.msg.text
    #     print self.message
    #     self.assertEqual(self.message,u"支付宝")
    #     pass
    # def test_login7(self):
    #     self.fangfa.ClickClass("unfold")
    #     self.fangfa.TimeSleep(1)
    #     self.msg = self.fangfa.FingXpath("/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[2]/a")
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"网易")
    #     pass
    # def test_login8(self):
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("unfold")
    #     self.fangfa.ClickXpath("/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[1]/a")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.fangfa.TimeSleep(1)
    #     self.title=self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title,u"支付宝快捷登录")
    #     pass
    # def test_login9(self):
    #     self.current = self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("unfold")
    #     self.fangfa.ClickXpath("/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[2]/a")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.fangfa.TimeSleep(1)
    #     self.title = self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title, u"网易账号中心")
    #     pass
    # def test_login10(self):
    #     self.current = self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("unfold")
    #     self.fangfa.ClickXpath("/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[3]/a")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.fangfa.TimeSleep(1)
    #     self.title = self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title, u"与百度连接")
    #     pass
    # def test_login11(self):
    #     self.current = self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("unfold")
    #     self.fangfa.ClickXpath("/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[4]/a")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.fangfa.TimeSleep(1)
    #     self.title = self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title, u"与人人连接")
    #     pass
    # def test_login12(self):
    #     self.current = self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("unfold")
    #     self.fangfa.ClickXpath("/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[5]/a")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.fangfa.TimeSleep(1)
    #     self.title = self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title, u"万里通登录")
    #     pass

    # def test_zhuce1(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.switch_to_window(self.current)
    #     self.message=self.fangfa.getTitle()
    #     print self.message
    #     self.assertEqual(self.message,u"注册1号店")
    #     pass
    # def test_zhuce2(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.SendKeysID("userName","")
    #     self.fangfa.SendKeysID("phone","")
    #     self.fangfa.SendKeysID("validPhoneCode","")
    #     self.fangfa.SendKeysID("password","")
    #     self.fangfa.SendKeysID("password2","")
    #     self.fangfa.ClickID("register_button")
    #     self.msg=self.fangfa.FindClass("y_tips_words")
    #     self.message=self.msg.text
    #     self.assertEqual(self.message,u"格式错误，请输入正确的用户名")
    #     pass
    # def test_zhuce3(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.SendKeysID("userName", "dalian")
    #     self.fangfa.SendKeysID("phone", "1")
    #     self.fangfa.SendKeysID("validPhoneCode", "")
    #     self.fangfa.SendKeysID("password", "")
    #     self.fangfa.SendKeysID("password2", "")
    #     self.fangfa.ClickID("register_button")
    #     self.msg = self.fangfa.FingXpath("//li[@class='ifocus ipt_wrong']/div[2]")
    #     self.fangfa.TimeSleep(3)
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"格式错误，请输入正确的手机号")
    #     pass
    # def test_zhuce4(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.SendKeysID("userName", "dalian678678")
    #     self.fangfa.SendKeysID("phone", "13234117830")
    #     self.fangfa.SendKeysID("validPhoneCode", "")
    #     self.fangfa.SendKeysID("password", "")
    #     self.fangfa.SendKeysID("password2", "")
    #     self.fangfa.ClickID("register_button")
    #     self.msg = self.fangfa.FingXpath("//li[@class='ipt_wrong ifocus']/div[2]")
    #     self.fangfa.TimeSleep(3)
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"密码不能为空")
    #     pass
    # def test_zhuce5(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.SendKeysID("userName", "dalian678678")
    #     self.fangfa.SendKeysID("phone", "13234117830")
    #     self.fangfa.SendKeysID("validPhoneCode", "")
    #     self.fangfa.SendKeysID("password", "1")
    #     self.fangfa.SendKeysID("password2", "")
    #     self.fangfa.ClickID("register_button")
    #     self.msg = self.fangfa.FingXpath("//li[@class='ipt_wrong ifocus']/div[2]")
    #     self.fangfa.TimeSleep(3)
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"密码应为6-20位字符")
    #     pass
    # def test_zhuce6(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.SendKeysID("userName", "dalian678678")
    #     self.fangfa.SendKeysID("phone", "13234117830")
    #     self.fangfa.SendKeysID("validPhoneCode", "")
    #     self.fangfa.SendKeysID("password", "123456")
    #     self.fangfa.SendKeysID("password2", "")
    #     self.fangfa.ClickID("register_button")
    #     self.msg = self.fangfa.FingXpath("//li[@class='ipt_wrong ifocus']/div[2]")
    #     self.fangfa.TimeSleep(3)
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"密码不能全为数字")
    #     pass
    # def test_zhuce7(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.SendKeysID("userName", "dalian678678")
    #     self.fangfa.SendKeysID("phone", "13234117835")
    #     self.fangfa.SendKeysID("validPhoneCode", "")
    #     self.fangfa.SendKeysID("password", "ylg123")
    #     self.fangfa.SendKeysID("password2", "")
    #     self.fangfa.ClickID("register_button")
    #     self.msg = self.fangfa.FingXpath("//li[@class='ipt_wrong ifocus']/div[2]")
    #     self.fangfa.TimeSleep(3)
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"该手机号已存在，登录")
    # def test_zhuce8(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.SendKeysID("userName", "dalian678678")
    #     self.fangfa.SendKeysID("phone", "18886666888")
    #     self.fangfa.SendKeysID("validPhoneCode", "")
    #     self.fangfa.SendKeysID("password", "ylg123")
    #     self.fangfa.SendKeysID("password2", "")
    #     self.fangfa.ClickID("register_button")
    #     self.msg = self.fangfa.FingXpath("/html/body/div[2]/div[6]/div/ul/li[6]/div[2]/div/div")
    #     self.fangfa.TimeSleep(3)
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"两次密码输入不一致")
    # def test_zhuce9(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(5)
    #     self.fangfa.SendKeysID("userName", "dalian678678")
    #     self.fangfa.SendKeysID("phone", "18812345678")
    #     self.fangfa.SendKeysID("validPhoneCode", "")
    #     self.fangfa.SendKeysID("password", "ylg123")
    #     self.fangfa.SendKeysID("password2", "ylg123")
    #     self.fangfa.ClickID("register_button")
    #     self.msg = self.fangfa.FingXpath("//*[@id='validPhoneCodeDiv']/div[2]/div/div")
    #     self.fangfa.TimeSleep(3)
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"请输入6位短信验证码")
    #     pass
    # def test_zhuce10(self):
    #     self.fangfa.ClickClass("regist_new")
    #     self.fangfa.TimeSleep(3)
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("y_agreement_word")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.title=self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title,u"服务协议及隐私声明-1号店帮助中心")
    # def test_wangji1(self):
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("forget_pswd")
    #     self.fangfa.TimeSleep(3)
    #     self.fangfa.switch_to_window(self.current)
    #     self.title=self.fangfa.getTitle()
    #     self.assertEqual(self.title,u"找回密码")
    # def test_wangji2(self):
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("forget_pswd")
    #     self.fangfa.TimeSleep(3)
    #     self.fangfa.switch_to_window(self.current)
    #     self.fangfa.ClickClass("y_agreement_btn")
    #     self.fangfa.TimeSleep(2)
    #     self.msg=self.fangfa.FingXpath("/html/body/div[2]/div[2]/div/ul/li[1]/div[2]/div/div")
    #     self.message=self.msg.text
    #     print self.message
    #     self.assertEqual(self.message,u"请输入您的账号")
    #     pass
    # def test_wangji3(self):
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("forget_pswd")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.fangfa.SendKeysClass("ysame_input","13234117888")
    #     self.fangfa.ClickClass("y_agreement_btn")
    #     self.fangfa.TimeSleep(2)
    #     self.msg=self.fangfa.FindClass("receive_code")
    #     self.message=self.msg.text
    #     print self.message
    #     self.assertEqual(self.message,u"获取验证码")
    #     pass
    # def test_wangji4(self):
    #     self.current = self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("forget_pswd")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.fangfa.SendKeysClass("ysame_input", "1323411788")
    #     self.fangfa.ClickClass("y_agreement_btn")
    #     self.fangfa.TimeSleep(1)
    #     self.msg = self.fangfa.FingXpath("/html/body/div[2]/div[2]/div/ul/li[1]/div[2]/div/div")
    #     self.message = self.msg.text
    #     print self.message
    #     self.assertEqual(self.message, u"您输入的账户名不存在")
    #     pass
    # def test_bangzhu1(self):
    #     self.current=self.fangfa.getCurrent_window()
    #     self.fangfa.ClickClass("hd_menu")
    #     self.fangfa.TimeSleep(2)
    #     self.fangfa.switch_to_window(self.current)
    #     self.title=self.fangfa.getTitle()
    #     print self.title
    #     self.assertEqual(self.title,u"购物流程-1号店帮助中心")
    #     pass



    #firefox报错：AttributeError: 'FireFox' object has no attribute 'w3c'可以使用Chrome浏览器
    # def test_bangzhu2(self):
    #     ele = self.fangfa.FindLink("帮助中心")
    #     ActionChains(self.fangfa).move_to_element(ele).perform()
    #     self.fangfa.ClickXpath("/html/body/div[1]/div/div/div/div/ul/li[1]/a")






    # def test_login4(self):
    #     # 获取当前窗口
    #     self.current=self.fangfa.getCurrent_window()
    #     #点击联系我们
    #     self.fangfa.ClickLink("联系我们")
    #     # 切换窗口
    #     self.fangfa.switch_to_window(self.current)
    #     #获取title
    #     self.title=self.fangfa.getTitle()
    #     #断言
    #     self.assertEqual(self.title, u"联系我们")
    #
    #
    #     pass






