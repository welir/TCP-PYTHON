from unittest.test.test_result import __init__

__author__ = 'Voronin Denis Albertovich'
import sqlite3
import datetime
base = 'sessions.db'
class BASE:

    def __init__(self, base):
        self.base = base

    def cr_base(self, exec_string = []):
        global conn
        try:
            conn = sqlite3.connect(base)
            c = conn.cursor()
            print("Initialization Database...")
            for i in range(len(exec_string)):
                c.execute(exec_string[i])
            # c.execute('CREATE TABLE IF NOT EXISTS SES (CLIENT_NAME TEXT, IP TEXT, DT DATE)')
            # c.execute('CREATE TABLE IF NOT EXISTS DATA (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, DT DATE, DATA TEXT)')
            # c.execute('CREATE TABLE IF NOT EXISTS LOG (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, DT DATE, LOG_SYS TEXT)')
            conn.commit()
            print('Initialization complete.')
            conn.close()
        except Exception:
            conn.close()
            print('Initialization Database Error!.')
            exit()


    def sql_insert(self, table, values):
        try:
            conn = sqlite3.connect(self.base)
            c = conn.cursor()
            c.execute('''INSERT INTO''' + table + '''VALUES''', values)
            conn.commit()
            conn.close()
            print( '---' + "Writing to base ... Ок")
        except sqlite3.DatabaseError:
            print('---' + "Error:", sqlite3.DatabaseError)

    # def sql_ins_data(self):
    #     try:
    #         conn = sqlite3.connect('sessions.db')
    #         c = conn.cursor()
    #         c.execute('''INSERT INTO DATA(dt,data) VALUES(:d2,:d3)''',
    #                   ((datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), self.data)))
    #         conn.commit()
    #         conn.close()
    #         print(self.ip + '---' + "Writing to base ... Ок")
    #     except sqlite3.DatabaseError:
    #         print(self.ip + '---' + "Error:", sqlite3.DatabaseError)
