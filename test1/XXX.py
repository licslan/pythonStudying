import os
import sys


if __name__ == '__main__':
    # 提升到root权限
    if os.geteuid():
        args = [sys.executable] + sys.argv
        # 下面两种写法，一种使用su，一种使用sudo，都可以
        #os.execlp('su', 'su', '-c', ' '.join(args))
        os.execlp('sudo', 'sudo', *args)

    # 从此处开始是正常的程序逻辑
    print('Running at root privilege. Your euid is', os.geteuid())
