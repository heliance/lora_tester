import datetime
import json
import pygal

filename = "formatted_topic2.json"

with open(filename) as f_obj:
    data_dict = json.load(f_obj)

temp_time_list = []
rssi_list = []
time_list = []

for time_index in data_dict:
    time_val = time_index["time"]
    rssi_value = time_index["rssi"]
    temp_time_list.append(time_val)
    rssi_list.append(int(rssi_value))

for d in temp_time_list:
    date = datetime.datetime.strptime(str(d), "%Y-%m-%dT%H:%M:%S.%fZ")
    new_time = "%Y-%m-%d %H:%M:%S"
    new_d = date.strftime(new_time)
    time_list.append(new_d)

line_chart = pygal.Bar()
line_chart.title = 'RSSI from the Node devEUI 0000000000000001'

line_chart.x_labels = time_list
line_chart.add('RSSI', rssi_list)

line_chart.render_to_file('rssi.svg')
