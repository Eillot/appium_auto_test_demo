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

"""
@version: python2.7
@Author  : Simon
@Explain : 模拟用户登录的UI操作
@contact:
@Time    : 17-12-21 下午4:22
@File    : TestUserLoginCase
@Software: PyCharm
"""
import unittest
from PublicModule.PublicUiMoudle import *

class TestUserLoginCase(unittest.TestCase):

    def setUp(self):

        # 向appium server 端发起session会话并建立连接
        self.devicer = appium_send_request(app_launchactivity_name=android_app_launchactivity_name,desired_capabilities=appium_desired_capabilities(app_package_name=android_app_package_name))
    def tearDown(self):
        pass

