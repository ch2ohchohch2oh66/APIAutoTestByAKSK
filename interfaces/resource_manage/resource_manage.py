# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/10
# Description: Keep Hungry Keep Foolish
import inspect
import os
from time import sleep
import logging

from utils.yaml_manage import load_yaml

logger = logging.getLogger()


class ResourceManage:
    def __init__(self):
        logger.info(f'ResourceManage init !')
        sleep(1)
        current_file_path = os.path.abspath(__file__)
        yaml_file_path = current_file_path.rsplit('.', 1)[0] + '.yaml'
        logger.info(f'ResourceManage load_yaml_content')
        self.yaml_content = load_yaml(yaml_file_path)

    def create_resource(self, client):
        interface_name = inspect.currentframe().f_code.co_name
        interface_param = self.yaml_content[interface_name]
        method = interface_param.get('method')
        endpoint = interface_param.get('url')
        body = interface_param.get('req_body')
        logger.info(f'{interface_name} : {endpoint}')
        client.send_request(method, endpoint, body)

    def update_resource(self, client):
        interface_name = inspect.currentframe().f_code.co_name
        interface_param = self.yaml_content[interface_name]
        method = interface_param.get('method')
        endpoint = interface_param.get('url').format(resId='1234567890')
        body = interface_param.get('req_body')
        logger.info(f'{interface_name} : {endpoint}')
        client.send_request(method, endpoint, body)


if '__main__' == __name__:
    user_manage_instance = ResourceManage()
    user_manage_instance.create_resource()
    user_manage_instance.update_resource()
