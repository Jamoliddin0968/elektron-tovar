from decouple import config
import time

import requests

# URL, qaysi serverga so'rov yuborish kerak
url = 'https://elektron-tovar.onrender.com'

# So'rovni yuboradigan funksiya


def send_request():
    try:
        requests.get(url)
    except:
        pass


# Har 5 daqiqada so'rov yuborib turish
while True:
    if config('RENDER', default=False, cast=bool):
        send_request()
        time.sleep(30)  # 300 sekund = 5 minut
