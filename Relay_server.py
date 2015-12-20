__author__ = 'Voronin Denis Albertovich'

import Server
import Relay_control
from SysLog import AddToLog
import Tempered
count_relay = 4

class Relay_client_thread(Server.ClientThread):

      Relay = Relay_control.Relay(count_relay)
      Tmpr = Tempered.TemperatureSensor

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
            AddToLog(self.sess.ip + '---' + 'Reserve main data...<-- ' + self.sess.data[5:])
            self.sess.sql_ins_data()
            AddToLog(self.sess.ip + '---' + 'Send confirm data...  --> ' + self.details[0])
            self.data_parse()
        except Exception:
             AddToLog(self.sess.ip + '---' + 'Connection refuse...' +  self.details[0])

      def data_parse(self):
        s = 'data//'

        if self.sess.data == 'data//status\r\n':
                for i in range(1, count_relay + 1):
                    s += 'R' + str(i)+'-'+  self.Relay.Position[i - 1]
                self.channel.send(bytes(s,'utf-8'))
                AddToLog(s)

        for i in range(1, count_relay + 1):
            if self.sess.data == 'data//R'+ str(i) +'-on\r\n':
                 self.Relay.setPositionRelay(i,'on')
                 self.channel.send(bytes('R'+ str(i) +'-' + self.Relay.Position[i - 1]+"\r\n", 'utf-8'))
                 AddToLog('R'+str(i)+'-' + self.Relay.Position[i - 1])
                 self.sess.data = ''
            if self.sess.data == 'data//R'+ str(i) +'-off\r\n':
                 self.Relay.setPositionRelay(i,'off')
                 self.channel.send(bytes('R'+ str(i) +'-' + self.Relay.Position[i - 1]+"\r\n", 'utf-8'))
                 AddToLog('R'+str(i)+'-' + self.Relay.Position[i - 1])
                 self.sess.data = ''

        if self.sess.data == 'data//relays-off\r\n':
            self.Relay.setPositionAll('off')
            AddToLog('data//relays-off')
            self.channel.send(bytes('relays-off', 'utf-8'))
            self.sess.data = ''
        if self.sess.data == 'data//relays-on\r\n':
            self.Relay.setPositionAll('on')
            AddToLog('data//relays-on')
            self.channel.send(bytes('relays-on', 'utf-8'))

            self.sess.data = ''
        if self.sess.data == 'data//temp\r\n':
            self.channel.send(bytes(self.Tmpr.GetTempandVlaga,'utf-8'))
        for i in range(count_relay):
            if self.sess.data == 'data//R'+str(i)+'-status\r\n':
                self.channel.send(bytes('data//R'+str(i)+'-' + self.Relay.Position[i-1]+"\r\n", 'utf-8'))
                AddToLog('data//R'+str(i)+'-' + self.Relay.Position[i-1])
                self.sess.data = ''

ServRel = Server.Server('192.168.1.4', 1800, Relay_client_thread)

ServRel.start_server()
