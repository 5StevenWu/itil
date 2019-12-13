import importlib


def get_class(class_path):
    # 'src.engine.agent.AgentHandler',
    module_str, cls_str = class_path.rsplit('.', maxsplit=1)
    module = importlib.import_module(module_str)
    cls = getattr(module, cls_str)
    return cls
