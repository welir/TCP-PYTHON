# -*- coding: utf-8 -*-
__author__ = 'Voronin Denis Albertovich'


import Server
import  datetime
from SysLog import AddToLog




class GPS_client_thread(Server.ClientThread):


      def run(self):
        #self.get_session_info()
        try:
            while True:
                if self.type_input_data() == 'data':
                    self.get_data()
        except Exception:
            AddToLog('Unknown reserving data type')



      def get_data(self):
        try:
            print(str(datetime.datetime.now()) +self.sess.ip + '---' + '  Reserve main data...<-- ', self.sess.data[5:])
            self.sess.sql_ins_data()
            print(str(datetime.datetime.now()) +  self.sess.ip + '---' + '  Send confirm data...  --> ', self.details[0])
            self. data_parse()
        except Exception:
            print(str(datetime.datetime.now()) +  self.sess.ip + '---' + '  Connection refuse...', self.details[0])

      def data_parse(self):
        if self.sess.data[0:16] == 'data//GPS-status':
            self.channel.send(bytes( 'GPS-OK', 'utf-8'))
            print(str(datetime.datetime.now()) + '  GPS-OK')


servGps = Server.Server('192.168.0.156', 1900,  GPS_client_thread)

servGps.start_server()
