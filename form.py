__author__ = 'пользователь'
# -*- coding: utf-8 -*-
import sys
import server_threads
import threading
#from PySide import QtGui
from tkinter import *
import threading

import time


from tkinter import *


class AppGUI(object):

    def __init__(self):
         self.tk = Tk()
         self.tk.geometry('800x300')
         frame = Frame()
         frame.pack()

         Button(frame, text="Запустить сервер", command = self.Startserv).pack(side = 'top')
         Button(frame, text="Остановить", command = self.Stopserv).pack(side = 'top')
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

