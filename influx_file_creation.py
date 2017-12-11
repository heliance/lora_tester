import json
import datetime
import time

filename = "formatted_topic2.json"

with open(filename) as f_obj:
    json_data_list = json.load(f_obj)

write_list = []

for dic_index in json_data_list:

    gw_tag = dic_index["nodeName"]
    field_snr_value = dic_index["loRaSNR"]
    field_rssi_value = dic_index["rssi"]
    field_timestamp = dic_index["time"]

    date = datetime.datetime.strptime(str(field_timestamp),
                                      "%Y-%m-%dT%H:%M:%S.%fZ")
    unixtime = str(int(time.mktime(date.timetuple()))) + "000000000"

    str_to_append = str("snr_value,ID=" + gw_tag + " " + "snr_val=" +
                        field_snr_value + "," + "rssi_val=" +
                        field_rssi_value + " " + unixtime)

    write_list.append(str_to_append)

with open("data_to_write.txt", "w") as f_obj:
    for string in write_list:
        f_obj.writelines(string + "\n")
