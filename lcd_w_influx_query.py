import subprocess
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD


lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=27, d6=17, d7=22,
                       cols=16, lines=2)

while True:
    call2 = """ curl -G -k -s "https://172.16.0.225:8086/query?db=lora_gw" \
    --data-urlencode "q=SELECT last(value) FROM "humidity" 
    WHERE ("GW_ID" = '1')" """
    db_query = str(subprocess.check_output(call2, shell=True))
    humidity = db_query[131:136]

    call3 = """ curl -G -k -s "https://172.16.0.225:8086/query?db=lora_gw" \
    --data-urlencode "q=SELECT last(value) FROM "temperature" 
    WHERE ("GW_ID" = '1')" """
    db_query = str(subprocess.check_output(call3, shell=True))
    temp = db_query[134:139]

    lcd.clear()
    lcd.message('Temp.: ' + temp + 'C' + '\nHumidity: ' + humidity + '%')
    sleep(60)
