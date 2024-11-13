# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 11/10/2024
# Description: Keep Hungry Keep Foolish

import json
import os


# 设置报告的浏览器窗口标题
# 通过修改Allure报告目录下index.html中head.title字段来设置Allure报告的浏览器窗口名称
def set_windows_title(allure_report_path, new_title):
    old_title = 'Allure Report'
    report_title_filepath = os.path.join(allure_report_path, "index.html")

    # 读取文件内容
    with open(report_title_filepath, 'r', encoding="utf-8") as f:
        all_the_lines = f.readlines()

    # 修改内容
    modified_lines = [line.replace(old_title, new_title) for line in all_the_lines]

    # 写回文件
    with open(report_title_filepath, 'w', encoding="utf-8") as f:
        f.writelines(modified_lines)


# 设置报告的Overview名称
# 通过修改Allure报告目录下widgets/summary.json中reportName字段来设置Allure报告Overview栏的报告名称
def set_overview_report_name(allure_html_path, new_name):
    report_name_filepath = os.path.join(allure_html_path, "widgets", "summary.json")
    # 读取文件内容
    with open(report_name_filepath, 'r') as f:
        params = json.load(f)

    # 修改内容
    params['reportName'] = new_name

    # 写回文件
    with open(report_name_filepath, 'w', encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=4)


# 设置报告的环境和环境变量
# 通过修改Allure报告目录下widgets/environment.json文件的内容来设置Allure报告Environment栏的内容，@env_info的内容为键值对
def set_report_env_info(allure_html_path, env_info: dict):
    # 生成文件内容
    envs = [
        {"name": k, "values": v if isinstance(v, list) else [v]}
        for k, v in env_info.items()
    ]

    # 写入文件
    env_info_filepath = os.path.join(allure_html_path, "widgets", "environment.json")
    with open(env_info_filepath, 'w', encoding="utf-8") as f:
        json.dump(envs, f, ensure_ascii=False, indent=4)
