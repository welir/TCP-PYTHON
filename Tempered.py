import RPi.GPIO as GPIO
import time


def bin2dec(string_num):
    return str(int(string_num, 2))


class TemperatureSensor():
    def __init__(self):
        data = []

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        GPIO.output(4, GPIO.HIGH)
        time.sleep(0.025)
        GPIO.output(4, GPIO.LOW)
        time.sleep(0.02)

        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        for i in range(0, 500):
          data.append(GPIO.input(4))


bit_count = 0
tmp = 0
count = 0
HumidityBit = ""
TemperatureBit = ""
crc = ""
Humidity = 0
Temperature = 0


def GetTempandVlaga(self):
    try:
        while self.data[self.count] == 1:
            self.tmp = 1
            self.count = self.count + 1

        for i in range(0, 32):
            self.bit_count = 0

            while self.data[self.count] == 0:
               self.tmp = 1
                self.count = self.count + 1

            while self.data[count] == 1:
                self.bit_count =self.bit_count + 1
                self.count = self.count + 1

            if self.bit_count > 3:
                if i >= 0 and i < 8:
                    self.HumidityBit = self.HumidityBit + "1"
                if i >= 16 and i < 24:
                    self.TemperatureBit = self.TemperatureBit + "1"
            else:
                if i >= 0 and i < 8:
                    self.HumidityBit = self.HumidityBit + "0"
                if i >= 16 and i < 24:
                    self.TemperatureBit = self.TemperatureBit + "0"

    except:
        return "ERR_RANGE"

    try:
        for i in range(0, 8):
            self.bit_count = 0

            while data[self.count] == 0:
                self.tmp = 1
                self.count = self.count + 1

            while data[self.count] == 1:
                self.bit_count = self.bit_count + 1
                self.count = self.count + 1

            if self.bit_count > 3:
               self.crc = self.crc + "1"
            else:
               self.crc = self.crc + "0"
    except:
        return "ERR_RANGE"

    self.Humidity = bin2dec(self.HumidityBit)
    self.Temperature = bin2dec(self.TemperatureBit)

    if int(self.Humidity) + int(self.Temperature) - int(bin2dec(self.crc)) == 0:
        return "Humidity:" + self.Humidity + "%" + " "" Temperature:" + self.Temperature + "C"
    else:
        return "ERR_CRC"
