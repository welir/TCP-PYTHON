__author__ = 'Voronin Denis Albertovich'


import server_threads
import  datetime
from SysLog import AddToLog




class GPS_client_thread(server_threads.ClientThread):


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


class Server_gps(server_threads.Server):
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
                        GPS_client_thread(channel, details).start()

        except Exception:
            print('---Server Stopped!----')

servGps = Server_gps(server_threads.get_my_ip(), 1900)

servGps.start_server()
