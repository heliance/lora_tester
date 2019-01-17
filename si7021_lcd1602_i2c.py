#!/usr/bin/env python

import smbus
import time
import i2c_lcd_driver


bus = smbus.SMBus(1)
lcd = i2c_lcd_driver.lcd()

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

    call = ("curl -k -s -i -XPOST " +
            "'https://172.16.0.225:8086/write?db=lora_gw'" +
            " --data-binary " + "'temperature,GW_ID=1 value=" +
            str(cTemp) + "'" + ">/dev/null")

    call2 = ("curl -k -s -i -XPOST " +
             "'https://172.16.0.225:8086/write?db=lora_gw'" +
             " --data-binary " + "'humidity,GW_ID=1 value=" +
             str(humidity) + "'" + ">/dev/null")

    lcd.lcd_clear()
    lcd.lcd_display_string('Temp.: ' + cTemp[:5] + 'C', 1)
    lcd.lcd_display_string('Humidity: ' + humidity[:5] + '%', 2)
    time.sleep(60)
