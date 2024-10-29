# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/8
# Description: Keep Hungry Keep Foolish
import os
from time import sleep
import logging
import yaml

# logging.basicConfig()
logger = logging.getLogger()


def load_yaml_content(yaml_file_path):
    try:
        with open(yaml_file_path, 'r', encoding='utf-8') as file:
            yaml_content = yaml.safe_load(file)
            sleep(1)
            logger.info("yaml content is : " + str(yaml_content))
        return yaml_content
    except FileNotFoundError:
        logger.info(f"The YAML file at {yaml_file_path} was not found.")
    except yaml.YAMLError as exc:
        logger.info(f"Error in parsing YAML file: {exc}")


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
    return load_yaml_content(env_config_path)

