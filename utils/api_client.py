# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2024/10/14
# Description: Keep Hungry Keep Foolish

import json
import urllib
import requests
import logging

from utils.cofig_cache import EnvConfig
from utils.signer import HttpRequest, Signer
from requests_toolbelt.multipart.encoder import MultipartEncoder

logger = logging.getLogger()


class ApiClient:
    def __init__(self):
        logger.info(f'ApiClient init')
        # logger.info(f'ApiClient load_env_config')
        # envconfig = load_env_config()
        self.base_url = EnvConfig.get('base_url')
        self.ak = EnvConfig.get('ak')
        self.sk = EnvConfig.get('sk')

    def send_request(self, **kwargs):
        method = kwargs.get('method', 'POST')
        url = self.base_url + kwargs.get('url')
        headers = kwargs.get('headers', {})
        json_data = kwargs.get('json')
        data = kwargs.get('data')
        files = kwargs.get('files')

        # 创建HttpRequest对象
        r = HttpRequest(method=method, url=url, headers=headers)

        # 更新HttpRequest对象的body
        # 处理JSON数据
        if json_data:
            if not isinstance(json_data, dict):
                raise ValueError("JSON data must be a dictionary")
            r.body = json.dumps(json_data).encode('utf-8')
            headers['Content-Type'] = 'application/json'

        # 处理表单数据
        elif data:
            if isinstance(data, dict):
                # 表单数据
                r.body = urllib.parse.urlencode(data).encode('utf-8')
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
            elif isinstance(data, str):
                # json转换字符串
                r.body = data.encode('utf-8')
                headers['Content-Type'] = 'application/json'

        # 处理文件内容
        elif files:
            if isinstance(files, dict):
                encoder = MultipartEncoder(fields=files)
                r.body = encoder
                headers['Content-Type'] = encoder.content_type
            elif isinstance(files, str):
                # 假设files是文件内容
                r.body = files.encode('utf-8')
                headers['Content-Type'] = 'application/octet-stream'

        # 更新HttpRequest对象的headers
        r.headers = headers

        # 签名
        sig = Signer()
        sig.Key = self.ak
        sig.Secret = self.sk
        sig.Sign(r)


        # 发送请求
        logger.info(f'ApiClient send_request')
        logger.info(f'+++ request method is: {method}')
        logger.info(f'+++ request url is: {url}')
        logger.info(f'+++ request headers is: {r.headers}')
        try:
            if files:
                logger.info(f'+++ request date type is: FILES, data content is: {r.body}')
                response = requests.request(method=method, url=url, headers=r.headers, files=r.body)
            elif json_data:
                logger.info(f'+++ request date type is: JSON, data content is: {json_data}')
                response = requests.request(method=method, url=url, headers=r.headers, json=json_data)
            elif data:
                logger.info(f'+++ request date type is: DATA, data content is: {r.body}')
                response = requests.request(method=method, url=url, headers=r.headers, data=r.body)
            else:
                response = requests.request(method=method, url=url, headers=r.headers)

            logger.info(f'=== response status_code is: {response.status_code}')
            logger.info(f'=== response text is: {response.text}')
            logger.info(f'=== response headers is: {response.text}')
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


if __name__ == '__main__':
    domain_id = '070787c9308010a60f48c00264a347c0'

    user_info = {
        'user': {
            'domain_id': domain_id,
            'name': 'IAMUser3',
            'password': 'IAMPassword@',
            'email': 'IAMEmail3@huawei.com',
            'areacode': '0086',
            'phone': '12345678913',
            'enabled': True,
            'pwd_status': False,
            'xuser_type': '',
            'xuser_id': '',
            'access_mode': 'default',
            'description': 'IAMDescription'
        }
    }

    print(user_info)

    client = ApiClient()

    # response = send_requests(
    #     method='POST',
    #     url='/v3.0/OS-USER/users',
    #     json=user_info
    # )


    response = client.send_request(
        method='POST',
        url='/v3.0/OS-USER/users',
        data=json.dumps(user_info)
    )

    # response = send_requests(
    #     method='POST',
    #     url='https://example.com/api',
    #     files={'file': ('filename', '文件内容', 'application/octet-stream')}  # 文件内容
    # )

    print(response.status_code)
    print(response.content)

