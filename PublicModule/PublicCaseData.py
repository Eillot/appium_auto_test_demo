#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from PublicModule.ConfigurationData import *
sys.path.append(os.path.abspath('%s../../' % sys.path[0]))


"""
@version: python2.7.11
@Author  : Simon
@Explain : 静态数据引用配置
@contact:
@Time    : 17-10-18 下午4:45
@File    : PiblicCaseData
@Software: PyCharm
"""

#--------------------------------用户Ui自动化测试常量数据---------------------------------------
url_webdriver_remote = userAppHost3 +"/wd/hub" #appium client端连接appium server端的远程地址（注：目的是向appium server端提交json文件，告诉appium server连接设备的信息)

#anroid设备的信息
"""
是否支持混合应用: 支持。请移步至hybrid doc参考相关文档。
通过默认的Appium的后台支持android 4.4以上的版本。
通过Selendroid的后台支持android 2.3以上的版本。
是否支持在同一个session中执行多个应用的自动化：支持（但是不支持使用Selendroid后台的场景）。
是否支持同时再多个设备上执行自动化：支持。
尽管Appium必须要启动另一个端口即通过添加参数的方式运行命令行，
例如--port，--bootstrap-port（或者--selendroid-port）或者--chromedriver-port。更多详情请移步至server args doc。
是否支持第三方应用自动化：支持（但是不支持Selendroid后台运行的场景）。
是否支持自定义的、非标准UI控件的自动化：不支持。

摘自：Android平台支持 http://appium.io

结论：
使用appium模式做Ui自动化测试只支持android 4.4（包括4.4）及以上的版本，
若想做android系统低于4.4的Ui自动化可以使用Selendroid模式
"""
android_appium_platform_name="Android" #设备名称
android_appium_platform_version={"v_4.4":"4.4","v_5.0":"5.0","v_5.1":"5.1","v_6.0":"6.0","v_7.0":"7.0"} #定义为字典保存android系统版本
android_appium_device_name = "Android Emulator" #默认值为android模拟器，若使用真机则使用真机设备名称
android_appium_app = "" #当前项目目录下保存app的绝对路径
url_webwebdriver_remote = "http://127.0.0.1:4723/wd/hub" #向本地appium server发送http请求的地址
android_appium_newcommand_timeout = 240 #请求超时时间

#ios设备的信息
