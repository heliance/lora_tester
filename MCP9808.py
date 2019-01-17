#!/usr/bin/env python

# This code is designed to work with the MCP9808_I2CS I2C Mini Module.
# You need to install smbus library first. Please refer to:
# https://pypi.python.org/pypi/smbus-cffi/0.5.1
# ATTENTION! This script uses Python 2.7 version!
# It reads temp every minute and sends it to InfluxDB via API call.

import smbus
from datetime import datetime
import calendar
import os
import time


# Get I2C bus
bus = smbus.SMBus(1)

# MCP9808 address, 0x18(24)
# Select configuration register, 0x01(1)
#               0x0000(00)      Continuous conversion mode, Power-up default
config = [0x00, 0x00]
bus.write_i2c_block_data(0x18, 0x01, config)
# MCP9808 address, 0x18(24)
# Select resolution rgister, 0x08(8)
#               0x03(03)        Resolution = +0.0625 / C
bus.write_byte_data(0x18, 0x08, 0x03)

time.sleep(0.5)

while True:
    # MCP9808 address, 0x18(24)
    # Read data back from 0x05(5), 2 bytes
    # Temp MSB, TEMP LSB
    data = bus.read_i2c_block_data(0x18, 0x05, 2)

    # Convert the data to 13-bits
    ctemp = ((data[0] & 0x1F) * 256) + data[1]
    if ctemp > 4095 :
        ctemp -= 8192
    ctemp = ctemp * 0.0625
    ftemp = ctemp * 1.8 + 32

    # Output data to screen
    # print "Temperature in Celsius is    : %.2f C" %ctemp
    # print "Temperature in Fahrenheit is : %.2f F" %ftemp

    d = datetime.utcnow()
    unixtime = calendar.timegm(d.utctimetuple())

    call = ("curl -s -u admin:abrcbrb -i -XPOST"
            "'http://172.16.0.192:8086/write?db=mydb'" +
            " --data-binary " + "'temp,GW_ID=1 value=" + str(ctemp) +
            str(unixtime) + "'" + ">/dev/null")

    os.system(call)
    print "Temp measurement (%.2f C) has been sent to the DB." %ctemp
    time.sleep(60)
