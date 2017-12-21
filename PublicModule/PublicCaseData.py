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
#--------------------------------appium desired capabilities for android------------------------------------
android_appium_platform_name="Android" #设备名称
android_appium_platform_version={"v_4.4":"4.4","v_5.0":"5.0","v_5.1":"5.1","v_6.0":"6.0","v_7.0":"7.0"} #定义为字典保存android系统版本
android_appium_device_name = "Android Emulator" #默认值为android模拟器，若使用真机则使用真机设备名称
android_hybrid_appname = "android_hybrid.apk" #当前项目apps目录下存放混合编程android应用的名称
android_appium_newcommand_timeout = 240 #请求超时时间
android_automation_name="Appium" #测试框架名称
android_app_package_name="" #app包名称(出于软件安全考虑不予给出)
android_app_launchactivity_name=""#默认启动的launch activity名称(出于软件安全考虑不予给出)

#--------------------------------appium desired capabilities for iOS------------------------------------
ios_appium_platform_name="iOS" #设备名称

#appium client端连接appium server端的远程地址（注：目的是向appium server端提交json文件，告诉appium server连接设备的信息)
url_webdriver_remote = user_app_host+"/wd/hub" #向本地appium server发送http请求的地址

#ios设备的信息
