from lib.conf import settings

class BasePlugin():

    def __init__(self):
        self.debug = settings.DEBUG
        self.base_dir = settings.BASE_DIR


    def get_os(self,handler, hostname=None):

        # ret= handler.cmd('uname',hostname)

        return 'Linux'

    def process(self, handler, hostname=None):
        os = self.get_os(handler, hostname)
        if os == 'Linux':
            return self.linux(handler, hostname)
        else:
            return self.win(handler, hostname)

    def linux(self, handler, hostname=None):
        raise NotImplementedError('linux() must be Implemented')

    def win(self, handler, hostname=None):
        raise NotImplementedError('win() must be Implemented')
