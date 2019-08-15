from .base import BaseHandler


class AnsibleHandler(BaseHandler):

    def handler(self):
        """
        收集硬件的信息 汇报给API
        :return:
        """
        print('ansible')
