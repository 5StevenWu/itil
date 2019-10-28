from lib.conf import settings
import requests
from ..plugins import get_server_info
import json
from concurrent.futures import ThreadPoolExecutor
import time
from lib.auth import gen_key


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
        info['action'] = 'update'
        #有init文件即不是首次执行
        init_status = self.cmd('ls /etc/itil/initfinish', hostname).decode('utf-8')

        if not init_status:
            info['action'] = 'create'

        ctime = time.time()
        print(info)
        ret = requests.post(
            url=self.asset_url,
            params={'key': gen_key(ctime), 'ctime': ctime},
            data=json.dumps(info).encode('utf-8'),

            headers={'content-type': 'application/json'}
        )
        # print(ret.json())
        ret = ret.json()
        if not init_status and ret.get('status'):
            self.cmd("mkdir /etc/itil ; touch /etc/itil/initfinish", hostname)
