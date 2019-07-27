# -*- coding: utf-8 -*-
'''
@author: Y_哦耶
explain: 公共元素与方法封装
'''

from selenium.webdriver.common.by import By #元素定位的封装类
from selenium.webdriver.support.ui import WebDriverWait #显醒等待
from selenium.webdriver.support import expected_conditions as EC  #场景判断方法封装类
import time

class Base:
    #初始化方法（当一个类起到模板的作用时，必须先实例化本身）
    def __init__(self,driver):
        self.driver=driver

    # 重写元素定位方法
    def find_element(self,timeout,poll_frequency,type,*loc):
        try:
            element=WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located((type,*loc)))
            return element
        except:
            timestr = time.strftime("%Y-%m-%d_%H_%M_%S")#定义截图名称即时间戳，字符串类型
            self.driver.get_screenshot_as_file(".\\result\\\screenshot_"+timestr+".png")

	# 重写多元素定位方法
    def find_elements(self,timeout,poll_frequency,index,type,*loc ):
        try:
            elements = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_all_elements_located((type, *loc)))
            return elements[index]
        except:
            timestr = time.strftime("%Y-%m-%d_%H_%M_%S")#定义截图名称即时间戳，字符串类型
            self.driver.get_screenshot_as_file(".\\result\\\screenshot_"+timestr+".png")
		
    # 重写定义send_keys方法
    def send_keys(self,timeout,poll_frequency,type,loc,value):
        try:
                self.find_element(timeout,poll_frequency,type,loc).clear()
                return self.find_element(timeout,poll_frequency,type,loc).send_keys(value)
        except AttributeError:
            print("%s 页面中未能找到 %s 元素" % (self,loc))
            timestr = time.strftime("%Y-%m-%d_%H_%M_%S")#定义截图名称即时间戳，字符串类型
            self.driver.get_screenshot_as_file(".\\result\\\screenshot_"+timestr+".png")

    # 重写定义click方法
    def click(self,timeout,poll_frequency,type,*loc):
        try:
            return self.find_element(timeout,poll_frequency,type,*loc).click()
        except:
            timestr = time.strftime("%Y-%m-%d_%H_%M_%S")#定义截图名称即时间戳，字符串类型
            self.driver.get_screenshot_as_file(".\\result\\\screenshot_"+timestr+".png")
    
    # 定义向上滑动方法
    def swipe_up(self,t=500,n= 1):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.75 # 起点y坐标
        y2 = s['height'] * 0.25 # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1,y1,x1,y2,t)

    # 每20S向上滑动
    def while_true(self):
        for i in (1,10):
            self.swipe_up()
            time.sleep(20)