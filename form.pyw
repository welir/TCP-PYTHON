__author__ = 'пользователь'
# -*- coding: utf-8 -*-

import server_threads
#from PySide import QtGui
import threading
import sys
import time


from tkinter import *


class AppGUI(object):

    def __init__(self):
         self.tk = Tk()
         self.tk.geometry('100x50')
         frame = Frame()
         frame.pack()

         Button(frame, text="Run  Server", command = self.Startserv).pack(side = 'top')
         Button(frame, text="Stop Server", command = self.Stopserv).pack(side = 'top')
    def run(self):
            self.tk.mainloop()
    def Startserv(self):
        threading.Thread(target=self.event).start()

    def Stopserv(self):
        threading.Thread(target=self.stop).start()

    def event(self):
        server_threads.serv.start_server()

    def stop(self):
        server_threads.serv.stop_server()
root = AppGUI()

root.run()

