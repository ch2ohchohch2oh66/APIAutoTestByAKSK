# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/11/7
# Description: Keep Hungry Keep Foolish
import pytest
from jsonpath import jsonpath
from interfaces.user_manage.user_manage import UserManage
import logging

from utils.cofig_cache import TempData
from utils.data_process import generate_random_alpha_string, find_value_by_key

logger = logging.getLogger()
interfaceUserManage = UserManage()


@pytest.fixture(scope='class', autouse=True)
def clear_users():
    logger.info(f'此处作为整个user_manage的前置，用以清理环境中的残留用户，以避免脏数据导致用例失败')
    list_res = interfaceUserManage.list_users()
    # assert list_res and len(list_res.json().users) > 2
    # user_ids = jsonpath(list_res.json(), '$.users[*].id')
    # for user_id in user_ids:
    #     interfaceUserManage.delete_user(user_id)


@pytest.fixture(scope='class')
def create_user_4_update():
    logger.info(f'开始预置用户')
    user_info = {'user': {'name': generate_random_alpha_string(32)}}
    res = interfaceUserManage.create_user(user_info)
    assert res
    user_id = find_value_by_key(res.json(), 'id')
    logger.info(f'完成预置用户：f{user_id}')
    yield user_id
    logger.info(f'开始清理预置用户：{user_id}')
    del_res = interfaceUserManage.delete_user(user_id)
    assert del_res
    logger.info(f'完成清理预置用户')