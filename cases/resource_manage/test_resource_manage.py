# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/10
# Description: Keep Hungry Keep Foolish

import logging
from interfaces.resource_manage.resource_manage import ResourceManage

logger = logging.getLogger()


class TestCaseResourceManage:
    def setup_class(self):
        logger.info(f'TestCaseResourceManage setup_class')
        self.interfaceResourceManage = ResourceManage()





    def test_01_create_resource(self, api_client):
        logger.info(f'testcase 01 create_resource')
        self.interfaceResourceManage.create_resource(api_client)
        assert 1==2


    def test_02_update_resource(self, api_client):
        logger.info(f'testcase 02 update_resource')
        self.interfaceResourceManage.update_resource(api_client)
        assert False
