import requests
import time
import random

api_key = "I790FYD7FORXWND4"

while True:

    temperatura = random.randint(20,35)
    umidade = random.randint(40,80)

    url = f"https://api.thingspeak.com/update, params=params"

    requests.get(url)

    print (f"Temperatura: {temperatura} ºC / Umidade: {umidade} %")

    time.sleep(15)