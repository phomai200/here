#RECEIVER

from cryptography.fernet import Fernet
import paho.mqtt.client as mqtt
import base64, os, time

#key = Fernet.generate_key()
#print(key)
# b'eeVnw8VV5EKdDFPsCq7Ubk25z8NOAwcru4P-twyemF0='

key = b'eeVnw8VV5EKdDFPsCq7Ubk25z8NOAwcru4P-twyemF0='
cipher = Fernet(key)

def alert(client, userdata, message):
    message = message.payload.decode("utf-8")
    decrypt = cipher.decrypt(message.encode("utf-8"))
    print(decrypt.decode("utf-8")+"\n")
    #os.system(decrypt.decode("utf-8")+"\n")

serv = "broker.hivemq.com"
cli = mqtt.Client()
cli.connect(serv)

while True:
    cli.loop_start()
    cli.subscribe("12/30")
    cli.on_message = alert
    time.sleep(60)
    cli.loop_stop()
