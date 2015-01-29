# -*- coding: utf-8 -*-
__author__ = 'Voronin Denis Albertovich'


import Server
import  datetime
from SysLog import AddToLog


class FIXi_client_thread(Server.ClientThread):


      def run(self):
        #self.get_session_info()

            while True:
                if self.type_input_data() == 'data':
                    self.get_data()

      def get_data(self):
        #try:
            print(str(datetime.datetime.now()) +  self.sess.ip + '---' + '  Reserve main data...<-- ', self.sess.data[5:])
            self.sess.sql_ins_data()
            print(str(datetime.datetime.now()) +  self.sess.ip + '---' + '  Send confirm data...  --> ', self.details[0])
            self. data_parse()
       #except Exception:
            #print(str(datetime.datetime.now()) +  self.sess.ip + '---' + '  Connection refuse...', self.details[0])

      def data_parse(self):
        if self.sess.data[0:14] == 'data//new_user':
            name = self.sess.data[15:len(self.sess.data) - 2]
            self.sess.sql_ins_user(name)
            self.channel.send(bytes('user_added', 'utf-8'))
            print(str(datetime.datetime.now()) + '  user_added')


class Server_fixi(Server.Server):
    host = '192.168.0.156'
    port = 1900
    def start_server(self):
        self.run = True


        print(str(datetime.datetime.now()) + '  +++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(str(datetime.datetime.now()) + "  ++ TCP Server Start, waiting clients...")
        print(str(datetime.datetime.now()) + '  ++ Server address: ' + self.host + '  Port: ' + str(self.port))
        print(str(datetime.datetime.now()) + '  +++++++++++++++++++++++++++++++++++++++++++++++++++')

        try:
            while True:
                if self.run:
                        channel, details = self.server_socket.accept()
                        FIXi_client_thread(channel, details).start()

        except Exception:
            print('---Server Stopped!----')

servfix = Server_fixi('192.168.0.156', 2000)



servfix.start_server()
