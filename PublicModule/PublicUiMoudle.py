#!/usr/bin/env python
# encoding: utf-8


# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
def get_abspath_apps(app=android_hybrid_appname):

    """
    :param app: str类型app名称
    :return: str类型的绝对路径
    """
    PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))
    apps_abspath =PATH('../apps/' + app)

    return apps_abspath

#创建appium客户端传递给appium server端的json文件
def appium_desired_capabilities(app_launchactivity_name=android_app_launchactivity_name,app_package_name=android_app_package_name,
                                    automation_name=android_automation_name,platform_name=android_appium_platform_name,
                                    platform_version=android_appium_platform_version.get("v_6.0"),device_name=android_appium_device_name,
                                    app_abspath=get_abspath_apps("android_hybrid.apk"),newcommand_timeout=android_appium_newcommand_timeout):

    """
    :param platform_name: 移动设备系统类型（anbdroid 或 ios）
    :param platform_version: 系统版本
    :param device_name:设备名称
    :param app_abspath: 当前目录下app的绝对路径
    :param newcommand_timeout: 连接appium server超时时间
    :param automation_name: 自动化测试框架名称（appium 或者selendroid）
    :param app_package_name: app包名称
    :param app_launchactivity_name: 启动app默认activity
    :return: 提交给appium server端的json文件
    """
    desired_caps={}
    desired_caps["platformName"]=platform_name
    desired_caps["platformVersion"]=platform_version
    desired_caps["deviceName"]=device_name
    desired_caps["app"]=app_abspath
    desired_caps["newCommandTimeout"]=newcommand_timeout
    desired_caps["automationName"]=automation_name
    desired_caps["appPackage"]=app_package_name
    desired_caps["appActivity"]=app_launchactivity_name


    #返回json文件
    return desired_caps

#appium客户端向appium server发起http网络请求
def appium_send_request(desired_capabilities=appium_desired_capabilities(),appium_remote_url=url_webdriver_remote,
                        browser_profile=None,proxy=None,keep_alive=False):

    """
    :param desired_capabilities: 连接appium server端的真机（或者手机模拟器)设备信息json文件
    :param appium_remote_url:连接appium server端的远程url地址
    :param browser_profile:浏览器名称
    :param proxy: 传入代理连接appium server 端（可一窥appium server端工作原理 ：D )
    :param keep_alive: 是否同appium server建立固定时长的有效连接
    """
    #同appium server 建立session会话
    appium_driver = webdriver.Remote(command_executor=appium_remote_url,desired_capabilities=desired_capabilities)
    return appium_driver


# print appium_send_request()
# print appium_send_request()
print appium_desired_capabilities()
# print get_abspath_apps()  pass
