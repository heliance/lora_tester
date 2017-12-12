#!/usr/bin/env python3

import subprocess
import os

print("Please provide accurate DATABASE name to write the data: ")
db_name = input(str("DATABASE: "))
print("Please provide the FILENAME to write: ")
filename = os.path.abspath(input(str("FILENAME: ")))
call = ("curl -u admin:abrcbrb -i -XPOST http://172.16.0.192:8086/write?db=" +
                db_name + " --data-binary @" + filename)
subprocess.call(call, shell=True)
