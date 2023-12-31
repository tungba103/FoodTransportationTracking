import paho.mqtt.client as mqtt
import time
import random

MQTT_BROKER_URL = "test.mosquitto.org"
MQTT_PORT_URL = 1883
MQTT_TOPIC_TEMPERATURE = "topic/temperature"
MQTT_TOPIC_HUMIDITY = "topic/humidity"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print(f"Failed to connect, return code {rc}")

def publish_temperature(client, topic):
    temperature = random.uniform(20.0, 30.0) 
    client.publish(topic, str(temperature))
    print(f"Temperature published: {temperature}")

def publish_humidity(client, topic):
    humidity = random.uniform(20.0, 30.0) 
    client.publish(topic, str(humidity))
    print(f"Humidity published: {humidity}")

client = mqtt.Client("IoT Sender")
client.on_connect = on_connect

client.connect(MQTT_BROKER_URL, MQTT_PORT_URL, 60)

try:
    while True:
        publish_temperature(client, MQTT_TOPIC_TEMPERATURE)
        publish_temperature(client, MQTT_TOPIC_HUMIDITY)
        time.sleep(1) 

except KeyboardInterrupt:
    print("User interrupted the program")

finally:
    client.disconnect()
    print("Disconnected from MQTT Broker")
