#!/usr/bin/env python

import smbus
import time
import os
# import calendar
# from datetime import datetime

# Get I2C bus (Номер шины в разных МК может отличаться. В PI3 - 1).
bus = smbus.SMBus(1)

while True:
    # SI7021 address, 0x40(64).
    # 0xF5(245)	Select Relative Humidity NO HOLD master mode.
    bus.write_byte(0x40, 0xF5)
    time.sleep(0.3)

    # SI7021 address, 0x40(64).
    # Read data back, 2 bytes, Humidity MSB first.
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)

    # Convert the data.
    humidity = ((data0 * 256 + data1) * 125 / 65536.0) - 6
    time.sleep(0.3)

    # SI7021 address, 0x40(64).
    # 0xF3(243)	Select temperature NO HOLD master mode.
    bus.write_byte(0x40, 0xF3)
    time.sleep(0.3)

    # SI7021 address, 0x40(64).
    # Read data back, 2 bytes, Temperature MSB first.
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)

    # Convert the data.
    cTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
    fTemp = cTemp * 1.8 + 32

    # Output data to screen.
    print "Влажность: %.2f %%" % humidity
    print "Температура C: %.2f" % cTemp

    # d = datetime.utcnow()
    # unixtime = calendar.timegm(d.utctimetuple())

    call = ("curl -k -s -i -XPOST " +
            "'https://172.16.0.225:8086/write?db=lora_gw'" +
            " --data-binary " + "'temperature,GW_ID=1 value=" +
            str(cTemp) + "'" + ">/dev/null")

    call2 = ("curl -k -s -i -XPOST " +
            "'https://172.16.0.225:8086/write?db=lora_gw'" +
            " --data-binary " + "'humidity,GW_ID=1 value=" +
            str(humidity) + "'" + ">/dev/null")

    os.system(call)
    os.system(call2)

    print "Temp measurement (%.2f C) has been sent to the DB." % cTemp
    print "Temp measurement (%.2f percents) has been sent to the DB." % humidity
    time.sleep(60)
