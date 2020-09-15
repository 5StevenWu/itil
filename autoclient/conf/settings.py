import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER = 'root'
PWD = 'XXXX'
#ENGINE示例 agent   ssh   salt 
ENGINE = 'ssh'

ENGINE_DICT = {
    'agent': 'src.engine.agent.AgentHandler',
    'ssh': 'src.engine.ssh.SshHandler',
    'salt': 'src.engine.salt.SaltHandler',
    'ansible': 'src.engine.ansible.AnsibleHandler',
}

PLUGINS_DICT = {
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.nic.NIC',
    'basic': 'src.plugins.basic.Basic',
    'cpu': 'src.plugins.cpu.Cpu',
    'main_board': 'src.plugins.main_board.MainBoard',
}

SSH_USER = 'root'
SSH_PWD = '1qaz@WSX'
SSH_PORT = '41022'

DEBUG = False

POST_ASSET_URL = 'http://127.0.0.1:8001/api/asset/'

LOG_NAME = 'itil.log'
LOG_FILE_PATH = os.path.join(BASE_DIR, 'log', 'log.log')

CERT_PATH = os.path.join(BASE_DIR, 'conf', 'cert')
# api验证的KEY
KEY = 'alkdjwqm'
