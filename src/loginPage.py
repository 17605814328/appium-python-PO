# -*- coding: utf-8 -*-
'''
@author: Y_哦耶
explain: 登录测试套件
'''

from src.common.basePage import Base
from selenium.webdriver.common.by import By

# 定义登录页面类，父类是Base
class LoginPage(Base):
    h5_loc = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView"

    myBtn_loc = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.FrameLayout/android.widget.Button"

    msgLogin_loc = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]"

    pwdLogin_loc = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]"

    username_loc = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.EditText"

    pwd_loc = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.EditText"

    loginBtn_loc = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.Button"


    def login_in(self, username, password):
        #关闭H5浮层
        self.click(20, 0.1, By.XPATH, self.h5_loc)
        #点击我的按钮
        self.click(20, 0.1, By.XPATH, self.myBtn_loc)
        #点击短信登录
        self.click(20, 0.1, By.XPATH, self.msgLogin_loc)
        #收起手机键盘
        self.driver.hide_keyboard()
        #点击密码登录按钮
        self.click(20, 0.1, By.XPATH, self.pwdLogin_loc)
        #输入用户名
        self.send_keys(10, 0.1, By.XPATH, self.username_loc, username)
        #输入密码
        self.send_keys(10, 0.1, By.XPATH, self.pwd_loc, password)
        #点击登录按钮
        self.click(20, 0.1, By.XPATH, self.loginBtn_loc)



