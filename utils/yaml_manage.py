# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/8
# Description: Keep Hungry Keep Foolish

from time import sleep
import logging
import yaml

logger = logging.getLogger()


def load_yaml(yaml_file_path):
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


