import paho.mqtt.client as mqtt

def on_connect(c, u, f, rc, p=None):
    c.subscribe("casa/#")

def on_message(c, u, m):
    print(f"{m.topic}: {m.payload.decode()}", flush=True)

c = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
c.on_connect = on_connect
c.on_message = on_message
c.connect("mosquitto", 1883)
c.loop_forever()
