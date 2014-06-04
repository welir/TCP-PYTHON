# -*- coding: utf-8 -*-
__author__ = "Voronin Denis Albertovich"
# connection-oriented server


import socket
import sqlite3
import os
import datetime
import threading
import time
import sys

#Server options
host = '192.168.1.11'
port = 1800

# We'll pickle a list of numbers:


class SessionData:

    client_name = 'unknown'
    ip = '127.0.0.1'
    dt = datetime.datetime.now
    data = ''

    def parse_inp_str(self, inp_str):
        if inp_str.find('pc_name', 0, len(inp_str)) != -1:

            self.client_name = inp_str[inp_str.find('pc_name:', 0) + 8 : inp_str.find('ip:', 0)]

            self.ip          = inp_str[inp_str.find('ip:', 0) + 3       : inp_str.find('dt:', 0)]

            self.dt          = inp_str[inp_str.find('dt:', 0) + 3       :]

    def sql_ins_session(self):
        try:
            conn = sqlite3.connect('sessions.db')
            c = conn.cursor()
            c.execute('''INSERT INTO SES VALUES(:s1,:s2,:s3)''', (self.client_name, self.ip, self.dt))
            conn.commit()
            conn.close()
        except Exception:
            print("Ошибка базы данных")

    def sql_ins_data(self):
        try:
            conn = sqlite3.connect('sessions.db')
            c = conn.cursor()
            c.execute('''INSERT INTO DATA(dt,data) VALUES(:d2,:d3)''', ((datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), self.data)))
            conn.commit()
            conn.close()
        except sqlite3.Exception:
            print(self.ip + '---' + "Ошибка:", sqlite3.Exception)
        else:
            print(self.ip + '---' + "Запись данных в базу: Ок")

# Our thread class:
class ClientThread(threading.Thread):
    sess = SessionData()

    # Override Thread's __init__ method to accept the parameters needed:

    def __init__(self, channel, details):
        self.channel = channel
        self.details = details
        threading.Thread.__init__(self)

    def run(self):
            #self.get_session_info()
            try:
                while True:
                    if self.type_input_data() == 'info':
                        self.get_session_info()
                    if self.type_input_data() == 'data':
                        self.get_data()
            except Exception:
                print('Неизветный тип возвращаемых данных')

    def listen_data(self):
        return (str(self.channel.recv(1024).decode("utf-8")))

    def type_input_data(self):

        data = self.listen_data()

        if data.find('info//', 0) != -1:
            self.sess.parse_inp_str(data)
            return 'info'

        if data.find('data//', 0) != -1:
            self.sess.data = data
            return 'data'

    def get_session_info(self):

                try:
                    print("-----------------------------------------------------------------")
                    print(self.sess.ip + '---' + 'Пришла информация о соединении <-- ', self.sess.client_name + ' ' + self.sess.dt + ' ' + self.sess.ip)
                    self.sess.sql_ins_session()
                    print(self.sess.ip + '---' + 'Отправляем подтверждениео о получении --> ',  self.details[0])
                    self.channel.send(bytes('sess_ok ' + str(self.channel), 'utf-8'))
                    time.sleep(1)
                except Exception:
                    print('Не удалось доставить данные, соединение потеряно c клиентом ', self.details[0])

    def get_data(self):
                try:
                    print(self.sess.ip + '---' + 'Пришли полезные данные <-- ' , self.sess.data[5:])
                    self.sess.sql_ins_data()
                    print(self.sess.ip + '---' + 'Отправляем подтверждениео о получении --> ' ,  self.details[0])
                    self.channel.send(bytes('data_ok', 'utf-8'))
                    print("-----------------------------------------------------------------")
                    time.sleep(1)
                except Exception:
                    print(self.sess.ip + '---' + 'Не удалось доставить данные, соединение потеряно c клиентом ', self.details[0])


curr_sess = SessionData()

class Server:
    run = False
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.settimeout(1024)
    server_socket.listen(10)

    def init(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.settimeout(1024)
        self.server_socket.listen(10)


    def start_server(self):
        self.run = True

        if serv.server_socket._closed:
            self.init()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("++ Сервер запущен, ожидание подключения клиентов")
        print('++ Адрес сервера: '+ host + ' Порт: ' + str(port))
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        try:
            while True:
                if self.run:
                    channel, details = self.server_socket.accept()
                    ClientThread(channel, details).start()
        except Exception:
            print('---Сервер остановлен!----')


    def stop_server(self):

        try:
                self.server_socket.close()
                self.run = False
                exit()
        except Exception:
                print('---не удалось остановить сервер!----')

serv = Server()

def cr_base():
    try:
        conn = sqlite3.connect('sessions.db')
        c = conn.cursor()
        print('Выполняется инициализация базы данных...')
        c.execute("CREATE TABLE IF NOT EXISTS SES (CLIENT_NAME TEXT, IP TEXT, DT DATE)")
        c.execute("CREATE TABLE IF NOT EXISTS DATA (ID integer PRIMARY KEY AUTOINCREMENT NOT NULL, DT DATE, DATA TEXT)")
        conn.commit()
        print('Инициализация завершена.')
        conn.close()
    except Exception:
        conn.close()
        print('Ошибка инициализации.')
        exit()




base_locate = os.curdir



if not os.path.exists(base_locate + '/sessions.db'):
    if not os.path.isfile(base_locate + '/sessions.db'):
        cr_base()

#Запуск сервера
serv.start_server()
#serv.stop_server
