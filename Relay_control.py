__author__ = 'пользователь'
import DM
import RPi.GPIO as GPIO

class Relay:
        Base = DM.BASE('sessions.db')
        Position = []
        Relays = []
        ## Инициализация класса
		
        def __init__(self, relay_count, default_position='off'):
            self.Base.sql_drop('Relays')
            self.setRelayCount(relay_count, default_position)
            #self.setPositionAll(default_position)
            self.printaRelays()
            self.init_gpio()
			
        def init_gpio(self):
            GPIO.setwarnings(False)
            GPIO.cleanup()
            GPIO.setmode(GPIO.BOARD)
			
        def set_gpio(self, num_relay, status):
                if  (num_relay == 1):
                    if status == 1:
                        GPIO.setup(11, GPIO.OUT)
                        GPIO.output(11, True)
                    else:
                        GPIO.setup(11, GPIO.OUT)
                        GPIO.output(11, False)
                if  (num_relay == 2 ):
                    if status == 1:
                        GPIO.setup(12, GPIO.OUT)
                        GPIO.output(12, True)
                    else:
                        GPIO.setup(12, GPIO.OUT)
                        GPIO.output(12, False)
                if  (num_relay == 3):
                    if status == 1:
                        GPIO.setup(15, GPIO.OUT)
                        GPIO.output(15, True)
                    else:
                        GPIO.setup(15, GPIO.OUT)
                        GPIO.output(15, False)
                if  (num_relay == 4):
                    if status == 1:
                        GPIO.setup(16, GPIO.OUT)
                        GPIO.output(16, True)
                    else:
                        GPIO.setup(16, GPIO.OUT)
                        GPIO.output(16, False)

        def printaRelays(self):
            print(self.Relays)
            print(self.Position)

        ## Добавление нового реле в список
        def addRelay(self, position='on'):
            r = str(len(self.Relays))

            self.Relays.append('R' + str(len(self.Relays) + 1))
            self.Position.append(position)
            self.printaRelays()
            try:
                self.Base.sql_insert('RELAYS', ('R' + str(len(self.Relays)), position))
            except:
                pass

        ## Удаление реле

        def dellRelay(self, Relay_num ):
            self.Relays.remove('R' + str(Relay_num))
            self.Position.pop(Relay_num)
            self.printaRelays()

        ## Установка количества реле в системе

        def setRelayCount(self, count, position):
                for i in range(count):
                    self.addRelay(position)

        ## Установка положения реле - on и off

        def setPositionRelay(self, relay_num, position):

            if position == 'on':
                self.Position.pop(relay_num - 1)
                self.Position.insert(relay_num - 1, 'on')
                self.Base.sql_update('Relays', 'Position', 'Relay', ('on', 'R' + str(relay_num)))
                self.set_gpio(relay_num,1)
            if position == 'off':
                self.Position.pop(relay_num - 1)
                self.Position.insert(relay_num - 1, 'off')
                self.Base.sql_update('Relays', 'Position', 'Relay', ('off', 'R' + str(relay_num)))
                self.set_gpio(relay_num,0)
        ## Установка положения по умолчанию всем реле

        def setPositionAll(self, position):
            for i in range(len(self.Relays)):
                self.setPositionRelay(i, position)
