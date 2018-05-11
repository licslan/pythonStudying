import paramiko

# 测试环境   11.24.201.223
HostIP = '11.24.201.223'
username = 'crdadmin'
passwd = 'mTmtdieu%NNrh'


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HostIP, 22, username, passwd)
client.exec_command('sudo su root')
client.exec_command('echo "test" >> /a.txt')
client.close()