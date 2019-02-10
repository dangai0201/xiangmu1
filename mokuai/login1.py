#-*-coding:utf-8-*-


from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains包





#driver=webdriver.Chrome()
driver=webdriver.Firefox()
driver.maximize_window()

#鼠标悬浮的方法，Chrome适用的


#driver.get("http://www.yhd.com")

driver.get("http://search.yhd.com/c0-0/kiphone/")
# i=0
# for i in range(50):
#     time.sleep(5)
#     js = "var q=document.documentElement.scrollTop=1000000"
#     driver.execute_script(js)
#     time.sleep(5)
#     js = "var q=document.documentElement.scrollTop=1000000"
#     driver.execute_script(js)
#     time.sleep(5)
#     driver.find_element_by_class_name("page_next").click()



#driver.get("https://passport.yhd.com/passport/login_input.do?returnUrl=http%3A%2F%2Fhome.yhd.com%2Forder%2FtoOrderList.do")
# driver.current=driver.current_window_handle
# ele=driver.find_element_by_link_text("帮助中心")
# ActionChains(driver).move_to_element(ele).perform()
# driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/ul/li[1]/a").click()
# allwindows=driver.window_handles
# for window in allwindows:
#     if window != driver.current:
#         driver.switch_to_window(window)
# title=driver.title
# print title
#进度条滚动
#2
# js="var q=document.documentElement.scrollTop=1000"
# driver.execute_script(js)
#滚动到最底部的方法
# js="var q=document.documentElement.scrollTop=1000000"
# driver.execute_script(js)
#
#
# time.sleep(5)
#
# js="var q=document.documentElement.scrollTop=1000000"
# driver.execute_script(js)

# target = driver.find_element_by_id('footer')
# driver.execute_script("arguments[0].scrollIntoView();", target)


# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



#3
#driver.find_element_by_class_name("buy_btn6").click()

#driver.find_element_by_class_name("hd_search_ipt").send_keys("iphone")
# self.fangfa.SendKeysClass("hd_search_ipt", "iphone")
#         self.fangfa.TimeSleep(2)
#         self.fangfa.ClickClass("hd_search_btn")
#         self.fangfa.TimeSleep(2)
#         self.fangfa.ClickID("pdlink1_100000177760")
#         self.fangfa.FindClass("buy_btn6 btn_init_class").click()
#         self.fangfa.TimeSleep(2)





# import os,time
# import pyautogui as pag
# try:
#     while True:
#             print("Press Ctrl-C to end")
#             x,y = pag.position() #返回鼠标的坐标
#             posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
#             print (posStr)#打印坐标
#             time.sleep(0.2)
#             os.system('cls')#清楚屏幕
# except  KeyboardInterrupt:
#     print ('end....')



