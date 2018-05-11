import paramiko

hostname = '192.168.0.73'
username = 'root'
password = 'toor'
# ifconfig;free;df -h
if __name__ == '__main__':
    #  开启连接服务
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = s.exec_command('whoami')
    print(stdout.read())
    print("---------------欢迎使用昆山一键发版操作---------------------")
    print("---------------输入1：一键启动服务---------------------")
    print("---------------输入2：一键停止服务---------------------")
    stdin, stdout, stderr = s.exec_command('cd /tools/OneClick_StartAndStop;./kunShan_killAll.sh')
    # 接收用户输入
    name = input('请输入:  ')
    print(name)
    if name == 1:
        stdin, stdout, stderr = s.exec_command('cd /tools/OneClick_StartAndStop;./kunShan_killAll.sh')
        print(stdout.read())
    elif name == 2:
        stdin, stdout, stderr = s.exec_command('cd /tools/OneClick_StartAndStop;./kunShan_startAll.sh')
        print(stdout.read())
    print(name)
    #  停掉所有服务
    stdin, stdout, stderr = s.exec_command('ps -ef|grep tomcat')
    print(stdout.read())
    s.close()