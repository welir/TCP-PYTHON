# -*- coding: utf-8 -*-
__author__ = "Voronin Denis Аlbertovich"
# connection-oriented client

import socket
import datetime
import time
import base64

host = 'fhoc.no-ip.org'
port = 1800
data = 'client'
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect(to_host,to_port):
    try:
        client_socket.connect((to_host, to_port))
        print("[Connection established]")

    except Exception:
        print('[Connection error:  '+ to_host + ":" + str(port)+']')
        client_socket.close()
    pass


def run():
                global data
                with open('logo.png', "rb") as image_file:
                    data = base64.b64encode(image_file.read())

                print('---------------------------------------------------------------------------------------------')
                data_send = bytes('info//'+'pc_name:' + socket.gethostname() + 'ip:' + socket.gethostbyname(socket.gethostname()) + 'dt:' + (datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')), 'UTF-8')
                print("Send session data: " + str(socket.gethostname() + 'ip:' + socket.gethostbyname(socket.gethostname()) + 'dt:' + (datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))))
                client_socket.send(data_send)
                data_input = (client_socket.recv(1024).decode("UTF-8"))
                print("Waiting confirm session data...: ", data_input)
                if data_input.find('sess_ok',0) != -1:
                    print("Send main data: " + str(data))
                    client_socket.send(bytes('data//' + str(data),'UTF-8'))
                    data_input = (client_socket.recv(1024).decode("UTF-8"))
                    print("Waiting confirm main data..." + data_input)
                    client_socket.close()
                print('---------------------------------------------------------------------------------------------')

try:
    connect(host, port)
    while True:
        run()
        time.sleep(1)
except Exception:
    while True:
        #try:
            time.sleep(3)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect(host,port)
            run()
      #  except Exception:
        #    print('Connection Failed')


