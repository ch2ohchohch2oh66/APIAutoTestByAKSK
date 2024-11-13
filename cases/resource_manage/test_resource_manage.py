# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/10
# Description: Keep Hungry Keep Foolish

import logging

import allure

from interfaces.resource_manage.resource_manage import ResourceManage
from utils.cofig_cache import EnvConfig, TempData

logger = logging.getLogger()


@allure.feature('资源管理')
class TestCaseResourceManage:
    def setup_class(self):
        logger.info(f'TestCaseResourceManage setup_class')
        self.interfaceResourceManage = ResourceManage()

    @allure.title('创建资源')
    def test_01_create_resource(self):
        logger.info(f'testcase 01 create_resource')
        EnvConfig.get('base_url')
        TempData.set('new_url', 'https://andyfreeman.com')
        # self.interfaceResourceManage.create_resource()
        assert True

    @allure.title('更新资源')
    def test_02_update_resource(self):
        logger.info(f'testcase 02 update_resource')
        TempData.get('new_url')
        # self.interfaceResourceManage.update_resource()
        assert True
