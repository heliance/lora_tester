import paho.mqtt.client as mqtt
import subprocess

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(user_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    message = str(msg.payload)
    print(msg.topic + ":    " + message)
    with open(filename, 'a') as f_obj:
        f_obj.writelines(message + "\n")
    # print(msg.payload)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnected.")


user_topic = str(input("Please, provide required topic for logging: "))
print("Logging has been set to: " + user_topic)

filename = 'topic_data_log'
if filename:
    pass
else:
    subprocess.call(['touch', filename])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()
