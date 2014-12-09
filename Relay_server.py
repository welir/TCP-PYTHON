__author__ = 'Voronin Denis Albertovich'

import server_threads
import Relay_control
from SysLog import AddToLog


count_relay = 4

class Relay_client_thread(server_threads.ClientThread):
      Relay = Relay_control.Relay(count_relay)

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
        s = 'data//'

        if self.sess.data == 'data//status\r\n':
                for i in range(1, count_relay + 1):
                    s += 'R' + str(i)+'-'+  self.Relay.Position[i - 1]
                self.channel.send(bytes(s,'utf-8'))
                print(s)

        for i in range(1, count_relay + 1):
            if self.sess.data == 'data//R'+ str(i) +'-on\r\n':
                 self.Relay.setPositionRelay(i,'on')
                 self.channel.send(bytes('R'+ str(i) +'-' + self.Relay.Position[i - 1], 'utf-8'))
                 print('R'+str(i)+'-' + self.Relay.Position[i - 1])
                 self.sess.data = ''
            if self.sess.data == 'data//R'+ str(i) +'-off\r\n':
                 self.Relay.setPositionRelay(i,'off')
                 self.channel.send(bytes('R'+ str(i) +'-' + self.Relay.Position[i - 1], 'utf-8'))
                 print('R'+str(i)+'-' + self.Relay.Position[i - 1])
                 self.sess.data = ''

        if self.sess.data == 'data//relays-off\r\n':
            self.Relay.setPositionAll('off')
            print('data//relays-off')
            self.channel.send(bytes('relays-off', 'utf-8'))
            self.sess.data = ''
        if self.sess.data == 'data//relays-on\r\n':
            self.Relay.setPositionAll('on')
            print('data//relays-on')
            self.channel.send(bytes('relays-on', 'utf-8'))
            self.sess.data = ''

        for i in range(count_relay):
            if self.sess.data == 'data//R'+str(i)+'-status\r\n':
                self.channel.send(bytes('data//R'+str(i)+'-' + self.Relay.Position[i-1], 'utf-8'))
                print('data//R'+str(i)+'-' + self.Relay.Position[i-1])
                self.sess.data = ''


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
