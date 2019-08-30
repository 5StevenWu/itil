from lib.conf import settings
import requests
from ..plugins import get_server_info
import json
from concurrent.futures import ThreadPoolExecutor


class BaseHandler:

    def __init__(self):
        self.asset_url = settings.POST_ASSET_URL


    def handler(self):
        """
        收集硬件的信息 汇报给API
        :return:
        """
        raise NotImplementedError('handler() must be Implemented')


class SshAndSaltHandler(BaseHandler):

    def handler(self):
        """
        收集硬件的信息 汇报给API
        :return:
        """
        # 获取要采集信息的主机列表

        ret = requests.get(url=self.asset_url)

        host_lit = ret.json()


        pool = ThreadPoolExecutor(20)

        for hostname in host_lit:
            pool.submit(self.task, hostname)

    def task(self, hostname):
        info = get_server_info(self, hostname)
        print('#####',info)
        print(self.asset_url)
        ret = requests.post(
            url=self.asset_url,
            data=json.dumps(info).encode('utf-8'),
            headers={'content-type': 'application/json'}
        )
        print(ret.json())
