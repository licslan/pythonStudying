import paramiko

# 使用ptython调用Linux调用Linux发版任务


# 测试环境   11.24.201.223
HostIP = 'XXXXX'
username = 'XXX'
passwd = 'XXXXX'
# HostIP = '192.168.0.73'
# username = 'root'
# passwd = 'toor'


def run():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HostIP, 22, username, passwd)
        stdin, stdout, stderr = ssh.exec_command('cd /acme_dbgo;ls -l')
        print(stdout.read().strip())
        stdin, stdout, stderr = ssh.exec_command('ifconfig;free;df -h')
        # ssh.exec_command('echo "test" >> /a.txt')
        print(stdout.read())
        stdin, stdout, stderr = ssh.exec_command('whoami')
        print(stdout.read())
        print("----------------------START")
        stdin, stdout, stderr = ssh.exec_command('sudo su root;whoami')
        print(stdout.read())
        print("----------------------END")
        ssh.close()
    except Exception as ex:
        print("Error %s") % ex


if __name__ == '__main__':
    print("begin")
    run()