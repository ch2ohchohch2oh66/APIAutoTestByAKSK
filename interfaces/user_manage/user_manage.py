# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/8
# Description: Keep Hungry Keep Foolish

import os
import sys
import time
import utils.load_yaml_content as load_yaml
import logging

logger = logging.getLogger()


class UserManage:
    def __init__(self):
        time.sleep(1)
        logger.info("UserManage __init__ !")

        # 获取当前文件的完整路径
        current_file_path = os.path.abspath(__file__)

        # 构建YAML文件的路径
        yaml_file_path = current_file_path.rsplit('.',1)[0] + '.yaml'
        logger.info(f'UserManage load_yaml_content')
        self.yaml_content = load_yaml.load_yaml_content(yaml_file_path)

    def create_user(self, api_client, body=None):
        interface_name = sys._getframe().f_code.co_name
        logger.info("interface_name is : " + interface_name)
        interface_param = self.yaml_content.get(interface_name)
        method = interface_param.get('method')
        url = interface_param.get('url')
        if body is None:
            body = interface_param.get('req_body')
        logger.info(f'{interface_name} : {url}')
        return api_client.send_request(method=method, url=url, json=body)

    def update_user(self,api_client):
        interface_name = sys._getframe().f_code.co_name
        logger.info("interface_name is : " + interface_name)
        interface_param = self.yaml_content.get(interface_name)
        method = interface_param.get('method')
        url = interface_param.get('url')
        body = interface_param.get('req_body')
        logger.info(f'{interface_name} : {url}')
        api_client.send_request(method=method, url=url, json=body)
