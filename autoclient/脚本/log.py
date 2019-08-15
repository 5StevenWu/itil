import logging


# logging.basicConfig(filename='log.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=10)
#
# logging.debug('debugxxx   sasoud')
# logging.info('info')
#
# logging.basicConfig(filename='log1.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=10)
#
# logging.debug('debugx1111   sasoud')
# logging.info('info 222 ')


# file_handler = logging.FileHandler('l1_1.log', 'a', encoding='utf-8')
# fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
# file_handler.setFormatter(fmt)
#
# file_handler_1 = logging.FileHandler('l1_1.log', 'a', encoding='utf-8')
# fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
# file_handler_1.setFormatter(fmt)
#
# logger1 = logging.Logger('s1', level=logging.DEBUG)
# logger1.addHandler(file_handler)
# logger1.addHandler(file_handler_1)
# logger1.debug('1111')


class Logger():

    def __init__(self, name, log_file, level=logging.DEBUG):
        file_handler = logging.FileHandler(log_file, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        file_handler.setFormatter(fmt)

        self.logger = logging.Logger(name, level=level)
        self.logger.addHandler(file_handler)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def error(self, msg):
        self.logger.error(msg)


logger = Logger('log1', '1111.log')

logger.info('kjwqheklwqheklwjqlek')
