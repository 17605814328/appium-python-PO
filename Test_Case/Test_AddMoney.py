# -*- coding: utf-8 -*-
'''
@author: Y_哦耶
explain: 自动加金币测试用例
'''

import unittest
from config.driverConfig import DriverConfig
from src.loginPage import LoginPage
from src.autoAddMoney import AutoAddMoney

class AddMoney(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  #必须使用@classmethod 装饰器,所有case运行之前只运行一次
        driver = DriverConfig.get_driver()
        cls.driver = driver

    def setUp(self):  #每个测试case运行之前运行
        self.LoginPage = LoginPage(self.driver)
        self.AutoAddMoney = AutoAddMoney(self.driver)

    def test_1(self):
        # 登录
        u'测试登录'
        self.LoginPage.login_in("17605814328", "1122334455")

    def test_2(self):
        # 加金币
        u'测试加金币'
        self.AutoAddMoney.add_money()

    def tearDown(self):  #每个测试case运行完之后执行
        pass

    @classmethod
    def tearDownClass(cls):  #必须使用@classmethod装饰器,所有case运行完之后只运行一次
        cls.driver.quit()

if __name__ =="__main__":
    suite = unittest.TestSuite()
    suite.addTest(AddMoney('test_1'))
    suite.addTest(AddMoney('test_2'))
    runner = unittest.TextTestRunner()
    runner.run(suite)



