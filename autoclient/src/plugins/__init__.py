from lib.conf import settings
from lib.import_string import get_class


def get_server_info(handler, hostname=None):
    """
    根据配置 采集对应插件的信息
    :return:
    """
    info = {}
    for name, plugin_str in settings.PLUGINS_DICT.items():
        # 'disk'   disk src.plugins.disk.Disk
        cls = get_class(plugin_str)
        obj = cls()
        ret = obj.process(handler, hostname)
        info[name] = ret

    return info
