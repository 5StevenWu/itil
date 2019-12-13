import os
import importlib
from . import global_settings

class Settings():

    def __init__(self):

        # 默认配置
        for i in dir(global_settings):  # dir  获取对象的属性
            if i.isupper():  #  ‘USER’  'PWD'  'EMAIL'
                v = getattr(global_settings, i)  # 通过反射获取值
                setattr(self, i, v)  # 给settings本身设置值

        #  用户自定义的配置
        path = os.environ.get('USER_SETTINGS')
        module = importlib.import_module(path)  # 导入用户的自定义的配置   'conf.settings'
        for i in dir(module):  # dir  获取对象的属性
            if i.isupper():
                v = getattr(module, i)  # 通过反射获取值
                setattr(self, i, v)  # 给settings本身设置值


settings = Settings()

