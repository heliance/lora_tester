#!/usr/bin/env python

import smbus
import time
from Adafruit_CharLCD import Adafruit_CharLCD

bus = smbus.SMBus(1)
lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=27, d6=17, d7=22,
                       cols=16, lines=2)

while True:
    bus.write_byte(0x40, 0xF5)
    time.sleep(0.3)

    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)

    humidity = str(((data0 * 256 + data1) * 125 / 65536.0) - 6)
    time.sleep(0.3)

    bus.write_byte(0x40, 0xF3)
    time.sleep(0.3)

    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)

    cTemp = str(((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85)
    # fTemp = cTemp * 1.8 + 32

    lcd.clear()
    lcd.message('Temp.: ' + cTemp[:5] + 'C' + '\nHumidity: '
                + humidity[:5] + '%')
    time.sleep(60)
