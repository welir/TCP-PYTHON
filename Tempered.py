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
        while this.data[this.count] == 1:
            this.tmp = 1
            this.count = this.count + 1

        for i in range(0, 32):
            this.bit_count = 0

            while data[this.count] == 0:
                this.tmp = 1
                this.count = this.count + 1

            while data[count] == 1:
                this.bit_count = this.bit_count + 1
                this.count = this.count + 1

            if bit_count > 3:
                if i >= 0 and i < 8:
                    this.HumidityBit = this.HumidityBit + "1"
                if i >= 16 and i < 24:
                    this.TemperatureBit = this.TemperatureBit + "1"
            else:
                if i >= 0 and i < 8:
                    this.HumidityBit = this.HumidityBit + "0"
                if i >= 16 and i < 24:
                    this.TemperatureBit = this.TemperatureBit + "0"

    except:
        return "ERR_RANGE"

    try:
        for i in range(0, 8):
            this.bit_count = 0

            while data[this.count] == 0:
                this.tmp = 1
                this.count = this.count + 1

            while data[this.count] == 1:
                this.bit_count = this.bit_count + 1
                this.count = this.count + 1

            if this.bit_count > 3:
                this.crc = this.crc + "1"
            else:
                this.crc = this.crc + "0"
    except:
        return "ERR_RANGE"

    this.Humidity = bin2dec(this.HumidityBit)
    this.Temperature = bin2dec(this.TemperatureBit)

    if int(this.Humidity) + int(this.Temperature) - int(bin2dec(crc)) == 0:
        return "Humidity:" + this.Humidity + "%" + " "" Temperature:" + this.Temperature + "C"
    else:
        return "ERR_CRC"
