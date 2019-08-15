from .base import BaseHandler
from ..plugins import get_server_info
import requests
import json
import os
from lib.conf import settings
from lib.auth import gen_key
import time

class AgentHandler(BaseHandler):

    def cmd(self, command, hostname=None):
        import subprocess

        ret = subprocess.getoutput(command)

        return ret

    def handler(self):
        """
        agent模式具体的处理流程
        收集硬件的信息 汇报给API
        :return:
        """
        # 收集本地硬件的信息
        info = get_server_info(self)

        if not os.path.exists(settings.CERT_PATH):
            info['action'] = 'create'
        else:
            # 老机器
            # 判断主机名是否修改
            with open(settings.CERT_PATH, 'r', encoding='utf-8') as f:
                old_hostname = f.read()

            hostname = info['basic']['data']['hostname']
            if hostname == old_hostname:
                # 没有修改主机名  告知API只更新资产信息
                info['action'] = 'update'
            else:
                # 修改了主机名  告知API 更新资产信息 + 主机名
                info['action'] = 'update_host'
                info['old_hostname'] = old_hostname


        ctime = time.time()
        res = requests.post(
            url=self.asset_url,
            params={'key':gen_key(ctime),'ctime':ctime},
            data=json.dumps(info).encode('utf-8'),
            headers={'content-type': 'application/json'}
        )

        ret = res.json()

        if ret.get('status'):
            # 响应正常 写入主机名
            with open(settings.CERT_PATH, 'w', encoding='utf-8') as f:
                f.write(ret['hostname'])
