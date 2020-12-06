#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Describe :
# @Time     : 12/6/20 2:37 PM
# @Author   : Jinlei
import socket
import json

HOST = 'localhost'
PORT = 10000

ECHO_FILE = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(ECHO_FILE)

try:
    with open('zhihu_answers.json', "r", encoding='utf-8') as f:
        # 如果本地有文件，就打开，然后覆盖之前的 json_str
        json_str = json.dumps(f.read())
except Exception as e:
    print(f'warning: {e}')


def echo_client():
    """
        Echo Server 的 Client 端
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        # 发送数据到服务端
        s.sendall(json_str.encode(encoding='utf-8'))

        # 接收服务端数据
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))  # 为什么返回结果不是中文？
            break  # 测试，传一次就好

    s.close()


if __name__ == '__main__':
    echo_client()
