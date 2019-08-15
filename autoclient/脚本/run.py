def agent():
    #  ###########   agent  ###########

    import subprocess
    import requests

    disk = subprocess.getoutput('idd')[:20]
    nic = subprocess.getoutput('ipconfig')

    url = 'http://127.0.0.1:8000/api/asset/'

    import json

    info = {'disk': {'slot1':{'中文':'xx'}}, 'nic':{'slot1':{'qqq':'qq'}}}
    ret = requests.post(
        url=url,
        # data=json.dumps(info,ensure_ascii=False).encode('utf-8'),
        data={'k1':'v1','k2':'v2'},
        # json={'disk': {'slot1':{'中文':'xx'}}, 'nic':{'slot1':{'qqq':'qq'}}},
    )
    print(ret.text)
    print(ret.json())


def ssh():
    #  ###########   ssh  ###########

    import requests

    import paramiko

    # private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(hostname='10.0.0.128', port=22, username='root', password='1')

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('ls')
    # 获取命令结果
    result = stdout.read()

    print(result.decode('utf-8'))
    # 关闭连接
    ssh.close()

    url = 'http://127.0.0.1:8000/api/asset/'

    ret = requests.post(
        url=url,
        data={'msg': result.decode('utf-8')},
    )
    print(ret.text)
    print(ret.json())


def salt():
    #  ###########   salt  ###########

    import subprocess
    ret = subprocess.getoutput("salt '{}' cmd.run '{}' ".format('*', 'ls'))

    import salt.client
    local = salt.client.LocalClient()
    result = local.cmd('c2.salt.com', 'cmd.run', ['ifconfig'])


mode = 'agent'
if mode == 'agent':
    agent()
elif mode == 'ssh':
    ssh()
elif mode == 'salt':
    salt()
