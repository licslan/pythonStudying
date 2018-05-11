# 在自动化运维过程中,需要远程服务器切换到root用户下执行命令,尝试了一些方法,得到如下好用的方法,供大家使用:

import time
import paramiko


def verification_ssh(host, username, password, port, root_pwd, cmd):
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=host, port=int(port), username=username, password=password)

    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('sudo su root')
        buff = ''
        while not buff.endswith('Password: '):
            resp = ssh.recv(9999)
            buff += resp
        ssh.send(root_pwd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff += resp
        ssh.send(cmd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff += resp
        s.close()
        result = buff
        print("XXXXXXXXXXXXXX "+result)
    else:
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        print("YYYYYYYYYYYYY " + result)
        print(result)
        s.close()
    return result


if __name__ == "main":
    verification_ssh('192.168.0.73', 'root', 'toor', 22, 'toor', 'echo "test" >> /testing.txt')