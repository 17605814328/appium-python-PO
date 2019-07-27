# -*- coding: utf-8 -*-
'''
@author: Y_哦耶
Project: 基于page objects的appium+python自动化测试框架
'''

TIP:
1.在项目使用前要把整个项目路径添加到用户环境变量PYTHONPATH中，以便模块的引入
2.加入用户环境变量PYTHONDONTWRITEBYTECODE=1  让项目启动时不生产__pycache__文件夹
3.如果要让某个测试用例先执行，不能使用默认的main()方法，需要通过TestSuite类的addTest（）方法按照一定的顺序来加载

框架结构介绍：
data：测试数据,后期准备把代码中会所有测试数据都整合到excel.
src：元素定位及页面(都基于basePage)
 |—— common: 存放封装的公共方法
public：一些公共的方法，比如生成测试报告脚本，封装好的
result：测试结果，存放所有的测试报告和错误截图
Test_Case：存放所有测试用例
run_case.py：测试套件，利用HTMLTestRunner,输出测试报告到result下


代码规范：
1.函数或者变量命名要遵循驼峰命名法，首字母小写
2.定义一个类时，首字母要大写
3.写代码时需勤加注释，便于后期维护
