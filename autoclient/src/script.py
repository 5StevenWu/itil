from lib.conf import settings
from lib.import_string import get_class


# def run():
#     """程序的入口"""
#     if settings.ENGINE == 'agent':
#         obj = AgentHandler()
#         obj.handler()
#     elif settings.ENGINE == 'ssh':
#         obj = SshHandler()
#         obj.handler()
#     elif settings.ENGINE == 'salt':
#         obj = SaltHandler()
#         obj.handler()
#     else:
#         print('不支持该模式')


def run():
    """程序的入口"""
    class_path = settings.ENGINE_DICT.get(settings.ENGINE)  # 'src.engine.agent.AgentHandler',

    # 'src.engine.agent'  'AgentHandler'
    cls = get_class(class_path)
    obj = cls()
    obj.handler()
