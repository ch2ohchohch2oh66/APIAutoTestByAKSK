# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/8
# Description: Keep Hungry Keep Foolish

from time import sleep
import pytest
import logging
from interfaces.user_manage.user_manage import UserManage
from utils.data_process import find_value_by_key, generate_random_string, generate_random_alpha_string, \
    generate_random_digit_string

logger = logging.getLogger()


class TestCaseUserManage:

    def setup_class(self):
        logger.info(f'TestCaseUserManage setup_class')
        self.interfaceUserManage = UserManage()

    @pytest.mark.parametrize('user_name', (
            generate_random_alpha_string(1),
            generate_random_alpha_string(64),
            generate_random_alpha_string(32),
            generate_random_alpha_string(32) + generate_random_digit_string(10),
            generate_random_string(32) + ' -_'))
    def test_01_create_user(self, api_client, user_name):
        logger.info("testcase 01 create_user")
        user_info = {
            'user': {
                'name': user_name
            }
        }
        res = self.interfaceUserManage.create_user(api_client, user_info)
        res_user_name = find_value_by_key(res.json(), 'name')
        user_id = find_value_by_key(res.json(), 'id')
        logger.info(f'create user_name: {res_user_name}, user_id: {user_id}')
        assert res.status_code in [200, 201] and user_id and user_name == res_user_name

        del_res = self.interfaceUserManage.delete_user(api_client, user_id)
        assert del_res.status_code in [200, 201, 204]

    def test_02_update_user(self, api_client):
        logger.info("testcase 02 update_user")
        self.interfaceUserManage.update_user(api_client)


if '__main__' == __name__:
    logger.info('start !')
    sleep(1)
    pytest.main(["-s", "-v", "cases/user_manage/test_user_manage.py"])
    # example_function()
