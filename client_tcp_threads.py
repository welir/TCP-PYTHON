# -*- coding: utf-8 -*-
__author__ = "Voronin Denis Аlbertovich"
# connection-oriented client

import socket
import datetime
import time




host = '192.168.1.11'
port = 1800
data = 'client'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(to_host,to_port):
    try:
        client_socket.connect((to_host, to_port))
        print("Соединение установлено")
    except Exception:
        print('Ошибка подключения к серверу:  '+ to_host + ":" + str(port))
        client_socket.close
    pass


def run():

                print('---------------------------------------------------------------------------------------------')
                data_send = bytes('info//'+'pc_name:' + socket.gethostname() + 'ip:' + socket.gethostbyname(socket.gethostname()) + 'dt:' + (datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')), 'UTF-8')
                print("Отправляем данные о подключении: " + str(socket.gethostname() + 'ip:' + socket.gethostbyname(socket.gethostname()) + 'dt:' + (datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))))
                client_socket.send(data_send)
                data_input = (client_socket.recv(1024).decode("UTF-8"))
                print("Ожидаем подтверждения: ", data_input)
                if data_input.find('sess_ok',0) != -1:
                    print("Отправляем полезные данные: " + data)
                    client_socket.send(bytes('data//' + data,'UTF-8'))
                    data_input = (client_socket.recv(1024).decode("UTF-8"))
                    print("Ожидаем подтверждения: " + data_input)
                print('---------------------------------------------------------------------------------------------')

try:
    connect(host, port)
    while True:
        run()
        time.sleep(1)
except Exception:
    while True:
        try:
            time.sleep(3)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect(host,port)
            run()
        except Exception:
            pass


