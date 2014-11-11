__author__ = 'пользователь'
class Relay:
        Position = []
        Relays = []

        def addRelay(self):
            self.Relays.append('R' + str(len(self.Relays)))

        def setRelayCount(self, count):
            for i in range(count):
                self.addRelay()

        def setPositionRelay(self, relay_num, position):
            """

            :rtype : object
            """
            if position == 'on':
                self.Position.insert(relay_num, 'on')
            if position == 'off':
                self.Position.insert(relay_num, 'off')

        def setPositionAll(self, position):
            for i in self.Relays:
                self.setPositionRelay(i, position)



Rel = Relay()

Rel.setRelayCount(100)
Rel.setPositionAll(5)

print(Rel.Relays)
print(Rel.Position)