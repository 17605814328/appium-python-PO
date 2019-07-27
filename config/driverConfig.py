# -*- coding: utf-8 -*-
'''
@author: Y_哦耶
explain: 驱动配置
'''

from appium import webdriver
import time

# appium远程启动app
# 定义获取驱动方法
class DriverConfig:
    def get_driver():
        try:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'  # 设备系统
            desired_caps['platformVersion'] = '8.1.0'  # 设备系统版本
            desired_caps['deviceName'] = 'b598dcb0'  # 设备名称
            desired_caps['appPackage'] = 'com.jifen.qukan'  # 获取包名
            desired_caps['appActivity'] = 'com.jifen.qkbase.main.MainActivity'  # 获取activity启动
            driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
            time.sleep(5)  # 等待5秒
            return driver
        except Exception as e:
            raise e
