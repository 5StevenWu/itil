from .base import SshAndSaltHandler
from lib.conf import settings



class SshHandler(SshAndSaltHandler):

    def cmd(self, command, hostname=None):
        import paramiko

        # private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

        # 创建SSH对象
        ssh = paramiko.SSHClient()

        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, password=settings.SSH_PWD)

        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        ret = stdout.read()

        ssh.close()

        return ret

