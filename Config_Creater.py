import socket
import re
import json
'''
sentences_list = [
    ("接下来你需要回答几个问题来完成配置","Next, you need to answer a few questions to complete the configuration"),
    ("无法或取本地ip，请手动输入：","Unable to retrieve local IP address, please manually enter:"),
    ("请输入有效ip","Please enter a valid IP address"),
    ('Next')
]
'''

def print_logo():
    logo = '''
   ____                    __   _         
  / ___|   ___    _ __    / _| (_)   __ _ 
 | |      / _ \  | '_ \  | |_  | |  / _` |
 | |___  | (_) | | | | | |  _| | | | (_| |
  \____|  \___/  |_| |_| |_|   |_|  \__, |
                                    |___/ 
            '''
    print("\033[92m", logo, "\033[0m")

def is_valid_ip(ip_str):
    '''
    IP是否匹配
    :param ip_str:
    :return:
    '''
    # 定义IPv4地址的正则表达式模式
    ip_pattern = re.compile(r'^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)$')

    # 使用正则表达式进行匹配
    match = ip_pattern.match(ip_str)

    # 如果匹配成功，进一步检查每个数字是否在0到255之间
    if match:
        octets = ip_str.split('.')
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                return False
        return True
    else:
        return False

def get_local_ip():
    '''
    或取本地IP
    :return:
    '''
    try:
        # 创建一个临时套接字
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip
    except socket.error:
        return False

def main():
    conf = {
        "my_ip":None,
        "target_ip":None,
        "port":2024,
    }
    print("[*]开始或取本机IP")
    my_ip = get_local_ip()
    if not my_ip:
        my_ip = input('\033[91m[err]或取本机IP失败，请手动输入：\033[0m')
        while True:
            if not is_valid_ip(my_ip):
                my_ip = input('\033[91m[err]ip输入有误，请输入正确的ip：\033[0m')
            else:
                break
    conf["my_ip"] = my_ip
    target_ip = input('[*]输入目标ip：')
    while True:
        if not is_valid_ip(target_ip):
            target_ip = input('\033[91m[err]ip输入有误，请输入正确的ip：\033[0m')
        else:
            break
    conf["target_ip"] = target_ip
    with open('config.json',mode='wt',encoding='utf-8')as f:
        f.write(json.dumps(conf))
    print("[*]配置设置完成，按任意键退出")
if __name__ == '__main__':
    try:
        print_logo()
        main()
    except KeyboardInterrupt:
        print("\n")
        print("配置程序已退出".center(25,'*'))
