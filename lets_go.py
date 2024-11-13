# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/11
# Description: Keep Hungry Keep Foolish
import os
from time import sleep
from utils.allure_cumtom import set_windows_title, set_overview_report_name, set_report_env_info
import pytest

from utils.cofig_cache import EnvConfig


def lets_go():
    pytest.main()
    # sleep(3)
    os.system('allure generate ./temp -o ./report -c')
    # 定制Allure报告
    set_windows_title('./report', 'IAM测试报告')
    set_overview_report_name('./report', 'IAM测试报告汇总')
    set_report_env_info('./report', {'baseUrl': EnvConfig.get('base_url')})



if '__main__' == __name__:
    lets_go()
