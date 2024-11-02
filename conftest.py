# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/10
# Description: Keep Hungry Keep Foolish
import logging
import os.path

import pytest

from utils.api_client import ApiClient
from utils.cofig_cache import load_env_config, EnvConfig

logger = logging.getLogger()


# @pytest.fixture(scope='session')
def env_config(request):
    logger.info(f'conftest env_config')
    # current_file_path = os.path.abspath(__file__)
    # current_dir = os.path.dirname(current_file_path)
    # envconfig_path = os.path.join(current_dir, 'config', 'EnvConfig.yaml')
    # logging.info(f'EnvConfig file path is {envconfig_path}')
    logger.info(f'conftest load_env_config')
    return load_env_config()


def pytest_sessionstart(session):
    EnvConfig.load()


@pytest.fixture(scope='session')
def api_client():
    logger.info(f'conftest api_client')
    client = ApiClient()
    return client
