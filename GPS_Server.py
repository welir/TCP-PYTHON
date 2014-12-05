__author__ = 'Voronin Denis Albertovich'


import server_threads

from SysLog import AddToLog
host = '192.168.0.156'
port = 1900



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
            print(self.sess.ip + '---' + 'Reserve main data...<-- ', self.sess.data[5:])
            self.sess.sql_ins_data()
            print(self.sess.ip + '---' + 'Send confirm data...  --> ', self.details[0])
            self. data_parse()
        except Exception:
            print(self.sess.ip + '---' + 'Connection refuse...', self.details[0])

      def data_parse(self):
        if self.sess.data[0:15] == 'data//GPS-status':
            self.channel.send(bytes('GPS-OK', 'utf-8'))
            print('GPS-OK')


class Server_gps(server_threads.Server):

    def start_server(self):
        self.run = True
        if servGps.server_socket._closed:
            self.init()

        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("++ TCP Server Start, waiting clients...")
        print('++ Server address: ' + host + '  Port: ' + str(port))
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')

        try:
            while True:
                if self.run:
                        channel, details = self.server_socket.accept()
                        GPS_client_thread(channel, details).start()

        except Exception:
            print('---Server Stopped!----')

servGps = Server_gps()

servGps.start_server()
