# -*- coding: utf-8 -*-
'''
@author: Y_哦耶
explain: 启动Test_Case下所有测试用例，并生成HTML报告
'''

import unittest
from public import HTMLTestRunner
import time
import os

case_path = ".\\Test_Case"
result = ".\\result\\"

def Creatsuite():
    #定义单元测试容器
    testunit = unittest.TestSuite()

    #定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='Test_*.py', top_level_dir=None)

    #将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
    return testunit

test_case = Creatsuite()

#获取系统当前时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

#定义个报告存放路径，支持相对路径
tdresult = result + day
if os.path.exists(tdresult):
    filename = tdresult + "\\" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Appium测试报告', description=u'用例详情：')

    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件
else:
    os.mkdir(tdresult)
    filename = tdresult + "\\" + now + "_result.html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'Appium测试报告', description=u'用例详情：')

    #运行测试用例
    runner.run(test_case)
    fp.close()  #关闭报告文件
