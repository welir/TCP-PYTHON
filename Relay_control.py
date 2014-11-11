__author__ = 'пользователь'
import DM


class Relay:
        Base = DM.BASE('sessions.db')
        Position = []
        Relays = []
        ## Инициализация класса

        def __init__(self, relay_count, default_position='off'):
            self.setRelayCount(relay_count, default_position)
            #self.setPositionAll(default_position)
            self.printaRelays()

        def printaRelays(self):
            print(self.Relays)
            print(self.Position)

        ## Добавление нового реле в список
        def addRelay(self, position='on'):
            r = str(len(self.Relays))

            self.Relays.append('R' + str(len(self.Relays) + 1))
            self.Position.append(position)
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
                self.Position.insert(relay_num - 1, 'on')
                self.Base.sql_update('Relays','Position','Relay',('on','R' + str(relay_num )))
            if position == 'off':
                self.Position.insert(relay_num - 1, 'off')
                self.Base.sql_update('Relays','Position','Relay',('off','R' + str(relay_num)))

        ## Установка положения по умолчанию всем реле

        def setPositionAll(self, position):
            for i in range(len(self.Relays)):
                self.setPositionRelay(i, position)



