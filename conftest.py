# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/10
# Description: Keep Hungry Keep Foolish
import logging
import os.path

import pytest

from utils.api_client import ApiClient
from utils.cofig_cache import load_env_config, EnvConfig

logger=logging.getLogger(__name__)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    print("pytest_configure hook.")
    # 打印 config.option 以查看所有可用选项
    # print("Available options in config.option:")
    # for option in dir(config.option):
    #     print(option)

    # 获取项目根目录
    project_root = os.path.dirname(os.path.abspath(__file__))

    # 修改 pytest 配置，动态设置 log_file
    log_file_path = os.path.join(project_root, "temp", "log", "test_demo.log")
    config.option.log_file = log_file_path
    print(f"Logging to {log_file_path}")

    # 修改 allure 配置，动态设置 allure_dir
    allure_dir_path = os.path.join(project_root, "temp", "original_report_data")
    config.option.allure_report_dir = allure_dir_path
    config.option.clean_alluredir = True
    print(f"Allure report dir is {allure_dir_path}")
    EnvConfig._set('original_report_data', allure_dir_path)


def pytest_sessionstart(session):
    print("Session start hook.")
    EnvConfig.load()


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    logger.info("\n")
    logger.info("Session finish hook.")




