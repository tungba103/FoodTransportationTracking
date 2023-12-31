import os
import django
import paho.mqtt.client as mqtt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from humidity.models import Humidity

MQTT_BROKER_URL = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "topic/humidity"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic+": "+str(msg.payload))

    try:
        humidity_value = float(msg.payload)
        Humidity.objects.create(value=humidity_value)
        print("Humidity saved to database.")
    except ValueError:
        print("Invalid Humidity received.")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER_URL, MQTT_PORT, 60)

client.loop_forever()
