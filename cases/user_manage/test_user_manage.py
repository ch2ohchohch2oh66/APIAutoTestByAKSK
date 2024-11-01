# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/8
# Description: Keep Hungry Keep Foolish

from time import sleep
import pytest
import logging
from interfaces.user_manage.user_manage import UserManage
from utils.data_process import generate_random_string, find_value_by_key

logger = logging.getLogger()


class TestCaseUserManage:

    def setup_class(self):
        logger.info(f'TestCaseUserManage setup_class')
        self.interfaceUserManage = UserManage()

    def test_01_create_user(self, api_client):
        logger.info("testcase 01 create_user")
        user_info = {
            'user': {
                'name': 'autotest_' + generate_random_string(8)
            }
        }
        res = self.interfaceUserManage.create_user(api_client, user_info)
        user_id = find_value_by_key(res.json(), 'id')
        logger.info(f'create user id : {user_id}')
        assert res.status_code in [200, 201]  and user_id

    def test_02_update_user(self, api_client):
        logger.info("testcase 02 update_user")
        self.interfaceUserManage.update_user(api_client)


if '__main__' == __name__:
    logger.info('start !')
    sleep(1)
    pytest.main(["-s", "-v", "cases/user_manage/test_user_manage.py"])
    # example_function()
