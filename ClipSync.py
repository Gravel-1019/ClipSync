import socket
import sys
from threading import Thread
import pyperclip
import time
import json

with open('config.json', mode='rt', encoding='utf-8') as f:
    content = f.read()
conf = json.loads(content)
my_ip = conf["my_ip"]
target_ip = conf["target_ip"]
port = conf["port"]
def monitor_clipboard():
    # 初始剪贴板内容
    previous_clipboard_content = pyperclip.paste()

    while True:
        # 获取当前剪贴板内容
        current_clipboard_content = pyperclip.paste()
        # 检查剪贴板内容是否发生变化
        if current_clipboard_content != previous_clipboard_content:
            sock = socket.socket()
            sock.connect((target_ip,port))
            if len(current_clipboard_content.encode('utf-8')) > 4096:
                pass
            sock.sendall(current_clipboard_content.encode('utf-8'))


            previous_clipboard_content = current_clipboard_content
        # 等待一段时间后再次检查，可以根据需要调整时间间隔
        time.sleep(1)

def start_server(host, port):
    # 创建一个套接字对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址和端口
    server_socket.bind((host, port))

    # 开始监听
    server_socket.listen(1)

    while True:
        # 等待客户端连接
        client_socket, client_address = server_socket.accept()

        data = client_socket.recv(4096)
        data = data.decode('utf-8')
        pyperclip.copy(data)

        # 关闭与客户端的连接
        client_socket.close()

def main():

    t1 = Thread(target=monitor_clipboard)
    t1.start()
    t2 = Thread(target=start_server,args=(my_ip,port))
    t2.start()




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("程序已退出".center(50, '*'))
        sys.exit()
    except OSError:
        print("2024端口被占用，请停止改端口的进程或在config.json中更改默认端口".center(50, '*'))
        sys.exit()
    except ConnectionRefusedError:
        print("请确认目标计算机开启程序")
        sys.exit()
