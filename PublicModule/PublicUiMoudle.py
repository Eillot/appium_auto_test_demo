#!/usr/bin/env python
# encoding: utf-8

import os
import sys
from appium import webdriver
from PublicModule.PublicCaseData import *
sys.path.append(os.path.abspath('%s../../' % sys.path[0]))

"""
@version: python2.7.11
@Author  : Simon
@Explain : 公用的类用于封装Ui自动化测试的通用方法---参考地址：https://github.com/appium/python-client
@contact:
@Time    : 17-10-20 下午2:28
@File    : PublicUiMoudle
@Software: PyCharm
"""
#获取当前目录被测app的绝对路径
def get_abspath_apps(app):

    """
    :param app: str类型app名称
    :return: str类型的绝对路径
    """
    PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
    apps_abspath =PATH('../../apps/' + app)

    return apps_abspath

#创建appium客户端端传递给appium server端的json文件
def appium_desired_capabilities(platform_name=android_appium_platform_name,platform_version=android_appium_platform_version.get("v_4.4"),
                                   device_name=android_appium_device_name,app_abspath=get_abspath_apps("joytest_1.7.5.1.apk"),
                                   newcommand_timeout=android_appium_newcommand_timeout):

    """
    :param platform_name: 移动设备系统类型（anbdroid 或 ios）
    :param platform_version: 系统版本
    :param device_name:设备名称
    :param app_abspath: 当前目录下app的绝对路径
    :param newcommand_timeout: 连接appium server超时时间
    :return: json文件
    """
    desired_caps={}
    desired_caps["platformName"]=platform_name
    desired_caps["platformVersion"]=platform_version
    desired_caps["deviceName"]=device_name
    desired_caps["app"]=app_abspath
    desired_caps["newCommandTimeout"]=newcommand_timeout

    #返回json文件
    return desired_caps

#appium客户端向appium server发起http网络请求
def appium_send_request(desired_capabilities=appium_desired_capabilities(),appium_remote_url=url_webwebdriver_remote):

    #向appium server 发送
    pass

