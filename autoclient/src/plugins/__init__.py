from lib.conf import settings
from lib.import_string import get_class


def get_server_info(handler, hostname=None):
    """
    根据配置 采集对应插件的信息
    :return:
    """
    info = {}
    # 'disk'   disk src.plugins.disk.Disk  循环需要收集的硬件信息
    for name, plugin_str in settings.PLUGINS_DICT.items():

        cls = get_class(plugin_str)
        obj = cls()
        ret = obj.process(handler, hostname)
        info[name] = ret

    return info
