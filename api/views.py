from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
import paramiko


# Create your views here.

def asset(request):
    print(request.body.decode('utf-8'))
    return JsonResponse({'msg': 200, 'stat': '存储成功'})


def paramiko_info():
    private_key = paramiko.RSAKey.from_private_key_file(r'D:\globalconf\keyssh\root')

    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='10.2.40.10', port=41022, username='root', pkey=private_key)

    # 执行命令
    # stdin, stdout, stderr = ssh.exec_command('hostname')
    stdin, stdout, stderr = ssh.exec_command('salt 10.2.41.162 cmd.run  "hostname"')
    # 获取命令结果
    result = stdout.read()
    print(result.decode('utf-8'))
    # 关闭连接
    ssh.close()



if __name__ == '__main__':
    paramiko_info()
