# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/11/2
# Description: Keep Hungry Keep Foolish

import logging
import os
from utils.yaml_manage import load_yaml

logger = logging.getLogger()


def load_env_config():
    root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    config_folder = os.path.join(root_path, "config")

    env_name = os.getenv('TEST_ENV')
    if env_name == 'TEST_1':
        env_config_path = os.path.join(config_folder, 'EnvConfig_test1.yaml')
    elif env_name == 'TEST_2':
        env_config_path = os.path.join(config_folder, 'EnvConfig_test2.yaml')
    else:
        env_config_path = os.path.join(config_folder, 'EnvConfig.yaml')

    logger.info(f'env config path is : {env_config_path}')
    return load_yaml(env_config_path)


class EnvConfig:
    _data = {}

    @classmethod
    def load(cls):
        if not cls._data:
            cls._data.update(load_env_config())
        logger.info(f'global EnvConfig is: {cls._data}')

    @classmethod
    def get(cls, key):
        value = cls._data.get(key, None)
        logger.info(f'get global config: {key} = {value}')
        return value

    @classmethod
    def _set(cls, key, value):
        logger.info(f'set global config: {key} = {value}')
        cls._data.__setitem__(key, value)


class TempData:
    _data = {}

    @classmethod
    def set(cls, key, value):
        logger.info(f'set temp date: {key} = {value}')
        cls._data.__setitem__(key, value)

    @classmethod
    def get(cls, key):
        value = cls._data.get(key, None)
        logger.info(f'get temp data: {key} = {value}')
        return value
