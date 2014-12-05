__author__ = 'Voronin Denis Albertovich'

import server_threads
import Relay_control
from SysLog import AddToLog



class Relay_client_thread(server_threads.ClientThread):
      Relay = Relay_control.Relay(4)

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
            print(self.sess.ip + '---' + 'Reserve main data...<-- ', self.sess.data[5:])
            self.sess.sql_ins_data()
            print(self.sess.ip + '---' + 'Send confirm data...  --> ', self.details[0])
            self. data_parse()
        except Exception:
            print(self.sess.ip + '---' + 'Connection refuse...', self.details[0])

      def data_parse(self):
        if self.sess.data == 'data//R1-on\r\n':
            self.Relay.setPositionRelay(1,'on')
            self.channel.send(bytes('R1-' + self.Relay.Position[0], 'utf-8'))
            print('R1-' + self.Relay.Position[0])
        if self.sess.data == 'data//R1-off\r\n':
            self.Relay.setPositionRelay(1,'off')
            self.channel.send(bytes('R1-' + self.Relay.Position[0], 'utf-8'))
            print('R1-' + self.Relay.Position[0])
        if self.sess.data == 'data//R2-on\r\n':
            self.Relay.setPositionRelay(2,'on')
            self.channel.send(bytes('R2-' + self.Relay.Position[1], 'utf-8'))
            print('R2-' + self.Relay.Position[1])
        if self.sess.data == 'data//R2-off\r\n':
            self.Relay.setPositionRelay(2,'off')
            self.channel.send(bytes('R2-' + self.Relay.Position[1], 'utf-8'))
            print('R2-' + self.Relay.Position[1])
        if self.sess.data == 'data//R3-on\r\n':
            self.Relay.setPositionRelay(3,'on')
            self.channel.send(bytes('R3-' + self.Relay.Position[2], 'utf-8'))
            print('R3-' + self.Relay.Position[2])
        if self.sess.data == 'data//R3-off\r\n':
            self.Relay.setPositionRelay(3,'off')
            self.channel.send(bytes('R3-' + self.Relay.Position[2], 'utf-8'))
            print('R3-' + self.Relay.Position[2])
        if self.sess.data == 'data//R4-on\r\n':
            self.Relay.setPositionRelay(4,'on')
            self.channel.send(bytes('R4-' + self.Relay.Position[3], 'utf-8'))
            print('R4-' + self.Relay.Position[3])
        if self.sess.data == 'data//R4-off\r\n':
            self.Relay.setPositionRelay(4,'off')
            self.channel.send(bytes('R4-' + self.Relay.Position[3], 'utf-8'))
            print('R4-' + self.Relay.Position[3])

        if self.sess.data == 'data//relays-off\r\n':
            self.Relay.setPositionAll('off')
            print('data//relays-off')
            self.channel.send(bytes('relays-off', 'utf-8'))

        if self.sess.data == 'data//relays-on\r\n':
            self.Relay.setPositionAll('on')
            print('data//relays-on')
            self.channel.send(bytes('relays-on', 'utf-8'))

        if self.sess.data == 'data//R1-status\r\n':
            self.channel.send(bytes('data//R1-' + self.Relay.Position[0], 'utf-8'))
            print('data//R1-' + self.Relay.Position[0])
        if self.sess.data == 'data//R2-status\r\n':
            self.channel.send(bytes('data//R2-' + self.Relay.Position[1], 'utf-8'))
            print('data//R2-' + self.Relay.Position[1])
        if self.sess.data == 'data//R3-status\r\n':
            self.channel.send(bytes('data//R3-' + self.Relay.Position[2], 'utf-8'))
            print('data//R3-' + self.Relay.Position[2])
        if self.sess.data == 'data//R4-status\r\n':
            self.channel.send(bytes('data//R4-' + self.Relay.Position[3], 'utf-8'))
            print('data//R4-' + self.Relay.Position[3])

        if self.sess.data == 'data//status\r\n':
            self.channel.send(bytes('data//R1-' + self.Relay.Position[0] + 'R2-' + self.Relay.Position[1] +'R3-'+ self.Relay.Position[2] + 'R4-'  +  self.Relay.Position[3], 'utf-8'))
            print('data//R1-' + self.Relay.Position[0] + ' R2-' + self.Relay.Position[1]  + ' R3-'+ self.Relay.Position[2] + ' R4-' + self.Relay.Position[3])

class Server_relay(server_threads.Server):

    def start_server(self):
        self.run = True
        if servRel.server_socket._closed:
            self.init()

        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("++ TCP Server Start, waiting clients...")
        print('++ Server address: ' + self.host + '  Port: ' + str(self.port))
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')

        try:
            while True:
                if self.run:
                        channel, details = self.server_socket.accept()
                        Relay_client_thread(channel, details).start()

        except Exception:
            print('---Server Stopped!----')

servRel = Server_relay()

servRel.start_server()
