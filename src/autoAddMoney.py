# -*- coding: utf-8 -*-
'''
@author: Y_哦耶
explain: 登录测试套件
'''

from src.common.basePage import Base
from selenium.webdriver.common.by import By

# 定义登录页面类，父类是Base
class AutoAddMoney(Base):
    smallVideo_loc = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.FrameLayout[1]/android.widget.Button"

    def add_money(self):
        #点击小视频菜单栏
        self.click(20, 0.1, By.XPATH, self.smallVideo_loc)
        #调用循环十次的方法
        self.while_true()




