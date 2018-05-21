import PortScannerUtils as ps
import datetime


def main(id):
    # Initialize a Scanner object that will scan top 50 commonly used ports.
    host_list = {
        # 生产的服务康面  KM
        '109': ["11.24.201.109", "康面测试", [80, 21, 8080, 9090, 8765, 8880, 6379, 2181, 27017, 9102]],
        '110': ["11.24.201.110", "康面生产电子票", [80, 3306, 46567]],
        '130': ["11.24.201.130", "康面生产", [80, 21, 8080]],
        # 生产的服务康饮  KY
        '79': ["11.24.200.79", "反向代理服务用户1(ALL)", [27017, 9102, 2181, 8080, 9090, 21, 8765, 8880]],
        '27': ["11.24.200.27", "反向代理服务用户2/TASK", [2181, 8080, 9090]],
        '172': ["11.24.201.172", "接收SAP数据服务", [9102, 2181, 8080, 9090]],
        '224': ["11.24.200.224", "接收回调数据服务", [9102, 2181, 8080, 9090]],
        '36': ["11.24.201.36", "电子票服务/ftp服务", [9090, 21, 8765, 8880]],
        # 生产的服务百饮  BY
        '6': ["11.24.201.6", "反向代理服务用户1(ALL)", [27017, 9102, 2181, 8080, 9090, 21, 8765, 8880]],
        '230': ["11.24.200.230", "反向代理服务用户2/TASK", [2181, 8080, 9090]],
        '231': ["11.24.200.231", "接收SAP数据服务", [9102, 2181, 8080, 9090]],
        '233': ["11.24.200.233", "接收回调数据服务", [9102, 2181, 8080, 9090]],
        '225': ["11.24.200.225", "电子票服务/ftp服务", [9090, 21, 8765, 8880]],
        # 生产的服务昆山  KS
        '153': ["172.18.1.153", "153运行ACME", [18888, 8888, 18080, 8080, 2181]],
        '154': ["172.18.1.154", "154运行VICA、mongodb、redis服务",
                [8880, 28880, 8080, 21, 20, 8080, 28080, 27017, 11433, 28765, 8765, 6379, 22]],
        '155': ["172.18.1.155", "sqlserver2016数据库服务端", [1433]],
        # 测试的服务昆山  KS
        '73': ["192.168.0.73", "153运行ACME", [6379, 27017, 18080, 8080, 2181]],

    }
    host_name = '11.24.201.109'
    port_list = []  # 端口列表
    host_title = "服务器为："
    host_name = host_list[id][0]
    port_list = host_list[id][2]

    scanner = ps.PortScannerUtils(target_ports=port_list)
    # print (target_ports)
    print('当前扫描的服务器信息:\t')
    print(host_title + host_list[id][1] + "\t")
    print('扫描时间：%s\t' % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("IP:%s" % host_name)
    print("扫描的的端口列表：:%s" % port_list)

    message = 'put whatever message you want here'

    '''
    output contains a dictionary of {port:status} pairs
    in which port is the list of ports we scanned 
    and status is either 'OPEN' or 'CLOSE'
    '''

    # This line sets the thread limit of the scanner to 1500
    scanner.set_thread_limit(1500)

    # This line sets the timeout delay to 15s
    scanner.set_delay(15)

    # This line shows the target port list of the scanner
    scanner.show_target_ports()
    '''
    Current port list is: 
    [blah, blah ....]
    '''

    # This line shows the timeout delay of the scanner
    scanner.show_delay()
    '''
    Current timeout delay is 15 seconds.
    '''

    # This line shows the top 100 commonly used ports.
    # scanner.show_top_k_ports(100)
    '''
    Top 100 commonly used ports:
    [blah, blah ....]
    '''

    output = scanner.scan(host_name, message)
    '''
    start scanning website: google.com
    server ip is: 172.217.4.110
    80: OPEN

    443: OPEN

    2000: OPEN

    5060: OPEN

    host google.com scanned in  30.956103 seconds
    finish scanning!
    '''


# 定义一个数组
ipsKM = [
    '109', '110', '130'
]

ipsKY = [
    '79', '27', '172', '224', '36',
]

ipsBY = [
    '6', '230', '231', '233', '225',
]

ipsKS = [
    '153', '154', '155'
]

ipsNone = []

ipsALL = [
    '109', '110', '130',
    '79', '27', '172', '224', '36',
    '6', '230', '231', '233', '225',
    '153', '154', '155'
]

if __name__ == "__main__":
    print("请输入你要扫描的类型：1[输入1，扫描康面]  2[输入2，扫描康饮]"
          " 3[输入3，扫描百饮] 4[输入4，扫描昆山]  5[输入5,扫描所有] 0[不扫描 pass]")
    inSomethng = input('请输入您的选择: ')
    if int(inSomethng) == 1:
        for x in ipsKM:
            main(x)
    elif int(inSomethng) == 2:
        for x in ipsKY:
            main(x)
    elif int(inSomethng) == 3:
        for x in ipsBY:
            main(x)
    elif int(inSomethng) == 4:
        for x in ipsKS:
            main(x)
    elif int(inSomethng) == 5:
        for x in ipsALL:
            main(x)
    else:
        print("您选择了不扫描！！")
