# -*- coding: utf-8 -*-

__author__ = 'Voronin Denis Albertovich'
import sqlite3
import os
import datetime
from SysLog import AddToLog
base = 'sessions.db'
class BASE:

    def __init__(self, base):
        self.base = base

    def cr_base(self, exec_string = []):
        global conn
        try:
            conn = sqlite3.connect(base)
            c = conn.cursor()
            AddToLog("Initialization Database...")
            for i in range(len(exec_string)):
                c.execute(exec_string[i])
            conn.commit()
            AddToLog('Initialization complete.')
            conn.close()
        except Exception:
            conn.close()
            AddToLog('Initialization Database Error!.')
            exit()

    def del_base(self):
        try:
            os.remove(base)
            AddToLog('Database removed.')
        except EOFError:
                AddToLog('Error removing base ')
        except PermissionError:
                AddToLog('Процесс не может получить доступ к базе, так как этот файл занят другим процессом,попробуте закрыть все программы, которые используют базу ')

    def sql_insert(self, table, values):

            conn = sqlite3.connect(self.base)
            c = conn.cursor()
            c.execute('''INSERT INTO ''' + table + ''' VALUES(:s1,:s2)''' , values)
            conn.commit()
            conn.close()
            AddToLog( '---' + "Writing to base ... Ок")

    def sql_drop(self, table):

            conn = sqlite3.connect(self.base)
            c = conn.cursor()
            c.execute('''DELETE FROM ''' + table)
            conn.commit()
            conn.close()
            AddToLog( '---' + 'Delete from Table ' + table + '... Ок')

    def sql_update(self, table, Row,  where_, values):

            conn = sqlite3.connect(self.base)
            c = conn.cursor()
            c.execute('''UPDATE ''' + table + ''' SET '''+ Row +'''  =  :v1 where   ''' + where_ +''' = :v2  ''' , values)
            conn.commit()
            conn.close()
            AddToLog( '---' + "Update base ... Ок")

    # def sql_ins_data(self):
    #     try:
    #         conn = sqlite3.connect('sessions.db')
    #         c = conn.cursor()
    #         c.execute('''INSERT INTO DATA(dt,data) VALUES(:d2,:d3)''',
    #                   ((datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), self.data)))
    #         conn.commit()
    #         conn.close()
    #         AddToLog(self.ip + '---' + "Writing to base ... Ок")
    #     except sqlite3.DatabaseError:
    #         AddToLog(self.ip + '---' + "Error:", sqlite3.DatabaseError)
