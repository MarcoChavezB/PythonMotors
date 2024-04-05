import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

# Configura el pin del LED
LED_PIN = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Configura los parámetros de conexión MQTT
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "led_control"

# Función para manejar los mensajes MQTT
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print("Mensaje recibido:", payload)
    
    # Enciende o apaga el LED según el mensaje recibido
    if payload == "ON":
        print(payload)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.slee(2)
    elif payload == "OFF":
        print(payload)
        time.sleep(2)
        GPIO.output(LED_PIN, GPIO.LOW)
    

# Configura el cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_start()

# Bucle principal
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    client.disconnect()
    client.loop_stop()

