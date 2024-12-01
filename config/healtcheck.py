from decouple import config
import time

import requests

# URL, qaysi serverga so'rov yuborish kerak
url = 'https://elektron-tovar.onrender.com'

# So'rovni yuboradigan funksiya


def send_request():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("So'rov muvaffaqiyatli bajarildi")
        else:
            print(f"So'rov xatolik bilan yakunlandi: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"So'rov yuborishda xatolik yuz berdi: {e}")


# Har 5 daqiqada so'rov yuborib turish
while True:
    if config('RENDER', default=False, cast=bool):
        send_request()
        time.sleep(30)  # 300 sekund = 5 minut
