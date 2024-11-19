# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/11
# Description: Keep Hungry Keep Foolish
import os
from time import sleep
from utils.allure_cumtom import set_windows_title, set_overview_report_name, set_report_env_info
import pytest
import logging

from utils.cofig_cache import EnvConfig


def lets_go():
    # 执行测试并获取退出码
    # pytest.ExitCode.OK = 0 (测试全部通过)
    # pytest.ExitCode.TESTS_FAILED = 1 (测试部分失败)
    # pytest.ExitCode.INTERRUPTED = 2 (测试被中断)
    # pytest.ExitCode.INTERNAL_ERROR = 3 (内部错误)
    exit_code = pytest.main()
    logging.info(f'Test execution completed with exit code: {exit_code}')
    
    # 只有在内部错误或被中断时跳过报告生成
    if exit_code in [pytest.ExitCode.INTERRUPTED, pytest.ExitCode.INTERNAL_ERROR]:
        logging.error(f'Tests were interrupted or had internal error (exit code: {exit_code}). Report generation skipped.')
        return
        
    # 测试全部通过或部分失败都生成报告
    os.system('allure generate ./temp -o ./report -c')
    # 定制Allure报告
    set_windows_title('./report', 'IAM测试报告')
    set_overview_report_name('./report', 'IAM测试报告汇总')
    set_report_env_info('./report', {'baseUrl': EnvConfig.get('base_url')})



if '__main__' == __name__:
    lets_go()
