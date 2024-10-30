# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/8
# Description: Keep Hungry Keep Foolish

from time import sleep
import pytest
import logging
from interfaces.user_manage.user_manage import UserManage

logger = logging.getLogger()


class TestCaseUserManage:

    def setup_class(self):
        logger.info(f'TestCaseUserManage setup_class')
        self.interfaceUserManage = UserManage()

    def test_01_create_user(self, api_client):
        logger.info("testcase 01 create_user")
        user_info = {
            'user': {
                'name': 'IAMUser002'
            }
        }
        self.interfaceUserManage.create_user(api_client, user_info)

    def test_02_update_user(self, api_client):
        logger.info("testcase 02 update_user")
        self.interfaceUserManage.update_user(api_client)


if '__main__' == __name__:
    logger.info('start !')
    sleep(1)
    pytest.main(["-s", "-v", "cases/user_manage/test_user_manage.py"])
    # example_function()
