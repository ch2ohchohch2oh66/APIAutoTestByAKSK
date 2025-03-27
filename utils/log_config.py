#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/28
# Description: Keep Hungry Keep Foolish

import logging

'''
pytest机制运行时日志统一在pytest.ini中设置
调试阶段临时日志打印在此设置
'''
def logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[
            logging.StreamHandler(),  # 输出到控制台
        ]
    )
    return logging.getLogger()