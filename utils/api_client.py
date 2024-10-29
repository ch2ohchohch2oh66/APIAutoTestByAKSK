# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/14
# Description: Keep Hungry Keep Foolish

import requests
import logging

from exceptiongroup import catch

from utils import signer
from utils.load_yaml_content import load_env_config

logger = logging.getLogger()


class ApiClient:
    def __init__(self):
        logger.info(f'ApiClient init')
        logger.info(f'ApiClient load_env_config')
        envconfig = load_env_config()
        self.base_url = envconfig.get('base_url')
        self.ak = envconfig.get('ak')
        self.sk = envconfig.get('sk')

    def send_request(self, **kwargs):
        method = kwargs.get('method')
        url = self.base_url + kwargs.get('url')

        sig = signer.Signer()
        sig.Key = self.ak
        sig.Secret = self.sk
        r = signer.HttpRequest(method, url)
        r.headers = kwargs.get('headers')
        r.body = kwargs.get('body')
        sig.Sign(r)

        logger.info(f'ApiClient send_request')
        logger.info(f'send_request url : {url}')
        try:
            response = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
            return response
        except requests.exceptions.HTTPError as http_err:
            logger.info(f'HTTP error occured : {http_err}')
        except requests.exceptions.ConnectionError as conn_err:
            logger.info(f'Connection error occured : {conn_err}')
        except requests.exceptions.Timeout as timeout_err:
            logger.info(f'Timeout error occured : {timeout_err}')
        except requests.exceptions.RequestException as req_err:
            logger.info(f'Something error occured : {req_err}')
        except ValueError as val_err:
            logger.info(f'Error prasing JSON : {val_err}')

