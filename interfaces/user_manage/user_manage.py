# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/8
# Description: Keep Hungry Keep Foolish

import logging
import os
import sys
import time
import utils.yaml_manage as load_yaml
from utils.api_client import ApiClient

logger = logging.getLogger()


class UserManage:
    def __init__(self):
        time.sleep(1)
        logger.info("UserManage __init__ !")

        # 获取当前文件的完整路径
        current_file_path = os.path.abspath(__file__)

        # 构建YAML文件的路径
        yaml_file_path = current_file_path.rsplit('.', 1)[0] + '.yaml'
        logger.info(f'UserManage load_yaml_content')
        self.yaml_content = load_yaml.load_yaml(yaml_file_path)

        self.api_client = ApiClient()

    def create_user(self, body=None):
        interface_name = sys._getframe().f_code.co_name
        logger.info("interface_name is : " + interface_name)
        interface_param = self.yaml_content.get(interface_name)
        method = interface_param.get('method')
        url = interface_param.get('url')
        if body is None:
            body = interface_param.get('req_body')
        logger.info(f'{interface_name} : {url}')
        return self.api_client.send_request(method=method, url=url, json=body)

    def update_user(self, user_id, body=None):
        interface_name = sys._getframe().f_code.co_name
        logger.info("interface_name is: " + interface_name)
        interface_param = self.yaml_content.get(interface_name)
        method = interface_param.get('method')
        url = interface_param.get('url').format(user_id=user_id)
        if body is None:
            body = interface_param.get('req_body')
        logger.info(f'{interface_name}: {url}')
        return self.api_client.send_request(method=method, url=url, json=body)

    def delete_user(self, user_id):
        interface_name = sys._getframe().f_code.co_name
        logger.info('interface_name is: ' + interface_name)
        interface_param = self.yaml_content.get(interface_name)
        method = interface_param.get('method')
        url = interface_param.get('url').format(user_id=user_id)
        body = interface_param.get('req_body')
        logger.info(f'{interface_name}: {url}')
        return self.api_client.send_request(method=method, url=url, json=body)

    def get_user(self, user_id):
        interface_name = sys._getframe().f_code.co_name
        interface_param = self.yaml_content.get(interface_name)
        method = interface_param.get('method')
        url = interface_param.get('url').format(user_id=user_id)
        return self.api_client.send_request(method=method, url=url)

    def list_users(self):
        interface_name = sys._getframe().f_code.co_name
        interface_param = self.yaml_content.get(interface_name)
        method = interface_param.get('method')
        url = interface_param.get('url')
        return self.api_client.send_request(method=method, url=url)
