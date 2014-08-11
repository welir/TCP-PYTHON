__author__ = 'пользователь'

filename = 'Log.txt'


def AddToLog(str):
    log = open(filename,'a')
    try:
        log.writelines(str)
    finally:
        log.close()
