__author__ = 'пользователь'

filename = 'Log.txt'
import datetime

def AddToLog(str_):
    log = open(filename,'a')
    try:
        str_ = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S') + '  ' +  str_
        print(str_)
        log.writelines(str_ + '\r\n')
    finally:
        log.close()
