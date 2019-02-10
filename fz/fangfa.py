#-*-coding:utf-8-*-
from selenium import webdriver
import time
from enum import Enum
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import  By
#引入ActionChains包
from selenium.webdriver.common.action_chains import ActionChains

#定义继承单元测试
class FireFox(object):
    #打开浏览器
    def fire_start(self,url):
        #打开火狐浏览器
        self.driver=webdriver.Firefox()
        #设置最大化
        self.driver.maximize_window()

        #指定网站
        self.driver.get(url)
        #设置休眠
        self.TimeSleep(ENUM.FIVE_TIME)
        pass
    #静态休眠
    def TimeSleep(self,number):
        time.sleep(number)
        pass
    #隐士休眠
    def TimeImplay(self,number):
        # sleep()： 强制等待，设置固定休眠时间。 python的time包提供了休眠方法sleep() ， 导入time包后就可以使用sleep()，进行脚本的执行过程进行休眠。
        # implicitly_wait()：隐石等待，也叫智能等待，是webdirver提供的一个超时等待。隐的等待一个元素被发现，或一个命令完成。如果超出了设置时间的则抛出异常。
        # WebDriverWait()：显示等待，同样也是webdirver提供的方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。
        # 默认检测频率为0.5s，默认抛出异常为：NoSuchElementException
        self.driver.implicitly_wait(number)
        pass
    #关闭浏览器
    def firefox_close(self):
        self.driver.quit()
        pass


    #移动到新人有礼位置
    def firefox_yidong(self):
        self.TimeSleep(2)
        js = "var q=document.documentElement.scrollTop=400"
        self.driver.execute_script(js)

    #移动到最底部
    def fifefox_bottom(self):
        self.TimeSleep(2)
        js = "var q=document.documentElement.scrollTop=1000000"
        self.driver.execute_script(js)
        time.sleep(5)
        js = "var q=document.documentElement.scrollTop=1000000"
        self.driver.execute_script(js)






        #1.查找控件的方式
    def FindID(self,ID):
        ids=(By.ID,ID)
        #使用显示休眠，义工休眠20s，每隔0.5s休眠一次
        WebDriverWait(self.driver,ENUM.TWENTY_TIME,ENUM.ONE_HALF).until(EC.presence_of_all_elements_located(ids))
        return  self.driver.find_element_by_id(ID)
    def ClickID(self,ID):
        self.FindID(ID).click()
        pass
    def SendKeysID(self,ID,message):
        self.FindID(ID).send_keys(message)
        pass


    #2种
    def FindName(self, name):
        # 使用显示休眠，一共休眠20秒，每个0.5秒休眠一次
        names = (By.NAME, name)
        # 休眠
        WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ONE_HALF).until(EC.presence_of_element_located(names))
        return self.driver.find_element_by_name(name)
        # 根据id设置点击事件A

    def ClickName(self, name):
        self.FindName(name).click()
        # 输入内容

    def SendKeyName(self, name, message):
        self.FindName(name).send_keys(message)

    # 3种
    def FindClass(self, cls):
        clss = (By.CLASS_NAME, cls)
        WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ONE_HALF).until(EC.presence_of_element_located(clss))
        return self.driver.find_element_by_class_name(cls)

    def ClickClass(self, cls):
        self.FindClass(cls).click()

    def SendKeysClass(self, cls, message):
        self.FindClass(cls).send_keys(message)

    # 4种
    def FingXpath(self, xpath):
        xpaths = (By.XPATH, xpath)
        WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ONE_HALF).until(EC.presence_of_element_located(xpaths))
        return self.driver.find_element_by_xpath(xpath)

    def ClickXpath(self, xpath):
        self.FingXpath(xpath).click()

    def SendKeyxpath(self, xpath, message):
        self.FingXpath(xpath).send_keys(message)

    # 5种
        # 通过内容实现显示休眠
    def TimeLink(self, message):
        # 检查元素
        msg = (By.LINK_TEXT, message)
        # 设置休眠
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(msg))
        pass


    def FindLink(self, link):
        links = (By.LINK_TEXT, link)
        WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ONE_HALF).until(EC.presence_of_element_located(links))
        return self.driver.find_element_by_link_text(link)

    def ClickLink(self, link):
        self.FindLink(link).click()

    def SendkeyLink(self, link, message):
        self.FindLink(link).send_keys(message)

    # 6种
    def FindPaty(self, link):
        links = (By.PARTIAL_LINK_TEXT, link)
        WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ONE_HALF).until(EC.presence_of_element_located(links))
        return self.driver.find_element_by_partial_link_text(link)

    def ClickPart(self, link):
        self.FindPaty(link).click()

    def SendKeysPart(self, link, msg):
        self.FindPaty(link).send_keys(msg)

    # 7种
    def FindTag(self, tag):
        tags = (By.TAG_NAME, tag)
        WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ONE_HALF).until(EC.presence_of_element_located(tags))
        return self.driver.find_element_by_tag_name(tag)

    def ClickTag(self, tag):
        self.FindTag(tag).click()

    def SendkeysTag(self, tag, msg):
        self.FindTag(tag).send_keys(msg)

    # 8种
    def FindCss(self, css):
        csss = (By.CSS_SELECTOR, css)
        WebDriverWait(self.driver, ENUM.TWENTY_TIME, ENUM.ONE_HALF).until(EC.presence_of_element_located(csss))
        return self.driver.find_element_by_css_selector(css)

    def ClickCss(self, css):
        self.FindTag(css).click()

    def SendkeysCss(self, css, msg):
        self.FindCss(css).send_keys()





     #获取title
    def getTitle(self):
        return  self.driver.title
    #获取当前窗口
    def getCurrent_window(self):
        return self.driver.current_window_handle
    #切换窗口的方法
    def switch_to_window(self,current):
        #获取所有窗口
        allwindows=self.driver.window_handles
        #使用for循环进行切换
        for window in allwindows:
            if window !=current:
                self.driver.switch_to_window(window)





    #设置点击事件，以及切换窗口的封装
    def ClickID_Window(self,ID):
        #获取当前窗口
        current_window=self.getCurrent_window()
        #进行点击
        self.ClickID(ID)
        #休眠5秒
        self.TimeSleep(ENUM.FIVE_TIME)
        #切换窗口
        self.switch_to_window(current_window)

    def ClickName_window(self, name):
        current_window = self.getCurrent_window()
        self.ClickName(name)
        self.Timesleep(ENUM.FIVE_TIME)
        self.switch_to_window(current_window)

    def ClickClass_Window(self, cls):
        current_window = self.getCurrent_window()
        self.ClickClass(cls)
        self.TimeSleep(ENUM.FIVE_TIME)
        self.switch_to_window(current_window)

    def ClickXpath_Window(self, xpath):
        current_window = self.getCurrent_window()
        self.ClickXpath(xpath)
        self.TimeSleep(ENUM.FIVE_TIME)
        self.switch_to_window(current_window)

    def ClickTag_Window(self, tag):
        current_window = self.getCurrent_Window()
        self.ClickTag(tag)
        self.TimeSleep(ENUM.FIVE_TIME)
        self.switch_to_window(current_window)

    def ClickCss_Window(self, css):
        current_window = self.getCurrent_Window()
        self.ClickCss(css)
        self.TimeSleep(ENUM.FIVE_TIME)
        self.switch_to_window(current_window)

    def ClickLink_Window(self, link):
        current_window = self.getCurrent_Window()
        self.ClickLink(link)
        self.TimeSleep(ENUM.FIVE_TIME)
        self.switch_to_window(current_window)

    def ClickPart_Window(self, part):
        current_window = self.getCurrent_Window()
        self.ClickPart(part)
        self.TimeSleep(ENUM.FIVE_TIME)
        self.switch_to_window(current_window)

    def ClickPart_Window(self, part):
        current_window = self.getCurrent_Window()
        self.ClickPart(part)
        self.TimeSleep(ENUM.FIVE_TIME)
        self.switch_to_window(current_window)


 # 通过js定位当前窗口
    def switch_to_view_js_ID(self,ID):
        # 执行 js
        self.driver.execute_script("arguments[0].scrollintoView()",ID)
        pass
    def switch_to_view_js_Name(self,name):
        self.driver.execute_script("arguments[0].scrollintoView()",name)
        pass

    def switch_to_view_js_Class(self, cls):
        self.driver.execute_script("arguments[0].scrollintoView()",cls)
        pass

    def switch_to_view_js_Xpath(self, xpath):
        # 执行 js
        self.driver.execute_script("arguments[0].scrollintoView()", xpath)

        pass
    def switch_to_view_js_Tag(self, tag):
        self.driver.execute_script("arguments[0].scrollintoView()", tag)
        pass

    def switch_to_view_js_css(self, css):
        self.driver.execute_script("arguments[0].scrollintoView()", css)
        pass

    def switch_to_view_js_link(self, link):
        # 执行 js
        self.driver.execute_script("arguments[0].scrollintoView()", link)

        pass

    def switch_to_view_js_part(self, part):
        # 执行 js
        self.driver.execute_script("arguments[0].scrollintoView()", part)

        pass
    # 切换到frame ID
    def seitch_to_id_frame(self,ID):

        # 切换到frame里面
        self.driver.switch_to.frame(self.FindID(ID))
        # 注意 pass没有任何意义,只是在写代码的时候怕报错,用来占位的
        pass
 # 切换到frame Name
    def seitch_to_name_frame(self, name):
        # 切换到frame里面
        self.driver.switch_to.frame(self.FindName(name))
        # 注意 pass没有任何意义,只是在写代码的时候怕报错,用来占位的
        pass

    # 切换到frame Class
    def seitch_to_class_frame(self, cls):
        # 切换到frame里面
        self.driver.switch_to.frame(self.FindClass(cls))
        # 注意 pass没有任何意义,只是在写代码的时候怕报错,用来占位的
        pass

    # 切换到frame xpath
    def seitch_to_xpath_frame(self, xpath):
        # 切换到frame里面
        self.driver.switch_to.frame(self.FindXpath(xpath))
        # 注意 pass没有任何意义,只是在写代码的时候怕报错,用来占位的
        pass

    # 切换到frame tag
    def seitch_to_tag_frame(self, tag):
        # 切换到frame里面
        self.driver.switch_to.frame(self.FindTag(tag))
        # 注意 pass没有任何意义,只是在写代码的时候怕报错,用来占位的
        pass

    # 切换到frame tag
    def seitch_to_css_frame(self, css):
        # 切换到frame里面
        self.driver.switch_to.frame(self.FindCss(css))
        # 注意 pass没有任何意义,只是在写代码的时候怕报错,用来占位的
        pass






    # 封装断言, 查找控件,获取内容,断言前后是不是一致
    def AssertEqualClass(self,self1,cls,expect):

        # 查找控件,获取内容
        self.message = self.FindClass(cls).text
        # 进行断言
        self1.assertEqual(self.message,expect)

        pass

    # 通过 title去断言
    def AssertEquilTitle(self,self1,expect):

        # 设置休眠,在这里使用强制等待
        self.TimeSleep(ENUM.FIVE_TIME)
        # 查找控件,获取内容
        self.message = self.getTitle()
        # 进行断言
        self1.assertEqual(self.message,expect)

        pass

    # 断言数量
    def AssertEquilCount(self,self1,cls,number):

        # 查询一组控件,进行断言
        clses = self.FindClasses(cls)

        # 进行断言
        self1.assertEqual(len(clses), number)

        pass

    # 断言控件是不是可见
    def AssertTrueID(self,self1,ID):

        # 设置休眠 给网络请求或者逻辑判断的加载时间
        self.TimeSleep(ENUM.FIVE_TIME)
        # 进行断言
        self1.assertTrue(self.FindID(ID).is_displayed())
        pass








# 通过 class 查询一组列表的元素
    def FindClasses(self,cls):

        # 查询cls
        clss = (By.CLASS_NAME,cls)

        # 设置休眠,同时检查元素的存在
        WebDriverWait(self.driver,ENUM.TWENTY_TIME,ENUM.ONE_HALF).until(EC.presence_of_element_located(clss))

        # 返回查找控件的数量
        return self.driver.find_elements_by_class_name(cls)

    # 通过指定下标进行点击的
    def ClickClasses(self,cls,index):

        # 进行点击
        self.FindClasses(cls)[index].click()


    # 查询一组切换窗口的方法
    def ClickWindowClsses(self,cls,index):

        # 获取当前窗口
        current = self.driver.current_window_handle
        # 查询一组控件,进行点击
        self.ClickClasses(cls,index)
        # 设置休眠 这里设置休眠的原因是 1: 有的电脑反应慢,点击完成以后,一会才跳转,而我们的代码执行的比较快,所以需要进行休眠一会再获取所有窗口,不然获取的窗口只有一个
        # 2: 我们点击完成以后,这里一般有逻辑判断,需要请求网络加载数据需要时间,所以需要休眠
        # 使用强制休眠 设置休眠时间
        self.TimeSleep(ENUM.FIVE_TIME)
        # 获取所有的窗口
        all_window = self.switch_to_window(current)


















class ENUM(Enum):
    TWO_TIME=2
    FIVE_TIME=5
    TEN_TIME=10
    TWENTY_TIME=20
    ONE_HALF=0.5