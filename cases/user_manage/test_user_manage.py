# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/8
# Description: Keep Hungry Keep Foolish

from time import sleep

import allure
from allure_pytest.utils import allure_title
from jsonpath import jsonpath
import pytest
import logging
from interfaces.user_manage.user_manage import UserManage
from utils.cofig_cache import EnvConfig
from utils.data_process import find_value_by_key, generate_random_string, generate_random_alpha_string, \
    generate_random_digit_string

logger = logging.getLogger()


@allure.feature('用户管理')
class TestCaseUserManage:

    def setup_class(self):
        logger.info(f'TestCaseUserManage setup_class')
        self.interfaceUserManage = UserManage()

    @pytest.mark.parametrize('user_name', (
            generate_random_alpha_string(1),
            generate_random_alpha_string(64),
            generate_random_alpha_string(32),
            generate_random_alpha_string(32) + generate_random_digit_string(10),
            '_' + generate_random_string(32) + ' -_'))
    @allure.story('创建用户')
    @allure.title('创建用户-用户名校验-正常场景')
    def test_create_user_check_name_normal(self, user_name):
        logger.info("创建用户-用户名校验-正常场景")
        user_info = {
            'user': {
                'name': user_name
            }
        }
        EnvConfig.get('ak')
        EnvConfig.get('sk')
        res = self.interfaceUserManage.create_user(user_info)
        assert res and 201 == res.status_code
        res_user_name = find_value_by_key(res.json(), 'name')
        user_id = jsonpath(res.json(), '$.user.id')[0]
        logger.info(f'create user_name: {res_user_name}, user_id: {user_id}')
        assert user_id and user_name == res_user_name

        get_res = self.interfaceUserManage.get_user(user_id)
        assert get_res
        get_res_user_name = find_value_by_key(get_res.json(), 'name')
        assert user_name == get_res_user_name

        del_res = self.interfaceUserManage.delete_user(user_id)
        assert del_res and 204 == del_res.status_code

    @allure.story('创建用户')
    @allure.title('创建用户-用户名校验-异常场景')
    @pytest.mark.parametrize('user_name', (
            generate_random_alpha_string(65),
            '',
            ' ' + generate_random_string(32),
            generate_random_digit_string(1) + generate_random_string(32)))
    def test_create_user_check_name_abnormal(self, user_name):
        logger.info(f'创建用户-用户名校验-异常场景')
        error_message = ['']
        user_info = {'user': {'name': user_name}}
        res = self.interfaceUserManage.create_user(user_info)
        assert 400 == res.status_code and 400 == find_value_by_key(res.json(), 'code')

    @pytest.mark.parametrize('description', [
        generate_random_string(1),
        generate_random_alpha_string(256)
    ])
    @allure.story('更新用户')
    @allure.title('更新用户-描述-正常场景')
    def test_update_user_check_description_nomal(self, create_user_4_update, description):
        logger.info(f'更新用户-描述-正常场景')
        user_info = {'user': {'description': description}}
        res = self.interfaceUserManage.update_user(user_id=create_user_4_update, body=user_info)
        assert res
        get_res = self.interfaceUserManage.get_user(user_id=create_user_4_update)
        assert get_res
        update_description = find_value_by_key(get_res.json(), 'description')
        assert update_description == description


if __name__ == "__main__":
    logger.info('start !')
    sleep(1)
    pytest.main(["-s", "-v", "cases/user_manage/test_user_manage.py"])
    # example_function()
