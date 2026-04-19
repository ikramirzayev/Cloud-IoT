import requests
import time
import random


URL = "https://kmhj56l57bvd46jz24wsufntf40qjzru.lambda-url.eu-north-1.on.aws/"

while True:
    veri = {
        "vehicleId": "Kamyon-34",
        "hiz": random.randint(60, 140), # Rastgele hız
        "yakit": random.randint(10, 100),
        "timestamp": int(time.time())
    }
    
    response = requests.post(URL, json=veri)
    print(f"Veri gitti: {veri} - Sunucu Yanıtı: {response.text}")
    
    time.sleep(5) # 5 saniyede bir veri gönder