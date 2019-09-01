from lib.conf import settings
from .base import BasePlugin
import os
import re
import traceback
from lib.response import BaseResponse
from lib.logger import logger


class Disk(BasePlugin):

    def linux(self, handler, hostname=None):
        response = BaseResponse()

        try:
            if self.debug:
                # 读取文件
                with open(os.path.join(self.base_dir, 'files', 'disk.out')) as f:
                    ret = f.read()

            else:
                # ret = handler.cmd('sudo MegaCli  -PDList -aALL', hostname)
                ret = handler.cmd("lsblk | grep '^s' | grep 'disk'", hostname)

            response.data = self.parse_disk(ret.decode('utf-8'))

        except Exception:
            error = traceback.format_exc()
            response.status = False
            response.error = error
            logger.debug(error)

        return response.dict

    def win(self, handler, hostname=None):
        ret = handler.cmd('wmic logicaldisk', hostname)
        return ret[:20]

    def parse_disk(self, content):
        dic = {}
        disk_list = content.split(
            '\n')  # {'0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'}}
        count = 0
        #print(disk_list)
        for disk in disk_list:
            if disk:
                info_lst = [i for i in disk.split(' ') if i]  # ['sda', '8:0', '0', '60G', '0', 'disk']
                dic[count] = {'slot': count, 'pd_type': info_lst[0], 'capacity': info_lst[3].strip('G'),
                              'model': info_lst[-1]}
        return dic

            # dic[i]={'slot': i, 'pd_type': dic[i][0], 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'}

    def parse(self, content):
        """
        解析shell命令返回结果
        :param content: shell 命令结果
        :return:解析后的结果
        """
        response = {}
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key, value = row.split(':')
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)', value.strip())
                        if raw_size:
                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response[temp_dict['slot']] = temp_dict
        return response  # {'0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'}}

    @staticmethod
    def mega_patter_match(needle):
        grep_pattern = {'Slot': 'slot', 'Raw Size': 'capacity', 'Inquiry': 'model', 'PD Type': 'pd_type'}
        for key, value in grep_pattern.items():
            if needle.startswith(key):
                return value
        return False
