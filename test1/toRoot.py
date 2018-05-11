import paramiko
import time

host = '11.24.201.223'
port = '22'
username = 'crdadmin'
passwd = 'mTmtdieu%NNrh'

s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(hostname = host,port=int(port),username=username, password=passwd)
#ssh = s.invoke_shell()
time.sleep(2)
#ssh.send('su root')
stdin, stdout, stderr = s.exec_command("whoami;pwd;")
result1 = stdout.read()
print(result1)
#stdin, stdout, stderr = s.exec_command("cd /;ls -l")
#result = stdout.read()
#print(result)
