# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/10
# Description: Keep Hungry Keep Foolish

import logging
from interfaces.resource_manage.resource_manage import ResourceManage
from utils.cofig_cache import EnvConfig, TempData

logger = logging.getLogger()


class TestCaseResourceManage:
    def setup_class(self):
        logger.info(f'TestCaseResourceManage setup_class')
        self.interfaceResourceManage = ResourceManage()

    def test_01_create_resource(self):
        logger.info(f'testcase 01 create_resource')
        EnvConfig.get('base_url')
        TempData.set('new_url', 'https://andyfreeman.com')
        # self.interfaceResourceManage.create_resource()
        assert True

    def test_02_update_resource(self):
        logger.info(f'testcase 02 update_resource')
        TempData.get('new_url')
        # self.interfaceResourceManage.update_resource()
        assert True
