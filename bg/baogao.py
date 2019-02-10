#-*-coding:utf-8-*-
#导入单元测试
import unittest
#导入单元测试类
from mokuai import login

#导入自动化测试报告
import HTMLTestRunner
#导入os包
import os
# 导入os包
import os
import unittest

# 导入自动化测试报告
import HTMLTestRunner

# 导入单元测试类
from mokuai import login
from mokuai import shop

#实例化suit
suit=unittest.TestSuite()
#将单元测试介入到套件里面
suit.addTest(unittest.makeSuite(login.Login))
suit.addTest(unittest.makeSuite(shop.Shop))

#指定自动化测试报告路径
files=os.getcwd()+"/项目.html"
#指定读写方式wb 以二进制的方式写入rb 以二进制的方式读取rb 以二进制的方式既可以读又可以写
filename=open(files,'wb')
#运行自动化测试报告
runner=HTMLTestRunner.HTMLTestRunner(stream=filename,title=u"项目",description=u"这是一个项目模块")
runner.run(suit)
